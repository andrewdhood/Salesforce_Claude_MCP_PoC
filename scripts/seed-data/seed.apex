// =============================================================================
// Project Management Seed Data Script
// Run via: sf apex run --file scripts/seed-data/seed.apex
// Date context: today is 2026-02-28
// =============================================================================

// Clean up any existing seed data to allow re-runs
delete [SELECT Id FROM Time_Entry__c];
delete [SELECT Id FROM Work_Item__c];
delete [SELECT Id FROM Project__c];

Id currentUserId = UserInfo.getUserId();

// =============================================================================
// 1. CREATE PROJECTS
// =============================================================================

Project__c acmeCRM = new Project__c(
    Name = 'Acme CRM Implementation',
    Client__c = 'Acme Corp',
    Status__c = 'Active',
    Start_Date__c = Date.newInstance(2026, 1, 6),
    End_Date__c = Date.newInstance(2026, 4, 30)
);

Project__c widgetMigration = new Project__c(
    Name = 'Widget Co Data Migration',
    Client__c = 'Widget Co',
    Status__c = 'Active',
    Start_Date__c = Date.newInstance(2026, 2, 1),
    End_Date__c = Date.newInstance(2026, 3, 31)
);

Project__c internalTool = new Project__c(
    Name = 'Internal Tool Modernization',
    Client__c = 'Internal',
    Status__c = 'On Hold',
    Start_Date__c = Date.newInstance(2025, 11, 1),
    End_Date__c = Date.newInstance(2026, 6, 30)
);

List<Project__c> projects = new List<Project__c>{ acmeCRM, widgetMigration, internalTool };
insert projects;

System.debug('Inserted ' + projects.size() + ' projects');

// =============================================================================
// 2. CREATE WORK ITEMS (22 total)
// =============================================================================

List<Work_Item__c> workItems = new List<Work_Item__c>();

// ---- PROJECT 1: Acme CRM Implementation (10 work items) ----

// WI-1: Done - Development - actual ~1.3x estimate
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Build custom Lead scoring engine with Apex triggers and batch processing',
    Status__c = 'Done',
    Priority__c = 'P1 - Critical',
    Type__c = 'Development',
    Estimated_Hours__c = 20,

    Due_Date__c = Date.newInstance(2026, 2, 6),
    Completed_Date__c = Date.newInstance(2026, 2, 8),
    Assigned_To__c = currentUserId
));

// WI-2: Done - Configuration - actual ~0.9x estimate
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Configure Opportunity stages, record types, and page layouts for sales team',
    Status__c = 'Done',
    Priority__c = 'P2 - High',
    Type__c = 'Configuration',
    Estimated_Hours__c = 12,

    Due_Date__c = Date.newInstance(2026, 1, 23),
    Completed_Date__c = Date.newInstance(2026, 1, 22),
    Assigned_To__c = currentUserId
));

// WI-3: In Progress - Development
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Develop email-to-case automation with custom routing rules',
    Status__c = 'In Progress',
    Priority__c = 'P1 - Critical',
    Type__c = 'Development',
    Estimated_Hours__c = 16,
    Due_Date__c = Date.newInstance(2026, 3, 6),
    Assigned_To__c = currentUserId
));

// WI-4: In Progress - Integration
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Build REST API integration with Acme ERP system for account sync',
    Status__c = 'In Progress',
    Priority__c = 'P2 - High',
    Type__c = 'Integration',
    Estimated_Hours__c = 24,
    Due_Date__c = Date.newInstance(2026, 3, 13),
    Assigned_To__c = currentUserId
));

// WI-5: In Progress - Testing
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Write unit tests for Lead scoring engine - target 90% coverage',
    Status__c = 'In Progress',
    Priority__c = 'P2 - High',
    Type__c = 'Testing',
    Estimated_Hours__c = 10,
    Due_Date__c = Date.newInstance(2026, 3, 6),
    Assigned_To__c = currentUserId
));

