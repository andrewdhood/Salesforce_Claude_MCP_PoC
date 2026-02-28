"""
Salesforce Project Management MCP Server.

Connects to Salesforce via simple_salesforce and exposes project management,
time tracking, and analytics tools to Claude via FastMCP.

Requires Python 3.10+ and the packages listed in requirements.txt.
"""

from __future__ import annotations

import datetime
import math
import os
import statistics
from collections import defaultdict
from typing import Any, Dict, List, Optional

import pandas as pd
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from simple_salesforce import Salesforce, SalesforceError

from soql_builder import SOQLBuilder

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

load_dotenv()

SF_USERNAME = os.getenv("SF_USERNAME", "")
SF_PASSWORD = os.getenv("SF_PASSWORD", "")
SF_SECURITY_TOKEN = os.getenv("SF_SECURITY_TOKEN", "")
SF_DOMAIN = os.getenv("SF_DOMAIN", "login")

# ---------------------------------------------------------------------------
# Salesforce connection
# ---------------------------------------------------------------------------


SF_ACCESS_TOKEN = os.getenv("SF_ACCESS_TOKEN", "")
SF_INSTANCE_URL = os.getenv("SF_INSTANCE_URL", "")

_sf_connection: Optional[Salesforce] = None


def _connect_sf() -> Salesforce:
    """Create and return a Salesforce connection.

    Supports two auth modes:
    1. Access token + instance URL (set SF_ACCESS_TOKEN and SF_INSTANCE_URL)
    2. Username + password + security token (traditional)
    """
    if SF_ACCESS_TOKEN and SF_INSTANCE_URL:
        return Salesforce(instance_url=SF_INSTANCE_URL, session_id=SF_ACCESS_TOKEN)
    return Salesforce(
        username=SF_USERNAME,
        password=SF_PASSWORD,
        security_token=SF_SECURITY_TOKEN,
        domain=SF_DOMAIN,
    )


def get_sf() -> Salesforce:
    """Return the cached Salesforce connection, creating it on first use."""
    global _sf_connection
    if _sf_connection is None:
        _sf_connection = _connect_sf()
    return _sf_connection

# ---------------------------------------------------------------------------
# FastMCP server
# ---------------------------------------------------------------------------

mcp = FastMCP("salesforce-pm")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VALID_WORK_ITEM_STATUSES = {"To Do", "In Progress", "Done", "Blocked"}


def query_to_dataframe(soql: str) -> pd.DataFrame:
    """
    Execute a SOQL query via query_all() and return results as a pandas
    DataFrame.  Handles pagination automatically through query_all().
    Nested relationship dicts are flattened (e.g. Project__r.Name).
    """
    result = get_sf().query_all(soql)
    records: List[Dict[str, Any]] = result.get("records", [])
    if not records:
        return pd.DataFrame()
    flat = flatten_relationship_fields(records)
    df = pd.DataFrame(flat)
    # Drop Salesforce metadata column injected by simple_salesforce
    if "attributes" in df.columns:
        df = df.drop(columns=["attributes"])
    return df


def flatten_relationship_fields(
    records: List[Dict[str, Any]],
    parent_key: str = "",
) -> List[Dict[str, Any]]:
    """
    Flatten nested relationship objects in Salesforce query results.

    Example: {"Project__r": {"Name": "Alpha"}} becomes
             {"Project__r.Name": "Alpha"}
    """
    flat_records: List[Dict[str, Any]] = []
    for record in records:
        flat: Dict[str, Any] = {}
        for key, value in record.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict) and "attributes" in value:
                # This is a relationship object -- flatten it
                for sub_key, sub_val in value.items():
                    if sub_key == "attributes":
                        continue
                    flat[f"{full_key}.{sub_key}"] = sub_val
            elif isinstance(value, dict) and key == "attributes":
                # Skip Salesforce metadata
                continue
            else:
                flat[full_key] = value
        flat_records.append(flat)
    return flat_records


def _df_to_table(df: pd.DataFrame, max_rows: int = 200) -> str:
    """Convert a DataFrame to a readable text table."""
    if df.empty:
        return "(no results)"
    return df.head(max_rows).to_string(index=False)


def _today_soql() -> str:
    """Return today's date in YYYY-MM-DD format for SOQL."""
    return datetime.date.today().strftime("%Y-%m-%d")


# ===================================================================
# CORE TOOLS
# ===================================================================


