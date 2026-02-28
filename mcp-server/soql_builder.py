"""
Builder pattern class for constructing SOQL (Salesforce Object Query Language) queries.

Provides a fluent, method-chaining interface for building type-safe SOQL queries
with input validation, date literal support, and proper escaping.
"""

from __future__ import annotations

from typing import Any, List, Optional, Union


# SOQL date literals that must NOT be quoted
SOQL_DATE_LITERALS = {
    "YESTERDAY",
    "TODAY",
    "TOMORROW",
    "LAST_WEEK",
    "THIS_WEEK",
    "NEXT_WEEK",
    "LAST_MONTH",
    "THIS_MONTH",
    "NEXT_MONTH",
    "LAST_90_DAYS",
    "NEXT_90_DAYS",
    "THIS_QUARTER",
    "LAST_QUARTER",
    "NEXT_QUARTER",
    "THIS_YEAR",
    "LAST_YEAR",
    "NEXT_YEAR",
    "THIS_FISCAL_QUARTER",
    "LAST_FISCAL_QUARTER",
    "NEXT_FISCAL_QUARTER",
    "THIS_FISCAL_YEAR",
    "LAST_FISCAL_YEAR",
    "NEXT_FISCAL_YEAR",
}

# Patterns like LAST_N_DAYS:30, NEXT_N_QUARTERS:4, etc.
SOQL_DATE_LITERAL_PREFIXES = (
    "LAST_N_DAYS:",
    "NEXT_N_DAYS:",
    "LAST_N_WEEKS:",
    "NEXT_N_WEEKS:",
    "LAST_N_MONTHS:",
    "NEXT_N_MONTHS:",
    "LAST_N_QUARTERS:",
    "NEXT_N_QUARTERS:",
    "LAST_N_YEARS:",
    "NEXT_N_YEARS:",
    "LAST_N_FISCAL_QUARTERS:",
    "NEXT_N_FISCAL_QUARTERS:",
    "LAST_N_FISCAL_YEARS:",
    "NEXT_N_FISCAL_YEARS:",
)

VALID_OPERATORS = {"=", "!=", "<", ">", "<=", ">=", "LIKE", "IN", "NOT IN"}


def _is_date_literal(value: str) -> bool:
    """Check if a string value is a SOQL date literal."""
    upper = value.upper().strip()
    if upper in SOQL_DATE_LITERALS:
        return True
    for prefix in SOQL_DATE_LITERAL_PREFIXES:
        if upper.startswith(prefix):
            return True
    return False


def _escape_soql_string(value: str) -> str:
    """Escape single quotes in SOQL string values."""
    return value.replace("'", "\\'")


def _format_value(value: Any) -> str:
    """Format a Python value for use in a SOQL query."""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if _is_date_literal(value):
            return value
        return f"'{_escape_soql_string(value)}'"
    return f"'{_escape_soql_string(str(value))}'"


