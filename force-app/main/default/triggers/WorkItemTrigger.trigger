trigger WorkItemTrigger on Work_Item__c (before update) {
    WorkItemTriggerHandler.handleBeforeUpdate(Trigger.new, Trigger.oldMap);
}