// WI-6: To Do - Documentation
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Create end-user training guide and admin runbook for CRM workflows',
    Status__c = 'To Do',
    Priority__c = 'P3 - Medium',
    Type__c = 'Documentation',
    Estimated_Hours__c = 8,
    Due_Date__c = Date.newInstance(2026, 4, 10),
    Assigned_To__c = currentUserId
));

// WI-7: To Do - Configuration
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Set up dashboards and reports for sales leadership team',
    Status__c = 'To Do',
    Priority__c = 'P3 - Medium',
    Type__c = 'Configuration',
    Estimated_Hours__c = 6,
    Due_Date__c = Date.newInstance(2026, 3, 27),
    Assigned_To__c = currentUserId
));

// WI-8: Blocked - Integration
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Connect Marketing Cloud for campaign tracking - waiting on Acme API credentials',
    Status__c = 'Blocked',
    Priority__c = 'P2 - High',
    Type__c = 'Integration',
    Estimated_Hours__c = 14,
    Due_Date__c = Date.newInstance(2026, 3, 20),
    Assigned_To__c = currentUserId
));

// WI-9: In Progress - Development
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'Build custom Lightning Web Component for account hierarchy visualization',
    Status__c = 'In Progress',
    Priority__c = 'P3 - Medium',
    Type__c = 'Development',
    Estimated_Hours__c = 18,
    Due_Date__c = Date.newInstance(2026, 3, 20),
    Assigned_To__c = currentUserId
));

// WI-10: To Do - Testing
workItems.add(new Work_Item__c(
    Project__c = acmeCRM.Id,
    Description__c = 'UAT coordination and test script preparation for Acme stakeholders',
    Status__c = 'To Do',
    Priority__c = 'P2 - High',
    Type__c = 'Testing',
    Estimated_Hours__c = 12,
    Due_Date__c = Date.newInstance(2026, 4, 17),
    Assigned_To__c = currentUserId
));

// ---- PROJECT 2: Widget Co Data Migration (8 work items) ----

// WI-11: Done - Data Migration - actual ~1.5x estimate
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Extract and cleanse Account and Contact data from legacy Oracle database',
    Status__c = 'Done',
    Priority__c = 'P1 - Critical',
    Type__c = 'Data Migration',
    Estimated_Hours__c = 16,

    Due_Date__c = Date.newInstance(2026, 2, 14),
    Completed_Date__c = Date.newInstance(2026, 2, 16),
    Assigned_To__c = currentUserId
));

// WI-12: Done - Development - actual ~1.3x estimate
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Develop Apex data loader batch jobs for high-volume record import',
    Status__c = 'Done',
    Priority__c = 'P1 - Critical',
    Type__c = 'Development',
    Estimated_Hours__c = 14,

    Due_Date__c = Date.newInstance(2026, 2, 20),
    Completed_Date__c = Date.newInstance(2026, 2, 21),
    Assigned_To__c = currentUserId
));

// WI-13: In Progress - Data Migration
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Migrate Opportunity and Product data with historical close dates preserved',
    Status__c = 'In Progress',
    Priority__c = 'P1 - Critical',
    Type__c = 'Data Migration',
    Estimated_Hours__c = 20,
    Due_Date__c = Date.newInstance(2026, 3, 6),
    Assigned_To__c = currentUserId
));

// WI-14: In Progress - Testing
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Validate migrated data integrity - row counts, field mappings, relationships',
    Status__c = 'In Progress',
    Priority__c = 'P2 - High',
    Type__c = 'Testing',
    Estimated_Hours__c = 10,
    Due_Date__c = Date.newInstance(2026, 3, 13),
    Assigned_To__c = currentUserId
));

// WI-15: To Do - Data Migration
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Migrate attachments and file history from legacy document management system',
    Status__c = 'To Do',
    Priority__c = 'P3 - Medium',
    Type__c = 'Data Migration',
    Estimated_Hours__c = 12,
    Due_Date__c = Date.newInstance(2026, 3, 20),
    Assigned_To__c = currentUserId
));

// WI-16: Blocked - Integration
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Set up ongoing data sync between Widget Co ERP and Salesforce - awaiting VPN tunnel',
    Status__c = 'Blocked',
    Priority__c = 'P2 - High',
    Type__c = 'Integration',
    Estimated_Hours__c = 16,
    Due_Date__c = Date.newInstance(2026, 3, 13),
    Assigned_To__c = currentUserId
));

