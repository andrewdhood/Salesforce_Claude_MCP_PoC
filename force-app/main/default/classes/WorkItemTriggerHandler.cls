public with sharing class WorkItemTriggerHandler {

    public static void handleBeforeUpdate(List<Work_Item__c> newList, Map<Id, Work_Item__c> oldMap) {
        for (Work_Item__c wi : newList) {
            Work_Item__c oldWi = oldMap.get(wi.Id);

            if (wi.Status__c == 'Done' && oldWi.Status__c != 'Done') {
                wi.Completed_Date__c = Date.today();
            } else if (wi.Status__c != 'Done' && oldWi.Status__c == 'Done') {
                wi.Completed_Date__c = null;
            }
        }
    }
}
