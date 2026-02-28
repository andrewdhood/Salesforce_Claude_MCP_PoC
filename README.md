# Salesforce Project Management MCP Integration

A proof-of-concept that connects Salesforce custom objects to Claude via the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), enabling natural-language project management, time tracking, and analytics through conversational AI.

## Overview

This project deploys a lightweight project management data model into a Salesforce org and exposes it through a Python-based MCP server. Claude can then query, create, and update records, log time entries, and surface analytics -- all through natural conversation.

### What You Can Do

- **Manage work items** -- create tasks, update statuses, assign team members
- **Log time** -- record hours against work items with date and notes
- **Track project health** -- view summaries with completion rates, hour burn-down, and blocked-item counts
- **Run analytics** -- estimate accuracy, weekly utilization, velocity trends, scope estimation, and daily hour budgets

## Architecture

```
Claude <--MCP (stdio)--> Python MCP Server <--REST API--> Salesforce Org
                              |
                        simple_salesforce
```

The MCP server runs locally and communicates with Claude over stdio. It authenticates to Salesforce using either an access token (from `sf org display`) or username/password credentials, and calls the Salesforce REST API via `simple_salesforce`.

## Data Model

Three custom objects form a master-detail cascade:

```
Project__c  (1)──────(*)  Work_Item__c  (1)──────(*)  Time_Entry__c
```

### Project__c

| Field | Type | Notes |
|-------|------|-------|
| Name | Text | Project name (required) |
| Status__c | Picklist | Active, Complete, On Hold (default: Active) |
| Client__c | Text(100) | Client or stakeholder |
| Start_Date__c | Date | Project start |
| End_Date__c | Date | Project end |
| Total_Estimated_Hours__c | Roll-Up Summary | SUM of Work_Item__c.Estimated_Hours__c |
| Total_Actual_Hours__c | Roll-Up Summary | SUM of Work_Item__c.Actual_Hours__c |
| Work_Item_Count__c | Roll-Up Summary | COUNT of Work_Item__c |

**Validation**: End_Date__c must be after Start_Date__c.

### Work_Item__c

| Field | Type | Notes |
|-------|------|-------|
| Name | Auto-Number | Format: WI-{0000} |
| Project__c | Master-Detail | Links to Project__c (reparentable) |
| Assigned_To__c | Lookup(User) | Team member assignment |
| Status__c | Picklist | To Do, In Progress, Done, Blocked (default: To Do) |
| Priority__c | Picklist | P1-Critical, P2-High, P3-Medium, P4-Low (default: P3) |
| Type__c | Picklist | Development, Configuration, Testing, Documentation, Data Migration, Integration |
| Estimated_Hours__c | Number(5,1) | Planned effort |
| Actual_Hours__c | Roll-Up Summary | SUM of Time_Entry__c.Hours__c |
| Due_Date__c | Date | Target completion |
| Completed_Date__c | Date | Auto-set by trigger when Status = Done |
| Description__c | Long Text(5000) | Details and acceptance criteria |

**Validation**: Completed_Date__c requires Status__c = "Done".
**Trigger**: WorkItemTrigger auto-populates Completed_Date__c when status changes to/from Done.

### Time_Entry__c

| Field | Type | Notes |
|-------|------|-------|
| Name | Auto-Number | Format: TE-{0000} |
| Work_Item__c | Master-Detail | Links to Work_Item__c |
| Hours__c | Number(4,2) | Hours logged (required) |
| Date__c | Date | Date of work (required) |
| Notes__c | Text(255) | Description of work performed |

**Validations**: Hours must be > 0 and <= 24.

## MCP Server Tools

The server exposes 12 tools organized into three categories:

### Core Tools

| Tool | Description |
|------|-------------|
| `sf_get_my_work_items` | List work items with optional filters (status, priority, project, assignee) |
| `sf_log_time` | Create a time entry against a work item |
| `sf_update_work_item_status` | Change work item status with optional comment |
| `sf_get_project_summary` | Comprehensive project dashboard with metrics |

### Analytics Tools

| Tool | Description |
|------|-------------|
| `sf_estimate_accuracy` | Compare estimated vs. actual hours across completed items |
| `sf_weekly_utilization` | Hours logged per person per week |
| `sf_velocity_trend` | Items completed per week over time |
| `sf_scope_estimate` | Estimate remaining effort and projected completion |
| `sf_daily_budget` | Calculate recommended daily hours to meet a deadline |

### Generic Tools

| Tool | Description |
|------|-------------|
| `sf_query` | Execute arbitrary SOQL queries |
| `sf_aggregate` | Run aggregate SOQL (COUNT, SUM, AVG, etc.) |
| `sf_describe_object` | Get field metadata for any Salesforce object |

## Project Structure