// WI-17: In Progress - Documentation
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Document data mapping specifications and transformation rules',
    Status__c = 'In Progress',
    Priority__c = 'P3 - Medium',
    Type__c = 'Documentation',
    Estimated_Hours__c = 6,
    Due_Date__c = Date.newInstance(2026, 2, 28),
    Assigned_To__c = currentUserId
));

// WI-18: Done - Configuration - actual ~0.9x estimate
workItems.add(new Work_Item__c(
    Project__c = widgetMigration.Id,
    Description__c = 'Configure field mappings and validation rules for imported records',
    Status__c = 'Done',
    Priority__c = 'P2 - High',
    Type__c = 'Configuration',
    Estimated_Hours__c = 8,

    Due_Date__c = Date.newInstance(2026, 2, 10),
    Completed_Date__c = Date.newInstance(2026, 2, 9),
    Assigned_To__c = currentUserId
));

// ---- PROJECT 3: Internal Tool Modernization (4 work items) ----

// WI-19: In Progress - Development
workItems.add(new Work_Item__c(
    Project__c = internalTool.Id,
    Description__c = 'Refactor legacy Visualforce pages to Lightning Web Components',
    Status__c = 'In Progress',
    Priority__c = 'P3 - Medium',
    Type__c = 'Development',
    Estimated_Hours__c = 30,
    Due_Date__c = Date.newInstance(2026, 4, 30),
    Assigned_To__c = currentUserId
));

// WI-20: To Do - Development
workItems.add(new Work_Item__c(
    Project__c = internalTool.Id,
    Description__c = 'Build new employee onboarding flow with screen flows and approval process',
    Status__c = 'To Do',
    Priority__c = 'P4 - Low',
    Type__c = 'Development',
    Estimated_Hours__c = 20,
    Due_Date__c = Date.newInstance(2026, 5, 29),
    Assigned_To__c = currentUserId
));

// WI-21: Done - Documentation - treat like Configuration pattern ~0.9x
workItems.add(new Work_Item__c(
    Project__c = internalTool.Id,
    Description__c = 'Audit existing internal tools and document technical debt backlog',
    Status__c = 'Done',
    Priority__c = 'P3 - Medium',
    Type__c = 'Documentation',
    Estimated_Hours__c = 10,

    Due_Date__c = Date.newInstance(2025, 12, 19),
    Completed_Date__c = Date.newInstance(2025, 12, 18),
    Assigned_To__c = currentUserId
));

// WI-22: In Progress - Configuration
workItems.add(new Work_Item__c(
    Project__c = internalTool.Id,
    Description__c = 'Configure new Lightning App with custom navigation and permission sets',
    Status__c = 'In Progress',
    Priority__c = 'P4 - Low',
    Type__c = 'Configuration',
    Estimated_Hours__c = 8,
    Due_Date__c = Date.newInstance(2026, 3, 27),
    Assigned_To__c = currentUserId
));

insert workItems;

System.debug('Inserted ' + workItems.size() + ' work items');

// =============================================================================
// 3. QUERY BACK WORK ITEMS TO GET IDs
//    (Auto-number names mean we must identify by Project + Description)
// =============================================================================

// Build a map of Description -> Work_Item__c for easy lookup when creating time entries
Map<String, Work_Item__c> wiByDesc = new Map<String, Work_Item__c>();
for (Work_Item__c wi : [
    SELECT Id, Description__c, Status__c, Project__c
    FROM Work_Item__c
    WHERE Project__c IN :projects
]) {
    wiByDesc.put(wi.Description__c, wi);
}

