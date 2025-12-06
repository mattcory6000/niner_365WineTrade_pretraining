_Microsoft Dynamics__®_ _365 Business Central_

|     |     |
| --- | --- |
|     |
|     | ![](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image003.png) |

  
365WineTrade NYSLA V2 Update Guide

January 23, 2024

  

Table of Contents

[1. Introduction............................................................................................................................... 2](#_Toc2029870576)

[2. Dependencies and Assumptions.................................................................................................. 2](#_Toc458238344)

[3. NYSLA V2 Process....................................................................................................................... 2](#_Toc1985781071)

[3.1.1. License Update Process................................................................................................ 2](#_Toc1574220188)

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

# 2.   Dependencies and Assumptions

The minimum required version of BC for this version of **365WineTrade**, is v18, also known as Business Central 2021 release Wave 1.

This add-on also depends on the **365WineTrade** **Base** extension, v 1.0.0.0.

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating/viewing/editing/deleting records, filtering, and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

# 3.   NYSLA V2 Process

The **365WineTrade NYSLA V2** module provides additional functionality to the wine trade industry that enhances the capability to extend license update to the New York wine industry.

### 3.1.1.     License Update Process

Step 1: Western Computer to Update Sandbox with NEW NY SLA V2 Extension. Minimum requirement 365WineTrade US Compliance Ver. 1.3.2.2

  

Step 2: Proceed to Data Processing to Run New NYSLA V2 Update function.

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image004.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image005.png)

Step 3: Run the function “Get New Licenses” In addition to getting the new license information the system will also add new method codes that will need to be assigned manually.

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image006.png)

Step 4: Update under “State License Setup” the new SLAv2 methods as seen below in the screen shot.

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image007.png)

After you have updated the SLA state method to the V2 version you also have the optional setting under the “Payment License Handling” for “Automatic”. This setting is only available for the “Remove” method. What the setting provides is the automatic removal of a submitted delinquency to the SLA allowing a payment application to be made without manual intervention to remove the delinquency. See screen shot below for setting.

![](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image008.png)

Step 5: “Get New Licenses” Function run earlier in the process will populate the screen with current NY customers with old license with Cross Ref to the New License Number NY will be moving too. **The system has intelligence built in that if existing State License Categories have been defined and assigned to the License type it will migrate this matrix of category assignment to the new license type.**

Step 6. Customer with a License status code of “NF” not found the client will need to research these licenses to resolve the issue with the number?

Step 7: Validate the “State License Categories” have been applied correctly to the New State License Types. This task is completed under the License Type Management page. For each of the New License types that have been imported should have adopted the category assignments from the old license type.

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image009.png)

Step 8: After NF licenses have been resolved and the License type Management update tasks are complete. You can now make License active from the NY SLA Upgrade function discussed prior.

This task can be performed on a selective basis customer by customer:

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image010.png)

Or License can be made active by entire group by using base BC functionality for select all as seen in the screen shot below

![A screenshot of a computer
Description automatically generated](365WineTrade%20-%20NYSLAV2%20Update%20Process.fld/image011.png)

**Step 9: \*\*Client will perform transaction testing in the sandbox to validate for any possible issue with License update\*\***

Step 10: Repeat Steps 1-7 in the production environment. The final step 8 where licenses are made active for the new license should be performed the evening of Wednesday, January 31, 2024 assuming this is the formal cutoff the state has committed to.