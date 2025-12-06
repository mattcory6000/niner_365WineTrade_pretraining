_Microsoft Dynamics__®_ _365 Business Central_ 

![Shape](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image003.png)365WineTrade Chargebacks  
Users Guide 

Last Update: May 13, 2024

  

**Change Log:** 

|     |     |     |
| --- | --- | --- |
| **Date** | **Name** | **Description** |
| 3/19/2024 | Maurice | Section 5.2-Process DA Price updates |
| 4/08/2024 | Maurice Tisseur | Section 4 Chargeback setup. Updated wording to remove reference to Depletion Policy and better reflect the DA process |
| 5/13/2024 | Maurice Tisseur | Section 4 Chargeback setup page. Added additional information and screen shot for Chargeback Unit type as well as Chargeback dimension grouping |
|     |     |     |
|     |     |     |

  

Table of Contents

[1. Introduction. 4](#_Toc166501607)

[2. Dependencies and Assumptions 4](#_Toc166501608)

[3. 365WineTrade Chargebacks 4](#_Toc166501609)

[4. Chargeback Setup. 6](#_Toc166501610)

[4.1. Chargeback Posting Setup. 9](#_Toc166501611)

[4.2. Dimension Groups 9](#_Toc166501612)

[5. Process Chargebacks 11](#_Toc166501613)

[5.1. Process Depletion Allowances. 11](#_Toc166501614)

[5.1.1. Sales Credit Memo Process for Depletion Allowances 12](#_Toc166501615)

[5.2. Process Depletion Allowance Price Update. 14](#_Toc166501616)

[5.3. Process Sample Bill Backs 15](#_Toc166501617)

[5.4. Process Bad Bottles. 18](#_Toc166501618)

[6. Chargeback Ledger Entries. 19](#_Toc166501619)

  

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

The **365WineTrade Chargebacks** add-on provides extended functionality for dealing with Vendor Chargebacks, such as:

·       Depletion Allowances

·       Bad Bottles

·       Sample Billbacks

# 2.   Dependencies and Assumptions

The minimum required version of BC for this version of **365WineTrade**, is v18, also known as Business Central 2021 release Wave 1.

This add-on also depends on the **365WineTrade** **Base** extension, v 1.0.0.0.

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating, viewing, editing and deleting records, filtering and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

# 3.   365WineTrade Chargebacks

If the **365WineTrade** **Chargebacks** have been successfully installed, you will find a new menu option under the **365WineTrade** menu:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image004.png)

Figure 3‑1: Chargebacks Menu

**365WineTrade** supports users in processing Chargebacks (aka Billbacks) for the following transactions:

·       Depletion Allowances

·       (Sample) Bill Backs

·       Bad Bottles

When the system is properly setup, users can execute the different types of chargeback processes in order to generate Purchase Credit Memos for respective refunds.

For each transaction type (Depletion Allowances, Bill Backs, Bad Bottles), **365WineTrade** offers one out-of-the-box calculation process, but users can also customize the system for their own calculation process with their own business logic. Please refer to section Chargeback Setup below for more details.

  

 

# 4.   Chargeback Setup

You can find the Chargeback Setup under the **365WineTrade** menu, **Chargebacks**, **Chargeback Setup**. The setup card is shown below:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image005.png)

Figure 4‑1: Chargeback Setup Card

Table 4‑1: Chargeback Setup fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Depletion Allowance**<br><br>**Purchase Invoice Document No.** | No. Series override setting for this document type. |
| **Depletion Allowance**<br><br>**Purchase Credit Memo Document No.** | No. Series override setting for this document type. |
| **Depletion Allowance**<br><br>**Vendor Credit Memo No** | No. Series override setting for this document type. |
| **Depletion Allowance**<br><br>**Charge Item** | Charge Item to be used when creating Purchase Credit Memos for Depletion Allowances |
| **Amount Unit Type** | This defines what unit type is used in connection with creating a DA credit memo. |
| **Dimension Group Code** | When defined by dimension groups it allows the DA credit memo to consolidate lines based on dimension groups. The purpose is to reduce the number of lines created on a purchase credit memo. |
| **Depletion Allowance**<br><br>**Vendor Posting Group** | Alternative posting group option to provide flexibility in selecting another GL separate from the regular AP liability account. |
|     |     |
| **Depletion Allowance**<br><br>**Dimension Group Code** | Functionality to provide ability to group depletion lines by dimension. Feature primary purpose is to consolidate large amounts of information. |
| **Depletion Allowance**<br><br>**Payment Terms Code** | Override payment term code setting to deviate from normal vendor card |
| **Depletion Allowance**<br><br>**Reason Code** | Reason Code to be used on Depletion Allowances Purchase Credit Memos |
| **Depletion Allowance**<br><br>**Post Purchase Accrual to G/L** | Toggle switch when set to True Accrual Entries will be posted to the G/L |
| **Depletion Allowance**<br><br>**Use Sales Document Dimension** | Toggle switch to have chargeback function use Sales Document dimension vs. Purchase document for grouping purposes. |
| **Depletion Allowance**<br><br>**Processing Report Id** | Report ID for the Depletion Allowance calculation process. There is one out-of-the-box report for Depletion Allowances:<br><br>·       **89000**: Calculates depletion allowances based only on the general depletion amounts<br><br>For more details, please refer to section [Depletion Policies](#_Depletion_Policies) further below |
| **Bad Bottle**<br><br>**Location Code** | Location to be used for Bad Bottle bill back calculation |
| **Bad Bottle**<br><br>**Reason Code** | Reason Code to be used on Bad Bottles Purchase Credit Memos |
| **Bad Bottle**<br><br>**Vendor Posting Group** | Alternative posting group available for flexibility in posting to different G/L account |
| **Bad Bottle**<br><br>**Payment Terms Code** | Override payment term code available to deviate from vendor card default setting |
| **Bad Bottle**<br><br>**Vendor Credit Memo No** | No. Series override for this document type. |
| **Bad Bottle**<br><br>**Processing Report Id** | Report ID for the Bad Bottle calculation process. The out-of-the-box Report Id for this process is **89003** |
| **Bill Back**<br><br>**Reason Code** | Reason Code to be used on Bill Back Purchase Credit Memos |
| **Bill Back**<br><br>**Vendor Posting Group** | Alternative posting group available for flexibility in posting to different G/L account |
| **Bill Back**<br><br>**Payment Term Code** | Override payment term code available to deviate from vendor card default setting |
| **Bill Back**<br><br>**Bill-Back Charge Item** | Default Charge Item code to be used. |
| **Bill Back**<br><br>**Processing Report Id** | Report ID for the Bill Back calculation process. The out-of-the-box Report ID for this process is **89002** |

## 4.1.        Chargeback Posting Setup

The Chargeback Posting setup is needed to setup G/L Accounts that will be used for both Depletion Allowance and Bill Back processing processes.

You can find this setup under the **365WineTrade** menu, **Chargebacks**, **Chargeback Posting Setup**. You will be taken to the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image006.png)

Figure 4‑2: Chargeback Posting Setup list

When processing Depletion Allowances and Bill Backs, BC will refer to this setup to determine the correct G/L Account based on the **Gen. Bus. Posting Group** and **Gen. Prod. Posting Group** of the original transactions.  
  

If a combination is missing from the setup, an error message will be generated when processing the processes.

## 4.2.        Dimension Groups

Dimension group settings are used in the chargeback process when creating the purchase credit memo to group entries. The underlying premise for this feature is to reduce the number of lines printed on a purchase credit memo. There can be hundreds of pages for one credit memo, so by grouping the transactions by Dimensions will consolidate the line information.

Chargeback dimension groups can be found under the 365WineTrade menu as seen below in the screen shot provided.

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image007.png)

Figure 4‑3: Dimension Groups List

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image008.png)

Figure 4‑4: Dimension Groups List

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image009.png)

Figure 4‑5: Dimension Group Lines

# 5.   Process Chargebacks

To process any of the **Chargebacks**, you go to the **365WineTrade** menu, **Chargebacks**, **Process Chargebacks**. This will take you to the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image010.png)

Figure 5‑1: Process Chargebacks options

To run any of these processes, you must select the desired process by clicking on it, then **Run**.

For details on each one of these processes, please refer to the sections below.

## 5.1.        Process Depletion Allowances

**Please note**: all the details below relate to out-of-the-box report 89000. If you have customized your Depletion Allowances process, this section may not apply.

When running the Depletion Allowances process, you will first be prompted for a few parameters:

![A screenshot of a computer screen
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image011.png)

Figure 5‑2: Depletion Allowance parameters

Table 5‑1: Depletion Allowance parameters description

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Document Date** | Document Date to be used on the Purchase Credit Memo |
| **Posting Date** | Posting Date to be used on the Purchase Credit Memo. **Please note**: This is not a filter |
| **Reason Code** | Reason Code to be used on the Purchase Credit Memo. On the first run, this value will default to the Reason Code defined on the [Chargeback Setup](#_Chargeback_Setup) |
| **Description** | Posting Description that will be used when posting the Purchase Credit Memo |

BC will run against all open depletion allowance ledger entries based on the filters provided in the process window. The process will use these entries as the source information in creating a depletion allowance credit memo to the vendor. When the process has completed the depletion allowance purchase credit memo will be available for final review and posting. When the credit memo has been posted the depletion allowance ledger entries will be marked closed and the posting document number will be added to the ledger entry to complete the audit trail and process.

If a specific sales transaction is not picked up by the out-of-the-box calculation report, and you need to troubleshoot it, here are the most common reasons:

·       The Item Ledger Entry may not be of type **Sales**, or it may not have been Invoiced yet. If **Invoiced Quantity** = 0, BC will ignore this Item Ledger entry.

·       The Item Ledger Entry may have been processed by another Depletion Allowance calculation. You can search the Item Ledger Entry No. on the Depletion Allowance Ledger Entries.

·       The **Order Type** for the Item Ledger Entry does not have field **Depletion Allowance** set to True.

·       The Item Ledger Entry generates a calculated Depletion Amount of zero (if no depletion amounts could be found for the total quantity or total amount for the item ledger entry).

·       The Item Ledger Entry does not have an Inbound Item Ledger Entry applied to it

**Please note**: The out-of-the-box calculation report does not cross check that the **Item No**. belongs to a specific **Vendor No**. If you enter a wrong Item for a Vendor, BC will not stop the processing, and it will not issue any warnings either. This is by design, to allow for flexibility when setting up chained vendors structures.

### 5.1.1.     Sales Credit Memo Process for Depletion Allowances

There are four ways to appropriately create and process a Sales Credit Memo within a company where Depletion Allowances are active and in use.

·       **Correct** “function from the ribbon of the posted sales invoice document”

·       **Create Corrective Credit Memo** “function from the ribbon of the posted sales invoice document”

·       **Cancel** “function from the ribbon of the posted sales invoice document”

·       **Manually Created Credit Memo** “Using Copy Document Process”

All of these methods will create a proper Sales Credit Memo with all associated entries as expected including Depletion Allowance ledger entry information as well. **Note:** Never create a manual Sales Credit Memo without the Copy Document function as this will ignore Depletion Allowance ledger entries.

The first method to create a sales credit memo is **“Correct”** See below for a reference to the location on a posted sales invoice you can create:

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image012.png)

This method type will automatically **create and post** a document with all appropriate entries including Depletion Allowances entries based on the default active vendor from the item card.

The Second method to create a sales credit memo is “Create Corrective Credit Memo” See below for the location of the function on the Posted Sales Invoice document:

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image013.png)

Using this method the system will create a credit memo on your active screen that you can review prior to posting. This method will require the user to post the document manually. As outlined prior all appropriate entries will be created including Depletion Allowance ledger entries based on the active default vendor on the item card.

The 3rd method “Cancel” reacts the same way as the “Correct” function with the exception that it leaves the newly created sales credit memo on your screen for follow up review.

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image014.png)

The fourth and final method is the manual credit memo using the copy document function. Please refer to your base BC user guide for this process outline.

The best practice recommendation will depend on if you wish to review a document before or after posting or both. Each of the methods from the posted sale invoice document are the preferred method as they require less keystrokes to accomplish the task. The manual credit memo using the copy document function will get the process completed but requires several steps to complete.

## 5.2.        Process Depletion Allowance Price Update.

In the case of a DA price update that is affecting already posted sales invoices there is a WT function that will facilitate these changes on Posted Sales Invoice. There are a few steps in the process that are required in updating the DA Amouns on DA ledger entries.

·       The 1st step is to update the Sales Price List with the updated DA unit amounts.

·       2nd step is to delete all the DA ledger entries affected by the DA unit price update.

·       3rd step is to select all Posted Sales Invoices that will be affected by the DA price update.

·       4th and final step run the Update Depletion Allowance.

Updating the Sales Price List:

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image015.png)

Deleting Depletion Allowance Ledger entries:

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image016.png)

Selecting Posted Sales Invoices and Update Depletion Allowances:

![](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image017.png)

After the final step the Depletion Allowance ledger entries will have been created with the new Depletion Allowance amounts. This final step can be validated from the Depletion Allowance Ledger entry list for the updated Depletion Allowance amounts.

**Note:** Depletion allowance ledger entries already posted to a Chargeback vendor Credit memo are not intended to be included in this process.

## 5.3.        Process Sample Bill Backs

**Please note**: all the details below relate to out-of-the-box report 89002. If you have customized your Bill Backs process, this section may not apply.

When running the Bill Backs process, you will first be prompted for a few parameters:

![A screenshot of a computer screen
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image018.png)

Figure 5‑3: Bill Backs parameters

Table 5‑2: Bill Backs parameters description

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Document Date** | Document Date to be used on the Purchase Credit Memo |
| **Posting Date** | Posting Date to be used on the Purchase Credit Memo. **Please note**: This is not a filter |
| **Description** | Posting Description that will be used when posting the Purchase Credit Memo |
| **Reason Code** | Reason Code to be used on the Purchase Credit Memo. On the first run, this value will default to the Reason Code defined on the [Chargeback Setup](#_Chargeback_Setup) |
| **Bill Back Rate** | Choose from **Use Order Type** or **Force to Percent** |
| **Bill Back Percent** | If **Bill Back Type** is **Force to Percent**, use this field to determine the percent to be used. **Please note**: Even if you use **Force to Percent** above, the **Order Type** for the Sales Order must be a type that has field **Bill Back %** filled out. For more details, please refer to section [Order Types](#_Brand_Item_Registration) |
| **Bottle Up-Charge** | Up-charge to be added to the Unit Cost |

It is also recommended that you set filters on the **Vendor** and **Item Ledger Entry** FastTabs of this report. If you do not set any **Vendor**, **Date** or **Item** filters, then BC may take a bit longer to run depending on how much historical data you currently have on your database:

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image019.png)

Figure 5‑4: FastTabs Vendor and Item Ledger Entry

Once you fill out all the parameters and press Ok, BC will run all Item Ledger Entries of type **Sales**, that has **Invoiced Quantity** <> 0.

When creating the Purchase Credit Memo, BC will always try to find an existing Purchase Credit Memo header where:

·       **Vendor No.** equals to the **Vendor No.** on the Item Card

·       **Posting Date** equals to the **Posting Date** defined on the Request Page of the report

·       **Reason Code** equals to the **Reason Code** defined on the Request Page of the report

If no Purchase Credit Memos are found for these filters, then BC will create a blank one. If it does find one, then any new lines will be added to the existing Purchase Credit Memo.  
  

For each sales transaction, BC will create 2 purchase lines: one for the actual item being billed back, and one with more details on the sales transaction that was calculated.

If a specific sales transaction is not picked up by the out-of-the-box calculation report and you need to troubleshoot it. Here are the most common reasons:

·       If you are filtering the Bill Back request page with a **Vendor No**. filter, it may be that the items on the specific sales transaction do not belong to the Vendor you’re filtering to.

·       The Item Ledger Entry may not be of type **Sales**, or it may not have been Invoiced yet. If **Invoiced Quantity** = 0, BC will ignore this Item Ledger Entry.

·       The Item Ledger Entry may have been processed by another Bill Back calculation. You can search the Item Ledger Entry No. on the Bill Back Ledger Entries.

·       The **Order Type** for the Item Ledger Entry does not have field **Bill Back %** filled out. Even if you have **Bill Back Type** set to “**Force to Percent”**, you still need to have a **Bill Back %** on the **Order Type.**

## 5.4.        Process Bad Bottles

**Please note**: all the details below relate to out-of-the-box report 89003. If you have customized your Bad Bottles process, this section may not apply.

When running the Bad Bottles process, you will first be prompted for a few parameters:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image020.png)

Figure 5‑5: Bad Bottles parameters

Table 5‑3: Bad Bottles parameters description

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Document Date** | Document Date to be used on the Purchase Credit Memo |
| **Posting Date** | Posting Date to be used on the Purchase Credit Memo. **Please note**: This is not a filter. For filtering, use the **Posting Date** field on the Item Ledger Entry Data Item |
| **Description** | Posting Description that will be used when posting the Purchase Credit Memo |
| **Location Code** | Location Code under which Bad Bottle transactions are recorded. On the first run, this value will default to the Location Code defined on the [Chargeback Setup](#_Chargeback_Setup) |
| **Reason Code** | Reason Code to be used on the Purchase Credit Memo. On the first run, this value will default to the Reason Code defined on the [Chargeback Setup](#_Chargeback_Setup) |

Once you fill out all the parameters and press Ok, BC will run all **Open** Item Ledger Entries where **Location Code** is the Bad Bottles Location (set on the Request Page).

For each Item Ledger Entry that satisfies the filter above, BC will check if they have not been processed before (e.g., the entry may be pending in another open Purchase Credit Memo). If they have been processed before, BC will skip them.

BC will also check that the item has a **Vendor No**. setup. If the **Vendor No**. field is blank, BC will throw an error message and it will abort the whole process.

When creating the Purchase Credit Memo, BC will always try to find an existing Purchase Credit Memo header where:

·       **Vendor No.** equals to the **Vendor No.** on the Item Card

·       **Posting Date** equals to the **Posting Date** defined on the Request Page of the report

·       **Reason Code** equals to the **Reason Code** defined on the Request Page of the report

If no Purchase Credit Memos are found for these filters, then BC will create a blank one. If it does find one, then any new lines will be added to the existing Purchase Credit Memo.

For each Item Ledger Entry, BC will create a Purchase Line. If the Item is currently blocked, BC will create a line with the Item No., and description will read “Item Blocked”. Once the blocked Items are unblocked and removed from the Purchase Credit Memo, then users can run the process again, if needed.

Note: two recommended paths for getting the bad bottles into the **return** location that allows the chargeback system to pick up the bad bottle entries are: Sales Return Credit Memo or an Item Reclassification journal. Both methods work as long as the correct Reason Code is used that matches the setup under the Chargeback Setup area.

# 6.   Chargeback Ledger Entries

Unlike most ledger entries in BC (that are created upon posting of documents), the Chargeback Ledger Entries are created as soon as they are processed using the different processes described in section Process Chargebacks above. The reason for this is to prevent any sales transaction/Item Ledger Entry from being processed twice. Therefore, the Chargeback Ledger Entries list will always list entries for both posted and unposted Purchase Credit Memos.

To find the Chargeback Ledger Entries, you can go to the **365WineTrade** menu, **Chargebacks**, **Chargeback Ledger Entries**, and select one of the following: **Depletion Allowance Ledger Entries**, **Bill Back Ledger Entries**, **Bad Bottle Ledger Entries**. They all resemble the page below:

![Graphical user interface
Description automatically generated with medium confidence](365WineTrade%20Users%20Guide%20-%20Chargebacks.fld/image021.png)Figure 6‑1: Depletion Allowance Ledger Entries

Note how the lines above do not show any information on field **Posted Document No**. This means that the document is not posted at this point. Once posted, then these lines will remain the same, and field **Posted Document No**. will also be populated.

From this page, if you try to delete any entries, BC will only allow deletion of unposted entries. Furthermore, BC will not delete individual Chargeback Ledger Entries. Rather, it will delete the original Purchase Credit Memo linked to the entry you are trying to delete. Therefore, all entries for the same Purchase Credit Memo will also be deleted. If you delete any unposted entries, the original transactions will then be available for calculation again.

Lastly, from this page, you have some convenience actions to access the original documents, such as **Show Purchase Document**, **Show Sales Shipmen**t, **Show Sales Invoice**, etc.