// Helper references by description prefix (first 30 chars are unique enough)
// We will reference work items by their list index from above:
// Index 0  = WI-1:  Lead scoring engine (Done, Dev)
// Index 1  = WI-2:  Configure Opportunity stages (Done, Config)
// Index 2  = WI-3:  Email-to-case automation (In Progress, Dev)
// Index 3  = WI-4:  REST API integration (In Progress, Integration)
// Index 4  = WI-5:  Unit tests for Lead scoring (In Progress, Testing)
// Index 5  = WI-6:  Training guide (To Do) - no time entries
// Index 6  = WI-7:  Dashboards (To Do) - no time entries
// Index 7  = WI-8:  Marketing Cloud (Blocked) - no time entries
// Index 8  = WI-9:  Account hierarchy LWC (In Progress, Dev)
// Index 9  = WI-10: UAT coordination (To Do) - no time entries
// Index 10 = WI-11: Extract Account data (Done, Data Migration)
// Index 11 = WI-12: Apex data loader batch (Done, Dev)
// Index 12 = WI-13: Migrate Opportunity data (In Progress, Data Migration)
// Index 13 = WI-14: Validate migrated data (In Progress, Testing)
// Index 14 = WI-15: Migrate attachments (To Do) - no time entries
// Index 15 = WI-16: Ongoing data sync (Blocked) - no time entries
// Index 16 = WI-17: Data mapping docs (In Progress, Documentation)
// Index 17 = WI-18: Field mappings config (Done, Config)
// Index 18 = WI-19: Refactor VF to LWC (In Progress, Dev)
// Index 19 = WI-20: Employee onboarding (To Do) - no time entries
// Index 20 = WI-21: Audit internal tools (Done, Documentation)
// Index 21 = WI-22: Lightning App config (In Progress, Config)

// =============================================================================
// 4. CREATE TIME ENTRIES (~50 total)
//    Spread across 2026-02-02 through 2026-02-27 (4 weeks of weekdays)
//    Done and In Progress items get 2-5 entries each
// =============================================================================

List<Time_Entry__c> timeEntries = new List<Time_Entry__c>();

// --- WI-1: Lead scoring engine (Done, 26 actual hrs) - 5 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[0].Id,
    Date__c = Date.newInstance(2026, 2, 2),
    Hours__c = 6.0,
    Notes__c = 'Initial scaffold of LeadScoringEngine class and trigger framework'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[0].Id,
    Date__c = Date.newInstance(2026, 2, 3),
    Hours__c = 5.0,
    Notes__c = 'Implemented scoring criteria: demographic and behavioral rules'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[0].Id,
    Date__c = Date.newInstance(2026, 2, 4),
    Hours__c = 6.0,
    Notes__c = 'Built batch processing for historical lead rescoring'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[0].Id,
    Date__c = Date.newInstance(2026, 2, 5),
    Hours__c = 5.0,
    Notes__c = 'Bug fixes for null pointer edge cases and bulk trigger handling'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[0].Id,
    Date__c = Date.newInstance(2026, 2, 6),
    Hours__c = 4.0,
    Notes__c = 'Code review feedback and final refactoring'
));

// --- WI-2: Configure Opportunity stages (Done, 11 actual hrs) - 3 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[1].Id,
    Date__c = Date.newInstance(2026, 2, 2),
    Hours__c = 4.0,
    Notes__c = 'Configured Opportunity stages and probability mappings'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[1].Id,
    Date__c = Date.newInstance(2026, 2, 3),
    Hours__c = 4.0,
    Notes__c = 'Created record types and assigned page layouts per sales role'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[1].Id,
    Date__c = Date.newInstance(2026, 2, 4),
    Hours__c = 3.0,
    Notes__c = 'Validated stage transitions with Acme sales team leads'
));

// --- WI-3: Email-to-case automation (In Progress) - 3 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[2].Id,
    Date__c = Date.newInstance(2026, 2, 16),
    Hours__c = 3.0,
    Notes__c = 'Set up Email-to-Case and initial routing rules'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[2].Id,
    Date__c = Date.newInstance(2026, 2, 17),
    Hours__c = 4.0,
    Notes__c = 'Developed custom case assignment logic based on product line'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[2].Id,
    Date__c = Date.newInstance(2026, 2, 18),
    Hours__c = 2.5,
    Notes__c = 'Handling edge cases for forwarded and CC emails'
));