```
devOrgAgentforce/
├── sfdx-project.json                  # SFDX project config (API v63.0)
├── CLAUDE.md                          # Auto-generated schema reference for Claude
├── force-app/main/default/
│   ├── objects/
│   │   ├── Project__c/               # Object, 7 fields, 2 list views, 1 validation rule
│   │   ├── Work_Item__c/             # Object, 10 fields, 4 list views, 1 validation rule
│   │   └── Time_Entry__c/            # Object, 4 fields, 2 list views, 2 validation rules
│   ├── layouts/                       # Page layouts for all three objects
│   ├── permissionsets/                # Project_Management_User permission set
│   ├── tabs/                          # Custom tabs for all three objects
│   ├── triggers/                      # WorkItemTrigger (before update)
│   └── classes/                       # WorkItemTriggerHandler + test class
├── mcp-server/
│   ├── server.py                      # MCP server with 12 tools
│   ├── soql_builder.py                # Fluent SOQL query builder
│   ├── dump_schema.py                 # Generates CLAUDE.md from org metadata
│   ├── requirements.txt               # Python dependencies
│   ├── .env.example                   # Credential template
│   └── .env                           # Actual credentials (git-ignored)
├── scripts/
│   └── seed-data/
│       └── seed.apex                  # Anonymous Apex: 3 projects, 22 work items, 43 time entries
└── src/
    └── package.xml                    # Legacy Metadata API manifest
```

## Prerequisites

- **Salesforce**: A Developer Edition or scratch org
- **Salesforce CLI** (`sf`): For deploying metadata and executing Apex
- **Python 3.10+**: For the MCP server
- **Claude Desktop** or **Claude Code**: For connecting to the MCP server

## Setup

### 1. Deploy Metadata to Salesforce

```bash
# Authenticate to your org
sf org login web --alias devOrgAgentforce

# Deploy all metadata
sf project deploy start --source-dir force-app/main/default --target-org devOrgAgentforce
```

### 2. Assign the Permission Set

```bash
sf org assign permset \
  --name Project_Management_User \
  --target-org devOrgAgentforce
```

### 3. Load Seed Data

```bash
sf apex run \
  --file scripts/seed-data/seed.apex \
  --target-org devOrgAgentforce
```

This creates 3 projects, 22 work items, and 43 time entries with realistic distributions across statuses and priorities.

### 4. Configure the MCP Server

```bash
cd mcp-server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create your `.env` file using one of two authentication methods:

**Option A: Access Token (recommended for development)**

```bash
# Get credentials from Salesforce CLI
sf org display --target-org devOrgAgentforce --json
```

Then populate `.env`:

```env
SF_ACCESS_TOKEN=<accessToken from above>
SF_INSTANCE_URL=<instanceUrl from above>
```

**Option B: Username/Password**

```env
SF_USERNAME=your_username@example.com
SF_PASSWORD=your_password
SF_SECURITY_TOKEN=your_security_token
SF_DOMAIN=login
```

### 5. Connect to Claude

Add the server to your Claude configuration:

**Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "salesforce-pm": {
      "command": "/path/to/mcp-server/.venv/bin/python",
      "args": ["/path/to/mcp-server/server.py"]
    }
  }
}
```

**Claude Code** (`.mcp.json` in project root):

```json
{
  "mcpServers": {
    "salesforce-pm": {
      "command": "/path/to/mcp-server/.venv/bin/python",
      "args": ["/path/to/mcp-server/server.py"]
    }
  }
}
```

## Usage Examples

Once connected, you can interact with your Salesforce data through natural conversation:

- *"Show me all blocked work items"*
- *"Log 3 hours against WI-0012 for today -- worked on API integration"*
- *"Give me a summary of the Website Redesign project"*
- *"How accurate are our estimates across completed items?"*
- *"What's the team's utilization this week?"*
- *"Run a velocity trend for the last 4 weeks"*
- *"How many hours per day do we need to finish the Mobile App project by March 15?"*

## Regenerating CLAUDE.md

The `CLAUDE.md` file provides Claude with detailed schema context. To regenerate it after org changes:

```bash
cd mcp-server
source .venv/bin/activate
python dump_schema.py
```

This introspects the org's metadata and writes a comprehensive field-level reference to `../CLAUDE.md`.

## Testing

The Apex trigger has a dedicated test class with 100% coverage:

```bash
sf apex run test \
  --class-names WorkItemTriggerHandlerTest \
  --result-format human \
  --target-org devOrgAgentforce
```

Four test methods cover:
1. Status change to Done sets Completed_Date__c
2. Status change away from Done clears Completed_Date__c
3. Non-status updates leave Completed_Date__c unchanged
4. Bulk operations (200 records)

## Key Technical Decisions

- **Master-Detail relationships** provide cascade delete and roll-up summaries without custom Apex aggregation
- **Auto-Number name fields** on Work_Item__c and Time_Entry__c give human-readable IDs (WI-0001, TE-0001)
- **Lazy Salesforce connection** in the MCP server avoids connection failures at import time when credentials are not yet configured
- **SOQLBuilder** provides a fluent, injection-safe query builder that validates field names and escapes string values
- **Access token auth** lets developers reuse their existing SF CLI session without managing passwords

## License

This project is a proof-of-concept for demonstration and educational purposes.