@mcp.tool()
def sf_get_my_work_items(
    status: Optional[str] = None,
    project_name: Optional[str] = None,
    due_today: bool = False,
) -> str:
    """
    Retrieve work items from Salesforce with optional filters.

    Filters:
    - status: filter by Status__c value (e.g. "In Progress", "Blocked")
    - project_name: filter by related Project name
    - due_today: if True, only items with Due_Date__c = TODAY

    Returns a formatted table of work items including project name,
    assigned user, status, priority, due date, and estimated hours.
    """
    try:
        builder = (
            SOQLBuilder()
            .select([
                "Id",
                "Name",
                "Subject__c",
                "Status__c",
                "Priority__c",
                "Type__c",
                "Due_Date__c",
                "Estimated_Hours__c",
                "Actual_Hours__c",
                "Project__r.Name",
                "Assigned_To__r.Name",
            ])
            .from_object("Work_Item__c")
        )

        if status:
            builder.where("Status__c", "=", status)
        if project_name:
            builder.where("Project__r.Name", "=", project_name)
        if due_today:
            builder.where("Due_Date__c", "=", "TODAY")

        builder.order_by("Due_Date__c", "ASC").limit(200)

        soql = builder.build()
        df = query_to_dataframe(soql)
        return _df_to_table(df)
    except Exception as e:
        return f"Error fetching work items: {e}"


@mcp.tool()
def sf_log_time(
    work_item_name: str,
    hours: float,
    date: str,
    notes: str = "",
) -> str:
    """
    Log time against a work item by creating a Time_Entry__c record.

    Parameters:
    - work_item_name: The auto-number Name of the work item (e.g. "WI-0005")
    - hours: Number of hours to log (must be > 0 and <= 24)
    - date: Date of the time entry in YYYY-MM-DD format
    - notes: Optional description of work performed

    Returns confirmation with the new time entry details.
    """
    try:
        # Validate hours
        if hours <= 0:
            return "Error: hours must be greater than 0."
        if hours > 24:
            return "Error: hours cannot exceed 24 for a single entry."

        # Look up Work_Item__c by Name
        lookup_soql = (
            SOQLBuilder()
            .select(["Id", "Name", "Subject__c"])
            .from_object("Work_Item__c")
            .where("Name", "=", work_item_name)
            .limit(1)
            .build()
        )
        result = get_sf().query(lookup_soql)
        records = result.get("records", [])
        if not records:
            return f"Error: Work item '{work_item_name}' not found."

        work_item_id = records[0]["Id"]
        work_item_subject = records[0].get("Subject__c", "")

        # Create Time_Entry__c
        entry_data: Dict[str, Any] = {
            "Work_Item__c": work_item_id,
            "Hours__c": hours,
            "Date__c": date,
        }
        if notes:
            entry_data["Notes__c"] = notes

        create_result = get_sf().Time_Entry__c.create(entry_data)
        new_id = create_result.get("id", "unknown")

        return (
            f"Time entry created successfully.\n"
            f"  ID: {new_id}\n"
            f"  Work Item: {work_item_name} - {work_item_subject}\n"
            f"  Hours: {hours}\n"
            f"  Date: {date}\n"
            f"  Notes: {notes or '(none)'}"
        )
    except Exception as e:
        return f"Error logging time: {e}"


@mcp.tool()
def sf_update_work_item_status(work_item_name: str, new_status: str) -> str:
    """
    Update the status of a work item.

    Parameters:
    - work_item_name: The auto-number Name of the work item (e.g. "WI-0005")
    - new_status: New status value. Must be one of: To Do, In Progress, Done, Blocked

    Returns confirmation of the status change.
    """
    try:
        if new_status not in VALID_WORK_ITEM_STATUSES:
            return (
                f"Error: Invalid status '{new_status}'. "
                f"Valid statuses: {', '.join(sorted(VALID_WORK_ITEM_STATUSES))}"
            )

        # Look up Work_Item__c by Name
        lookup_soql = (
            SOQLBuilder()
            .select(["Id", "Name", "Status__c", "Subject__c"])
            .from_object("Work_Item__c")
            .where("Name", "=", work_item_name)
            .limit(1)
            .build()
        )
        result = get_sf().query(lookup_soql)
        records = result.get("records", [])
        if not records:
            return f"Error: Work item '{work_item_name}' not found."

        work_item = records[0]
        old_status = work_item.get("Status__c", "unknown")
        work_item_id = work_item["Id"]

        get_sf().Work_Item__c.update(work_item_id, {"Status__c": new_status})

        return (
            f"Status updated successfully.\n"
            f"  Work Item: {work_item_name} - {work_item.get('Subject__c', '')}\n"
            f"  Old Status: {old_status}\n"
            f"  New Status: {new_status}"
        )
    except Exception as e:
        return f"Error updating status: {e}"