// --- WI-4: REST API integration (In Progress) - 4 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[3].Id,
    Date__c = Date.newInstance(2026, 2, 9),
    Hours__c = 3.0,
    Notes__c = 'Reviewed Acme ERP API documentation and authentication flow'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[3].Id,
    Date__c = Date.newInstance(2026, 2, 10),
    Hours__c = 4.0,
    Notes__c = 'Built callout service class and named credential configuration'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[3].Id,
    Date__c = Date.newInstance(2026, 2, 11),
    Hours__c = 3.5,
    Notes__c = 'Implemented account upsert logic from ERP payload'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[3].Id,
    Date__c = Date.newInstance(2026, 2, 24),
    Hours__c = 2.0,
    Notes__c = 'Added retry logic and error handling for timeout scenarios'
));

// --- WI-5: Unit tests for Lead scoring (In Progress) - 2 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[4].Id,
    Date__c = Date.newInstance(2026, 2, 23),
    Hours__c = 3.0,
    Notes__c = 'Created test data factory and positive test scenarios'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[4].Id,
    Date__c = Date.newInstance(2026, 2, 24),
    Hours__c = 2.5,
    Notes__c = 'Added negative and bulk test cases for governor limits'
));

// --- WI-9: Account hierarchy LWC (In Progress) - 3 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[8].Id,
    Date__c = Date.newInstance(2026, 2, 19),
    Hours__c = 4.0,
    Notes__c = 'Designed component wireframes and data model for hierarchy tree'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[8].Id,
    Date__c = Date.newInstance(2026, 2, 20),
    Hours__c = 5.0,
    Notes__c = 'Built LWC tree grid with lazy-loading child accounts'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[8].Id,
    Date__c = Date.newInstance(2026, 2, 25),
    Hours__c = 3.0,
    Notes__c = 'Added expand/collapse state management and search filter'
));

// --- WI-11: Extract Account data from Oracle (Done, 24 actual hrs) - 4 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[10].Id,
    Date__c = Date.newInstance(2026, 2, 9),
    Hours__c = 6.0,
    Notes__c = 'Connected to Oracle instance and mapped source tables to Salesforce objects'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[10].Id,
    Date__c = Date.newInstance(2026, 2, 10),
    Hours__c = 7.0,
    Notes__c = 'Data cleansing: deduplicated accounts, standardized phone and address formats'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[10].Id,
    Date__c = Date.newInstance(2026, 2, 11),
    Hours__c = 6.0,
    Notes__c = 'Contact extraction and parent account relationship mapping'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[10].Id,
    Date__c = Date.newInstance(2026, 2, 12),
    Hours__c = 5.0,
    Notes__c = 'Final validation of extracted dataset and reconciliation with source'
));

// --- WI-12: Apex data loader batch jobs (Done, 18 actual hrs) - 4 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[11].Id,
    Date__c = Date.newInstance(2026, 2, 16),
    Hours__c = 4.0,
    Notes__c = 'Designed batch architecture with configurable scope size'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[11].Id,
    Date__c = Date.newInstance(2026, 2, 17),
    Hours__c = 5.0,
    Notes__c = 'Implemented AccountImportBatch and ContactImportBatch classes'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[11].Id,
    Date__c = Date.newInstance(2026, 2, 18),
    Hours__c = 5.0,
    Notes__c = 'Built error logging and partial success handling'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[11].Id,
    Date__c = Date.newInstance(2026, 2, 19),
    Hours__c = 4.0,
    Notes__c = 'Performance tuning - reduced batch execution time by 40%'
));

// --- WI-13: Migrate Opportunity data (In Progress) - 3 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[12].Id,
    Date__c = Date.newInstance(2026, 2, 23),
    Hours__c = 4.0,
    Notes__c = 'Mapped Opportunity fields from legacy schema to Salesforce model'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[12].Id,
    Date__c = Date.newInstance(2026, 2, 24),
    Hours__c = 5.0,
    Notes__c = 'Migrated 3 years of historical Opportunity data with Products'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[12].Id,
    Date__c = Date.newInstance(2026, 2, 25),
    Hours__c = 3.0,
    Notes__c = 'Fixed currency conversion issues on international deal records'
));

