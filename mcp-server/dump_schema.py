#!/usr/bin/env python3
"""
Salesforce Schema Dump Utility.

Connects to Salesforce, describes custom and key standard objects,
and generates a CLAUDE.md file at the project root with comprehensive
schema documentation for use as context by Claude.

Usage:
    python dump_schema.py
"""

from __future__ import annotations

import datetime
import os
import sys
from typing import Any, Dict, List

from dotenv import load_dotenv
from simple_salesforce import Salesforce

load_dotenv()

# Objects to document
CUSTOM_OBJECTS = ["Project__c", "Work_Item__c", "Time_Entry__c"]
STANDARD_OBJECTS = ["User", "RecordType"]
ALL_OBJECTS = CUSTOM_OBJECTS + STANDARD_OBJECTS

# Output path - project root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "..", "CLAUDE.md")


def connect() -> Salesforce:
    """Create a Salesforce connection from environment variables.

    Supports two auth modes:
    1. Access token + instance URL (set SF_ACCESS_TOKEN and SF_INSTANCE_URL)
    2. Username + password + security token (traditional)
    """
    access_token = os.getenv("SF_ACCESS_TOKEN", "")
    instance_url = os.getenv("SF_INSTANCE_URL", "")
    if access_token and instance_url:
        return Salesforce(instance_url=instance_url, session_id=access_token)
    return Salesforce(
        username=os.getenv("SF_USERNAME", ""),
        password=os.getenv("SF_PASSWORD", ""),
        security_token=os.getenv("SF_SECURITY_TOKEN", ""),
        domain=os.getenv("SF_DOMAIN", "login"),
    )


def describe_object(sf: Salesforce, object_name: str) -> Dict[str, Any]:
    """Fetch the full describe result for a Salesforce object."""
    return getattr(sf, object_name).describe()


def format_field_table(fields: List[Dict[str, Any]]) -> List[str]:
    """Format fields as a Markdown table."""
    lines = [
        "| API Name | Label | Type | Required | Updateable |",
        "|----------|-------|------|----------|------------|",
    ]
    for f in sorted(fields, key=lambda x: x["name"]):
        required = "Yes" if (not f.get("nillable", True) and f.get("createable", False)) else ""
        updateable = "Yes" if f.get("updateable", False) else ""
        ftype = f["type"]
        if ftype == "reference" and f.get("referenceTo"):
            ftype = f"reference({', '.join(f['referenceTo'])})"
        elif ftype == "double" or ftype == "currency":
            precision = f.get("precision", "")
            scale = f.get("scale", "")
            if precision:
                ftype = f"{f['type']}({precision},{scale})"
        lines.append(
            f"| `{f['name']}` | {f['label']} | {ftype} | {required} | {updateable} |"
        )
    return lines


def format_picklist_values(fields: List[Dict[str, Any]]) -> List[str]:
    """Extract and format picklist fields and their values."""
    lines: List[str] = []
    for f in sorted(fields, key=lambda x: x["name"]):
        if f["type"] == "picklist" and f.get("picklistValues"):
            active_values = [
                pv for pv in f["picklistValues"] if pv.get("active", True)
            ]
            if active_values:
                lines.append(f"**{f['name']}** ({f['label']}):")
                for pv in active_values:
                    default_marker = " *(default)*" if pv.get("defaultValue") else ""
                    lines.append(f"- `{pv['value']}`{default_marker}")
                lines.append("")
    return lines


def format_relationships(fields: List[Dict[str, Any]]) -> List[str]:
    """Extract and format relationship (lookup/master-detail) fields."""
    lines: List[str] = []
    for f in sorted(fields, key=lambda x: x["name"]):
        if f["type"] == "reference" and f.get("referenceTo"):
            rel_name = f.get("relationshipName", "N/A")
            targets = ", ".join(f["referenceTo"])
            lines.append(f"- `{f['name']}` -> **{targets}** (relationship: `{rel_name}`)")
    return lines


def format_child_relationships(child_rels: List[Dict[str, Any]]) -> List[str]:
    """Format child relationship metadata."""
    lines: List[str] = []
    for rel in sorted(child_rels, key=lambda x: x.get("relationshipName") or ""):
        if rel.get("relationshipName"):
            lines.append(
                f"- `{rel['relationshipName']}` -> "
                f"`{rel['childSObject']}.{rel['field']}`"
            )
    return lines


def generate_object_section(desc: Dict[str, Any]) -> List[str]:
    """Generate the full Markdown section for one Salesforce object."""
    lines: List[str] = []
    name = desc["name"]
    label = desc["label"]

    lines.append(f"## {label} (`{name}`)")
    lines.append("")
    lines.append(f"- **Key Prefix:** `{desc.get('keyPrefix', 'N/A')}`")
    lines.append(f"- **Custom:** {desc.get('custom', False)}")
    lines.append(f"- **Createable:** {desc.get('createable', False)}")
    lines.append(f"- **Updateable:** {desc.get('updateable', False)}")
    lines.append(f"- **Deletable:** {desc.get('deletable', False)}")
    lines.append("")

    # Fields table
    lines.append("### Fields")
    lines.append("")
    lines.extend(format_field_table(desc["fields"]))
    lines.append("")

    # Picklist values
    picklist_lines = format_picklist_values(desc["fields"])
    if picklist_lines:
        lines.append("### Picklist Values")
        lines.append("")
        lines.extend(picklist_lines)

    # Relationships (lookups)
    rel_lines = format_relationships(desc["fields"])
    if rel_lines:
        lines.append("### Relationships (Lookups)")
        lines.append("")
        lines.extend(rel_lines)
        lines.append("")

    # Child relationships
    child_rels = desc.get("childRelationships", [])
    child_lines = format_child_relationships(child_rels)
    if child_lines:
        lines.append("### Child Relationships")
        lines.append("")
        lines.extend(child_lines)
        lines.append("")

    return lines