@mcp.tool()
def sf_get_project_summary(project_name: str) -> str:
    """
    Get a comprehensive summary of a project including status breakdown,
    overdue items, blocked items, and burn rate.

    Parameters:
    - project_name: The name of the Project__c record

    Returns a formatted project summary with key metrics.
    """
    try:
        # Fetch the project record
        proj_soql = (
            SOQLBuilder()
            .select([
                "Id",
                "Name",
                "Status__c",
                "Start_Date__c",
                "End_Date__c",
                "Total_Estimated_Hours__c",
                "Total_Actual_Hours__c",
            ])
            .from_object("Project__c")
            .where("Name", "=", project_name)
            .limit(1)
            .build()
        )
        proj_result = get_sf().query(proj_soql)
        proj_records = proj_result.get("records", [])
        if not proj_records:
            return f"Error: Project '{project_name}' not found."

        project = proj_records[0]
        project_id = project["Id"]

        # Work items grouped by status
        status_soql = (
            SOQLBuilder()
            .select(["Status__c", "COUNT(Id) item_count"])
            .from_object("Work_Item__c")
            .where("Project__c", "=", project_id)
            .group_by("Status__c")
            .build()
        )
        status_df = query_to_dataframe(status_soql)

        # Overdue items
        today = _today_soql()
        overdue_soql = (
            SOQLBuilder()
            .select(["Name", "Subject__c", "Due_Date__c", "Status__c", "Assigned_To__r.Name"])
            .from_object("Work_Item__c")
            .where("Project__c", "=", project_id)
            .where("Due_Date__c", "<", "TODAY")
            .where_not_in("Status__c", ["Done"])
            .order_by("Due_Date__c", "ASC")
            .limit(50)
            .build()
        )
        overdue_df = query_to_dataframe(overdue_soql)

        # Blocked items
        blocked_soql = (
            SOQLBuilder()
            .select(["Name", "Subject__c", "Assigned_To__r.Name"])
            .from_object("Work_Item__c")
            .where("Project__c", "=", project_id)
            .where("Status__c", "=", "Blocked")
            .limit(50)
            .build()
        )
        blocked_df = query_to_dataframe(blocked_soql)

        # Build summary
        lines: List[str] = []
        lines.append(f"=== Project Summary: {project_name} ===")
        lines.append(f"  Status: {project.get('Status__c', 'N/A')}")
        lines.append(f"  Start Date: {project.get('Start_Date__c', 'N/A')}")
        lines.append(f"  End Date: {project.get('End_Date__c', 'N/A')}")

        est = project.get("Total_Estimated_Hours__c") or 0
        act = project.get("Total_Actual_Hours__c") or 0
        burn_pct = (act / est * 100) if est > 0 else 0
        lines.append(f"  Estimated Hours: {est}")
        lines.append(f"  Actual Hours: {act}")
        lines.append(f"  Burn Rate: {burn_pct:.1f}% of estimate consumed")

        lines.append("")
        lines.append("--- Status Breakdown ---")
        if status_df.empty:
            lines.append("  No work items found.")
        else:
            lines.append(_df_to_table(status_df))

        lines.append("")
        lines.append(f"--- Overdue Items ({len(overdue_df)}) ---")
        if overdue_df.empty:
            lines.append("  None - all items are on track!")
        else:
            lines.append(_df_to_table(overdue_df))

        lines.append("")
        lines.append(f"--- Blocked Items ({len(blocked_df)}) ---")
        if blocked_df.empty:
            lines.append("  None - no blockers!")
        else:
            lines.append(_df_to_table(blocked_df))

        return "\n".join(lines)
    except Exception as e:
        return f"Error fetching project summary: {e}"


# ===================================================================
# ANALYTICS TOOLS
# ===================================================================


