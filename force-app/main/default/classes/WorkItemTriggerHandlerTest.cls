@IsTest
private class WorkItemTriggerHandlerTest {

    @TestSetup
    static void setupData() {
        Project__c project = new Project__c(Name = 'Test Project');
        insert project;
    }

    private static Project__c getProject() {
        return [SELECT Id FROM Project__c LIMIT 1];
    }

    @IsTest
    static void testStatusChangeToDoneSetsCompletedDate() {
        Project__c project = getProject();

        Work_Item__c wi = new Work_Item__c(
            Status__c = 'In Progress',
            Project__c = project.Id
        );
        insert wi;

        Test.startTest();
        wi.Status__c = 'Done';
        update wi;
        Test.stopTest();

        Work_Item__c updated = [SELECT Completed_Date__c FROM Work_Item__c WHERE Id = :wi.Id];
        System.assertEquals(Date.today(), updated.Completed_Date__c,
            'Completed_Date__c should be set to today when Status changes to Done');
    }

    @IsTest
    static void testStatusChangeFromDoneClearsCompletedDate() {
        Project__c project = getProject();

        Work_Item__c wi = new Work_Item__c(
            Status__c = 'Done',
            Project__c = project.Id
        );
        insert wi;

        // Manually set date since trigger only fires on update, not insert
        wi.Completed_Date__c = Date.today();
        update wi;

        Test.startTest();
        wi.Status__c = 'In Progress';
        update wi;
        Test.stopTest();

        Work_Item__c updated = [SELECT Completed_Date__c FROM Work_Item__c WHERE Id = :wi.Id];
        System.assertEquals(null, updated.Completed_Date__c,
            'Completed_Date__c should be cleared when Status changes away from Done');
    }

    @IsTest
    static void testStatusUnchangedDoesNotModifyCompletedDate() {
        Project__c project = getProject();

        Work_Item__c wi = new Work_Item__c(
            Status__c = 'In Progress',
            Project__c = project.Id
        );
        insert wi;

        Test.startTest();
        wi.Description__c = 'Updated description';
        update wi;
        Test.stopTest();

        Work_Item__c updated = [SELECT Completed_Date__c FROM Work_Item__c WHERE Id = :wi.Id];
        System.assertEquals(null, updated.Completed_Date__c,
            'Completed_Date__c should remain null when Status stays In Progress');
    }

    @IsTest
    static void testBulkStatusChangeToDone() {
        Project__c project = getProject();

        List<Work_Item__c> workItems = new List<Work_Item__c>();
        for (Integer i = 0; i < 200; i++) {
            workItems.add(new Work_Item__c(
                Status__c = 'In Progress',
                Project__c = project.Id
            ));
        }
        insert workItems;

        Test.startTest();
        for (Work_Item__c wi : workItems) {
            wi.Status__c = 'Done';
        }
        update workItems;
        Test.stopTest();

        List<Work_Item__c> updatedItems = [
            SELECT Completed_Date__c
            FROM Work_Item__c
            WHERE Id IN :workItems
        ];

        System.assertEquals(200, updatedItems.size(),
            'All 200 records should be returned');
        for (Work_Item__c wi : updatedItems) {
            System.assertEquals(Date.today(), wi.Completed_Date__c,
                'Each record should have Completed_Date__c set to today');
        }
    }
}
