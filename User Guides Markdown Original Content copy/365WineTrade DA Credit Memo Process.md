_Microsoft Dynamics__®_ _365 Business Central_

|     |     |
| --- | --- |
|     |
|     | ![](365WineTrade%20-%20DA%20Credit%20Memo%20Process.fld/image003.png) |

  
365WineTrade by Western Computer Users Guide

365WineTrade DA’s Credit Memo Process

January 15th, 2024

  

Table of Contents

[1. Introduction. 2](#_Toc155940592)

[2. Dependencies and Assumptions 2](#_Toc155940593)

[3. Sales Invoice CM Overview.. 2](#_Toc155940594)

[3.1.1. Sales Credit Memo Process 2](#_Toc155940595)

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

The **365WineTrade Depletion Allowance functionality** adds-and provides extended functionality for dealing with depletion allowance in the wine industry. For a complete review of DA’s please refer to the Chargeback User Guide. The function of this guide is to review the best practices recommended when processing Sales Credit Memo’s where DA’s are active in a company.

# 2.   Dependencies and Assumptions

The minimum required version of BC for this version of **365WineTrade**, is v18, also known as Business Central 2021 release Wave 1.

This add-on also depends on the **365WineTrade** **Base** extension, v 1.0.0.0.

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating/viewing/editing/deleting records, filtering, and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

# 3.   Sales Invoice Credit Memo Overview

The **365WineTrade Depletion Allowance** **(DA)** module provides additional functionality to the wine trade industry that enhances the capability to extend DA functionality common to the wine industry. Please refer to the Chargeback user guide for an extensive review of the functionality. This user guide will focus on the Sales Invoice Credit Memo process.

**Disclaimer:** On the posted sales invoice the DA’s can be traced to a Vendor from the source item ledger entry. With regards to Sale Credit memo the DA chargeback amounts are created based on the default vendor setting of the item card. Industry assumption in design is that items are strongly influenced by brands which have but one vendor source. Multiple supply sources of a product is uncommon reducing this risk to a negligible level. Under this assumption it is important to note that BC functionality does provide for purchasing from different vendors and this will cause a miss match of DA’s Under a Sales Order vs. a Sales Credit memo if more the one vendor source is being used.

### 3.1.1.     Sales Credit Memo Process

There are four ways to appropriately create and process a Sales Credit Memo with in a company where DA’s are active and in use.

·       **Correct** “function from the ribbon of the posted sales invoice document”

·       **Create Corrective Credit Memo** “function from the ribbon of the posted sales invoice document”

·       **Cancel** “function from the ribbon of the posted sales invoice document”

·       **Manually Created Credit Memo** “Using Copy Document Process”

All of these methods will create a proper Sales Credit Memo with all associated entries as expected including DA ledger entry information as well. **Note: Never create a manual Sales Credit Memo with out the Copy Document function as this will ignore DA ledger entries**.

The first method to create a sales credit memo is **“Correct”** See below for a reference to the location on a posted sales invoice you can create:

![](365WineTrade%20-%20DA%20Credit%20Memo%20Process.fld/image004.png)

This method type will automatically create and post a document with all appropriate entries including DA entries based on the default active vendor from the item card.

The Second method to create a sales credit memo is “Create Corrective Credit Memo” See below for the location of the function on the Posted Sales Invoice document:

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20DA%20Credit%20Memo%20Process.fld/image005.png)

Using this method the system will create a credit memo on your active screen that you can review prior to posting. This method will require the user to post the document manually. As outlined prior all appropriate entries will be created including DA ledger entries based on the active default vendor on the item card.

The 3rd method “Cancel” reacts the same way as the “Correct” function with the exception that it leaves the newly created sales credit memo on your screen for follow up review.

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20DA%20Credit%20Memo%20Process.fld/image006.png)

The fourth and final method is the manual credit memo using the copy document function. Please refer to your base BC user guide for this process outline.

The best practice recommendation will depend on if you wish to review a document before or after posting or both. Each of the methods from the posted sale invoice document are the preferred method as they require less key strokes to accomplish the task. The manual credit memo using the copy document function will get the job done but requires several steps to complete.