// --- WI-14: Validate migrated data (In Progress) - 2 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[13].Id,
    Date__c = Date.newInstance(2026, 2, 25),
    Hours__c = 2.0,
    Notes__c = 'Built validation queries comparing row counts and checksums'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[13].Id,
    Date__c = Date.newInstance(2026, 2, 26),
    Hours__c = 3.0,
    Notes__c = 'Identified and logged 47 records with relationship mismatches'
));

// --- WI-17: Data mapping documentation (In Progress) - 2 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[16].Id,
    Date__c = Date.newInstance(2026, 2, 20),
    Hours__c = 2.0,
    Notes__c = 'Drafted field mapping spreadsheet for Account and Contact objects'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[16].Id,
    Date__c = Date.newInstance(2026, 2, 26),
    Hours__c = 1.5,
    Notes__c = 'Added transformation rules and default value documentation'
));

// --- WI-18: Field mappings config (Done, 7 actual hrs) - 2 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[17].Id,
    Date__c = Date.newInstance(2026, 2, 5),
    Hours__c = 4.0,
    Notes__c = 'Set up field mappings and picklist value translations'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[17].Id,
    Date__c = Date.newInstance(2026, 2, 6),
    Hours__c = 3.0,
    Notes__c = 'Configured validation rules to catch bad data on import'
));

// --- WI-19: Refactor VF to LWC (In Progress) - 3 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[18].Id,
    Date__c = Date.newInstance(2026, 2, 3),
    Hours__c = 3.0,
    Notes__c = 'Inventoried all Visualforce pages and prioritized migration order'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[18].Id,
    Date__c = Date.newInstance(2026, 2, 4),
    Hours__c = 4.0,
    Notes__c = 'Converted TimeTracker VF page to LWC with reactive data binding'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[18].Id,
    Date__c = Date.newInstance(2026, 2, 12),
    Hours__c = 3.5,
    Notes__c = 'Migrated ProjectDashboard VF page including chart components'
));

// --- WI-21: Audit internal tools (Done, 9 actual hrs) - 2 entries ---
// Note: this was completed in Dec 2025, but time entries are within our 4-week window
// We will log entries in the earlier part of February to represent final wrap-up review
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[20].Id,
    Date__c = Date.newInstance(2026, 2, 2),
    Hours__c = 1.0,
    Notes__c = 'Final review of technical debt backlog and priority classification'
));

// --- WI-22: Lightning App config (In Progress) - 2 entries ---
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[21].Id,
    Date__c = Date.newInstance(2026, 2, 13),
    Hours__c = 2.0,
    Notes__c = 'Created Lightning App and configured utility bar items'
));
timeEntries.add(new Time_Entry__c(
    Work_Item__c = workItems[21].Id,
    Date__c = Date.newInstance(2026, 2, 27),
    Hours__c = 1.5,
    Notes__c = 'Set up permission sets and assigned to internal user profiles'
));

insert timeEntries;

System.debug('Inserted ' + timeEntries.size() + ' time entries');

// =============================================================================
// 5. SUMMARY
// =============================================================================

System.debug('====================================');
System.debug('SEED DATA COMPLETE');
System.debug('====================================');
System.debug('Projects created:    ' + projects.size());
System.debug('Work Items created:  ' + workItems.size());
System.debug('Time Entries created: ' + timeEntries.size());
System.debug('====================================');

// Status distribution verification
Integer doneCount = 0, inProgressCount = 0, toDoCount = 0, blockedCount = 0;
for (Work_Item__c wi : workItems) {
    if (wi.Status__c == 'Done') doneCount++;
    else if (wi.Status__c == 'In Progress') inProgressCount++;
    else if (wi.Status__c == 'To Do') toDoCount++;
    else if (wi.Status__c == 'Blocked') blockedCount++;
}
System.debug('Work Item Status Distribution:');
System.debug('  Done:        ' + doneCount);
System.debug('  In Progress: ' + inProgressCount);
System.debug('  To Do:       ' + toDoCount);
System.debug('  Blocked:     ' + blockedCount);
System.debug('====================================');