@mcp.tool()
def sf_estimate_accuracy(group_by: str = "type") -> str:
    """
    Analyze estimation accuracy for completed work items.

    Calculates the ratio of actual hours to estimated hours, grouped by
    a chosen dimension.

    Parameters:
    - group_by: How to group results. Options: "type" (Type__c),
      "project" (Project__r.Name), or "priority" (Priority__c).
      Defaults to "type".

    Returns a table showing estimation accuracy percentages per group.
    """
    try:
        group_field_map = {
            "type": "Type__c",
            "project": "Project__r.Name",
            "priority": "Priority__c",
        }
        group_field = group_field_map.get(group_by.lower())
        if not group_field:
            return (
                f"Error: Invalid group_by '{group_by}'. "
                f"Options: type, project, priority"
            )

        soql = (
            SOQLBuilder()
            .select([
                "Id",
                "Name",
                group_field,
                "Estimated_Hours__c",
                "Actual_Hours__c",
            ])
            .from_object("Work_Item__c")
            .where("Status__c", "=", "Done")
            .where_not_null("Estimated_Hours__c")
            .where_not_null("Actual_Hours__c")
            .limit(2000)
            .build()
        )
        df = query_to_dataframe(soql)
        if df.empty:
            return "No completed work items with both estimated and actual hours found."

        # The group field might be flattened (e.g. Project__r.Name)
        col = group_field if group_field in df.columns else group_field.replace(".", "_")
        if col not in df.columns:
            # Try to find a column that ends with the field name
            matching = [c for c in df.columns if c.endswith(group_field.split(".")[-1])]
            col = matching[0] if matching else group_field

        grouped = df.groupby(col).agg(
            items=("Id", "count"),
            total_estimated=("Estimated_Hours__c", "sum"),
            total_actual=("Actual_Hours__c", "sum"),
        ).reset_index()

        grouped["accuracy_%"] = (
            grouped["total_actual"] / grouped["total_estimated"] * 100
        ).round(1)
        grouped["overrun_%"] = (grouped["accuracy_%"] - 100).round(1)

        lines = [f"=== Estimation Accuracy by {group_by.title()} ===", ""]
        lines.append(grouped.to_string(index=False))
        lines.append("")
        overall_est = df["Estimated_Hours__c"].sum()
        overall_act = df["Actual_Hours__c"].sum()
        overall_pct = (overall_act / overall_est * 100) if overall_est > 0 else 0
        lines.append(
            f"Overall: {overall_act:.1f}h actual / {overall_est:.1f}h estimated "
            f"= {overall_pct:.1f}%"
        )
        return "\n".join(lines)
    except Exception as e:
        return f"Error calculating estimate accuracy: {e}"


@mcp.tool()
def sf_weekly_utilization(weeks: int = 2) -> str:
    """
    Show a weekly utilization report from time entries.

    Queries Time_Entry__c for the last N weeks and creates a pivot table
    showing hours logged per project per day, with daily totals and
    utilization percentage (based on an 8-hour workday).

    Parameters:
    - weeks: Number of past weeks to include (default: 2)

    Returns a formatted pivot table with utilization metrics.
    """
    try:
        n_days = weeks * 7
        soql = (
            SOQLBuilder()
            .select([
                "Id",
                "Date__c",
                "Hours__c",
                "Work_Item__r.Project__r.Name",
            ])
            .from_object("Time_Entry__c")
            .where("Date__c", ">=", f"LAST_N_DAYS:{n_days}")
            .order_by("Date__c", "ASC")
            .limit(5000)
            .build()
        )
        df = query_to_dataframe(soql)
        if df.empty:
            return f"No time entries found in the last {weeks} week(s)."

        # Identify the project name column
        proj_col = None
        for c in df.columns:
            if "Project" in c and "Name" in c:
                proj_col = c
                break
        if proj_col is None:
            proj_col = "Work_Item__r.Project__r.Name"

        df["Date__c"] = pd.to_datetime(df["Date__c"])
        df["day"] = df["Date__c"].dt.strftime("%a %m/%d")

        pivot = df.pivot_table(
            index=proj_col,
            columns="day",
            values="Hours__c",
            aggfunc="sum",
            fill_value=0,
            margins=True,
            margins_name="TOTAL",
        )

        lines = [f"=== Weekly Utilization (last {weeks} weeks) ===", ""]
        lines.append(pivot.to_string())

        # Daily utilization
        lines.append("")
        lines.append("--- Daily Utilization (8hr day) ---")
        if "TOTAL" in pivot.index:
            totals = pivot.loc["TOTAL"].drop("TOTAL", errors="ignore")
            for day_label, hrs in totals.items():
                pct = hrs / 8 * 100
                bar = "#" * int(pct / 5)
                lines.append(f"  {day_label}: {hrs:.1f}h / 8h ({pct:.0f}%) {bar}")

        return "\n".join(lines)
    except Exception as e:
        return f"Error calculating utilization: {e}"