class SOQLBuilder:
    """
    A builder for constructing SOQL queries with method chaining.

    Usage:
        query = (
            SOQLBuilder()
            .select(["Id", "Name", "Status__c"])
            .from_object("Work_Item__c")
            .where("Status__c", "=", "In Progress")
            .where("Due_Date__c", "<=", "TODAY")
            .order_by("Due_Date__c", "ASC")
            .limit(50)
            .build()
        )
    """

    def __init__(self) -> None:
        self._select_fields: List[str] = []
        self._from: Optional[str] = None
        self._where_clauses: List[str] = []
        self._order_by_clauses: List[str] = []
        self._group_by_fields: List[str] = []
        self._having_clauses: List[str] = []
        self._limit: Optional[int] = None
        self._offset: Optional[int] = None

    def select(self, fields: Union[str, List[str]]) -> SOQLBuilder:
        """Add fields to the SELECT clause."""
        if isinstance(fields, str):
            fields = [f.strip() for f in fields.split(",")]
        self._select_fields.extend(fields)
        return self

    def from_object(self, sobject: str) -> SOQLBuilder:
        """Set the FROM object."""
        self._from = sobject
        return self

    def where(self, field: str, operator: str, value: Any) -> SOQLBuilder:
        """
        Add a WHERE condition.

        Supports standard operators: =, !=, <, >, <=, >=, LIKE, IN, NOT IN.
        SOQL date literals (TODAY, LAST_N_DAYS:30, etc.) are not quoted.
        String values are automatically single-quote escaped.
        """
        op = operator.upper().strip()
        if op not in VALID_OPERATORS:
            raise ValueError(
                f"Invalid operator '{operator}'. "
                f"Valid operators: {', '.join(sorted(VALID_OPERATORS))}"
            )

        if op in ("IN", "NOT IN"):
            if not isinstance(value, (list, tuple, set)):
                raise ValueError(f"Operator '{op}' requires a list/tuple/set of values.")
            formatted_values = ", ".join(_format_value(v) for v in value)
            clause = f"{field} {op} ({formatted_values})"
        else:
            clause = f"{field} {op} {_format_value(value)}"

        self._where_clauses.append(clause)
        return self

    def where_null(self, field: str) -> SOQLBuilder:
        """Add a WHERE field = NULL condition."""
        self._where_clauses.append(f"{field} = NULL")
        return self

    def where_not_null(self, field: str) -> SOQLBuilder:
        """Add a WHERE field != NULL condition."""
        self._where_clauses.append(f"{field} != NULL")
        return self

    def where_in(self, field: str, values: List[Any]) -> SOQLBuilder:
        """Add a WHERE field IN (...) condition."""
        return self.where(field, "IN", values)

    def where_not_in(self, field: str, values: List[Any]) -> SOQLBuilder:
        """Add a WHERE field NOT IN (...) condition."""
        return self.where(field, "NOT IN", values)

    def where_subquery(self, field: str, operator: str, subquery: str) -> SOQLBuilder:
        """
        Add a WHERE condition using a subquery.

        Example:
            .where_subquery("Id", "IN",
                "SELECT Work_Item__c FROM Time_Entry__c WHERE Hours__c > 4")
        """
        op = operator.upper().strip()
        if op not in ("IN", "NOT IN"):
            raise ValueError("Subquery operator must be 'IN' or 'NOT IN'.")
        self._where_clauses.append(f"{field} {op} ({subquery})")
        return self

    def where_raw(self, clause: str) -> SOQLBuilder:
        """Add a raw WHERE clause string (for complex conditions)."""
        self._where_clauses.append(clause)
        return self

    def group_by(self, fields: Union[str, List[str]]) -> SOQLBuilder:
        """Set the GROUP BY clause."""
        if isinstance(fields, str):
            fields = [f.strip() for f in fields.split(",")]
        self._group_by_fields.extend(fields)
        return self

    def having(self, clause: str) -> SOQLBuilder:
        """Add a HAVING clause (used with GROUP BY)."""
        self._having_clauses.append(clause)
        return self

    def order_by(self, field: str, direction: str = "ASC") -> SOQLBuilder:
        """Add an ORDER BY clause. Direction must be ASC or DESC."""
        direction = direction.upper().strip()
        if direction not in ("ASC", "DESC"):
            raise ValueError(f"Invalid order direction '{direction}'. Use 'ASC' or 'DESC'.")
        self._order_by_clauses.append(f"{field} {direction}")
        return self

    def limit(self, n: int) -> SOQLBuilder:
        """Set the LIMIT. Must be between 1 and 50000."""
        if not (1 <= n <= 50000):
            raise ValueError(f"LIMIT must be between 1 and 50000, got {n}.")
        self._limit = n
        return self

    def offset(self, n: int) -> SOQLBuilder:
        """Set the OFFSET. Must be between 0 and 2000."""
        if not (0 <= n <= 2000):
            raise ValueError(f"OFFSET must be between 0 and 2000, got {n}.")
        self._offset = n
        return self

    def build(self) -> str:
        """
        Build and return the SOQL query string.

        Raises ValueError if required clauses (SELECT, FROM) are missing.
        """
        if not self._select_fields:
            raise ValueError("SELECT clause is required. Call .select() first.")
        if not self._from:
            raise ValueError("FROM clause is required. Call .from_object() first.")

        parts = [f"SELECT {', '.join(self._select_fields)}"]
        parts.append(f"FROM {self._from}")

        if self._where_clauses:
            parts.append(f"WHERE {' AND '.join(self._where_clauses)}")

        if self._group_by_fields:
            parts.append(f"GROUP BY {', '.join(self._group_by_fields)}")

        if self._having_clauses:
            parts.append(f"HAVING {' AND '.join(self._having_clauses)}")

        if self._order_by_clauses:
            parts.append(f"ORDER BY {', '.join(self._order_by_clauses)}")

        if self._limit is not None:
            parts.append(f"LIMIT {self._limit}")

        if self._offset is not None:
            parts.append(f"OFFSET {self._offset}")

        return " ".join(parts)

    def __str__(self) -> str:
        return self.build()

    def __repr__(self) -> str:
        return f"SOQLBuilder(select={self._select_fields}, from={self._from})"