def generate_soql_reference() -> List[str]:
    """Generate a SOQL quick reference section."""
    return [
        "## SOQL Quick Reference",
        "",
        "### Date Literals",
        "",
        "| Literal | Description |",
        "|---------|-------------|",
        "| `TODAY` | Current date |",
        "| `YESTERDAY` | Previous day |",
        "| `TOMORROW` | Next day |",
        "| `THIS_WEEK` | Current week (Sun-Sat) |",
        "| `LAST_WEEK` | Previous week |",
        "| `NEXT_WEEK` | Next week |",
        "| `THIS_MONTH` | Current calendar month |",
        "| `LAST_MONTH` | Previous calendar month |",
        "| `NEXT_MONTH` | Next calendar month |",
        "| `THIS_QUARTER` | Current quarter |",
        "| `THIS_YEAR` | Current calendar year |",
        "| `LAST_90_DAYS` | Last 90 days |",
        "| `LAST_N_DAYS:n` | Last n days |",
        "| `NEXT_N_DAYS:n` | Next n days |",
        "| `LAST_N_WEEKS:n` | Last n weeks |",
        "| `LAST_N_MONTHS:n` | Last n months |",
        "",
        "### Aggregate Functions",
        "",
        "| Function | Description | Example |",
        "|----------|-------------|---------|",
        "| `COUNT(field)` | Count non-null values | `SELECT COUNT(Id) FROM Work_Item__c` |",
        "| `COUNT_DISTINCT(field)` | Count distinct values | `SELECT COUNT_DISTINCT(Status__c) FROM Work_Item__c` |",
        "| `SUM(field)` | Sum numeric field | `SELECT SUM(Hours__c) FROM Time_Entry__c` |",
        "| `AVG(field)` | Average value | `SELECT AVG(Estimated_Hours__c) FROM Work_Item__c` |",
        "| `MIN(field)` | Minimum value | `SELECT MIN(Due_Date__c) FROM Work_Item__c` |",
        "| `MAX(field)` | Maximum value | `SELECT MAX(Due_Date__c) FROM Work_Item__c` |",
        "",
        "### Common Patterns",
        "",
        "```sql",
        "-- Group by with aggregate",
        "SELECT Status__c, COUNT(Id) cnt",
        "FROM Work_Item__c",
        "GROUP BY Status__c",
        "",
        "-- Relationship query (parent)",
        "SELECT Name, Project__r.Name, Assigned_To__r.Name",
        "FROM Work_Item__c",
        "",
        "-- Subquery (children)",
        "SELECT Name, (SELECT Hours__c, Date__c FROM Time_Entries__r)",
        "FROM Work_Item__c",
        "",
        "-- Date filtering",
        "SELECT Name FROM Work_Item__c",
        "WHERE Due_Date__c = TODAY",
        "  AND CreatedDate >= LAST_N_DAYS:30",
        "```",
        "",
    ]


def main() -> None:
    """Main entry point: connect, describe objects, write CLAUDE.md."""
    print("Connecting to Salesforce...")
    sf = connect()
    print(f"Connected as: {sf.sf_instance}")

    doc_lines: List[str] = []

    # Header
    doc_lines.append("# Salesforce Org Schema Reference")
    doc_lines.append("")
    doc_lines.append(
        f"Auto-generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
        f"by `dump_schema.py`."
    )
    doc_lines.append("")
    doc_lines.append(
        "This document describes the Salesforce objects, fields, and relationships "
        "available in this org. Use it as context for building SOQL queries and "
        "understanding the data model."
    )
    doc_lines.append("")

    # Table of contents
    doc_lines.append("## Table of Contents")
    doc_lines.append("")
    descriptions: List[Dict[str, Any]] = []

    for obj_name in ALL_OBJECTS:
        print(f"  Describing {obj_name}...")
        try:
            desc = describe_object(sf, obj_name)
            descriptions.append(desc)
            doc_lines.append(f"- [{desc['label']} (`{obj_name}`)](#{obj_name.lower().replace('_', '-')})")
        except Exception as e:
            print(f"  WARNING: Could not describe {obj_name}: {e}")
            doc_lines.append(f"- ~~{obj_name}~~ (not accessible)")

    doc_lines.append(f"- [SOQL Quick Reference](#soql-quick-reference)")
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")

    # Object sections
    for desc in descriptions:
        doc_lines.extend(generate_object_section(desc))
        doc_lines.append("---")
        doc_lines.append("")

    # SOQL reference
    doc_lines.extend(generate_soql_reference())

    # Write output
    output = "\n".join(doc_lines)
    abs_output = os.path.abspath(OUTPUT_PATH)
    with open(abs_output, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\nSchema documentation written to: {abs_output}")
    print(f"  Objects documented: {len(descriptions)}")
    total_fields = sum(len(d["fields"]) for d in descriptions)
    print(f"  Total fields: {total_fields}")


if __name__ == "__main__":
    main()