@mcp.tool()
def sf_velocity_trend(weeks: int = 6) -> str:
    """
    Show the team's velocity trend over recent weeks.

    Queries completed work items by Completed_Date__c, groups them by
    ISO week, counts items completed per week, and calculates a 4-week
    rolling average with trend indicators.

    Parameters:
    - weeks: Number of past weeks to analyze (default: 6)

    Returns a formatted table with weekly velocity and trend arrows.
    """
    try:
        n_days = weeks * 7
        soql = (
            SOQLBuilder()
            .select(["Id", "Completed_Date__c", "Estimated_Hours__c", "Actual_Hours__c"])
            .from_object("Work_Item__c")
            .where("Status__c", "=", "Done")
            .where("Completed_Date__c", ">=", f"LAST_N_DAYS:{n_days}")
            .where_not_null("Completed_Date__c")
            .order_by("Completed_Date__c", "ASC")
            .limit(5000)
            .build()
        )
        df = query_to_dataframe(soql)
        if df.empty:
            return f"No completed items found in the last {weeks} weeks."

        df["Completed_Date__c"] = pd.to_datetime(df["Completed_Date__c"])
        df["iso_week"] = df["Completed_Date__c"].dt.isocalendar().week.astype(int)
        df["iso_year"] = df["Completed_Date__c"].dt.isocalendar().year.astype(int)
        df["week_label"] = df["iso_year"].astype(str) + "-W" + df["iso_week"].astype(str).str.zfill(2)

        weekly = (
            df.groupby("week_label")
            .agg(
                items_completed=("Id", "count"),
                total_hours=("Actual_Hours__c", "sum"),
            )
            .reset_index()
            .sort_values("week_label")
        )

        # 4-week rolling average
        weekly["rolling_avg"] = (
            weekly["items_completed"].rolling(window=4, min_periods=1).mean().round(1)
        )

        # Trend indicators
        trends = []
        for i in range(len(weekly)):
            if i == 0:
                trends.append("--")
            else:
                diff = weekly.iloc[i]["items_completed"] - weekly.iloc[i - 1]["items_completed"]
                if diff > 0:
                    trends.append("^ UP")
                elif diff < 0:
                    trends.append("v DOWN")
                else:
                    trends.append("= STABLE")
        weekly["trend"] = trends

        lines = [f"=== Velocity Trend (last {weeks} weeks) ===", ""]
        lines.append(weekly.to_string(index=False))
        lines.append("")
        avg_velocity = weekly["items_completed"].mean()
        lines.append(f"Average velocity: {avg_velocity:.1f} items/week")

        return "\n".join(lines)
    except Exception as e:
        return f"Error calculating velocity trend: {e}"


