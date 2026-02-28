# Salesforce Org Schema Reference

Auto-generated on 2026-02-28 01:08:29 by `dump_schema.py`.

This document describes the Salesforce objects, fields, and relationships available in this org. Use it as context for building SOQL queries and understanding the data model.

## Table of Contents

- [Project (`Project__c`)](#project--c)
- [Work Item (`Work_Item__c`)](#work-item--c)
- [Time Entry (`Time_Entry__c`)](#time-entry--c)
- [User (`User`)](#user)
- [Record Type (`RecordType`)](#recordtype)
- [SOQL Quick Reference](#soql-quick-reference)

---

## Project (`Project__c`)

- **Key Prefix:** `a00`
- **Custom:** True
- **Createable:** True
- **Updateable:** True
- **Deletable:** True

### Fields

| API Name | Label | Type | Required | Updateable |
|----------|-------|------|----------|------------|
| `Client__c` | Client | string |  | Yes |
| `CreatedById` | Created By ID | reference(User) |  |  |
| `CreatedDate` | Created Date | datetime |  |  |
| `End_Date__c` | End Date | date |  | Yes |
| `Id` | Record ID | id |  |  |
| `IsDeleted` | Deleted | boolean |  |  |
| `LastActivityDate` | Last Activity Date | date |  |  |
| `LastModifiedById` | Last Modified By ID | reference(User) |  |  |
| `LastModifiedDate` | Last Modified Date | datetime |  |  |
| `LastReferencedDate` | Last Referenced Date | datetime |  |  |
| `LastViewedDate` | Last Viewed Date | datetime |  |  |
| `Name` | Project Name | string |  | Yes |
| `OwnerId` | Owner ID | reference(Group, User) | Yes | Yes |
| `Start_Date__c` | Start Date | date |  | Yes |
| `Status__c` | Status | picklist | Yes | Yes |
| `SystemModstamp` | System Modstamp | datetime |  |  |
| `Total_Actual_Hours__c` | Total Actual Hours | double(4,2) |  |  |
| `Total_Estimated_Hours__c` | Total Estimated Hours | double(5,1) |  |  |
| `Work_Item_Count__c` | Work Item Count | double(18,0) |  |  |

### Picklist Values

**Status__c** (Status):
- `Active` *(default)*
- `Complete`
- `On Hold`

### Relationships (Lookups)

- `CreatedById` -> **User** (relationship: `CreatedBy`)
- `LastModifiedById` -> **User** (relationship: `LastModifiedBy`)
- `OwnerId` -> **Group, User** (relationship: `Owner`)

### Child Relationships

- `ActivityHistories` -> `ActivityHistory.WhatId`
- `AttachedContentDocuments` -> `AttachedContentDocument.LinkedEntityId`
- `Attachments` -> `Attachment.ParentId`
- `CombinedAttachments` -> `CombinedAttachment.ParentId`
- `ContactRequests` -> `ContactRequest.WhatId`
- `ContentDocumentLinks` -> `ContentDocumentLink.LinkedEntityId`
- `DestinationFinanceTransactions` -> `FinanceTransaction.DestinationEntityId`
- `DuplicateRecordItems` -> `DuplicateRecordItem.RecordId`
- `Emails` -> `EmailMessage.RelatedToId`
- `Events` -> `Event.WhatId`
- `FeedSubscriptionsForEntity` -> `EntitySubscription.ParentId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.LegalEntityId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.ReferenceEntityId`
- `FinanceTransactions` -> `FinanceTransaction.LegalEntityId`
- `FinanceTransactions` -> `FinanceTransaction.ReferenceEntityId`
- `FlowOrchestrationWorkItems` -> `FlowOrchestrationWorkItem.RelatedRecordId`
- `Histories` -> `Project__History.ParentId`
- `InventoryReservationSources` -> `InventoryItemReservation.ItemReservationSourceId`
- `InventoryReservations` -> `InventoryReservation.ReservationSourceId`
- `Notes` -> `Note.ParentId`
- `NotesAndAttachments` -> `NoteAndAttachment.ParentId`
- `OpenActivities` -> `OpenActivity.WhatId`
- `ParentFinanceTransactions` -> `FinanceTransaction.ParentReferenceEntityId`
- `ProcessExceptions` -> `ProcessException.AttachedToId`
- `ProcessInstances` -> `ProcessInstance.TargetObjectId`
- `ProcessSteps` -> `ProcessInstanceHistory.TargetObjectId`
- `RecordActionHistories` -> `RecordActionHistory.ParentRecordId`
- `RecordActions` -> `RecordAction.RecordId`
- `RecordAssociatedGroups` -> `CollaborationGroupRecord.RecordId`
- `RelatedRecords` -> `VoiceCall.RelatedRecordId`
- `Shares` -> `Project__Share.ParentId`
- `SourceFinanceTransactions` -> `FinanceTransaction.SourceEntityId`
- `Tasks` -> `Task.WhatId`
- `TopicAssignments` -> `TopicAssignment.EntityId`
- `UserDefinedLabelAssignments` -> `UserDefinedLabelAssignment.ItemId`
- `Work_Items__r` -> `Work_Item__c.Project__c`

---

## Work Item (`Work_Item__c`)

- **Key Prefix:** `a02`
- **Custom:** True
- **Createable:** True
- **Updateable:** True
- **Deletable:** True

### Fields

| API Name | Label | Type | Required | Updateable |
|----------|-------|------|----------|------------|
| `Actual_Hours__c` | Actual Hours | double(4,2) |  |  |
| `Assigned_To__c` | Assigned To | reference(User) |  | Yes |
| `Completed_Date__c` | Completed Date | date |  | Yes |
| `CreatedById` | Created By ID | reference(User) |  |  |
| `CreatedDate` | Created Date | datetime |  |  |
| `Description__c` | Description | textarea |  | Yes |
| `Due_Date__c` | Due Date | date |  | Yes |
| `Estimated_Hours__c` | Estimated Hours | double(5,1) |  | Yes |
| `Id` | Record ID | id |  |  |
| `IsDeleted` | Deleted | boolean |  |  |
| `LastActivityDate` | Last Activity Date | date |  |  |
| `LastModifiedById` | Last Modified By ID | reference(User) |  |  |
| `LastModifiedDate` | Last Modified Date | datetime |  |  |
| `LastReferencedDate` | Last Referenced Date | datetime |  |  |
| `LastViewedDate` | Last Viewed Date | datetime |  |  |
| `Name` | Work Item Number | string |  |  |
| `Priority__c` | Priority | picklist |  | Yes |
| `Project__c` | Project | reference(Project__c) | Yes | Yes |
| `Status__c` | Status | picklist | Yes | Yes |
| `SystemModstamp` | System Modstamp | datetime |  |  |
| `Type__c` | Type | picklist |  | Yes |

### Picklist Values

**Priority__c** (Priority):
- `P1 - Critical`
- `P2 - High`
- `P3 - Medium` *(default)*
- `P4 - Low`

**Status__c** (Status):
- `To Do` *(default)*
- `In Progress`
- `Done`
- `Blocked`

**Type__c** (Type):
- `Development`
- `Configuration`
- `Testing`
- `Documentation`
- `Data Migration`
- `Integration`

### Relationships (Lookups)

- `Assigned_To__c` -> **User** (relationship: `Assigned_To__r`)
- `CreatedById` -> **User** (relationship: `CreatedBy`)
- `LastModifiedById` -> **User** (relationship: `LastModifiedBy`)
- `Project__c` -> **Project__c** (relationship: `Project__r`)

### Child Relationships

- `ActivityHistories` -> `ActivityHistory.WhatId`
- `AttachedContentDocuments` -> `AttachedContentDocument.LinkedEntityId`
- `Attachments` -> `Attachment.ParentId`
- `CombinedAttachments` -> `CombinedAttachment.ParentId`
- `ContactRequests` -> `ContactRequest.WhatId`
- `ContentDocumentLinks` -> `ContentDocumentLink.LinkedEntityId`
- `DestinationFinanceTransactions` -> `FinanceTransaction.DestinationEntityId`
- `DuplicateRecordItems` -> `DuplicateRecordItem.RecordId`
- `Emails` -> `EmailMessage.RelatedToId`
- `Events` -> `Event.WhatId`
- `FeedSubscriptionsForEntity` -> `EntitySubscription.ParentId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.LegalEntityId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.ReferenceEntityId`
- `FinanceTransactions` -> `FinanceTransaction.LegalEntityId`
- `FinanceTransactions` -> `FinanceTransaction.ReferenceEntityId`
- `FlowOrchestrationWorkItems` -> `FlowOrchestrationWorkItem.RelatedRecordId`
- `Histories` -> `Work_Item__History.ParentId`
- `InventoryReservationSources` -> `InventoryItemReservation.ItemReservationSourceId`
- `InventoryReservations` -> `InventoryReservation.ReservationSourceId`
- `Notes` -> `Note.ParentId`
- `NotesAndAttachments` -> `NoteAndAttachment.ParentId`
- `OpenActivities` -> `OpenActivity.WhatId`
- `ParentFinanceTransactions` -> `FinanceTransaction.ParentReferenceEntityId`
- `ProcessExceptions` -> `ProcessException.AttachedToId`
- `ProcessInstances` -> `ProcessInstance.TargetObjectId`
- `ProcessSteps` -> `ProcessInstanceHistory.TargetObjectId`
- `RecordActionHistories` -> `RecordActionHistory.ParentRecordId`
- `RecordActions` -> `RecordAction.RecordId`
- `RecordAssociatedGroups` -> `CollaborationGroupRecord.RecordId`
- `RelatedRecords` -> `VoiceCall.RelatedRecordId`
- `SourceFinanceTransactions` -> `FinanceTransaction.SourceEntityId`
- `Tasks` -> `Task.WhatId`
- `Time_Entries__r` -> `Time_Entry__c.Work_Item__c`
- `TopicAssignments` -> `TopicAssignment.EntityId`
- `UserDefinedLabelAssignments` -> `UserDefinedLabelAssignment.ItemId`

---

## Time Entry (`Time_Entry__c`)

- **Key Prefix:** `a01`
- **Custom:** True
- **Createable:** True
- **Updateable:** True
- **Deletable:** True

### Fields

| API Name | Label | Type | Required | Updateable |
|----------|-------|------|----------|------------|
| `CreatedById` | Created By ID | reference(User) |  |  |
| `CreatedDate` | Created Date | datetime |  |  |
| `Date__c` | Date | date | Yes | Yes |
| `Hours__c` | Hours | double(4,2) | Yes | Yes |
| `Id` | Record ID | id |  |  |
| `IsDeleted` | Deleted | boolean |  |  |
| `LastActivityDate` | Last Activity Date | date |  |  |
| `LastModifiedById` | Last Modified By ID | reference(User) |  |  |
| `LastModifiedDate` | Last Modified Date | datetime |  |  |
| `LastReferencedDate` | Last Referenced Date | datetime |  |  |
| `LastViewedDate` | Last Viewed Date | datetime |  |  |
| `Name` | Time Entry Number | string |  |  |
| `Notes__c` | Notes | string |  | Yes |
| `SystemModstamp` | System Modstamp | datetime |  |  |
| `Work_Item__c` | Work Item | reference(Work_Item__c) | Yes |  |

### Relationships (Lookups)

- `CreatedById` -> **User** (relationship: `CreatedBy`)
- `LastModifiedById` -> **User** (relationship: `LastModifiedBy`)
- `Work_Item__c` -> **Work_Item__c** (relationship: `Work_Item__r`)

### Child Relationships

- `ActivityHistories` -> `ActivityHistory.WhatId`
- `AttachedContentDocuments` -> `AttachedContentDocument.LinkedEntityId`
- `Attachments` -> `Attachment.ParentId`
- `CombinedAttachments` -> `CombinedAttachment.ParentId`
- `ContactRequests` -> `ContactRequest.WhatId`
- `ContentDocumentLinks` -> `ContentDocumentLink.LinkedEntityId`
- `DestinationFinanceTransactions` -> `FinanceTransaction.DestinationEntityId`
- `DuplicateRecordItems` -> `DuplicateRecordItem.RecordId`
- `Emails` -> `EmailMessage.RelatedToId`
- `Events` -> `Event.WhatId`
- `FeedSubscriptionsForEntity` -> `EntitySubscription.ParentId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.LegalEntityId`
- `FinanceBalanceSnapshots` -> `FinanceBalanceSnapshot.ReferenceEntityId`
- `FinanceTransactions` -> `FinanceTransaction.LegalEntityId`
- `FinanceTransactions` -> `FinanceTransaction.ReferenceEntityId`
- `FlowOrchestrationWorkItems` -> `FlowOrchestrationWorkItem.RelatedRecordId`
- `Histories` -> `Time_Entry__History.ParentId`
- `InventoryReservationSources` -> `InventoryItemReservation.ItemReservationSourceId`
- `InventoryReservations` -> `InventoryReservation.ReservationSourceId`
- `Notes` -> `Note.ParentId`
- `NotesAndAttachments` -> `NoteAndAttachment.ParentId`
- `OpenActivities` -> `OpenActivity.WhatId`
- `ParentFinanceTransactions` -> `FinanceTransaction.ParentReferenceEntityId`
- `ProcessExceptions` -> `ProcessException.AttachedToId`
- `ProcessInstances` -> `ProcessInstance.TargetObjectId`
- `ProcessSteps` -> `ProcessInstanceHistory.TargetObjectId`
- `RecordActionHistories` -> `RecordActionHistory.ParentRecordId`
- `RecordActions` -> `RecordAction.RecordId`
- `RecordAssociatedGroups` -> `CollaborationGroupRecord.RecordId`
- `RelatedRecords` -> `VoiceCall.RelatedRecordId`
- `SourceFinanceTransactions` -> `FinanceTransaction.SourceEntityId`
- `Tasks` -> `Task.WhatId`
- `TopicAssignments` -> `TopicAssignment.EntityId`
- `UserDefinedLabelAssignments` -> `UserDefinedLabelAssignment.ItemId`

---

## User (`User`)

- **Key Prefix:** `005`
- **Custom:** False
- **Createable:** True
- **Updateable:** True
- **Deletable:** False

### Fields

| API Name | Label | Type | Required | Updateable |
|----------|-------|------|----------|------------|
| `AboutMe` | About Me | textarea |  | Yes |
| `AccountId` | Account ID | reference(Account) |  |  |
| `Address` | Address | address |  |  |
| `Alias` | Alias | string | Yes | Yes |
| `BadgeText` | User Photo badge text overlay | string |  |  |
| `BannerPhotoUrl` | URL for banner photo | url |  |  |
| `CallCenterId` | Call Center ID | reference(CallCenter) |  | Yes |
| `City` | City | string |  | Yes |
| `CommunityNickname` | Nickname | string | Yes | Yes |
| `CompanyName` | Company Name | string |  | Yes |
| `ContactId` | Contact ID | reference(Contact) |  | Yes |
| `Country` | Country | string |  | Yes |
| `CountryCode` | Country Code | picklist |  | Yes |
| `CreatedById` | Created By ID | reference(User) |  |  |
| `CreatedDate` | Created Date | datetime |  |  |
| `DefaultGroupNotificationFrequency` | Default Notification Frequency when Joining Groups | picklist | Yes | Yes |
| `DelegatedApproverId` | Delegated Approver ID | reference(Group, User) |  | Yes |
| `Department` | Department | string |  | Yes |
| `DigestFrequency` | Chatter Email Highlights Frequency | picklist | Yes | Yes |
| `Division` | Division | string |  | Yes |
| `Email` | Email | email | Yes | Yes |
| `EmailEncodingKey` | Email Encoding | picklist | Yes | Yes |
| `EmailPreferencesAutoBcc` | AutoBcc | boolean | Yes | Yes |
| `EmailPreferencesAutoBccStayInTouch` | AutoBccStayInTouch | boolean | Yes | Yes |
| `EmailPreferencesStayInTouchReminder` | StayInTouchReminder | boolean | Yes | Yes |
| `EmployeeNumber` | Employee Number | string |  | Yes |
| `EndDay` | End of Day | picklist |  | Yes |
| `Extension` | Extension | phone |  | Yes |
| `Fax` | Fax | phone |  | Yes |
| `FederationIdentifier` | SAML Federation ID | string |  | Yes |
| `FirstName` | First Name | string |  | Yes |
| `ForecastEnabled` | Allow Forecasting | boolean | Yes | Yes |
| `FullPhotoUrl` | Url for full-sized Photo | url |  |  |
| `GeocodeAccuracy` | Geocode Accuracy | picklist |  | Yes |
| `Id` | User ID | id |  |  |
| `IndividualId` | Individual ID | reference(Individual) |  | Yes |
| `IsActive` | Active | boolean | Yes | Yes |
| `IsExtIndicatorVisible` | Show external indicator | boolean |  |  |
| `IsProfilePhotoActive` | Has Profile Photo | boolean |  |  |
| `JigsawImportLimitOverride` | Data.com Monthly Addition Limit | int |  | Yes |
| `LanguageLocaleKey` | Language | picklist | Yes | Yes |
| `LastLoginDate` | Last Login | datetime |  |  |
| `LastModifiedById` | Last Modified By ID | reference(User) |  |  |
| `LastModifiedDate` | Last Modified Date | datetime |  |  |
| `LastName` | Last Name | string | Yes | Yes |
| `LastPasswordChangeDate` | Last Password Change or Reset | datetime |  |  |
| `LastReferencedDate` | Last Referenced Date | datetime |  |  |
| `LastViewedDate` | Last Viewed Date | datetime |  |  |
| `Latitude` | Latitude | double(18,15) |  | Yes |
| `LocaleSidKey` | Locale | picklist | Yes | Yes |
| `Longitude` | Longitude | double(18,15) |  | Yes |
| `ManagerId` | Manager ID | reference(User) |  | Yes |
| `MediumBannerPhotoUrl` | URL for Android banner photo | url |  |  |
| `MediumPhotoUrl` | URL for medium profile photo | url |  |  |
| `MobilePhone` | Mobile | phone |  | Yes |
| `Name` | Full Name | string |  |  |
| `NumberOfFailedLogins` | Failed Login Attempts | int |  |  |
| `OfflinePdaTrialExpirationDate` | Sales Anywhere Trial Expiration Date | datetime |  |  |
| `OfflineTrialExpirationDate` | Offline Edition Trial Expiration Date | datetime |  |  |
| `OutOfOfficeMessage` | Out of office message | string |  |  |
| `PasswordExpirationDate` | Password Expiration Date | datetime |  |  |
| `Phone` | Phone | phone |  | Yes |
| `PostalCode` | Zip/Postal Code | string |  | Yes |
| `ProfileId` | Profile ID | reference(Profile) | Yes | Yes |
| `ReceivesAdminInfoEmails` | Admin Info Emails | boolean | Yes | Yes |
| `ReceivesInfoEmails` | Info Emails | boolean | Yes | Yes |
| `SenderEmail` | Email Sender Address | email |  | Yes |
| `SenderName` | Email Sender Name | string |  | Yes |
| `Signature` | Email Signature | textarea |  | Yes |
| `SmallBannerPhotoUrl` | URL for IOS banner photo | url |  |  |
| `SmallPhotoUrl` | Photo | url |  |  |
| `StartDay` | Start of Day | picklist |  | Yes |
| `State` | State/Province | string |  | Yes |
| `StateCode` | State/Province Code | picklist |  | Yes |
| `StayInTouchNote` | Stay-in-Touch Email Note | string |  | Yes |
| `StayInTouchSignature` | Stay-in-Touch Email Signature | textarea |  | Yes |
| `StayInTouchSubject` | Stay-in-Touch Email Subject | string |  | Yes |
| `Street` | Street | textarea |  | Yes |
| `SuAccessExpirationDate` | SU Access Expiration Date | date |  |  |
| `SystemModstamp` | System Modstamp | datetime |  |  |
| `TimeZoneSidKey` | Time Zone | picklist | Yes | Yes |
| `Title` | Title | string |  | Yes |
| `UserPermissionsCallCenterAutoLogin` | Auto-login To Call Center | boolean | Yes | Yes |
| `UserPermissionsInteractionUser` | Flow User | boolean | Yes | Yes |
| `UserPermissionsJigsawProspectingUser` | Data.com User | boolean | Yes | Yes |
| `UserPermissionsKnowledgeUser` | Knowledge User | boolean | Yes | Yes |
| `UserPermissionsMarketingUser` | Marketing User | boolean | Yes | Yes |
| `UserPermissionsOfflineUser` | Offline User | boolean | Yes | Yes |
| `UserPermissionsSFContentUser` | Salesforce CRM Content User | boolean | Yes | Yes |
| `UserPermissionsSiteforceContributorUser` | Site.com Contributor User | boolean | Yes | Yes |
| `UserPermissionsSiteforcePublisherUser` | Site.com Publisher User | boolean | Yes | Yes |
| `UserPermissionsSupportUser` | Service Cloud User | boolean | Yes | Yes |
| `UserPermissionsWorkDotComUserFeature` | WDC User | boolean | Yes | Yes |
| `UserPreferencesActivityRemindersPopup` | ActivityRemindersPopup | boolean | Yes | Yes |
| `UserPreferencesApexPagesDeveloperMode` | ApexPagesDeveloperMode | boolean | Yes | Yes |
| `UserPreferencesCacheDiagnostics` | CacheDiagnostics | boolean | Yes | Yes |
| `UserPreferencesContentEmailAsAndWhen` | ContentEmailAsAndWhen | boolean | Yes | Yes |
| `UserPreferencesContentNoEmail` | ContentNoEmail | boolean | Yes | Yes |
| `UserPreferencesCreateLEXAppsWTShown` | CreateLEXAppsWTShown | boolean | Yes | Yes |
| `UserPreferencesDisCommentAfterLikeEmail` | DisCommentAfterLikeEmail | boolean | Yes | Yes |
| `UserPreferencesDisMentionsCommentEmail` | DisMentionsCommentEmail | boolean | Yes | Yes |
| `UserPreferencesDisProfPostCommentEmail` | DisProfPostCommentEmail | boolean | Yes | Yes |
| `UserPreferencesDisableAllFeedsEmail` | DisableAllFeedsEmail | boolean | Yes | Yes |
| `UserPreferencesDisableBookmarkEmail` | DisableBookmarkEmail | boolean | Yes | Yes |
| `UserPreferencesDisableChangeCommentEmail` | DisableChangeCommentEmail | boolean | Yes | Yes |
| `UserPreferencesDisableEndorsementEmail` | DisableEndorsementEmail | boolean | Yes | Yes |
| `UserPreferencesDisableFileShareNotificationsForApi` | DisableFileShareNotificationsForApi | boolean | Yes | Yes |
| `UserPreferencesDisableFollowersEmail` | DisableFollowersEmail | boolean | Yes | Yes |
| `UserPreferencesDisableLaterCommentEmail` | DisableLaterCommentEmail | boolean | Yes | Yes |
| `UserPreferencesDisableLikeEmail` | DisableLikeEmail | boolean | Yes | Yes |
| `UserPreferencesDisableMentionsPostEmail` | DisableMentionsPostEmail | boolean | Yes | Yes |
| `UserPreferencesDisableMessageEmail` | DisableMessageEmail | boolean | Yes | Yes |
| `UserPreferencesDisableProfilePostEmail` | DisableProfilePostEmail | boolean | Yes | Yes |
| `UserPreferencesDisableSharePostEmail` | DisableSharePostEmail | boolean | Yes | Yes |
| `UserPreferencesEnableAutoSubForFeeds` | EnableAutoSubForFeeds | boolean | Yes | Yes |
| `UserPreferencesEventRemindersCheckboxDefault` | EventRemindersCheckboxDefault | boolean | Yes | Yes |
| `UserPreferencesExcludeMailAppAttachments` | ExcludeMailAppAttachments | boolean | Yes | Yes |
| `UserPreferencesFavoritesShowTopFavorites` | FavoritesShowTopFavorites | boolean | Yes | Yes |
| `UserPreferencesFavoritesWTShown` | FavoritesWTShown | boolean | Yes | Yes |
| `UserPreferencesGlobalNavBarWTShown` | GlobalNavBarWTShown | boolean | Yes | Yes |
| `UserPreferencesGlobalNavGridMenuWTShown` | GlobalNavGridMenuWTShown | boolean | Yes | Yes |
| `UserPreferencesHasCelebrationBadge` | HasCelebrationBadge | boolean | Yes | Yes |
| `UserPreferencesHasSentWarningEmail` | HasSentWarningEmail | boolean | Yes | Yes |
| `UserPreferencesHasSentWarningEmail238` | HasSentWarningEmail238 | boolean | Yes | Yes |
| `UserPreferencesHasSentWarningEmail240` | HasSentWarningEmail240 | boolean | Yes | Yes |
| `UserPreferencesHideBiggerPhotoCallout` | HideBiggerPhotoCallout | boolean | Yes | Yes |
| `UserPreferencesHideCSNDesktopTask` | HideCSNDesktopTask | boolean | Yes | Yes |
| `UserPreferencesHideCSNGetChatterMobileTask` | HideCSNGetChatterMobileTask | boolean | Yes | Yes |
| `UserPreferencesHideChatterOnboardingSplash` | HideChatterOnboardingSplash | boolean | Yes | Yes |
| `UserPreferencesHideEndUserOnboardingAssistantModal` | HideEndUserOnboardingAssistantModal | boolean | Yes | Yes |
| `UserPreferencesHideLightningMigrationModal` | HideLightningMigrationModal | boolean | Yes | Yes |
| `UserPreferencesHideS1BrowserUI` | HideS1BrowserUI | boolean | Yes | Yes |
| `UserPreferencesHideSecondChatterOnboardingSplash` | HideSecondChatterOnboardingSplash | boolean | Yes | Yes |
| `UserPreferencesHideSfxWelcomeMat` | HideSfxWelcomeMat | boolean | Yes | Yes |
| `UserPreferencesJigsawListUser` | JigsawListUser | boolean | Yes | Yes |
| `UserPreferencesLightningExperiencePreferred` | LightningExperiencePreferred | boolean | Yes | Yes |
| `UserPreferencesLiveAgentMiawSetupDeflection` | LiveAgentMiawSetupDeflection | boolean | Yes | Yes |
| `UserPreferencesNativeEmailClient` | NativeEmailClient | boolean | Yes | Yes |
| `UserPreferencesNewLightningReportRunPageEnabled` | NewLightningReportRunPageEnabled | boolean | Yes | Yes |
| `UserPreferencesPathAssistantCollapsed` | PathAssistantCollapsed | boolean | Yes | Yes |
| `UserPreferencesPreviewCustomTheme` | PreviewCustomTheme | boolean | Yes | Yes |
| `UserPreferencesPreviewLightning` | PreviewLightning | boolean | Yes | Yes |
| `UserPreferencesReceiveNoNotificationsAsApprover` | ReceiveNoNotificationsAsApprover | boolean | Yes | Yes |
| `UserPreferencesReceiveNotificationsAsDelegatedApprover` | ReceiveNotificationsAsDelegatedApprover | boolean | Yes | Yes |
| `UserPreferencesRecordHomeReservedWTShown` | RecordHomeReservedWTShown | boolean | Yes | Yes |
| `UserPreferencesRecordHomeSectionCollapseWTShown` | RecordHomeSectionCollapseWTShown | boolean | Yes | Yes |
| `UserPreferencesReminderSoundOff` | ReminderSoundOff | boolean | Yes | Yes |
| `UserPreferencesReverseOpenActivitiesView` | ReverseOpenActivitiesView | boolean | Yes | Yes |
| `UserPreferencesSRHOverrideActivities` | SRHOverrideActivities | boolean | Yes | Yes |
| `UserPreferencesShowCityToExternalUsers` | ShowCityToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowCityToGuestUsers` | ShowCityToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowCountryToExternalUsers` | ShowCountryToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowCountryToGuestUsers` | ShowCountryToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowEmailToExternalUsers` | ShowEmailToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowEmailToGuestUsers` | ShowEmailToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowFaxToExternalUsers` | ShowFaxToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowFaxToGuestUsers` | ShowFaxToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowForecastingChangeSignals` | ShowForecastingChangeSignals | boolean | Yes | Yes |
| `UserPreferencesShowForecastingRoundedAmounts` | ShowForecastingRoundedAmounts | boolean | Yes | Yes |
| `UserPreferencesShowManagerToExternalUsers` | ShowManagerToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowManagerToGuestUsers` | ShowManagerToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowMobilePhoneToExternalUsers` | ShowMobilePhoneToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowMobilePhoneToGuestUsers` | ShowMobilePhoneToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowPostalCodeToExternalUsers` | ShowPostalCodeToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowPostalCodeToGuestUsers` | ShowPostalCodeToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowProfilePicToGuestUsers` | ShowProfilePicToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowStateToExternalUsers` | ShowStateToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowStateToGuestUsers` | ShowStateToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowStreetAddressToExternalUsers` | ShowStreetAddressToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowStreetAddressToGuestUsers` | ShowStreetAddressToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowTerritoryTimeZoneShifts` | ShowTerritoryTimeZoneShifts | boolean | Yes | Yes |
| `UserPreferencesShowTitleToExternalUsers` | ShowTitleToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowTitleToGuestUsers` | ShowTitleToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesShowWorkPhoneToExternalUsers` | ShowWorkPhoneToExternalUsers | boolean | Yes | Yes |
| `UserPreferencesShowWorkPhoneToGuestUsers` | ShowWorkPhoneToGuestUsers | boolean | Yes | Yes |
| `UserPreferencesSortFeedByComment` | SortFeedByComment | boolean | Yes | Yes |
| `UserPreferencesSuppressEventSFXReminders` | SuppressEventSFXReminders | boolean | Yes | Yes |
| `UserPreferencesSuppressTaskSFXReminders` | SuppressTaskSFXReminders | boolean | Yes | Yes |
| `UserPreferencesTaskRemindersCheckboxDefault` | TaskRemindersCheckboxDefault | boolean | Yes | Yes |
| `UserPreferencesUserDebugModePref` | UserDebugModePref | boolean | Yes | Yes |
| `UserRoleId` | Role ID | reference(UserRole) |  | Yes |
| `UserType` | User Type | picklist |  |  |
| `Username` | Username | string | Yes | Yes |

### Picklist Values

**CountryCode** (Country Code):
- `AF`
- `AX`
- `AL`
- `DZ`
- `AD`
- `AO`
- `AI`
- `AQ`
- `AG`
- `AR`
- `AM`
- `AW`
- `AU`
- `AT`
- `AZ`
- `BS`
- `BH`
- `BD`
- `BB`
- `BY`
- `BE`
- `BZ`
- `BJ`
- `BM`
- `BT`
- `BO`
- `BQ`
- `BA`
- `BW`
- `BV`
- `BR`
- `IO`
- `BN`
- `BG`
- `BF`
- `BI`
- `KH`
- `CM`
- `CA`
- `CV`
- `KY`
- `CF`
- `TD`
- `CL`
- `CN`
- `CX`
- `CC`
- `CO`
- `KM`
- `CG`
- `CD`
- `CK`
- `CR`
- `CI`
- `HR`
- `CW`
- `CY`
- `CZ`
- `DK`
- `DJ`
- `DM`
- `DO`
- `EC`
- `EG`
- `SV`
- `GQ`
- `ER`
- `EE`
- `SZ`
- `ET`
- `FK`
- `FO`
- `FJ`
- `FI`
- `FR`
- `GF`
- `PF`
- `TF`
- `GA`
- `GM`
- `GE`
- `DE`
- `GH`
- `GI`
- `GR`
- `GL`
- `GD`
- `GP`
- `GT`
- `GG`
- `GN`
- `GW`
- `GY`
- `HT`
- `HM`
- `VA`
- `HN`
- `HU`
- `IS`
- `IN`
- `ID`
- `IQ`
- `IE`
- `IM`
- `IL`
- `IT`
- `JM`
- `JP`
- `JE`
- `JO`
- `KZ`
- `KE`
- `KI`
- `KR`
- `XK`
- `KW`
- `KG`
- `LA`
- `LV`
- `LB`
- `LS`
- `LR`
- `LY`
- `LI`
- `LT`
- `LU`
- `MO`
- `MG`
- `MW`
- `MY`
- `MV`
- `ML`
- `MT`
- `MQ`
- `MR`
- `MU`
- `YT`
- `MX`
- `MD`
- `MC`
- `MN`
- `ME`
- `MS`
- `MA`
- `MZ`
- `MM`
- `NA`
- `NR`
- `NP`
- `NL`
- `NC`
- `NZ`
- `NI`
- `NE`
- `NG`
- `NU`
- `NF`
- `MK`
- `NO`
- `OM`
- `PK`
- `PS`
- `PA`
- `PG`
- `PY`
- `PE`
- `PH`
- `PN`
- `PL`
- `PT`
- `QA`
- `RE`
- `RO`
- `RU`
- `RW`
- `BL`
- `SH`
- `KN`
- `LC`
- `MF`
- `PM`
- `VC`
- `WS`
- `SM`
- `ST`
- `SA`
- `SN`
- `RS`
- `SC`
- `SL`
- `SG`
- `SX`
- `SK`
- `SI`
- `SB`
- `SO`
- `ZA`
- `GS`
- `SS`
- `ES`
- `LK`
- `SR`
- `SJ`
- `SE`
- `CH`
- `TW`
- `TJ`
- `TZ`
- `TH`
- `TL`
- `TG`
- `TK`
- `TO`
- `TT`
- `TN`
- `TR`
- `TM`
- `TC`
- `TV`
- `UG`
- `UA`
- `AE`
- `GB`
- `US`
- `UY`
- `UZ`
- `VU`
- `VE`
- `VN`
- `VG`
- `WF`
- `EH`
- `YE`
- `ZM`
- `ZW`

**DefaultGroupNotificationFrequency** (Default Notification Frequency when Joining Groups):
- `P`
- `D`
- `W`
- `N` *(default)*

**DigestFrequency** (Chatter Email Highlights Frequency):
- `D`
- `W`
- `N` *(default)*

**EmailEncodingKey** (Email Encoding):
- `UTF-8`
- `ISO-8859-1`
- `Shift_JIS`
- `ISO-2022-JP`
- `EUC-JP`
- `ks_c_5601-1987`
- `Big5`
- `GB2312`
- `Big5-HKSCS`
- `x-SJIS_0213`

**EndDay** (End of Day):
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `10`
- `11`
- `12`
- `13`
- `14`
- `15`
- `16`
- `17`
- `18`
- `19`
- `20`
- `21`
- `22`
- `23`

**GeocodeAccuracy** (Geocode Accuracy):
- `Address`
- `NearAddress`
- `Block`
- `Street`
- `ExtendedZip`
- `Zip`
- `Neighborhood`
- `City`
- `County`
- `State`
- `Unknown`

**LanguageLocaleKey** (Language):
- `en_US`
- `de`
- `es`
- `fr`
- `it`
- `ja`
- `sv`
- `ko`
- `zh_TW`
- `zh_CN`
- `pt_BR`
- `nl_NL`
- `da`
- `th`
- `fi`
- `ru`
- `es_MX`
- `no`

**LocaleSidKey** (Locale):
- `af_ZA`
- `sq_AL`
- `am_ET`
- `ar_DZ`
- `ar_BH`
- `ar_EG`
- `ar_IQ`
- `ar_JO`
- `ar_KW`
- `ar_LB`
- `ar_LY`
- `ar_MA`
- `ar_OM`
- `ar_QA`
- `ar_SA`
- `ar_SD`
- `ar_TN`
- `ar_AE`
- `ar_YE`
- `hy_AM`
- `az_AZ`
- `bn_BD`
- `bn_IN`
- `eu_ES`
- `be_BY`
- `bs_BA`
- `bg_BG`
- `my_MM`
- `ca_ES`
- `zh_CN_PINYIN`
- `zh_CN_STROKE`
- `zh_CN`
- `zh_HK_STROKE`
- `zh_HK`
- `zh_MO`
- `zh_MY`
- `zh_SG`
- `zh_TW_STROKE`
- `zh_TW`
- `hr_HR`
- `cs_CZ`
- `da_DK`
- `nl_AW`
- `nl_BE`
- `nl_NL`
- `nl_SR`
- `dz_BT`
- `en_AG`
- `en_AU`
- `en_BS`
- `en_BB`
- `en_BE`
- `en_BZ`
- `en_BM`
- `en_BW`
- `en_CM`
- `en_CA`
- `en_KY`
- `en_CY`
- `en_ER`
- `en_SZ`
- `en_FK`
- `en_FJ`
- `en_GM`
- `en_DE`
- `en_GH`
- `en_GI`
- `en_GY`
- `en_HK`
- `en_IN`
- `en_ID`
- `en_IE`
- `en_IL`
- `en_JM`
- `en_KE`
- `en_LR`
- `en_MG`
- `en_MW`
- `en_MY`
- `en_MT`
- `en_MU`
- `en_NA`
- `en_NL`
- `en_NZ`
- `en_NG`
- `en_PK`
- `en_PG`
- `en_PH`
- `en_RW`
- `en_WS`
- `en_SC`
- `en_SL`
- `en_SG`
- `en_SX`
- `en_SB`
- `en_ZA`
- `en_SH`
- `en_TZ`
- `en_TO`
- `en_TT`
- `en_UG`
- `en_AE`
- `en_GB`
- `en_US`
- `en_VU`
- `et_EE`
- `fi_FI`
- `fr_BE`
- `fr_CA`
- `fr_KM`
- `fr_FR`
- `fr_GN`
- `fr_HT`
- `fr_LU`
- `fr_MR`
- `fr_MC`
- `fr_MA`
- `fr_CH`
- `fr_WF`
- `ka_GE`
- `de_AT`
- `de_BE`
- `de_DE`
- `de_LU`
- `de_CH`
- `el_CY`
- `el_GR`
- `gu_IN`
- `ht_HT`
- `ht_US`
- `haw_US`
- `iw_IL`
- `hi_IN`
- `hmn_US`
- `hu_HU`
- `is_IS`
- `in_ID`
- `ga_IE`
- `it_IT`
- `it_CH`
- `ja_JP`
- `kl_GL`
- `kn_IN`
- `kk_KZ`
- `km_KH`
- `ko_KR`
- `ky_KG`
- `lo_LA`
- `lv_LV`
- `lt_LT`
- `lu_CD`
- `lb_LU`
- `mk_MK`
- `ms_BN`
- `ms_MY`
- `ml_IN`
- `mt_MT`
- `mr_IN`
- `sh_ME`
- `ne_NP`
- `no_NO`
- `ps_AF`
- `pl_PL`
- `pt_AO`
- `pt_BR`
- `pt_CV`
- `pt_MZ`
- `pt_PT`
- `pt_ST`
- `pa_IN`
- `ro_MD`
- `ro_RO`
- `rm_CH`
- `rn_BI`
- `ru_AM`
- `ru_BY`
- `ru_KZ`
- `ru_KG`
- `ru_LT`
- `ru_MD`
- `ru_PL`
- `ru_RU`
- `ru_UA`
- `sm_WS`
- `sm_US`
- `sr_BA`
- `sr_CS`
- `sh_BA`
- `sh_CS`
- `sr_RS`
- `sk_SK`
- `sl_SI`
- `so_DJ`
- `so_SO`
- `es_AR`
- `es_BO`
- `es_CL`
- `es_CO`
- `es_CR`
- `es_DO`
- `es_EC`
- `es_SV`
- `es_GT`
- `es_HN`
- `es_MX`
- `es_NI`
- `es_PA`
- `es_PY`
- `es_PE`
- `es_PR`
- `es_ES`
- `es_US`
- `es_UY`
- `es_VE`
- `sw_KE`
- `sv_SE`
- `tl_PH`
- `tg_TJ`
- `ta_IN`
- `ta_LK`
- `te_IN`
- `mi_NZ`
- `th_TH`
- `ti_ET`
- `tr_TR`
- `uk_UA`
- `ur_PK`
- `uz_LATN_UZ`
- `vi_VN`
- `cy_GB`
- `xh_ZA`
- `ji_US`
- `yo_BJ`
- `zu_ZA`

**StartDay** (Start of Day):
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `10`
- `11`
- `12`
- `13`
- `14`
- `15`
- `16`
- `17`
- `18`
- `19`
- `20`
- `21`
- `22`
- `23`

**StateCode** (State/Province Code):
- `AC`
- `AG`
- `AG`
- `05`
- `02`
- `AL`
- `AL`
- `AK`
- `AB`
- `AL`
- `AP`
- `AM`
- `AN`
- `AN`
- `AP`
- `34`
- `23`
- `AO`
- `AR`
- `AZ`
- `AR`
- `AR`
- `AP`
- `AS`
- `AT`
- `ACT`
- `AV`
- `BA`
- `BC`
- `BS`
- `BA`
- `BT`
- `11`
- `BL`
- `BN`
- `BG`
- `BI`
- `BR`
- `BO`
- `BZ`
- `BS`
- `BR`
- `BC`
- `CA`
- `CA`
- `CL`
- `CM`
- `CB`
- `CI`
- `CW`
- `CE`
- `CT`
- `CZ`
- `CN`
- `CE`
- `CH`
- `CT`
- `CS`
- `12`
- `CH`
- `CH`
- `50`
- `CE`
- `CO`
- `CL`
- `CO`
- `CO`
- `CT`
- `CO`
- `CS`
- `CR`
- `KR`
- `CN`
- `DN`
- `DD`
- `DE`
- `DL`
- `DC`
- `DF`
- `DL`
- `D`
- `DG`
- `38`
- `EN`
- `ES`
- `DF`
- `FM`
- `FE`
- `FI`
- `FL`
- `FG`
- `FC`
- `FR`
- `35`
- `18`
- `40`
- `07`
- `G`
- `62`
- `GE`
- `GA`
- `21`
- `GA`
- `GO`
- `GO`
- `GR`
- `GT`
- `44`
- `45`
- `GR`
- `52`
- `GJ`
- `10`
- `46`
- `HR`
- `HI`
- `13`
- `23`
- `41`
- `HG`
- `HP`
- `34`
- `01`
- `91`
- `42`
- `43`
- `28`
- `08`
- `ID`
- `IL`
- `IM`
- `IN`
- `IA`
- `IS`
- `17`
- `03`
- `JA`
- `JK`
- `JH`
- `32`
- `36`
- `22`
- `37`
- `46`
- `14`
- `KS`
- `KA`
- `KY`
- `KL`
- `KY`
- `KE`
- `KK`
- `39`
- `43`
- `26`
- `AQ`
- `LD`
- `LS`
- `SP`
- `LT`
- `LE`
- `LC`
- `LM`
- `21`
- `LK`
- `LI`
- `LO`
- `LD`
- `LA`
- `LH`
- `LU`
- `92`
- `MC`
- `MP`
- `MH`
- `ME`
- `MN`
- `MB`
- `MN`
- `MA`
- `MD`
- `MS`
- `MA`
- `MT`
- `MT`
- `MS`
- `MO`
- `MH`
- `VS`
- `ML`
- `ME`
- `ME`
- `MI`
- `MI`
- `24`
- `MI`
- `MG`
- `MN`
- `MS`
- `MO`
- `04`
- `45`
- `MZ`
- `MO`
- `MN`
- `MT`
- `MB`
- `MO`
- `NL`
- `20`
- `42`
- `NA`
- `29`
- `NA`
- `NE`
- `15`
- `NV`
- `NB`
- `NL`
- `NH`
- `NJ`
- `NM`
- `NSW`
- `NY`
- `15`
- `64`
- `NC`
- `ND`
- `NT`
- `NT`
- `NO`
- `NS`
- `NL`
- `NU`
- `NU`
- `OA`
- `OR`
- `OY`
- `OG`
- `OH`
- `44`
- `33`
- `47`
- `OK`
- `OT`
- `ON`
- `OR`
- `OR`
- `27`
- `PD`
- `PA`
- `PA`
- `PB`
- `PR`
- `PR`
- `PV`
- `PA`
- `PE`
- `PG`
- `PU`
- `PE`
- `PC`
- `PI`
- `PI`
- `PT`
- `PN`
- `PZ`
- `PO`
- `PE`
- `PY`
- `PB`
- `PB`
- `63`
- `QC`
- `QLD`
- `QE`
- `QR`
- `RG`
- `RJ`
- `RA`
- `RC`
- `RE`
- `RI`
- `RI`
- `RN`
- `RJ`
- `RN`
- `RS`
- `RM`
- `RO`
- `RR`
- `RN`
- `RO`
- `41`
- `11`
- `SA`
- `SL`
- `SC`
- `SP`
- `SK`
- `SS`
- `SV`
- `SE`
- `61`
- `37`
- `31`
- `14`
- `25`
- `32`
- `22`
- `51`
- `SI`
- `SK`
- `SI`
- `SO`
- `SO`
- `SO`
- `SA`
- `SC`
- `SD`
- `SR`
- `TB`
- `71`
- `TM`
- `TN`
- `TA`
- `TAS`
- `TG`
- `TN`
- `TE`
- `TR`
- `TX`
- `12`
- `TA`
- `TL`
- `TO`
- `09`
- `36`
- `13`
- `31`
- `16`
- `TP`
- `TN`
- `TV`
- `TS`
- `TR`
- `TO`
- `UD`
- `UT`
- `UT`
- `UP`
- `VA`
- `VE`
- `VE`
- `VB`
- `VC`
- `VT`
- `VR`
- `VV`
- `VI`
- `VIC`
- `VA`
- `VT`
- `30`
- `WA`
- `WD`
- `WB`
- `WA`
- `WH`
- `WV`
- `WX`
- `WW`
- `WI`
- `WY`
- `65`
- `54`
- `06`
- `35`
- `19`
- `YU`
- `YT`
- `53`
- `ZA`
- `33`

**TimeZoneSidKey** (Time Zone):
- `Pacific/Kiritimati`
- `Pacific/Chatham`
- `Antarctica/McMurdo`
- `Pacific/Apia`
- `Pacific/Auckland`
- `Pacific/Enderbury`
- `Pacific/Fakaofo`
- `Pacific/Tongatapu`
- `Asia/Anadyr`
- `Asia/Kamchatka`
- `Pacific/Fiji`
- `Pacific/Funafuti`
- `Pacific/Kwajalein`
- `Pacific/Majuro`
- `Pacific/Nauru`
- `Pacific/Norfolk`
- `Pacific/Tarawa`
- `Pacific/Wake`
- `Pacific/Wallis`
- `Antarctica/Macquarie`
- `Asia/Magadan`
- `Asia/Sakhalin`
- `Asia/Srednekolymsk`
- `Australia/Currie`
- `Australia/Hobart`
- `Australia/Lord_Howe`
- `Australia/Melbourne`
- `Australia/Sydney`
- `Pacific/Bougainville`
- `Pacific/Efate`
- `Pacific/Guadalcanal`
- `Pacific/Kosrae`
- `Pacific/Noumea`
- `Pacific/Ponape`
- `Australia/Adelaide`
- `Australia/Broken_Hill`
- `Antarctica/DumontDUrville`
- `Asia/Ust-Nera`
- `Asia/Vladivostok`
- `Australia/Brisbane`
- `Australia/Lindeman`
- `Pacific/Guam`
- `Pacific/Port_Moresby`
- `Pacific/Saipan`
- `Pacific/Truk`
- `Australia/Darwin`
- `Asia/Chita`
- `Asia/Dili`
- `Asia/Jayapura`
- `Asia/Khandyga`
- `Asia/Seoul`
- `Asia/Tokyo`
- `Asia/Yakutsk`
- `Pacific/Palau`
- `Australia/Eucla`
- `Antarctica/Casey`
- `Asia/Brunei`
- `Asia/Choibalsan`
- `Asia/Hong_Kong`
- `Asia/Irkutsk`
- `Asia/Kuala_Lumpur`
- `Asia/Kuching`
- `Asia/Macau`
- `Asia/Makassar`
- `Asia/Manila`
- `Asia/Shanghai`
- `Asia/Singapore`
- `Asia/Taipei`
- `Asia/Ulaanbaatar`
- `Australia/Perth`
- `Antarctica/Davis`
- `Asia/Bangkok`
- `Asia/Barnaul`
- `Asia/Ho_Chi_Minh`
- `Asia/Hovd`
- `Asia/Jakarta`
- `Asia/Krasnoyarsk`
- `Asia/Novokuznetsk`
- `Asia/Novosibirsk`
- `Asia/Phnom_Penh`
- `Asia/Pontianak`
- `Asia/Tomsk`
- `Asia/Vientiane`
- `Indian/Christmas`
- `Asia/Rangoon`
- `Indian/Cocos`
- `Asia/Bishkek`
- `Asia/Dhaka`
- `Asia/Omsk`
- `Asia/Thimphu`
- `Asia/Urumqi`
- `Indian/Chagos`
- `Asia/Kathmandu`
- `Asia/Colombo`
- `Asia/Kolkata`
- `Antarctica/Mawson`
- `Antarctica/Vostok`
- `Asia/Almaty`
- `Asia/Aqtau`
- `Asia/Aqtobe`
- `Asia/Ashgabat`
- `Asia/Atyrau`
- `Asia/Dushanbe`
- `Asia/Karachi`
- `Asia/Oral`
- `Asia/Qostanay`
- `Asia/Qyzylorda`
- `Asia/Samarkand`
- `Asia/Tashkent`
- `Asia/Yekaterinburg`
- `Indian/Kerguelen`
- `Indian/Maldives`
- `Asia/Kabul`
- `Asia/Baku`
- `Asia/Dubai`
- `Asia/Muscat`
- `Asia/Tbilisi`
- `Asia/Yerevan`
- `Europe/Astrakhan`
- `Europe/Samara`
- `Europe/Saratov`
- `Europe/Ulyanovsk`
- `Indian/Mahe`
- `Indian/Mauritius`
- `Indian/Reunion`
- `Africa/Addis_Ababa`
- `Africa/Asmera`
- `Africa/Dar_es_Salaam`
- `Africa/Djibouti`
- `Africa/Kampala`
- `Africa/Mogadishu`
- `Africa/Nairobi`
- `Antarctica/Syowa`
- `Asia/Aden`
- `Asia/Amman`
- `Asia/Baghdad`
- `Asia/Bahrain`
- `Asia/Kuwait`
- `Asia/Qatar`
- `Asia/Riyadh`
- `Europe/Istanbul`
- `Europe/Kirov`
- `Europe/Minsk`
- `Europe/Moscow`
- `Europe/Volgograd`
- `Indian/Antananarivo`
- `Indian/Comoro`
- `Indian/Mayotte`
- `Africa/Blantyre`
- `Africa/Bujumbura`
- `Africa/Cairo`
- `Africa/Gaborone`
- `Africa/Harare`
- `Africa/Johannesburg`
- `Africa/Juba`
- `Africa/Khartoum`
- `Africa/Kigali`
- `Africa/Lubumbashi`
- `Africa/Lusaka`
- `Africa/Maputo`
- `Africa/Maseru`
- `Africa/Mbabane`
- `Africa/Tripoli`
- `Africa/Windhoek`
- `Asia/Beirut`
- `Asia/Famagusta`
- `Asia/Gaza`
- `Asia/Hebron`
- `Asia/Jerusalem`
- `Asia/Nicosia`
- `Europe/Athens`
- `Europe/Bucharest`
- `Europe/Chisinau`
- `Europe/Helsinki`
- `Europe/Kaliningrad`
- `Europe/Kiev`
- `Europe/Mariehamn`
- `Europe/Riga`
- `Europe/Sofia`
- `Europe/Tallinn`
- `Europe/Uzhgorod`
- `Europe/Vilnius`
- `Europe/Zaporozhye`
- `Africa/Algiers`
- `Africa/Bangui`
- `Africa/Brazzaville`
- `Africa/Ceuta`
- `Africa/Douala`
- `Africa/Kinshasa`
- `Africa/Lagos`
- `Africa/Libreville`
- `Africa/Luanda`
- `Africa/Malabo`
- `Africa/Ndjamena`
- `Africa/Niamey`
- `Africa/Porto-Novo`
- `Africa/Tunis`
- `Arctic/Longyearbyen`
- `Europe/Amsterdam`
- `Europe/Andorra`
- `Europe/Belgrade`
- `Europe/Berlin`
- `Europe/Bratislava`
- `Europe/Brussels`
- `Europe/Budapest`
- `Europe/Busingen`
- `Europe/Copenhagen`
- `Europe/Gibraltar`
- `Europe/Ljubljana`
- `Europe/Luxembourg`
- `Europe/Madrid`
- `Europe/Malta`
- `Europe/Monaco`
- `Europe/Oslo`
- `Europe/Paris`
- `Europe/Podgorica`
- `Europe/Prague`
- `Europe/Rome`
- `Europe/San_Marino`
- `Europe/Sarajevo`
- `Europe/Skopje`
- `Europe/Stockholm`
- `Europe/Tirane`
- `Europe/Vaduz`
- `Europe/Vatican`
- `Europe/Vienna`
- `Europe/Warsaw`
- `Europe/Zagreb`
- `Europe/Zurich`
- `Africa/Abidjan`
- `Africa/Accra`
- `Africa/Bamako`
- `Africa/Banjul`
- `Africa/Bissau`
- `Africa/Casablanca`
- `Africa/Conakry`
- `Africa/Dakar`
- `Africa/El_Aaiun`
- `Africa/Freetown`
- `Africa/Lome`
- `Africa/Monrovia`
- `Africa/Nouakchott`
- `Africa/Ouagadougou`
- `Africa/Sao_Tome`
- `America/Danmarkshavn`
- `Antarctica/Troll`
- `Atlantic/Canary`
- `Atlantic/Faeroe`
- `Atlantic/Madeira`
- `Atlantic/Reykjavik`
- `Atlantic/St_Helena`
- `Europe/Dublin`
- `Europe/Guernsey`
- `Europe/Isle_of_Man`
- `Europe/Jersey`
- `Europe/Lisbon`
- `Europe/London`
- `GMT`
- `Atlantic/Azores`
- `Atlantic/Cape_Verde`
- `America/Godthab`
- `America/Noronha`
- `America/Scoresbysund`
- `Atlantic/South_Georgia`
- `America/Araguaina`
- `America/Argentina/Buenos_Aires`
- `America/Argentina/La_Rioja`
- `America/Argentina/Rio_Gallegos`
- `America/Argentina/Salta`
- `America/Argentina/San_Juan`
- `America/Argentina/San_Luis`
- `America/Argentina/Tucuman`
- `America/Argentina/Ushuaia`
- `America/Asuncion`
- `America/Bahia`
- `America/Belem`
- `America/Catamarca`
- `America/Cayenne`
- `America/Cordoba`
- `America/Fortaleza`
- `America/Jujuy`
- `America/Maceio`
- `America/Mendoza`
- `America/Miquelon`
- `America/Montevideo`
- `America/Paramaribo`
- `America/Punta_Arenas`
- `America/Recife`
- `America/Santarem`
- `America/Santiago`
- `America/Sao_Paulo`
- `Antarctica/Palmer`
- `Antarctica/Rothera`
- `Atlantic/Stanley`
- `America/St_Johns`
- `America/Anguilla`
- `America/Antigua`
- `America/Aruba`
- `America/Barbados`
- `America/Blanc-Sablon`
- `America/Boa_Vista`
- `America/Campo_Grande`
- `America/Caracas`
- `America/Cuiaba`
- `America/Curacao`
- `America/Dominica`
- `America/Glace_Bay`
- `America/Goose_Bay`
- `America/Grenada`
- `America/Guadeloupe`
- `America/Guyana`
- `America/Halifax`
- `America/Kralendijk`
- `America/La_Paz`
- `America/Lower_Princes`
- `America/Manaus`
- `America/Marigot`
- `America/Martinique`
- `America/Moncton`
- `America/Montserrat`
- `America/Port_of_Spain`
- `America/Porto_Velho`
- `America/Puerto_Rico`
- `America/Santo_Domingo`
- `America/St_Barthelemy`
- `America/St_Kitts`
- `America/St_Lucia`
- `America/St_Thomas`
- `America/St_Vincent`
- `America/Thule`
- `America/Tortola`
- `Atlantic/Bermuda`
- `America/Bogota`
- `America/Cancun`
- `America/Cayman`
- `America/Coral_Harbour`
- `America/Detroit`
- `America/Eirunepe`
- `America/Grand_Turk`
- `America/Guayaquil`
- `America/Indiana/Indianapolis`
- `America/Indiana/Marengo`
- `America/Indiana/Petersburg`
- `America/Indiana/Vevay`
- `America/Indiana/Vincennes`
- `America/Indiana/Winamac`
- `America/Iqaluit`
- `America/Jamaica`
- `America/Kentucky/Monticello`
- `America/Lima`
- `America/Louisville`
- `America/Montreal`
- `America/Nassau`
- `America/New_York`
- `America/Nipigon`
- `America/Panama`
- `America/Pangnirtung`
- `America/Port-au-Prince`
- `America/Rio_Branco`
- `America/Thunder_Bay`
- `America/Toronto`
- `Pacific/Easter`
- `America/Bahia_Banderas`
- `America/Belize`
- `America/Chicago`
- `America/Chihuahua`
- `America/Costa_Rica`
- `America/El_Salvador`
- `America/Guatemala`
- `America/Indiana/Knox`
- `America/Indiana/Tell_City`
- `America/Managua`
- `America/Matamoros`
- `America/Menominee`
- `America/Merida`
- `America/Mexico_City`
- `America/Monterrey`
- `America/North_Dakota/Beulah`
- `America/North_Dakota/Center`
- `America/North_Dakota/New_Salem`
- `America/Ojinaga`
- `America/Rainy_River`
- `America/Rankin_Inlet`
- `America/Regina`
- `America/Resolute`
- `America/Swift_Current`
- `America/Tegucigalpa`
- `America/Winnipeg`
- `Pacific/Galapagos`
- `America/Boise`
- `America/Cambridge_Bay`
- `America/Creston`
- `America/Dawson`
- `America/Dawson_Creek`
- `America/Denver`
- `America/Edmonton`
- `America/Fort_Nelson`
- `America/Hermosillo`
- `America/Inuvik`
- `America/Mazatlan`
- `America/Phoenix`
- `America/Whitehorse`
- `America/Yellowknife`
- `America/Los_Angeles`
- `America/Santa_Isabel`
- `America/Tijuana`
- `America/Vancouver`
- `Pacific/Pitcairn`
- `America/Anchorage`
- `America/Juneau`
- `America/Metlakatla`
- `America/Nome`
- `America/Sitka`
- `America/Yakutat`
- `Pacific/Gambier`
- `Pacific/Marquesas`
- `America/Adak`
- `Pacific/Honolulu`
- `Pacific/Johnston`
- `Pacific/Rarotonga`
- `Pacific/Tahiti`
- `Pacific/Midway`
- `Pacific/Niue`
- `Pacific/Pago_Pago`

**UserType** (User Type):
- `Standard`
- `PowerPartner`
- `PowerCustomerSuccess`
- `CustomerSuccess`
- `Guest`
- `CspLitePortal`
- `CsnOnly`
- `SelfService`

### Relationships (Lookups)

- `AccountId` -> **Account** (relationship: `Account`)
- `CallCenterId` -> **CallCenter** (relationship: `None`)
- `ContactId` -> **Contact** (relationship: `Contact`)
- `CreatedById` -> **User** (relationship: `CreatedBy`)
- `DelegatedApproverId` -> **Group, User** (relationship: `None`)
- `IndividualId` -> **Individual** (relationship: `Individual`)
- `LastModifiedById` -> **User** (relationship: `LastModifiedBy`)
- `ManagerId` -> **User** (relationship: `Manager`)
- `ProfileId` -> **Profile** (relationship: `Profile`)
- `UserRoleId` -> **UserRole** (relationship: `UserRole`)

### Child Relationships

- `AcceptedEventRelations` -> `AcceptedEventRelation.RelationId`
- `AccountCleanInfoReviewers` -> `AccountCleanInfo.LastStatusChangedById`
- `AttachedContentDocuments` -> `AttachedContentDocument.LinkedEntityId`
- `AuthorizationFormConsents` -> `AuthorizationFormConsent.ConsentGiverId`
- `Carts` -> `WebCart.AccountId`
- `Carts` -> `WebCart.OrderOwnerId`
- `CombinedAttachments` -> `CombinedAttachment.ParentId`
- `CommSubscriptionConsents` -> `CommSubscriptionConsent.ConsentGiverId`
- `ContactCleanInfoReviewers` -> `ContactCleanInfo.LastStatusChangedById`
- `ContactRequests` -> `ContactRequest.WhoId`
- `ContentDocumentLinks` -> `ContentDocumentLink.LinkedEntityId`
- `Contexts` -> `VoiceChnlInteractionEvent.ContextId`
- `ContractsSigned` -> `Contract.CompanySignedId`
- `ConversationEntries` -> `ConversationEntry.ActorId`
- `ConversationParticipants` -> `ConversationParticipant.ParticipantEntityId`
- `DeclinedEventRelations` -> `DeclinedEventRelation.RelationId`
- `DelegatedUsers` -> `User.DelegatedApproverId`
- `EmailMessageRelations` -> `EmailMessageRelation.RelationId`
- `EventRelations` -> `EventRelation.RelationId`
- `ExternalDataUserAuths` -> `ExternalDataUserAuth.UserId`
- `FeedSubscriptions` -> `EntitySubscription.SubscriberId`
- `FeedSubscriptionsForEntity` -> `EntitySubscription.ParentId`
- `Feeds` -> `UserFeed.ParentId`
- `FlowOrchestrationWorkItems` -> `FlowOrchestrationWorkItem.RelatedRecordId`
- `GroupMembershipRequests` -> `CollaborationGroupMemberRequest.RequesterId`
- `GroupMemberships` -> `CollaborationGroupMember.MemberId`
- `InstalledMobileApps` -> `InstalledMobileApp.UserId`
- `LeadCleanInfoReviewers` -> `LeadCleanInfo.LastStatusChangedById`
- `ManagedUsers` -> `User.ManagerId`
- `OutgoingEmailRelations` -> `OutgoingEmailRelation.RelationId`
- `OwnedContentDocuments` -> `OwnedContentDocument.OwnerId`
- `PermissionSetAssignments` -> `PermissionSetAssignment.AssigneeId`
- `PermissionSetLicenseAssignments` -> `PermissionSetLicenseAssign.AssigneeId`
- `PersonRecord` -> `UserEmailPreferredPerson.PersonRecordId`
- `Problems` -> `Problem.ResolvedById`
- `RecordActionHistories` -> `RecordActionHistory.ParentRecordId`
- `RecordActions` -> `RecordAction.RecordId`
- `ServiceResources` -> `ServiceResource.RelatedRecordId`
- `SessionPermSetActivations` -> `SessionPermSetActivation.UserId`
- `Shares` -> `UserShare.UserId`
- `Sources` -> `VoiceChnlInteractionEvent.SourceId`
- `UndecidedEventRelations` -> `UndecidedEventRelation.RelationId`
- `UserEntityAccessRights` -> `UserEntityAccess.UserId`
- `UserFieldAccessRights` -> `UserFieldAccess.UserId`
- `UserLogins` -> `UserLogin.UserId`
- `UserPreferences` -> `UserPreference.UserId`
- `UserSites` -> `Site.AdminId`
- `VoiceCalls` -> `VoiceCall.UserId`
- `Work_Items__r` -> `Work_Item__c.Assigned_To__c`

---

## Record Type (`RecordType`)

- **Key Prefix:** `012`
- **Custom:** False
- **Createable:** True
- **Updateable:** True
- **Deletable:** False

### Fields

| API Name | Label | Type | Required | Updateable |
|----------|-------|------|----------|------------|
| `BusinessProcessId` | Business Process ID | reference(BusinessProcess) |  | Yes |
| `CreatedById` | Created By ID | reference(User) |  |  |
| `CreatedDate` | Created Date | datetime |  |  |
| `Description` | Description | string |  | Yes |
| `DeveloperName` | Record Type Name | string | Yes | Yes |
| `Id` | Record Type ID | id |  |  |
| `IsActive` | Active | boolean |  | Yes |
| `LastModifiedById` | Last Modified By ID | reference(User) |  |  |
| `LastModifiedDate` | Last Modified Date | datetime |  |  |
| `Name` | Name | string | Yes | Yes |
| `NamespacePrefix` | Namespace Prefix | string |  |  |
| `SobjectType` | SObject Type Name | picklist | Yes |  |
| `SystemModstamp` | System Modstamp | datetime |  |  |

### Picklist Values

**SobjectType** (SObject Type Name):
- `Account`
- `ActionCadenceAsyncJob`
- `ActivationTarget`
- `ActivationTargetPlatform`
- `ActivationTargetSecureFTP`
- `ActivationTrgtIntOrgAccess`
- `Actor`
- `ActorLock`
- `ActorMessage`
- `ActorSubscription`
- `ActvTgtPlatformFieldValue`
- `Address`
- `AgentWork`
- `AgentWorkActionVisibility`
- `AIError`
- `AiEvalCopilotTestCaseRslt`
- `AiEvalPrmptRagTestCsRslt`
- `AiEvalPromptTestCaseRslt`
- `AiEvalTestCaseCritRslt`
- `AiEvalTestCaseResult`
- `AiEvaluation`
- `AiGroundingFileRef`
- `AiGroundingSourceStage`
- `AiGroundingWebRef`
- `AIInsightAction`
- `AIInsightFeedback`
- `AIInsightReason`
- `AIInsightReasonMLModelFactor`
- `AIInsightSource`
- `AIInsightValue`
- `AiJobRun`
- `AiJobRunItem`
- `AiMetadataSyncStatus`
- `AIMetric`
- `AIRecordInsight`
- `AIState`
- `AITenantProvisionedFeature`
- `AITestSuiteRunJob`
- `AITestSuiteWorkbookAssoc`
- `AIWorkbook`
- `AIWorksheet`
- `AIWorksheetCell`
- `AIWorksheetColRelation`
- `AIWorksheetColumn`
- `AIWorksheetRow`
- `AlternativePaymentMethod`
- `AnalyticsUserAttrFuncTkn`
- `Announcement`
- `ApiAnomalyEventStore`
- `AppAnalyticsQueryRequest`
- `AppointmentCategory`
- `AppointmentInvitation`
- `AppointmentInvitee`
- `AppointmentScheduleAggr`
- `AppointmentScheduleLog`
- `AppointmentTopicTimeSlot`
- `Asset`
- `AssetAction`
- `AssetActionSource`
- `AssetRelationship`
- `AssetStatePeriod`
- `AssistantProgress`
- `AssistantStepProgress`
- `AssociatedLocation`
- `AsyncOperationLog`
- `AuthorizationForm`
- `AuthorizationFormConsent`
- `AuthorizationFormDataUse`
- `AuthorizationFormText`
- `AutomationStepProgress`
- `BusinessBrand`
- `BuyerGroup`
- `CalendarModel`
- `CalendarView`
- `Campaign`
- `CampaignMember`
- `CardPaymentMethod`
- `CartCheckoutSession`
- `CartDeliveryGroup`
- `CartDeliveryGroupMethod`
- `CartDeliveryGroupMethodAdj`
- `CartItem`
- `CartItemPriceAdjustment`
- `CartRelatedItem`
- `CartTax`
- `CartValidationOutput`
- `Case`
- `CaseRelatedIssue`
- `CatalogedSharedKey`
- `CdnTaskConfiguration`
- `ChangeRequest`
- `ChangeRequestRelatedIssue`
- `ChangeRequestRelatedItem`
- `CollabDocumentMetric`
- `CollabDocumentMetricRecord`
- `CollaborationGroup`
- `CollaborationGroupRank`
- `CollaborationGroupRecord`
- `CollabTemplateMetric`
- `CollabTemplateMetricRecord`
- `CollabUserEngagementMetric`
- `CollabUserEngmtRecordLink`
- `CommerceJobStatus`
- `CommerceSearchDocChangelist`
- `CommerceSearchIndexError`
- `CommerceSearchIndexInfo`
- `CommerceSearchIndexLog`
- `CommerceSearchIndexPayload`
- `CommerceSearchResultsRule`
- `CommSubscription`
- `CommSubscriptionChannelType`
- `CommSubscriptionConsent`
- `CommSubscriptionTiming`
- `ComponentResponseCache`
- `ConsumptionRate`
- `ConsumptionSchedule`
- `Contact`
- `ContactCenterBulkOp`
- `ContactPointAddress`
- `ContactPointConsent`
- `ContactPointEmail`
- `ContactPointPhone`
- `ContactPointTypeConsent`
- `ContactRequest`
- `ContentBuilderChannel`
- `ContentDocumentListViewMapping`
- `ContentFolderDistribution`
- `ContentVersion`
- `Contract`
- `ContractLineItem`
- `ConvCoachingRecommendation`
- `ConvEntryRelatedRecordCopy`
- `ConversationApiLog`
- `ConversationApiLogObjSum`
- `ConversationEntryCopy`
- `ConvMsgSessionAuthResult`
- `Coupon`
- `CredentialStuffingEventStore`
- `CreditMemo`
- `CreditMemoInvApplication`
- `CreditMemoLine`
- `Customer`
- `DataAction`
- `DataActionJobSummary`
- `DataActionTarget`
- `DataAnlytConfigSync`
- `DataAssetSemanticGraphEdge`
- `DataAssetUsageTrackingInfo`
- `DataCommCapActvTarget`
- `DataCommunicationCap`
- `DataContentLensSource`
- `DataflowTriggerEvent`
- `DataGraph`
- `DataHarmonizedModelObjRef`
- `DataKitDeploymentLog`
- `DataKnowledgeSpace`
- `DataKnowledgeSpaceSession`
- `DataKnowledgeSrcFileRef`
- `DataLakeObjectInstance`
- `DataLineageDefSyncLog`
- `DataLineageNodeDefSyncLog`
- `DataMaskCustomValueLibrary`
- `DataMceUmaMigrationStatus`
- `DataMceUmaMigStrmStatus`
- `DataModelRelationConstraint`
- `DataObjSecondaryIndex`
- `DataPackageKit`
- `DataPrepServiceLocator`
- `DataQueryWorkspace`
- `DataQueryWorkspaceTab`
- `DataSemanticSearch`
- `DataSourceBundle`
- `DataStream`
- `DataUseLegalBasis`
- `DataUsePurpose`
- `DcvrFeatureProgress`
- `DcvrPreEnblStepProgress`
- `DcvrRecipeProgress`
- `DcvrRecipeStepProgress`
- `DeliveryEstimationSetup`
- `DevopsEnvironment`
- `DevopsRequestInfo`
- `DigitalWallet`
- `DuplicateErrorLog`
- `DuplicateRecordItem`
- `DuplicateRecordSet`
- `EmailThreadingToken`
- `EngagementChannelType`
- `EngagementChannelWorkType`
- `Entitlement`
- `EntitlementContact`
- `EntityMilestone`
- `Event`
- `EventRelayFeedback`
- `EventStagedInviteeEmail`
- `ExpressionFilter`
- `ExpressionFilterCriteria`
- `ExtDataShare`
- `ExtDataShareTarget`
- `FeatureConfigProgress`
- `FeatureGroupSetupProgress`
- `FeatureSetupProgress`
- `FileBasedDataImport`
- `FileInspectionResult`
- `FileSearchActivity`
- `FinanceBalanceSnapshot`
- `FinanceTransaction`
- `FlowExecutionEventMetric`
- `FlowOrchestration`
- `FlowOrchestrationVersion`
- `FlowRecElementWinningPath`
- `FlowRecord`
- `FlowRecordElement`
- `FlowRecordElementOccurrence`
- `FlowRecordRelation`
- `FlowRecordVersion`
- `FlowRecordVersionOccurrence`
- `FlowStageRelation`
- `FlowTestResult`
- `FulfillmentOrder`
- `FulfillmentOrderItemAdjustment`
- `FulfillmentOrderItemTax`
- `FulfillmentOrderLineItem`
- `GuestUserAnomalyEventStore`
- `HawkingTenantProvStatus`
- `Idea`
- `IdentityResolution`
- `Image`
- `Incident`
- `IncidentRelatedItem`
- `Individual`
- `InventoryItemReservation`
- `InventoryReservation`
- `Invoice`
- `InvoiceLine`
- `Lead`
- `LearningAssignment`
- `LearningAssignmentProgress`
- `LearningItem`
- `LearningLesson`
- `LearningLessonItem`
- `LearningLink`
- `LearningLinkProgress`
- `LegalEntity`
- `ListEmail`
- `ListEmailIndividualRecipient`
- `ListEmailRecipientSource`
- `ListEmailSentResult`
- `Location`
- `LocationGroup`
- `LocationGroupAssignment`
- `LocationShippingCarrierMethod`
- `LocationWaitlist`
- `LocationWaitlistedParty`
- `LocWaitlistMsgTemplate`
- `LoginAnomalyEventStore`
- `Macro`
- `MacroAction`
- `MacroInstruction`
- `MacroUsage`
- `MalformedTemplateTracker`
- `MarketSegment`
- `MarketSegmentActivation`
- `MarketSegmentField`
- `MessagingDeliveryError`
- `MessagingEndUser`
- `MessagingSession`
- `MessagingSessionMetrics`
- `MgmtOrgProvisioningAttempt`
- `MgmtOrgProvisioningError`
- `MgmtOrgProvisioningRequest`
- `MktCalculatedInsight`
- `MktDataTransform`
- `MktDataTransformSvcLocator`
- `MktMLModel`
- `MktMLModelPartitionRun`
- `MktMLModelSetupRun`
- `MktMLPredictionJob`
- `MktSgmntActvtnAudAttribute`
- `MktSgmntActvtnContactPoint`
- `MktSgmtActvContactPtField`
- `MktSgmtActvContactPtSrc`
- `MktSgmtActvDataModelFld`
- `MktSgmtActvDataSource`
- `MlAppMigrationStatus`
- `MlFeatureValueMetric`
- `MLMigration`
- `MLModel`
- `MLModelDataAlert`
- `MLModelFactor`
- `MLModelFactorComponent`
- `MLModelMetric`
- `MobileHomeConfiguration`
- `ObjectMilestonePauseTime`
- `Opportunity`
- `Order`
- `OrgDeleteRequest`
- `OrgMetric`
- `OrgMetricScanResult`
- `OrgMetricScanSummary`
- `PackageSubscriberOrgInfo`
- `PageContentAssignment`
- `PartyConsent`
- `Payment`
- `PaymentAuthAdjustment`
- `PaymentAuthorization`
- `PaymentCredit`
- `PaymentCreditLinePayment`
- `PaymentCreditTransaction`
- `PaymentGateway`
- `PaymentGatewayLog`
- `PaymentGroup`
- `PaymentLineInvoice`
- `PendingServiceRouting`
- `PendingServiceRoutingInteractionInfo`
- `PersonalizationResource`
- `Pricebook2`
- `PrivacyBatchReservation`
- `PrivacyJobSession`
- `PrivacyObjectSession`
- `PrivacyPolicy`
- `PrivacyProcessorOrchestrator`
- `PrivacyRTBFRequest`
- `PrivacySessionRecordFailure`
- `Problem`
- `ProblemIncident`
- `ProblemRelatedItem`
- `ProcessException`
- `Product2`
- `ProductAttribute`
- `ProductAttributeSetProduct`
- `ProductCatalog`
- `ProductCategory`
- `ProductCategoryProduct`
- `ProductConsumptionSchedule`
- `Project__c`
- `Promotion`
- `PromotionLineItemRule`
- `PromotionMarketSegment`
- `PromotionQualifier`
- `PromotionSegment`
- `PromotionSegmentBuyerGroup`
- `PromotionSegmentSalesStore`
- `PromotionTarget`
- `PromotionTier`
- `PromptAction`
- `PromptError`
- `QuickText`
- `QuickTextUsage`
- `RebatePayoutSnapshot`
- `Recommendation`
- `RecommendationReaction`
- `RecommendationResponse`
- `RecordAction`
- `RecordMergeHistory`
- `RecordOrigin`
- `Refund`
- `RefundLinePayment`
- `ReleaseUpdateStep`
- `ReleaseUpdateStepLog`
- `ReportAnomalyEventStore`
- `ReportResultBlob`
- `RequestsForAccessSIQ`
- `ResourceAbsence`
- `RetentionStoreUsage`
- `ReturnOrder`
- `ReturnOrderItemAdjustment`
- `ReturnOrderItemTax`
- `ReturnOrderLineItem`
- `Scorecard`
- `ScorecardAssociation`
- `ScorecardMetric`
- `SearchActivity`
- `SearchIndexFieldConfig`
- `SearchIndexObjectConfig`
- `SearchPromotionRule`
- `SearchRecencyIndexingJob`
- `SecurityHealthCheckAlertRecipient`
- `SecurityHealthCheckResult`
- `Seller`
- `ServiceAiState`
- `ServiceAppointment`
- `ServiceAppointmentAttendee`
- `ServiceAppointmentShift`
- `ServiceContract`
- `ServiceResource`
- `ServiceSetupProvisioning`
- `ServiceTerritory`
- `ServiceTerritoryWorkType`
- `SessionHijackingEventStore`
- `SetupAssistantAnswer`
- `SetupAssistantProgress`
- `SetupAssistantStep`
- `SetupFlowProgress`
- `Shift`
- `ShiftEngagementChannel`
- `ShiftWorkTopic`
- `Shipment`
- `ShipmentItem`
- `ShippingCarrier`
- `ShippingCarrierMethod`
- `ShippingConfigurationSet`
- `ShippingRateArea`
- `ShippingRateGroup`
- `SiqUserBlacklist`
- `SiteUserViewMode`
- `SoftwareProduct`
- `Solution`
- `SolutionDeploymentStatus`
- `SolutionDplymtStepStatus`
- `StagedInviteeEmail`
- `StandardShippingRate`
- `StoreIntegratedService`
- `StrategyMonthlyStats`
- `StreamActivityAccess`
- `SyncTransactionLog`
- `TableauHostMapping`
- `Task`
- `TenantConsumptionAlert`
- `TenantEntitlementTransaction`
- `TenantPvsnProdtLicMap`
- `TenantPvsnProduct`
- `TenantScrAIPrmptInjection`
- `TenantScrPermRiskClsfn`
- `TenantSecurityAIGtwyUsage`
- `TenantSecurityAlertRuleSelectedTenant`
- `TenantSecurityAnomaly`
- `TenantSecurityApiAnomaly`
- `TenantSecurityCertificate`
- `TenantSecurityConfigAgent`
- `TenantSecurityConnectedApp`
- `TenantSecurityCredentialStuffing`
- `TenantSecurityCustomMetricDetail`
- `TenantSecurityCustomMetricSetup`
- `TenantSecurityCustomMetricStat`
- `TenantSecurityEncryptedField`
- `TenantSecurityEncryptionPolicy`
- `TenantSecurityFeature`
- `TenantSecurityFieldClsfn`
- `TenantSecurityGuestUserAnomaly`
- `TenantSecurityHealthCheckBaselineTrend`
- `TenantSecurityHealthCheckDetail`
- `TenantSecurityHealthCheckTrend`
- `TenantSecurityLicense`
- `TenantSecurityLogin`
- `TenantSecurityLoginIpRangeTrend`
- `TenantSecurityMetricDetail`
- `TenantSecurityMetricDetailLink`
- `TenantSecurityMobilePolicyTrend`
- `TenantSecurityMonitorMetric`
- `TenantSecurityNotification`
- `TenantSecurityNotificationRule`
- `TenantSecurityPackage`
- `TenantSecurityPolicy`
- `TenantSecurityPolicyChangeLog`
- `TenantSecurityPolicyDeployment`
- `TenantSecurityPolicySelectedTenant`
- `TenantSecurityReportAnomaly`
- `TenantSecuritySessionHijacking`
- `TenantSecurityTenantChangeLog`
- `TenantSecurityTenantInfo`
- `TenantSecurityTransactionPolicyTrend`
- `TenantSecurityTrigTransactionSecurityPol`
- `TenantSecurityTrustedIpRangeTrend`
- `TenantSecurityUiFilter`
- `TenantSecurityUserActivity`
- `TenantSecurityUserPerm`
- `TenantSecurityWebsite`
- `TenantUsageTypeMultiplier`
- `TenantUsageTypeMultiplierDef`
- `Time_Entry__c`
- `TransactionSecurityAction`
- `TransactionSecurityActionEvent`
- `UniversalAnomalyEventStore`
- `UserAssistantSummary`
- `UserCapabilityPreference`
- `UserDevopsPreference`
- `UserEmailPreferredPerson`
- `UserLocalWebServerIdentity`
- `UserMetrics`
- `UserNavItem`
- `UserPrioritizedRecord`
- `UserQuestionnaireAnswer`
- `UserQuestionnaireSummary`
- `UserServicePresence`
- `VoiceCall`
- `VoiceChnlInteractionEvent`
- `VoiceChnlIntrctnDtlEvent`
- `VoiceMailGreeting2`
- `VoiceMailGreeting2Rep`
- `VoiceProvisioningJob`
- `Waitlist`
- `WaitlistParticipant`
- `WaitlistServiceResource`
- `WaitlistWorkType`
- `WebCart`
- `WebCartAdjustmentBasis`
- `WebCartAdjustmentGroup`
- `WebCartCredit`
- `WebCartDocument`
- `WebStore`
- `WebStoreBuyerGroup`
- `WebStoreCatalog`
- `WebStoreCMS`
- `WebStoreConfig`
- `WebStoreInventorySource`
- `Work_Item__c`
- `WorkflowSLAAction`
- `WorkOrder`
- `WorkOrderLineItem`
- `WorkPlan`
- `WorkPlanTemplate`
- `WorkPlanTemplateEntry`
- `WorkStep`
- `WorkStepTemplate`
- `WorkType`
- `WorkTypeGroup`
- `WorkTypeGroupMember`

### Relationships (Lookups)

- `BusinessProcessId` -> **BusinessProcess** (relationship: `None`)
- `CreatedById` -> **User** (relationship: `CreatedBy`)
- `LastModifiedById` -> **User** (relationship: `LastModifiedBy`)

### Child Relationships

- `Localization` -> `RecordTypeLocalization.ParentId`

---

## SOQL Quick Reference

### Date Literals

| Literal | Description |
|---------|-------------|
| `TODAY` | Current date |
| `YESTERDAY` | Previous day |
| `TOMORROW` | Next day |
| `THIS_WEEK` | Current week (Sun-Sat) |
| `LAST_WEEK` | Previous week |
| `NEXT_WEEK` | Next week |
| `THIS_MONTH` | Current calendar month |
| `LAST_MONTH` | Previous calendar month |
| `NEXT_MONTH` | Next calendar month |
| `THIS_QUARTER` | Current quarter |
| `THIS_YEAR` | Current calendar year |
| `LAST_90_DAYS` | Last 90 days |
| `LAST_N_DAYS:n` | Last n days |
| `NEXT_N_DAYS:n` | Next n days |
| `LAST_N_WEEKS:n` | Last n weeks |
| `LAST_N_MONTHS:n` | Last n months |

### Aggregate Functions

| Function | Description | Example |
|----------|-------------|---------|
| `COUNT(field)` | Count non-null values | `SELECT COUNT(Id) FROM Work_Item__c` |
| `COUNT_DISTINCT(field)` | Count distinct values | `SELECT COUNT_DISTINCT(Status__c) FROM Work_Item__c` |
| `SUM(field)` | Sum numeric field | `SELECT SUM(Hours__c) FROM Time_Entry__c` |
| `AVG(field)` | Average value | `SELECT AVG(Estimated_Hours__c) FROM Work_Item__c` |
| `MIN(field)` | Minimum value | `SELECT MIN(Due_Date__c) FROM Work_Item__c` |
| `MAX(field)` | Maximum value | `SELECT MAX(Due_Date__c) FROM Work_Item__c` |

### Common Patterns

```sql
-- Group by with aggregate
SELECT Status__c, COUNT(Id) cnt
FROM Work_Item__c
GROUP BY Status__c

-- Relationship query (parent)
SELECT Name, Project__r.Name, Assigned_To__r.Name
FROM Work_Item__c

-- Subquery (children)
SELECT Name, (SELECT Hours__c, Date__c FROM Time_Entries__r)
FROM Work_Item__c

-- Date filtering
SELECT Name FROM Work_Item__c
WHERE Due_Date__c = TODAY
  AND CreatedDate >= LAST_N_DAYS:30
```
