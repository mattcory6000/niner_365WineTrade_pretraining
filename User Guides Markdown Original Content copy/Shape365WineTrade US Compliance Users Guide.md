![](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image001.png)

![](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image002.png)

_Microsoft Dynamics__®_ _365 Business Central_ 

![Shape](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image003.png)365WineTrade Pricing  
Users Guide 

Last Update: October 31, 2024

**Change Log:** 

|     |     |     |
| --- | --- | --- |
| **Date** | **Name** | **Description** |
| 04/05/2024 | Maurice Tisseur | Section 4.2 updated for co-op pricing based on Price start date |
| 04/05/2024 | Maurice Tisseur | Section 3.1.4 Price Priority new section |
| 04/23/2024 | Maurice Tisseur | Section 3.2.1 updated Co-Op Pricing |
| 10/31/2024 | Maurice Tisseur | Section 3.1.5 Updated Mix & Match to include Pricing Unit Type setting on Wine Setup |
|     |     |     |

  

Table of Contents

[1. Introduction. 4](#_Toc181358332)

[2. Dependencies and Assumptions 4](#_Toc181358333)

[3. Pricing Overview.. 4](#_Toc181358334)

[3.1.1. Customer Price Groups 4](#_Toc181358335)

[3.1.2. Pricing Based off Shipment Date. 6](#_Toc181358336)

[3.1.3. Customer Specific Pricing. 8](#_Toc181358337)

[3.1.4. Pricing Priority. 8](#_Toc181358338)

[3.1.5. Key Mix & Match Setup Areas 10](#_Toc181358339)

[3.2. Co-op Pricing. 14](#_Toc181358340)

[3.2.1. Co-op Pricing (“Co-oping”) 14](#_Toc181358341)

[3.2.2. Key Co-op Setup Areas 16](#_Toc181358342)

[3.3. Family Plans Pricing. 19](#_Toc181358343)

[3.3.1. Family Plans 19](#_Toc181358344)

[3.3.2. Calculation of Price upon Releasing. 20](#_Toc181358345)

  

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

The **365WineTrade Pricing** add-on provides extended functionality for dealing with Pricing in the wine industry. These Pricing features include:

·       Mix & Match

·       Family Plan

·       Co-op

·       Customer Specific

# 2.   Dependencies and Assumptions

The minimum required version of BC for this version of **365WineTrade**, is v18, also known as Business Central 2021 release Wave 1.

This add-on also depends on the **365WineTrade** **Base** extension, v 1.0.0.0.

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating/viewing/editing/deleting records, filtering, and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

# 3.   Pricing Overview

The **365WineTrade Pricing** module provides for additional functionality to the wine trade industry that enhances the capability to provide extended pricing common to the wine industry.

### 3.1.1.     Customer Price Groups

The following fields on the Customer Price Groups table are available:

·       **Co-Op Pricing**, Boolean

·       **Family Plans**, Boolean

·       **Mix-and-Match**, Boolean

All these fields become active and available in Customer Price Group table when “New sales pricing experience” is Enabled for “ALL Users” in the Feature Management area. Make sure this feature has been Enabled prior to embarking on any special pricing setup. To Access the feature management area, proceed to the search magnifier from the ribbon and proceed as normal. You will be presented with the feature management page as seen in the screenshot below.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image004.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image005.png)

For each of the pricing models available you can enable them by selecting the appropriate check box for a particular Price Group. To find the Customer Price Group page proceed to the base BC365 magnifier in the ribbon to search using the page name.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image006.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image007.png)

### 3.1.2.     Pricing Based off Shipment Date

Standard BC fetches prices based on the Order Date of a Sales Order. WineTrade365 offers functionality that will search for Sales Prices based on the **“Price Starting** **Date”** setup in Wine Setup. This global setting has the following date options (Shipment date, Order Date, Document date, and Posting Date). ![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image008.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image009.png)

Pricing based on **“Price Starting Date**” can also be set at a more granular level of the Price Group as seen in the screenshot below.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image010.png)

### 3.1.3.     Customer Specific Pricing

Standard BC allows for prices to be entered on different levels (All Customers, Customer Price Group, Customer-specific, etc.), but these levels are not organized in a top-down structure. This means that if a Customer-Specific-Price is more expensive than a Customer Price Group-price, BC will ignore the Customer-Specific-Price because its policy is to always find the best price for a customer, which is the LOWEST price among all levels.

WineTrade365 has been modified to overrides this best price behavior for Customer-specific pricing. Therefore, if any Customer-specific pricing is set, WineTrade365 will respect this price. Pricing Models Explained.

### 3.1.4.     Pricing Priority

For other pricing matrix requirements WineTrade365 offers additional pricing features that can override the lowest price function of Standard BC. By creating Price Priorities as seen in the screen shot below you can have “Campaign” pricing take a priority position and set pricing based on this.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image011.png)

To activate Price Priority, you must setup the setting on the Wine Setup card as seen below.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image012.png)  
The process flow of the system will follow based on this setup is 1st look at the Sales Price List for a campaign price match. If the system finds a match the system will stop and go no further and except the system price at this point. If the system does not find a match it will proceed to the next type for customer specific pricing and if no match there the system will default to the next available best price match as the following step have no method identified to “stop if found”. By way of this price priority functionality we are able to by pass best price functionality of BC under flexible user conditional setup.

Mix & Match

Mix-and-Match pricing works based on the Sales Price Group of an Item. In 365WineTrade, use the field **Sales Price Group (SPG)** (on the Item Card) to control items that you want to use in Mix & Match pricing promotions.

**Within one same sales order**, **WineTrade365** will need to calculate the total Case Count based on the **Sales Price Group** of each item. Then based on the total case count per **SPG**, BC will need to find the best price using the total case count as parameter of comparison with the Min. Quantity field.

Each individual Price List entry can be enabled or disabled for Mix & Match. When creating a new Price List entry, if the Customer Price Group allows for Mix & Match, then **Mix & Match Enabled** will default to true. Users will have to uncheck prices they don’t want as part of the Mix & Match pricing. Users should not be able to set **Mix & Match Enabled** if the Customer Price Group doesn’t allow it either.

**Note!:** The Selling UOM of the Sales Order must match the UOM on the Price List or Mix & Match will ignore the quantity break pricing of all quantity’s on the order. For Example, if your Sales Order has sales lines in UOM of **Bottle** and the Price List is using CASES the system will ignore any consolidated quantities of participating Mix & Match items. The system will still respect and make the conversion of quantity break pricing of the item itself but ignore the Mix & Match component.

Mix-and-Match Example

Consider the following items, and their price lists:

Items:

|     |     |
| --- | --- |
| Sku # | Sales Price Group |
| WINE1-750 | WINE1 |
| WINE1-1.5 | WINE1 |
| WINE2-750 | WINE2 |

Price Lists (Sales Price entry):

|     |     |     |     |
| --- | --- | --- | --- |
| Item | Min Qty | Price | **Mix-and-Match Enabled\*** |
| WINE1-750 | 1   | $ 35 | Yes |
| WINE1-750 | 5   | $ 33 | Yes |
| WINE1-750 | 10  | $ 31 | Yes |
| WINE1-1.5 | 1   | $ 55 | Yes |
| WINE1-1.5 | 5   | $ 53 | Yes |
| WINE1-1.5 | 10  | $ 51 | Yes |
| WINE2-750 | 1   | $ 66 | Yes |
| WINE2-750 | 5   | $ 64 | Yes |
| WINE2-750 | 10  | $ 62 | Yes |

Consider the following Sales Order Lines:

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Line #** | **Item No.** | **Sales Price Group** | **Qty (cases)** | **Original Price** | **Mix-and-Match Price** |
| **1** | WINE1-750 | WINE1 | 1   | $ 35 | $ 33 |
| **2** | WINE1-1.5 | WINE1 | 6   | $ 53 | $ 53 |
| **3** | WINE2-750 | WINE2 | 3   | $ 66 | $ 66 |
|     |     | Total Case Count | 10  |     |     |

·       The total case count for **SPG** WINE1 is 7, and for WINE2 is 3

·       The original price for Line #1 is $35, according to the price list, however, because the total count for Label WINE1 is 7, then BC needs to find the price range applicable for 7 cases, and it finds $ 33

·       The original price for Line #2 remains the same ($53), because the price for 7 cases is the same for the individual quantity of 6 cases

·       The original price for Line #3 remains the same ($66), because the total case count on the line is the same total case count for label WINE2.

·       Mix & Match price finding, WineTrade365 should not look into prices where **Mix & Match Enabled** is FALSE.

·       The sale order price calculation is repriced to the Mix & Match model when an order is placed in **Released status**.

·       In the event where the original price is cheaper than the Mix & Match Price, WineTrade365 needs to choose the lowest price, **unless** there’s a [**Customer Specific Pricing**](#_Customer_Specific_Pricing) setup.

### 3.1.5.     Key Mix & Match Setup Areas

·       The foundation for the setup starts with **Sales Price Categories**. You must create a group code that will be used to Link Items to the Price List and eventually customers that you want to participate in a Mix & Match promotion.

·       The Sales Price Category Code is then added to the Mix & Match Category Code for a particular Customer Price Group**. Note!** You cannot have more than one active Sales Price Category on a Customer Price Group at a time.

·       On the Item card under the **Prices & Sales** fast tab you must add the **Sales Price Category** code to the **Sales Price Group** of the Item card.

·       On the **Wine Setup** card under the sales menu, “**Pricing Unit Type**” has been added to allow Mix & Match pricing to use an alternative UOM. In prior versions this was limited to case. Setting the pricing unit type to “Unit” allows the user to use a UOM of bottle. It should be noted that whatever the setting, Case or Unit, the Mix & Match Price list must also be represented in the same UOM

·       The final piece to the setup is the customer card must have the **Customer Price Group** added under the **Invoicing** fast tab of the customer card.

Search for Sales Price Categories:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image013.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image014.png)

Search for Customer Price Group:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image015.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image016.png)

Search for Items:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image017.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image018.png)

Search for Customer:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image019.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image020.png)

Search for Wine Setup

![](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image021.png)

## 3.2.        Co-op Pricing

### 3.2.1.     Co-op Pricing (“Co-oping”)

New Jersey Alcoholic Beverage Purchasing Cooperative (also known as Co-ops) is an entity that groups multiple companies that can purchase Wine and Liquor, in the state of New Jersey. All companies affiliated to these co-ops are entitled to get the best-case price for any given item, considering the case count for such item across all other sales orders to the same co-op members. The 365WineTrade functionality to have these order quantities consolidated for pricing purposes based on date settings that can be selected under the Wine Setup page or Customer Price Group page. Available date options can be found under the “Price Starting Date” of the Wine Setup page or Customer Price Group with options of (Shipment date, Order date, Document date and Posting date). Depending on this date setting will dictate how or when Sales Order quantities will be consolidated for best case price under the co-op pricing functionality. For this, 365WineTrade has the structure to support the setup of Co-ops, and Co-op Customers, and default co-ops per customer as well.

Once a Sales Order is started, 365WineTrade fills out field **Co-op Code** with the code associated with the co-op for that sales order.

Each individual Price List entry can be enabled or disabled for Co-Op Pricing. When creating a new Price List entry, if the Customer Price Group allows for Co-op Pricing, then **Co-Op Pricing Enabled** will default to true. Users will have to uncheck prices they don’t want as part of the **Co-op pricing**. Users should not be able to set **Co-Op Pricing Enabled** if the Customer Price Group doesn’t allow for that either.

The unit price for a given line shall be the best-case price for that item, considering the total case count of that item across all sales orders for the **same co-op** and **same “Price Starting Date” setting**. **Please note**: The total case count shall be calculated based only on sales lines entered in Case UoM (defined on the 365WineTrade setup). If lines are entered in Bottle UoM, those will not count towards the case count. If Customer decides to count loose bottles against the total case count, they will need to enter decimal Case quantities on a Case UoM line.

Co-Op Pricing Example

Consider the following items, and their price lists:

Items:

|     |
| --- |
| Sku # |
| WINE1 |
| WINE2 |
| WINE3 |

Price Lists (Sales Price entry):

|     |     |     |     |
| --- | --- | --- | --- |
| Item | Min Qty | Price | **Co-Op Pricing Enabled\*** |
| WINE1 | 1   | $ 35 | Yes |
| WINE1 | 5   | $ 33 | Yes |
| WINE1 | 10  | $ 31 | No  |
| WINE2 | 1   | $ 55 | Yes |
| WINE2 | 5   | $ 53 | Yes |
| WINE2 | 10  | $ 51 | No  |
| WINE3 | 1   | $ 66 | Yes |
| WINE3 | 5   | $ 64 | Yes |
| WINE3 | 10  | $ 62 | No  |

Consider the following Sales Order Lines:

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SO #** | **Co Op #** | **Ship Date** | **Line #** | **Item No.** | **Qty (cases)** | **Original Price** | **Co-Op Price** |
| **001** | WCOOP | 1/15/21 | 1   | WINE1 | 1   | $ 35 | $ 33 |
| **001** | WCOOP | 1/15/21 | 2   | WINE2 | 6   | $ 53 | Same |
| **001** | WCOOP | 1/15/21 | 3   | WINE3 | 3   | $ 66 | $ 64 |
| **002** | WCOOP | 1/15/21 | 1   | WINE1 | 4   | $ 35 | $ 33 |
| **002** | WCOOP | 1/15/21 | 2   | WINE3 | 11  | $ 62 | Same |
| **003** |     | 1/15/21 | 1   | WINE1 | 5   | $ 33 | n/a |
| **004** | WCOOP | 1/16/21 | 1   | WINE1 | 4   | $ 35 | Same |

·       SO 001, Line 1 got a Co-op price due to SO 002, Line 1 reaching a better case count for WINE1 (total 5 cases for WCOOP, Ship Date 1/15)

·       SO 001, Line 2 got the same price because there are no other lines to co-op with

·       SO 001, Line 3 got a Co-op price due to SO 002, Line 2 reaching a better case count for WINE3 (total 14 cases for WCOOP, Ship Date 1/15). However, this line did not get the 10-case price, because the 10-case price is not enabled for NJ Co-Op pricing. Instead, BC grabbed the 5-case price ($ 64)

·       SO 002, Line 2 would get a Co-op price of $64 (5-case price), however, the original best price for a 10-case count is lower than the Co-op price, therefore, $62 is the correct price

·       SO 003 cannot get a Co-op Pricing because the order is not assigned to any Co-Op

·       SO 004, Line 1 got the same price because there are no other lines to co-op with for same Co-op, Same Shipment Date

·       \*For Co-op price finding, WineTrade365 should not look into prices where **Co-Op Pricing Enabled** is FALSE.

·       The price re-calculation under the Co-op pricing model will happen when the sales order is Released.

·       **Note!**: Since co-op pricing affects multiple orders, it will be imperative that all co-op orders for one **same co-op**, for the **same Pricing Start Date setting**, are released sequentially in a certain timeframe. Otherwise, if new co-op orders are added, that may impact the price on other orders, all related orders will need to be re-opened and re-released again for proper recalculation and order approvals in place. Based on the Released Sales Order Repricing Method setup on the Customer Price Groups page you can set it up to reprice orders without requiring the Order Approval process to be approved on a reprice. To setup the process, set the repricing method **to “Reprice and Retain Approvals”**.

·       **Note!**: In the event where the original price is cheaper than the Co-Op Price, WineTrade365 will choose the lowest price, **unless** there’s a Specific [Customer Pricing](#_Customer_Specific_Pricing) setup. This is the example for SO 002, Line 2. Additionally, in the event where both Co-Op Pricing and Family Plan pricing is applicable to an order, WineTrade365 will always need to choose the lowest price between both, unless there’s a Specific [Customer Pricing](#_Customer_Specific_Pricing) setup.

### 3.2.2.     Key Co-op Setup Areas

·       The first thing in the Co-op setup is to create a Co-op under the Co-ops page area.

·       On the Customer Price Group page Co-op Pricing must be Enabled.

·       The last part of Co-op pricing setup is on the Customer card. The customer must belong to the Customer Price Group that has the Co-op Enabled but must also be a member of the Co-op. Two setup areas on the customer card to consider.

Search for Co-ops:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image022.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image023.png)

Search for Customer Price Group

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image024.png)

Search for Customer

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image025.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image026.png)

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image027.png)

![](365WineTrade%20Users%20Guide%20-%20US%20Pricing.fld/image028.png)

Price starting date is set to establish which date setting will be used to consolidate sales order quantities for best case price can be seen above.

**Note!** If you want to have the Co-op code automatically apply to sales orders you must set the Co-op code with default Enabled. This will automatically add the co-op code to the sales order under the 365WineTrade fast tab. If a customer belongs to more than one co-op as seen in the screen shot above this can be manually set on the sales order by selecting a different co-op code under 365WineTrade fast tab.

3.3.        Family Plans Pricing

### 3.3.1.     Family Plans

Family Plans will find the best-case price for each item of a given sales order, based on the total case count for the order.

Within one same sales order, WineTrade365 will need to calculate the total Case Count for all items that are entered in the Case UoM defined on the 365WineTrade setup. Then, for each line, WineTrade365 will need to find the best price, using the total case count as a parameter of comparison with the Min. Quantity field.

Each individual Price List entry can be enabled or disabled for Family Plans. When creating a new Price List entry, if the Customer Price Group allows for Family Plans, then **Family Plan Enabled** will default to true. Users will have to uncheck prices they don’t want as part of the Family Plan pricing. Users should not be able to set **Family Plan Enabled** if the Customer Price Group doesn’t allow for it either.

Family Plans Example

Consider the following items, and their price lists:

Items:

|     |
| --- |
| Sku # |
| WINE1 |
| WINE2 |
| WINE3 |

Price Lists (Sales Price entry):

|     |     |     |     |
| --- | --- | --- | --- |
| Item | Min Qty | Price | **Family Plans Enabled\*** |
| WINE1 | 1   | $ 35 | Yes |
| WINE1 | 5   | $ 33 | Yes |
| WINE1 | 10  | $ 31 | No  |
| WINE2 | 1   | $ 55 | Yes |
| WINE2 | 5   | $ 53 | Yes |
| WINE2 | 10  | $ 51 | Yes |
| WINE3 | 1   | $ 66 | Yes |
| WINE3 | 5   | $ 64 | Yes |
| WINE3 | 10  | $ 62 | No  |

Consider the following Sales Order:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Line #** | **Item No.** | **Qty (cases)** | **Original Price** | **Family Plan Price** |
| **1** | WINE2 | 6   | $ 53 | $ 51 |
| **2** | WINE1 | 4   | $ 35 | $ 33 |
| **3** | WINE3 | 13  | $ 62 | Same |
|     | Total Case Count | 23  |     |     |

·       The total case count for this order is 23 cases. Therefore, for each line, we should find the best price, considering that the quantity is 23 cases for all lines.

·       For Family Plan price finding, WineTrade365 should not look into prices where **Family Plans Enabled** is FALSE.

·       Line 1, the original price is $53, for 6 cases, but then WineTrade365 is able to get the 10-case price break because the total count for the order is 23.

·       Line 2, the original price is $35, for 4 cases. WineTrade365 would be able to get the 10-case price break if it was enabled for Family Plans, but because it’s not, BC will then find the 5-case price break.

·       Line 3, WineTrade365 is not able to get the 10-case price break because it’s not enabled for Family Plans, however this price is the original price, and it’s lower than if BC were to take the 5-case price break. Therefore, BC keeps using the original price of $62.

·       Price re-calculation happens upon releasing the Sales Order.

·       **Note!** In the event where the original price is cheaper than the Family Plan Price, WineTrade365 needs to choose the lowest price, unless there’s a Specific [Customer Pricing](#_Customer_Specific_Pricing) setup. This is the example for Line 3. Additionally, in the event where both Co-Op Pricing and Family Plan pricing is applicable to an order, WineTrade365 will always need to choose the lowest price between both, unless there’s a Specific [Customer Pricing](#_Customer_Specific_Pricing) setup.

### 3.3.2.     Calculation of Price upon Releasing

As mentioned on each section, WineTrade365 calculations will occur at time of releasing the sales order.