@mcp.tool()
def sf_scope_estimate(work_type: str, gut_estimate: float) -> str:
    """
    Provide a data-driven scope estimate based on historical actuals.

    Queries historical completed work items of the same type, calculates
    statistical measures (mean, median, std dev), and applies the average
    overrun ratio to your gut estimate to produce an adjusted estimate.

    Parameters:
    - work_type: The Type__c value (e.g. "Bug", "Feature", "Task")
    - gut_estimate: Your initial gut-feel estimate in hours

    Returns statistical summary with the adjusted estimate.
    """
    try:
        soql = (
            SOQLBuilder()
            .select(["Id", "Estimated_Hours__c", "Actual_Hours__c"])
            .from_object("Work_Item__c")
            .where("Status__c", "=", "Done")
            .where("Type__c", "=", work_type)
            .where_not_null("Estimated_Hours__c")
            .where_not_null("Actual_Hours__c")
            .limit(5000)
            .build()
        )
        df = query_to_dataframe(soql)
        if df.empty:
            return (
                f"No completed '{work_type}' items with estimate data found. "
                f"Cannot produce adjusted estimate."
            )

        actuals = df["Actual_Hours__c"].dropna().tolist()
        estimates = df["Estimated_Hours__c"].dropna().tolist()

        if not actuals:
            return "No actual hours data available for analysis."

        mean_actual = statistics.mean(actuals)
        median_actual = statistics.median(actuals)
        stdev_actual = statistics.stdev(actuals) if len(actuals) > 1 else 0.0

        # Calculate average overrun ratio
        ratios = [
            a / e for a, e in zip(actuals, estimates) if e and e > 0
        ]
        avg_ratio = statistics.mean(ratios) if ratios else 1.0

        adjusted = gut_estimate * avg_ratio
        p80 = gut_estimate * avg_ratio + stdev_actual  # rough P80

        lines = [
            f"=== Scope Estimate for '{work_type}' ===",
            "",
            f"Historical data ({len(actuals)} completed items):",
            f"  Mean actual hours:    {mean_actual:.1f}h",
            f"  Median actual hours:  {median_actual:.1f}h",
            f"  Std deviation:        {stdev_actual:.1f}h",
            f"  Avg overrun ratio:    {avg_ratio:.2f}x",
            "",
            f"Your gut estimate:      {gut_estimate:.1f}h",
            f"Adjusted estimate:      {adjusted:.1f}h (gut x {avg_ratio:.2f})",
            f"Conservative (P80):     {p80:.1f}h",
            "",
        ]
        if avg_ratio > 1.2:
            lines.append(
                f"Warning: Historical items of type '{work_type}' tend to overrun "
                f"by {(avg_ratio - 1) * 100:.0f}% on average. Plan accordingly."
            )
        elif avg_ratio < 0.8:
            lines.append(
                f"Note: Historical items of type '{work_type}' tend to come in "
                f"under estimate by {(1 - avg_ratio) * 100:.0f}%."
            )
        else:
            lines.append("Estimates for this type are historically fairly accurate.")

        return "\n".join(lines)
    except Exception as e:
        return f"Error calculating scope estimate: {e}"


@mcp.tool()
def sf_daily_budget(target_hours: float = 8.0) -> str:
    """
    Generate a morning briefing showing today's work budget.

    Queries work items due today or currently In Progress, sums up their
    estimated hours, and calculates remaining budget against a target
    (default 8 hours).

    Parameters:
    - target_hours: Total hours available today (default: 8.0)

    Returns a morning briefing with today's workload and remaining capacity.
    """
    try:
        today = _today_soql()
        soql = (
            SOQLBuilder()
            .select([
                "Name",
                "Subject__c",
                "Status__c",
                "Priority__c",
                "Estimated_Hours__c",
                "Actual_Hours__c",
                "Due_Date__c",
                "Project__r.Name",
            ])
            .from_object("Work_Item__c")
            .where_raw(f"(Due_Date__c = {today} OR Status__c = 'In Progress')")
            .where("Status__c", "!=", "Done")
            .order_by("Priority__c", "ASC")
            .order_by("Due_Date__c", "ASC")
            .limit(100)
            .build()
        )
        df = query_to_dataframe(soql)

        lines = [
            f"=== Daily Budget - {datetime.date.today().strftime('%A, %B %d, %Y')} ===",
            f"Target: {target_hours:.1f} hours",
            "",
        ]

        if df.empty:
            lines.append("No items due today or in progress. Your day is open!")
            return "\n".join(lines)

        est_total = df["Estimated_Hours__c"].fillna(0).sum()
        act_total = df["Actual_Hours__c"].fillna(0).sum()
        remaining_work = max(est_total - act_total, 0)
        remaining_budget = target_hours - remaining_work

        lines.append(f"Items on plate: {len(df)}")
        lines.append(f"Estimated remaining work: {remaining_work:.1f}h")
        lines.append(f"Budget remaining: {remaining_budget:.1f}h")
        lines.append("")

        if remaining_budget < 0:
            lines.append(
                f"WARNING: Over-committed by {abs(remaining_budget):.1f}h! "
                f"Consider deferring or reassigning items."
            )
        elif remaining_budget < 1:
            lines.append("Tight day -- little room for unplanned work.")
        else:
            lines.append(
                f"You have ~{remaining_budget:.1f}h of slack for meetings or unplanned work."
            )

        lines.append("")
        lines.append("--- Today's Items ---")
        lines.append(_df_to_table(df))

        return "\n".join(lines)
    except Exception as e:
        return f"Error calculating daily budget: {e}"


# ===================================================================
# GENERIC QUERY TOOLS
# ===================================================================


@mcp.tool()
def sf_query(soql: str) -> str:
    """
    Execute an arbitrary read-only SOQL query against Salesforce.

    Returns up to 200 records as a formatted table. Use this for ad-hoc
    queries when the specialized tools don't cover your needs.

    Parameters:
    - soql: A valid SOQL query string

    Returns the query results as a formatted text table.
    """
    try:
        df = query_to_dataframe(soql)
        if len(df) > 200:
            df = df.head(200)
            note = f"\n(Showing first 200 of {len(df)} records)"
        else:
            note = ""
        return _df_to_table(df) + note
    except Exception as e:
        return f"Error executing SOQL: {e}"


@mcp.tool()
def sf_aggregate(
    object_name: str,
    aggregate_function: str,
    field: Optional[str] = None,
    group_by: Optional[str] = None,
    where: Optional[str] = None,
) -> str:
    """
    Execute an aggregate SOQL query (COUNT, SUM, AVG, MIN, MAX).

    Parameters:
    - object_name: Salesforce object API name (e.g. "Work_Item__c")
    - aggregate_function: One of COUNT, SUM, AVG, MIN, MAX
    - field: The field to aggregate (not required for COUNT)
    - group_by: Optional field to group results by
    - where: Optional WHERE clause (without the 'WHERE' keyword)

    Returns the aggregate results as a formatted table.
    """
    try:
        agg = aggregate_function.upper().strip()
        valid_aggs = {"COUNT", "SUM", "AVG", "MIN", "MAX"}
        if agg not in valid_aggs:
            return (
                f"Error: Invalid aggregate function '{aggregate_function}'. "
                f"Valid options: {', '.join(sorted(valid_aggs))}"
            )

        # Build the SELECT expression
        if agg == "COUNT":
            agg_expr = "COUNT(Id) record_count" if not field else f"COUNT({field}) field_count"
        else:
            if not field:
                return f"Error: field is required for {agg}."
            agg_expr = f"{agg}({field}) result"

        select_fields = [agg_expr]
        if group_by:
            select_fields.insert(0, group_by)

        soql_parts = [f"SELECT {', '.join(select_fields)} FROM {object_name}"]
        if where:
            soql_parts.append(f"WHERE {where}")
        if group_by:
            soql_parts.append(f"GROUP BY {group_by}")

        soql = " ".join(soql_parts)
        df = query_to_dataframe(soql)
        return _df_to_table(df)
    except Exception as e:
        return f"Error executing aggregate query: {e}"


@mcp.tool()
def sf_describe_object(object_name: str) -> str:
    """
    Describe a Salesforce object's metadata including fields, types,
    picklist values, and relationships.

    Parameters:
    - object_name: API name of the Salesforce object (e.g. "Work_Item__c")

    Returns a formatted description of the object's schema.
    """
    try:
        desc = getattr(get_sf(), object_name).describe()

        lines = [
            f"=== {desc['label']} ({desc['name']}) ===",
            f"  Key Prefix: {desc.get('keyPrefix', 'N/A')}",
            f"  Custom: {desc.get('custom', False)}",
            f"  Createable: {desc.get('createable', False)}",
            f"  Updateable: {desc.get('updateable', False)}",
            "",
            "--- Fields ---",
            f"{'API Name':<40} {'Label':<30} {'Type':<15} {'Req':<5} {'Update':<6}",
            "-" * 100,
        ]

        for field in sorted(desc["fields"], key=lambda f: f["name"]):
            req = "Yes" if not field.get("nillable", True) and field.get("createable", False) else ""
            upd = "Yes" if field.get("updateable", False) else ""
            lines.append(
                f"{field['name']:<40} {field['label']:<30} {field['type']:<15} {req:<5} {upd:<6}"
            )

            # Show picklist values
            if field["type"] == "picklist" and field.get("picklistValues"):
                for pv in field["picklistValues"]:
                    active = "" if pv.get("active", True) else " (inactive)"
                    default = " (default)" if pv.get("defaultValue", False) else ""
                    lines.append(f"  {'':>40}  -> {pv['value']}{active}{default}")

        # Relationships
        child_rels = desc.get("childRelationships", [])
        if child_rels:
            lines.append("")
            lines.append("--- Child Relationships ---")
            for rel in child_rels:
                if rel.get("relationshipName"):
                    lines.append(
                        f"  {rel['relationshipName']} -> {rel['childSObject']}.{rel['field']}"
                    )

        return "\n".join(lines)
    except Exception as e:
        return f"Error describing object '{object_name}': {e}"


# ===================================================================
# Entry point
# ===================================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")
