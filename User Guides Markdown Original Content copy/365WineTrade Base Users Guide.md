![](365WineTrade_Users%20Guide%20-%20Base.fld/image001.png)

![](365WineTrade_Users%20Guide%20-%20Base.fld/image002.png)

_Microsoft Dynamics__®_ _365 Business Central_ 

![Shape](365WineTrade_Users%20Guide%20-%20Base.fld/image003.png)365WineTrade Base  
Users Guide 

Last Update: November 4, 2024

  

**Change Log:** 

|     |     |     |
| --- | --- | --- |
| **Date** | **Name** | **Description** |
| 11/01/2024 | Maurice Tisseur | Section 5.15 365WineTrade Inventory Availability Added |
| 11/01/2024 | Anjali Saraf | Section 4.1 Updated screenshots for Wine Setup |
| 11/01/2024 | Maurice Tisseur | Section 5.16 added for Item ledger entry rounding feature |
| 11/04/2024 | Maurice Tisseur | Section 7.1 Vendor Card Chargeback Fast Tab |
|     |     |     |

  

Table of Contents

[1. Introduction. 6](#_Toc181622262)

[2. Dependencies and Assumptions 6](#_Toc181622263)

[3. Glossary / Terminology. 7](#_Toc181622264)

[4. Setups 8](#_Toc181622265)

[4.1. Wine Setup. 8](#_Toc181622266)

[4.1.1. Dimension Synchronize. 11](#_Toc181622267)

[4.2. Units of Measure. 12](#_Toc181622268)

[4.3. States. 12](#_Toc181622269)

[4.4. Sales Regions 13](#_Toc181622270)

[4.5. Order Types. 14](#_Toc181622271)

[4.6. Sales Order Charges. 16](#_Toc181622272)

[4.6.1. Minimum Order Details. 17](#_Toc181622273)

[4.6.2. Charge Amounts. 17](#_Toc181622274)

[4.6.3. Linking Sales Charges to Order Types 19](#_Toc181622275)

[4.7. Pickup Addresses. 20](#_Toc181622276)

[4.8. Customs Brokers 23](#_Toc181622277)

[4.9. Freight Forwarders 23](#_Toc181622278)

[4.10. Agents 23](#_Toc181622279)

[4.11. Chain Names. 23](#_Toc181622280)

[4.12. Co-ops 24](#_Toc181622281)

[5. Creating Items using 365WineTrade Features. 25](#_Toc181622282)

[5.1. Item Units of Measure. 25](#_Toc181622283)

[5.1.1. Unit Sizes 25](#_Toc181622284)

[5.2. Brands and Producers 26](#_Toc181622285)

[5.2.1. Producers 26](#_Toc181622286)

[5.2.2. Brands 28](#_Toc181622287)

[5.2.3. Producer and Brand Dimensions 30](#_Toc181622288)

[5.3. Vintages. 31](#_Toc181622289)

[5.4. Varietals 31](#_Toc181622290)

[5.5. Labels 31](#_Toc181622291)

[5.6. Alcohol Types 32](#_Toc181622292)

[5.7. Wine Colors 32](#_Toc181622293)

[5.8. Origin Regions 33](#_Toc181622294)

[5.9. Sub-Regions 33](#_Toc181622295)

[5.10. Appellations 33](#_Toc181622296)

[5.11. 365WineTrade FastTab. 34](#_Toc181622297)

[5.12. Item Reviews 35](#_Toc181622298)

[5.12.1. Setting up Item Reviews (Publications) 35](#_Toc181622299)

[5.12.2. Setting up Item Review Scores 35](#_Toc181622300)

[5.12.3. Adding an Item Review to an Item Card. 36](#_Toc181622301)

[5.13. Copying Items. 37](#_Toc181622302)

[5.14. Additional Actions and Navigation Options. 38](#_Toc181622303)

[5.15. 365WineTrade Item Availability Enhancement 38](#_Toc181622304)

[5.16. Item Ledger Entry Rounding Adjustment Enhancement 39](#_Toc181622305)

[6. Creating Customers using 365WineTrade Features 42](#_Toc181622306)

[6.1. Corporate Namebill 42](#_Toc181622307)

[6.2. 365WineTrade FastTab. 42](#_Toc181622308)

[6.3. Credit FastTab. 43](#_Toc181622309)

[6.4. Additional Actions and Navigation Options. 43](#_Toc181622310)

[7. Processing Purchase Orders 45](#_Toc181622311)

[7.1. Vendor Card. 45](#_Toc181622312)

[7.2. Blanket Purchase Order Synchronization. 46](#_Toc181622313)

[7.3. Purchase Orders 47](#_Toc181622314)

[7.4. Purchase Order Consolidations 47](#_Toc181622315)

[7.4.1. Receiving and Invoicing a Purchase Consolidation. 50](#_Toc181622316)

[8. Processing Sales Orders 52](#_Toc181622317)

[8.1. Sales Line Quantity. 53](#_Toc181622318)

[8.2. Releasing Sales Orders 53](#_Toc181622319)

[8.3. Shipping and Invoicing Sales Orders. 54](#_Toc181622320)

[9. Sales Order and Credit Reviews. 55](#_Toc181622321)

[9.1. Order Review Types. 55](#_Toc181622322)

[9.2. Setting up Sales Order Reviews. 56](#_Toc181622323)

[9.3. Credit Classes 58](#_Toc181622324)

[9.4. Approval Users 59](#_Toc181622325)

[9.5. Sales Order Review Approvals – Order by Order 60](#_Toc181622326)

[9.6. Sales Order Review Approvals – Multiple Documents 62](#_Toc181622327)

[9.6.1. Sales Order Review Filters Area. 62](#_Toc181622328)

[9.6.2. Sales Order Review Parameters 63](#_Toc181622329)

[9.6.3. Sales Order List – Shortcut Actions, Lines and FactBoxes. 64](#_Toc181622330)

[9.7. Credit Review Dashboard. 65](#_Toc181622331)

[9.7.1. Credit Reviews List – Shortcut Actions, Sales Orders and FactBoxes 66](#_Toc181622332)

[10. Document Worksheets 68](#_Toc181622333)

[10.1. Document Groups 68](#_Toc181622334)

[10.2. Email Reports 69](#_Toc181622335)

[10.3. Email Addresses. 69](#_Toc181622336)

[10.4. Email Body. 70](#_Toc181622337)

[10.5. Document Worksheet Template. 70](#_Toc181622338)

[10.6. Document Worksheet Template Batches 72](#_Toc181622339)

[10.7. Using the Document Worksheet 73](#_Toc181622340)

[10.8. Document Worksheet Entries 74](#_Toc181622341)

[11. Integrations to External Systems. 75](#_Toc181622342)

[11.1. Sites 75](#_Toc181622343)

[11.2. Site Communication. 76](#_Toc181622344)

[11.2.1. Site Communication Parameters. 77](#_Toc181622345)

[11.3. Site Logs 77](#_Toc181622346)

[11.4. Site Order Queue. 78](#_Toc181622347)

[12. sam.. 80](#_Toc181622348)

[12.1. Bill & Hold Agreements 80](#_Toc181622349)

[12.1.1. Bill & Hold Process. 80](#_Toc181622350)

[12.1.2. Bill & Hold Setup. 81](#_Toc181622351)

[12.1.3. Bill & Hold Order Processing. 82](#_Toc181622352)

[12.2. Salesperson Location. 83](#_Toc181622353)

[12.3. Sample Management Setup. 84](#_Toc181622354)

[12.3.1. Setting Up Sample Budget 85](#_Toc181622355)

[12.3.2. Sample Sales Orders Budget Check. 87](#_Toc181622356)

[12.4. Data Processing. 87](#_Toc181622357)

[12.4.1. Import Customer Delivery Instructions 88](#_Toc181622358)

[13. 365WineTrade Internal Permission System.. 89](#_Toc181622359)

  

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

As a wine and spirits manufacturer/distributor, you have enough challenges to deal with, like complex pricing and tax calculations, unique reporting requirements for every state, chargebacks, billbacks and suppliers around the globe. The **365WineTrade** add-on will help solve these challenges.

This add-on provides extended functionality to the base Dynamics 365 Business Central system in the areas of Items, Customers and Sales Orders. Additional screens and functions have been added to support some of the business requirements of a wine and spirits distributor.

# 2.   Dependencies and Assumptions

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating/viewing/editing/deleting records, filtering, and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

  

depl

# 3.   Glossary / Terminology

The **365WineTrade** module uses specific terms that are specific to the wine and spirits industry. This glossary describes the fields and functions used in the system.

|     |     |
| --- | --- |
| **Term** | **Description** |
| **COLA** | Certificate of Label Approval. All alcoholic beverages sold in the United States are required to have one of these. The winery submits a set of wine labels to the TTB (Alcohol & Tobacco Tax Trade Bureau) for approval |
| **SLA** | State Liquor Authority |
| **Franchise Law** | When a Brand or Producer can only be sold to specific customers, in specific States |
| **Chain** | Business Chain that owns multiple stores/retailers |
| **Co-ops** | Cooperative Purchasing Groups usually found in the state of New Jersey |

  

# 4.   Setups

## 4.1.        Wine Setup

The general Wine Setup can be found under menu **365WineTrade**, **Setup**, **Wine Setup**:

![A close-up of a computer screen
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image004.png)

Figure 4‑1: Wine Setup: FastTab General

![A close-up of a computer screen
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image005.png)

Figure 4‑2: Wine Setup: FastTab Compliance

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image006.png)

Figure 4‑3: Wine Setup: FastTab Sales

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image007.png)

Figure 4‑4: Wine Setup: FastTab Item List

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image008.png)

Figure 4‑5: Wine Setup: FastTab Item Availability

![A close-up of a link
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image009.png)

Figure 4‑6: Wine Setup: FastTab Blanket Purchase Order Consolidation

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image010.png)

Figure 4‑7: Wine Setup: FastTab Purchase Consolidations, Brands and Dimension Synchronize

Table 4‑1: Wine Setup Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Pickup Address No.** | Number series to be used when creating [Pickup Addresses](#_Pickup_Addresses_1) |
| **Use 365WineTrade Item Copy** | Enable an enhanced Copy Item functionality that allows items to be copied across different companies. Refer to section [Copying Items](#_Copying_Items) for more details. |
| **Case-Amount Rounding Precision** | Specifies the size of the interval to be used when rounding amounts in $. This covers amounts created with all types of transactions and is useful to avoid inconsistencies when viewing or summing different amounts. Amounts will be rounded to the nearest digit. |
| **Case-Amount Decimal Places** | Specifies the number of decimal places that are shown for amounts in $. This covers amounts created with all types of transactions and is useful to avoid inconsistencies when viewing or summing different amounts. |
| **Bypass License Type Check** | Toggle On/True to bypass license validation |
| **Bypass Item Registration Check** | Toggle On/True to bypass item registration validation |
| **Document Group Code** | Set Document Group code for COLA documents. Refer to US Compliance User Guide |
| **Website Address** | [https://www.ttbonline.gov/viewcoladetails.do?action=publicFormDisplay&ttbid=%1](https://www.ttbonline.gov/viewcoladetails.do?action=publicFormDisplay&ttbid=%251) “Online License validation service” |
| **Excise Tax Active** | Toggle On/True if Excise Tax is planned to be used |
| **Sales Price Priority Code** | A way to prioritize customer pricing |
| **Price Starting Date** | The effective date at which pricing is calculated typically set to Shipment Date. |
| **Automatic Sales Document Pricing** | System setting for when order pricing is calculated |
| **Pricing Unit Type** | Set the unit type to be used to calculate Mix & Match, Co-op and Family Plan Pricing. |
| **Sales Document Date Update** | If set to **Update Unit Price** then the sales prices will be updated whenever there is a change to the Document Date on the Sales Order |
| **Sales History Date Calculation** | Determines the date range of the sales history that will appear in the Sales History Factbox on the customer card |
| **Synchronize Purchase Orders to Blanket Purchase Orders** | Enables [Blanket Purchase Order Synchronization](#_Blanket_Purchase_Order) |
| **Allow Multiple Blanket Purchase Orders per Vendor per Item** | Please refer to section [Blanket Purchase Order Synchronization](#_Blanket_Purchase_Order) |
| **Link Purchase Orders to Blanket Purchase Orders** | Please refer to section [Blanket Purchase Order Synchronization](#_Blanket_Purchase_Order) |
| **Purchase Consolidation No.** | No. Series to be used with the [Purchase Order Consolidations](#_Purchase_Order_Consolidations_2) feature |
| **Synchronize Brand Dimensions to Items** | Please refer to section [Brand Dimensions](#_Brand_Dimensions,_Setup) |
| **Use Producers** | Enable the use of the [Producers](#_Producers) entity, which is a level above [Brands](#_Brands_1) |
| **Dimension Synchronize** | Refer to section [Dimension Synchronize](#_Dimension_Synchronize) below |

  

### 4.1.1.     Dimension Synchronize

In some companies, the Finance department can decide to breakdown financial reports by some special entities, such as Brand, Vintage, Label, Varietal and/or Producer. Most often, these entities are translated to Dimension Values. In order to avoid the double work of having the user create these values as dimension values and as their individual entity value, users can enable the Dimension Synchronize feature. This way, if a dimension is synchronized with an entity, each time a new value is created/modified/deleted in either side (Dimension Value or Entity Value), BC will automatically create the value on the other side.

E.g.: If the Dimension Synchronize is enabled for Source **Vintage**, and we map this to dimension **VINTAGE**, then, every time the user creates a new Vintage Dimension Value, a new record on the Vintage table will also be created, and vice-versa.

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image011.png)

Figure 4‑4: Dimension Synchronize for source Vintage

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image012.png)

Figure 4‑5: New Dimension Value: 1999

![Graphical user interface, text, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image013.png)

Figure 4‑6: Vintage record 1999 was automatically created

## 4.2.        Units of Measure

On the Units of Measure setup, **365WineTrade** creates a new Boolean field called **Fractional Quantity Not Allowed**. This field will prevent decimals from being posted in Item Ledger entries, for units of measure which ultimately can never be broken in less than 1 full unit. This is especially applicable to Bottles. However, you could apply this to Cases as well, in the event you never want to have decimal Cases in the system.

Lastly, if your BOTTLE Unit of Measure is marked with this field, and your items are in CASE Base Unit of Measure, BC will also make sure to round the Case quantity to best match a full bottle quantity. In this scenario, however, your Item Ledger Entries will not be free from decimal places, since Cases can be broken into smaller units.

**Please note**: This setup is global. It cannot be set up per item.

Please refer to section [Sales Line Quantity](#_Sales_Line_Quantity) to understand how this setup affects quantity entry in BC.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image014.png)

Figure 4‑7: Fractional Quantity Not Allowed on Units of Measure Setup

## 4.3.        States

In the United States, each State is responsible for regulating the alcohol industry. Some states have more control, and some states have very loose regulations. In the **365WineTrade** module, you need to set up all the states you work with, so that you can set up some rules if or how items can be sold to specific states and/or specific customers.

To setup States in the system, you need to go to the **365WineTrade** menu, **Setup**, **States**:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image015.png)

Figure 4‑8: List of States

Table 4‑2: State Setup Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **State Code** | State 2-character code |
| **Name** | State name |
| **Allow Co-op** | Global setting when checked allows co-op pricing to be used in the state for Customers |
| **Allocate** | Global setting when checked allows allocation functionality to be used for that state |
| **Allocation Code** | Prefix document code that will be added to allocation entries when posting allocation journals |
| **Customer Count** | Calculated field with number of customers assigned to this state. Drill-down on the number to see a list of customers. |

## 4.4.        Sales Regions

A ‘Sales Region’ is required on every sales order. This is to determine what products (items) are registered or allowed to be sold in that region.

Traditionally, a Sales Region is a state. However, if required (for regulatory reasons or by business decisions), a Sales Region can be broken down further. For example, New York state could have 2 Sales Regions: NYC (comprised of the 5 boroughs that are part of New York City) and NY-UP (Upstate New York). With this setup, some items can be configured in a way that they can be sold only to Upstate customers and not for NYC customers. Going in the other direction, a Sales Region could also represent a conglomerate of multiple states.

All customers are assigned a Sales Region, and this will be populated on a Sales Order automatically.

To set up Sales Regions, you need to go to the **365WineTrade** menu, **Setup**, **Sales Regions**:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image016.png)

Figure 4‑2: List of Sales Regions

Table 4‑3: Sales Region Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Code** | Sales Region Code, ideally should include the state 2-character code, if related to a specific state |
| **Description** | Sales Region name |
| **State** | The State Code that this Sales Region is related to |
| **Bypass Item Registration Check** | This setting when check allows to bypass any item registration check for a specific state. Typically set “checked” if no integration is planned or no setup in place yet. |
| **Defaul**t **Registration** | When set to True the system will automatically assign a default registration number for this Sales Region when a new Item is created |
| **Default Registration Code** | Code to be used for automatic item registration when Default Registration is True |
| **Sales Registration Sort Order** | Set Sort Order for Sorting Sales Regions on Brand Item Registrations |
| **Allocation** | If checked will allow a sales region to use allocation functionality |
| **Allocation Code** | Document Prefix code used in allocation entries posted from allocation journals for the sales region |
| **Customer Count** | Calculated field with number of customers assigned to this state. Drill-down on the number to see a list of customers. |

## 4.5.        Order Types

Standard BC does not offer any type of Sales Order templates or Sales Order types, but this is a recurring need in the Wine Industry. **365WineTrade** introduces the concept of Sales Order Types, to make Sales Order entry easier.

Sales Order Types help users with presetting a few fields on the Sales Order by selecting a descriptive code from a list. This way, users don’t have to remember what information they should supply to some fields on the Sales Order, making the process a bit more standardized.

Sales Order Types can be set up as a default setting on Customer Cards (under FastTab **365WineTrade**), and additionally, it can be changed on the Sales Order Header.

To manage Sales Order Types, you go to the **365WineTrade** menu, **Setup**, **Order Types**. You will then be brought into the Sales Order Types list:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image017.png)

Figure 4‑3: Sales Order Types List

Table 4‑4: Sales Order Types' Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Code** | Order Type Code |
| **Description** | Order Type Description |
| **Bill and Hold Type** | Please refer to section [Bill & Hold Agreements](#_Automated_Processing_of_1) |
| **Blocked** | If flagged, this Order Type cannot be used on a Sales Order |
| **Order Charges** | Displays the number of [Sales Order Charges](#_Pickup_Addresses) linked to this Order Type |
| **Location Code** | Location Code that will be set on the Sales Order header for this Order Type |
| **Depletion Allowance** | If flagged, this Order Type will trigger Depletion Allowance entries if applicable |
| **Bill Back %** | % in whole number to be used for samples. Defines what percentage will be billed back to the vendor in regards to samples |
| **Sample** | When flagged, orders may be stopped on the [Sales Order Review](#_Sales_Order_Reviews) process under Type “Order Type-Sample” |
| **Shipment Date Formula** | Overrides standard Shipment Date formulas, if needed. Usually used for Drop Shipment Order Types |
| **Purchasing Code** | Default Purchasing Code used when entering items on the Sales Order. This will override the Item’s Standard Purchasing Code |
| **Order Review Category Code** | Determines what group of [Sales Order Review](#_Setting_up_Sales) Items are being applied to this Order Type. |

## 4.6.        Sales Order Charges

**365WineTrade** supports two types of Sales Order Charges:

·       **Minimum Charges**: If the order total is below a minimum number of Bottles or Cases, or the order total dollar amount is under a minimum dollar amount, BC can add a charge to the Sales Order Lines

·       **Split Case Fees** (also known as **Bottle Mix Fees**): If any of the sales lines has a Quantity in Bottles that does not match a full Case Pack, BC can add a charge to the Sales Order Lines. This charge can be per bottle, or it can be one fixed amount per order. Please see more details further below on this section.

To set up Sales Order Charges, go to the **365WineTrade** menu, **Setup**, **Order Charge Setup**. You will be presented with the following page:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image018.png)

Figure 4‑4: Order Charges List

When the selected line is of type **Minimum**, you can open one of the following actions under the **Related Information** action menu:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image019.png)

Figure 4‑5: Types of Charge Setups

When the selected line is of type **Split Case**, only the option for **Charge Amounts** is available.

### 4.6.1.     Minimum Order Details

The Minimum Order Details can be set as follows:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image020.png)

Figure 4‑6: Minimum Order Details

Table 4‑5: List of Fields for Minimum Order Details

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Alcohol Type** | Determines the type of alcohol that the charge applies to. This must always be informed |
| **Minimum Type** | Determines which Unit of Measure to use for field Minimum Order Quantity |
| **Combine Order Quantity** | Determines if all Alcohol Types should be combined together when determining the minimum quantity and minimum amount |
| **Minimum Order Quantity** | If the total quantity on the Sales Order is below this number, a Minimum Order Charge will be added to the Sales Order. |
| **Minimum Order Amount** | If the total Sales Order Amount is below this amount, a Minimum Order Charge will be added to the Sales Order. Not to be confused with the actual Charge amount, which is set up on the next section. |

### 4.6.2.     Charge Amounts

The Charge Amounts determine the actual amounts that will be added to the Sales Orders as the result of a Minimum Order Amount that was not met, or as the result of a Split Case Charge.

The Charge Amounts are set as follows:

![A screenshot of a computer screen
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image021.png)

Figure 4‑7: Order Charge Amounts

Table 4‑6: List of fields for Charge Amounts

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Customer Price Group** | Indicates a Customer Price Group to which this split case will apply. This field must be informed |
| **Partial Shipment Limit** | Enter how many Order Charges should be applied to a Sales Order for Partial Shipments. In the case of a blank setting each additional shipment will also receive a charge amount added to the order. A Setting of 1 will limit order to 1 order charge with all subsequent orders having no additional order charges added. Leave blank for no limit |
| **Type** | Determines the type of Sales Line that will be added to the Sales Order. Options are: G/L Account, Item or Resource. |
| **No.** | This will be the G/L Account No., Item No. or Resource No. to be added to the Sales Order charge line |
| **Distributed By** | This provides for Item Charge Assignments functionality on how to be distributed on the Item layers ie: “by Amount, By Volume, By Quantity...etc.” |
| **Calculation Type** | This setting is only valid for Split Case charges. |
| **Calculation Limit** | Entering a number here will limit the Calculation Quantity to the entered number |
| **Item Category Code** | Used to apply charges to a specific Item Category when present on the item master record. |
| **Unit Size** | Unit size can be used in tandem with item category to target a charge for a specific bottle size within an item category. |
| **Amount** | Amount of the Charge. See details below on how it is calculated |

**Please note**: **Customer Price Group** must be **defined** If you have different Split Case charge for different Price Groups, you will need one record per Customer Price Group. If your Split case charge is the same for all customer price groups then having Customer Price Group set to blank is an acceptable setting that will apply to all.

When a Charge amount is to be added to the Sales Order due to an unmet Minimum Order amount, or due to a Split Case charge, BC will enter a new Sales Order Line as follows:

·       For Minimum Order Charges, Quantity will be 1 and the Unit Price will equal the charge Amount field. Therefore, the total amount for the charge line will equal the amount defined for the Minimum Charge amount.

·       For Split Case Charges:

o   Quantity will be 1 when Calculation Type is Per Order, or

o   Quantity will be the number of bottles outside of a full case when Calculation Type is Per Line. For example, if the Case Pack is 12, and the Sales Order Line quantity is 19, then Quantity will be 7.

o   Unit Price will equal the charge Amount.

o   Therefore, the total amount for the charge line may either equal the charge amount, or the charge amount multiplied by the number of bottles outside a case pack

### 4.6.3.     Linking Sales Charges to Order Types

Sales Charges must be linked to Order Types. If an Order Type doesn’t have any Sales Charges assigned to it, then **365WineTrade** will never add these automated Sales Charges.

To link the correct Sales Charges to their respective Order Types, you can go to the Order Types setup, and then click on **Related Information**, **Order Charges**:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image022.png)

Figure 4‑8: Order Type Sales Charges

Optionally, you can simply drill down from the Number of Order Charges on the Sales Order Type Line:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image023.png)

Figure 4‑9: Order Type Sales Charges Drilldown

You can add different charges on the same level, or you can indent some charges within others, which will make them conditional:

![A screenshot of a delivery list
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image024.png)

Figure 4‑10: Order Type Charges with indentation

If a charge is indented within another charge, this means that it will only be assessed if the main charge is added to the order. On the example above, the Split Case charge will only be assessed if the Order Minimum is added to the order.

Also, please note that you must activate these charges by setting field **Active**.

**Show Charge Confirmation:** If marked a pop-up message appears, letting the user know a charge is being added. The charges will populate regardless of whether this is enabled or not

**Allow Sales Order Line Override:** Users can turn off an order charge that has been applied to a sales line

## 4.7.        Pickup Addresses

Pickup Addresses are a global setup in the system that can be used in conjunction with Customers and Sales Orders, and Vendors and Purchase Orders. You can setup a Pickup Address to be used:

·       Globally

·       For Sales only

·       For specific customers only

·       For Purchasing only

·       For specific vendors only

To setup Pickup Addresses you can:

·       Go to **365WineTrade** menu, **Setup**, **Pickup Addresses**

·       Go to a **Customer Card**, **Navigate**, **Customer**, **Pickup Addresses**

·       Go to a **Vendor Card**, **Navigate**, **Vendor**, **Pickup Addresses**

Depending on where you access the Pickup Addresses from, BC will filter the list to match where you’re coming from. The Pickup Address List is shown below:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image025.png)

Figure 4‑11: List of Pickup Addresses

If you want to create a new Pickup Address, you can do so by clicking **New** on the Actions Ribbon. The Pickup Address Card is shown below:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image026.png)

Figure 4‑12: Pickup Address Card

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Code** | Unique code to be used with all Pickup Addresses. If you prefer to use an auto-generate number, make sure to set it up on the [Wine Setup](#_Wine_Setup) |
| **Type** | Type blank is global and can be used in both the Sales and Purchasing areas.<br><br>Type Sales determines the Pickup Address that can be used for any Sales Order<br><br>Type Customer determines the Pickup Address that is specific to the Customer defined on field No.<br><br>Type Purchase determines the Pickup Address that can be used for any Purchase Order<br><br>Type Vendor determines the Pickup Address that is specific to the vendor defined on field No. |
| **No.** | Can only be set if Type is Customer or Vendor |
| **Name** | Descriptive name that shows on the list |
| **Default** | Reserved for future use |

Once you setup Pickup Addresses in the system, you can use them in Sales Orders and Purchase Orders, as shown below:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image027.png)

Figure 4‑13: Sales Order, Shipping and Billing FastTab

![](365WineTrade_Users%20Guide%20-%20Base.fld/image028.png)

Figure 4‑14: Purchase Order, Shipping and Payment FastTab

As you can see, on the Sales side, a Pickup Address will be used as the final destination of the goods. On the Purchasing side, a Pickup Address can be used as an intermediary address to be used in the transaction.

When you look up the Pickup Address code fields, the list of options will also be contextual to where you are looking up from:

·       Looking up from a Sales Order will list Global Pickup Addresses, Sales Pickup Addresses and Pickup Addresses specific to the selected Customer on the Sales Order

·       Lookup up from a Purchase Order will list Global Pickup Addresses, Purchasing Pickup Addresses and Pickup Addresses specific to the selected vendor on the Purchase Order

**Please note**: the standard BC report for Purchase Orders has not been modified to include the Pickup Address field. This modification must be done project-by-project basis.

## 4.8.        Customs Brokers

Customs Brokers can be used in the [Purchase Order Consolidations](#_Purchase_Order_Consolidations_2) process.

To set up Customs Brokers, go to the **365WineTrade** menu, **Setup**, **Customs Brokers**. You will be presented with the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image029.png)

Figure 4‑15: List of Customs Brokers

## 4.9.        Freight Forwarders

Freight Forwarders can be used in Purchasing and Sales Return Orders, as well as in the [Purchase Order Consolidations](#_Purchase_Order_Consolidations_2) process.

To set up Freight Forwarders, go to the **365WineTrade** menu, **Setup**, **Freight Forwarders**. You will be presented with the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image030.png)

Figure 4‑16: List of Freight Forwarders

## 4.10.     Agents

Reserved for future use.

## 4.11.     Chain Names

Chain Names is a **365WineTrade** extension to standard BC field **Chain** on the Customer Card. Out-of-the-box in BC, this field is just a text field that is hidden by default. **365WineTrade** made this field visible on the customer card and created a lookup list for users to pick a Chain Name from a list of valid values, making this information less prone to typos.

To set up Chain Names, go to the **365WineTrade** menu, **Setup**, **Chain Names**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image031.png)

Figure 4‑17: Chain Names List

## 4.12.     Co-ops

This feature is to be used with **365WineTrade** **US Compliance** extension. Please refer to that User Guide for more details.

  

# 5.   Creating Items using 365WineTrade Features

**365WineTrade** customizations include additions to the standard BC Item Card. The next sections describe how to fill out **365WineTrade** fields on Item Cards.

## 5.1.        Item Units of Measure

Base Business Central recommends that the Base Unit of Measure should be the smallest unit that an Item is commercialized in. For wines and spirits, even though they are usually sold in cases, there are instances where they’re handled in bottles, such as returns of individual bottles. **365WineTrade** is flexible enough to handle items in either Case or Bottle as Base UoMs, so long as these UoMs are properly set up in the [Wine Setup](#_Wine_Setup).

**Please note**: All Items that are commercialized as alcoholic beverages, and that are price posted, must have conversions for both Bottles and Cases under the **Item Unit of Measure** table. This is automatically done using field **Case Pack** on the **365WineTrade** FastTab. For a migration project, however, make sure all Items are imported with both Units of Measure.

**Please note**: The Base Unit of Measure of an Item will be the unit in which quantities are displayed for the Item throughout the system, such as Quantity on Hand, Available Inventory, Quantity on Sales/Purchase Orders, Quantity Reserved, Inventory Valuation Reports, and any other standard BC report. Out-of-the-box, **365WineTrade** does **not** display special fields for quantities that are specific to Cases or Bottles.

Lastly, alcoholic beverage Items whose individual unit is not a Bottle (such as Cans and Kegs), can be kept in their respective Base UoM, so long as there’s a 1:1 conversion to the UoM setup as Bottle on the [Wine Setup](#_Wine_Setup). In these cases, as mentioned above, there also needs to be a conversion to the UoM setup as Case on the [Wine Setup](#_Wine_Setup).

### 5.1.1.     Unit Sizes

In **365WineTrade** you must set up Unit Sizes before you can use them on Item Cards. To do so, go to the **365WineTrade** Menu, **Item Setup**, **Unit Sizes**. You will be taken to the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image032.png)

Figure 5‑1: List of Unit Sizes

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Code** | Customers can define which codes suit the business best. Different implementations could adopt different codes, such as:<br><br>·       750ml, 1000ml, 1250ml, 3000ml, 12000ml<br><br>·       0.75L, 1L, 1.25L, 3L, 12L<br><br>·       00750ML, 01000ML, 01250ML, 03000ML, 12000ML<br><br>·       SMALL, MEDIUM, LARGE, X-LARGE |
| **Liters** | Number of liters in this bottle size |
| **Gallons** | Number of gallons in this bottle size. **Please note**: Updating the **Liters** field will automatically calculate the Gallons field, but not the other way around |
| **Item Count** | Provides a quick drill-down of all Items assigned to the current bottle size |

## 5.2.        Brands and Producers

**365WineTrade** has a special entity to control Brands and Producers. In some settings, you may need to work with both, in some settings, you may use just Brands.

### 5.2.1.     Producers

In order to use Producers, you must enable the field **Use Producers** on the [Wine Setup](#_Wine_Setup).

You can find the Producers list under the **365WineTrade** menu, **Item Setup**, **Producers**:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image033.png)

Figure 5‑2: Producers List

To create a new Producer, you can click **New** on the Actions ribbon; or you can click the **No.** field on any record to view it:

![Graphical user interface, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image034.png)

Figure 5‑3: Producer Card

No fields are mandatory on this setup, except for the **Producer No.** itself. Having the full Producer Card filled out is a best practice, but not required. Please see below a list of special fields and parts and their descriptions.

Table 5‑1: Brand Card special Fields and Parts

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Vendor No.** | Determines if this Producer is also setup as a Vendor |
| **FDA Registration No.** | The FDA Registration No. associated with this Producer |
| **FDA Registration Expiration Date** | The Expiration Date for the FDA Registration No. associated with this Producer |
| **Producer Type Code** | Used to categorize producers. There is no intelligence behind this field |
| **Small Winery** | Used for Beverage Tax purposes, further described in the User Guide for **365****WineTrade** **US Compliance** |
| **Brands FastTab** | Enter the list of Brands carried by this producer. Creating Brands on this list will create actual [Brands](#_Brands_1) in the system |
| **Communication FastTab** | You may link existing Contacts in the system, or you can simply enter new Contacts by entering their information. |
| **Documents FactBox** | You may see documents related to this producer. To manage these documents, use the Documents action below |

The following actions are available from both Producer Card and Producer List:

Table 5‑2: Actions for a Producer record

|     |     |
| --- | --- |
| **Action** | **Description** |
| **Documents** | Enables users to manage documents for this Producer |
| **Brands** | Show a list of [Brands](#_Brands_1) for this Producer |
| **Dimensions** | Sets up dimensions to be rolled down to items linked to this Producer. More details, refer to [Brand Dimensions](#_Brand_Dimensions) |

### 5.2.2.     Brands

You can find the Brands list under the **365WineTrade** menu, **Item Setup**, **Brands**:

![Graphical user interface, table
Description automatically generated with medium confidence](365WineTrade_Users%20Guide%20-%20Base.fld/image035.png)

Figure 5‑4: Brands List

**Please note**: If using Producers, the best way to manage Brands is directly from the Producer Card.

To create a new Brand, you can click **New** on the Actions ribbon; or you can click the No. field on any record to view it. Please note that the Brand Card will look different depending on whether your system is setup to use Producers or not:

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image036.png)

Figure 5‑5: Brand Card: FastTab General

![A white rectangle with a black rectangle
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image037.png)

Figure 5‑6: Brand Card: FastTab Chargebacks

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image038.png)

Figure 5‑7: Brand Card: FastTabs Communication

![A close-up of a computer screen
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image039.png)

Figure 5‑7: Brand Card: FastTabs Inventory Allocations

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image040.png)

Figure 5‑8: Brand Card if Producers are in use

No fields are mandatory on this setup, except for the Brand Code itself. Having the full Brand Card filled out is a best practice, but not required. If using Producers, most of the fields will be hidden, and you will only be able to set them up on the Producer Card. Please see below a list of special fields and parts and their descriptions.

Table 5‑3: Brand Card special Fields and Parts

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Brand Ownership** | Agent – you are an agent for this Brand<br><br>Owner – you are the owner of this Brand |
| **FDA Registration No.** | The FDA Registration No. associated with this Brand. Not visible if using Producers |
| **FDA Registration Expiration Date** | The Expiration Date for the FDA Registration No. associated with this Brand. Not visible if using Producers |
| **Brand Type Code** | Used to categorize brands. There is no intelligence behind this field |
| **Small Winery** | Used for Beverage Tax purposes, further described in the User Guide for **365****WineTrade** **US Compliance**. Not visible if using Producers |
| **Chargebacks FastTab** | Choose if Depletion Allowance amounts should be calculated on Sales Order Quantity or Extended Pricing Quantity |
| **Communication FastTab** | Enter contact information on these fields. Not visible if using Producers |
| **Inventory Allocations FastTab** | Toggle to allow if a Brand is eligible for allocations coupled with the allocation code to be used in allocation journals |
| **Contacts FastTab** | You may link existing Contacts in the system, or you can simply enter new Contacts by entering their information. Not visible if using producers |
| **Documents FactBox** | You may see documents related to this brand. To manage these documents, use the Documents action below |

The following actions are available from both Brand Card and Brand List:

Table 5‑4: Actions for a Brand record

|     |     |
| --- | --- |
| **Action** | **Description** |
| **Documents** | Enables users to manage documents for this Brand |
| **Dimensions** | Sets up dimensions to be rolled down to items linked to this Brand. More details, refer to [Brand Dimensions](#_Brand_Dimensions) |

### 5.2.3.     Producer and Brand Dimensions

Just like many standard BC entities, Producers and Brands allow for default dimensions. You can set up these default dimensions from the Producer List or Card, and Brand List or Card. You will be taken to the Default Dimensions page:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image041.png)

Figure 5‑6: Brand Dimensions

You can define a Dimension Code, a Dimension Value and the Value Posting, following BC best practices.

When you setup default dimensions for **Producers**, all new **Brands** for that producer will get the same set of dimensions. Changing dimensions on a **Producer** will **not** automatically update the dimensions on its brands.

When you setup default dimensions for **Brands**, all new **Items** for that brand will get the same set of dimensions. Changing dimensions on a **Brand** **may** automatically update the dimensions on all of its items, if **Synchronize Brand Dimension** is enabled on the [Wine Setup](#_Wine_Setup). **Please note**: Changing Brand dimensions will **not** automatically update any existing Sales/Purchase documents.

## 5.3.        Vintages

In **365WineTrade** you must also set up Vintages before you can use them on Item Cards. To do so, go to the **365WineTrade** Menu, **Item Setup**, **Vintage List**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image042.png)

Figure 5‑7: List of Vintages

For Non-Vintage products, we suggest the creation of a “NV” Vintage.

## 5.4.        Varietals

In **365WineTrade** you can setup Varietals to be assigned to Items. This setup is optional. You can also use this entity with the [Dimension Synchronize](#_Dimension_Synchronize) feature.

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Varietal List**. You will be taken to the following list:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image043.png)

Figure 5‑8: List of Varietals

## 5.5.        Labels

In **365WineTrade** you can setup Labels to be assigned to Items. Labels can be used to group wines for the same family of products, and you can group them either by juice (no matter the format it is presented), or you can also group them by Bottle Size and Case Pack. If you assign a Label to an Item, and the Bottle Size and Case Packs are assigned to the Label, they will roll down automatically to the item.

This setup is optional. You can also use this entity with the [Dimension Synchronize](#_Dimension_Synchronize) feature.

To set Labels, go to the **365WineTrade** Menu, **Item Setup**, **Label List**. You will be taken to the following list:

![A close-up of a contact us
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image044.png)

Figure 5‑9: List of Labels

## 5.6.        Alcohol Types

In **365WineTrade** you can setup different Alcohol types to be assigned to Items. This setup is used in conjunction with [Sales Order Charges](#_Pickup_Addresses).

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Alcohol Types**. You will be taken to the following list:

![Graphical user interface, table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image045.png)

Figure 5‑10: List of Alcohol Types

## 5.7.        Wine Colors

In **365WineTrade** you can setup different Wine Colors to be assigned to Items. This setup is optional, and it does not influence any other parts of the system.

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Wine Colors**. You will be taken to the following list:

![Graphical user interface, text, application, table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image046.png)

Figure 5‑11: List of Wine Colors

## 5.8.        Origin Regions

In **365WineTrade** you can setup different Origin Regions to be assigned to Items. This setup is optional, and it does not influence any other parts of the system.

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Origin Regions**. You will be taken to the following list:

![A picture containing table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image047.png)

Figure 5‑12: List of Origin Regions

## 5.9.        Sub-Regions

In **365WineTrade** you can also setup different Sub-Regions to be assigned to Items. This setup is optional, and it does not influence any other parts of the system.

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Sub-Regions**. You will be taken to the following list:

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image048.png)

Figure 5‑13: List of Sub-Regions

## 5.10.     Appellations

In **365WineTrade** you can also setup different Appellations to be assigned to Items. This setup is optional, and it does not influence any other parts of the system.

To set them up, go to the **365WineTrade** Menu, **Item Setup**, **Appellation List**. You will be taken to the following list:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image049.png)

Figure 5‑14: List of Appellations

## 5.11.     365WineTrade FastTab

This FastTab contains base **365WineTrade** fields that are needed for general use of the system, as well as master data related to the wine industry.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image050.png)

Figure 5‑15: 365WineTrade FastTab on the Item Card

Most of these fields are self-explanatory on the wine industry. Please see below descriptions for some of these fields with special behavior assigned to them:

Table 5‑5: 365WineTrade FastTab fields with special remarks

|     |     |
| --- | --- |
| **Field** | **Note** |
| **Case Pack** | If the Item Base UoM is in Bottles, BC will create an automatic conversion to Cases out of this value; if the Item is in Cases, BC will create the conversion to Bottles |
| **Proof** | Proof is automatically calculated as Alcohol Content % \* 2 |
| **Department Code** | This is BC’s standard Global Dimension 1 Code |
| **Brand Code** | This is BC’s standard Global Dimension 2 Code |
| **Sales Order Review** | Flag that this Item will always stop on Order Review. Please see [Sales Order and Credit Reviews](#_Sales_Order_Reviews) for more details |

## 5.12.     Item Reviews

On the wine and spirits industry, it is common to have products being reviewed by a few renowned publications, such as magazines or websites that specialize in these types of beverages.

**365WineTrade** offers a flexible way to keep track of those for any Item in inventory.

### 5.12.1. Setting up Item Reviews (Publications)

In order to keep track of Item Reviews, first you need to set up which publications you will keep track of reviews, under the **365WineTrade** menu, **Item Setup**, **Item Reviews**. This will take you to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image051.png)

Figure 5‑16: Item Reviews, aka, Publications

To insert a new publication to the list, you can click action **New**, and then you can supply the record with a shortcut code and a name. Field **Item Count** can be drilled down into, in order to see a summary of all items rated for the selected review.

### 5.12.2. Setting up Item Review Scores

Once Item Reviews are setup, you can also setup standard Review Scores, for those publications which have a definite set of values acceptable for each review. Some other publications can accept any value within the range of 1-100, for example. **Please note**: For numerical scores, this setup is not mandatory.

To set up Review Scores, go to menu **365WineTrade**, **Item Setup**, **Item Review Scores**. You will then be presented with the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image052.png)

To insert a new Score to the list, you can click action **New**, and then you can supply the record with a Score and the description for that Score.

**Please note**: The Item Review Scores are not linked to the Item Reviews table. Therefore, the list of Scores will be shown for any publication.

### 5.12.3. Adding an Item Review to an Item Card

After Item Reviews and Review Scores are set up, you can assign these reviews for your items. To do so, go to the Item Card, under FastTab **Reviews**:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image053.png)

Figure 5‑17: Item Card, FastTab Reviews

Table 5‑6: Item Card Review fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Review** | Lookup field to the Item Reviews (publications) table |
| **Review Abbreviation** | Shortcut code coming from the Item Reviews table |
| **Score** | Select a value from the lookup list, or enter your own value |
| **Date** | Date this review was published |
| **Comment** | Description of the Review. This field supports up to 2048 characters |

If the Review Description is longer than what the field can display, you can click on the ellipsis button to the right of it, in order to see a popup message with the full description:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image054.png)

Figure 5‑18: Ellipsis to the right of the comment field

![](365WineTrade_Users%20Guide%20-%20Base.fld/image055.png)

Figure 5‑19: The contents of field Comment on a popup window

**Please note**: The Item Reviews are also available as a FactBox on the Item Card.

## 5.13.     Copying Items

Standard Business Central offers a function to copy an existing item into a new item. **365WineTrade** enhances this functionality by adding a few new features to this copy process. In order to be able to use this feature, first, it must be activated from the [Wine Setup](#_Wine_Setup).

Once it is active, when you select to copy an item using standard BC method (enter Item Card, ribbon Actions, Functions, Copy Item), BC will show the following page:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image056.png)

Figure 5‑20: Copy Item extended page

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image057.png)

Figure 5‑21:Destination Companies FastTab

**365WineTrade** adds the following fields and features over the existing Copy Item feature:

·       Description

·       Case Pack

o   This can only be changed if you are also copying the Units of Measure for this item

·       Bottle Size

·       Vintage Code

·       Blocked

·       Vendor No.

·       Destination Companies

o   This lets you pick other companies in the same Database where the new item should be copied to

## 5.14.     Additional Actions and Navigation Options

**365WineTrade** also adds the following action to the Related ribbon:

Table 5‑7: Additional 365WineTrade actions on the Item Card

|     |     |
| --- | --- |
| **Path** | **Purpose** |
| **Related > Item > Documents** | Allows for you to attach documents to the current Item Card. This is not to be confused with BC’s standard Attachments feature. Refer to section [Document Worksheets](#_Document_Worksheets) for more details. |

## 5.15.     365WineTrade Item Availability Enhancement

365WineTrade has introduced added functionality to provide user customizable inventory availability based on user defined requirements. The activation of this feature is managed from the Wine Setup page as seen below.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image058.png)

Activating this feature is accomplished with the toggle switch in the true/on position. After activation, the user will define the “Item Availability Code” as seen above. After the code has been defined, the following screen will be presented to the user for configuration.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image059.png)

In the quantity field, the user will place a check mark that will indicate these transaction types are to be included in the calculation of “OnHand Inventory”. When completed, the Item Availability can be viewed on the item card as seen below. The User Defined item availability column will be labeled **“365WineTrade Available Quantity”**

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image060.png)

## 5.16.     Item Ledger Entry Rounding Adjustment Enhancement

This feature tackles the issue of rounding calculation taken to 5 decimal places on remaining quantity when partial case shipments are occurring. An example of this rounding can be seen in the screen shot below.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image061.png)

To remove this rounding from the system, a job queue can be set up from the Wine Setup area.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image062.png)

This will create a job that will, on a regular basis as defined by the user, post adjusting entries to remove this rounding variation.

The job queue below is how it will appear when created from the wine setup card as discussed previously. This job queue can be edited for frequency as defined by Base Dynamics BC functionality.

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image063.png)

  

# 6.   Creating Customers using 365WineTrade Features

**365WineTrade** features include additions to the standard BC Customer Card. The next sections describe how to fill out **365WineTrade** fields on Customer Cards.

## 6.1.        Corporate Namebill

**365WineTrade** adds a new field, **Corporate Name**, on the **General** FastTab of the Customer Card. This field can be used as needed during implementation, as an option to existing fields **Name** and **Name 2**. This field is typically used for internal purposes, as opposed to being printed on customer-facing documents, since this field does not print on any standard BC reports. For customer-facing name information that should print on reports, you should use standard fields **Name** and **Name 2**.

![](365WineTrade_Users%20Guide%20-%20Base.fld/image064.png)

Figure 6‑1: Corporate Name field on Customer Card

## 6.2.        365WineTrade FastTab

This FastTab contains base **365WineTrade** fields that are needed for general use of the system, as well as master data related to the Wine Industry.

![A screenshot of a web page
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image065.png)

Figure 6‑2: 365WineTrade FastTab on the Customer Card

Table 6‑1: 365WineTrade FastTab Fields on the Customer Card

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Sales Region Code** | [Sales Region for this Customer](#_Sales_Regions) |
| **Category Code** | Provide users with the ability to use multiple different values to further categories of customers. |
| **Chain Name** | Optional. Pick from the list of [Chain Names](#_Chain_Names) |
| **Order Type Code** | Optional. Default [Order Type](#_Order_Types) for this customer. Can be changed at Sales Order level if needed |
| **Pickup Address Code** | Default [Pickup Address](#_Pickup_Addresses_1) that will be used on new Sales Orders |
| **Bill and Hold Bin Code** | Please refer to section [Bill & Hold Agreements](#_Automated_Processing_of_1) |
| **On Premise** | This feature is to be used with **365****WineTrade** **US Compliance** extension. Please refer to that User Guide for more details |
| **Co-Op Count** | Provides Co-op count that customer belongs to. Drill down feature to view detail co-ops. |
| **Price Category Code** | Optional. Define Price Category for this customer. Please refer to the Pricing User Guide for additional details. |
| **Delivery Instructions** | Optional. Default delivery instructions to be transferred to the Sales Order header. **Please note**: If the Customer has a Ship-to Address with a Delivery Instruction, the Delivery Instruction from the Ship-to Address will replace the Customer Ship-to Address; it will **not** append to it |

## 6.3.        Credit FastTab

The Credit FastTab contains the current and the historical information for the Customer [Credit Class](#_Approval_Users).

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image066.png)

Figure 6‑3: Credit FastTab on the Customer Card

The field Credit Class Code contains the current Credit Class assigned to the Customer. Each time a Customer is put **ON** hold, the Historical Credit Class code field is updated with the previous Credit Class Code that was **OFF** hold, and a transaction log is made to an internal table called **Historical Credit Class**. You can access this history by clicking on the drill-down button next to the **Historical Credit Class Code** field. Lastly, BC will update any Sales Orders with the new Credit Class Code for the Customer, no matter whether the previous Credit Class was **ON** or **OFF** hold.

**Please note**: Changing the Credit Class Code on a Customer Card will cause BC to update the Credit Class for **all** current orders for this Customer, whether they are Open or Released.

## 6.4.        Additional Actions and Navigation Options

**365WineTrade** also adds the following actions to the Actions ribbon:

Table 6‑2: Additional 365WineTrade actions on the Customer Card

|     |     |
| --- | --- |
| **Path** | **Purpose** |
| **Customer > Co-ops** | This feature is to be used with **365****WineTrade** **US Compliance** extension. Please refer to that User Guide for more details |
| **Customer > Documents** | Allows for you to attach documents to the current Item Card. This is not to be confused with BC’s standard Attachments feature. Refer to section [Document Worksheets](#_Document_Worksheets) for more details.<br><br>**Please Note**: There is also a FactBox available for this on the Customer Card |
| **Customer > Pickup Addresses** | Refer to section [Pickup Addresses](#_Pickup_Addresses_1) |
| **Customer > Email Addresses** | List of Email addresses for the Customer, to be used with the [Document Worksheets](#_Document_Worksheets) feature. |

  

# 7.   Processing Purchase Orders

## 7.1.        Vendor Card

**365WineTrade** adds a few elements to standard BC’s Vendor List and Cards.

![A screenshot of a login box
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image067.png)

Figure 7‑1: 365WineTrade FastTab on the Vendor Card

Table 7‑1: List of 365WineTrade fields on the Vendor Card

|     |     |
| --- | --- |
| **Field** | **Description** |
| **FDA Registration No.** | Determines the FDA Registration No. for this vendor |
| **FDA Registration Expiration Date** | Determines the FDA Registration Expiration Date for this vendor |
| **Pickup Address Code** | Default [Pickup Address](#_Pickup_Addresses_1) that will be used on new Purchase Orders |
| **Price Category Code** | Optional. Define Price Category for this vendor. Please refer to the Pricing User Guide for further details. |
| **Freight Forwarder Code** | Default [Freight Forwarders](#_Freight_Forwarders) that will be used on new Purchase Orders |
| **Vendor Type** | Used to categorize vendors. There is no intelligence behind this field |
| **Producers** | Displays the first Producer assigned to this vendor. If there are multiple Producers, drilling down on this field will show the list of Producers |

Table 7‑2: Vendor Card 365WineTrade new elements

|     |     |
| --- | --- |
| **Element** | **Purpose** |
| **Related > Vendor > Documents** | Enables users to manage documents attached to the currently selected Vendor |
| **Related > Vendor > Email Addresses** | Sets up email addresses to be used with the [Document Worksheets](#_Document_Worksheets) functionality |
| **Related > Vendor > Pickup Addresses** | Please refer to section [Pickup Addresses](#_Pickup_Addresses_1) for more details |

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image068.png)

Figure 7‑2: Chargeback FastTab on the Vendor Card

Table 7‑3: List of Chargeback fields on the Vendor Card

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Vendor No.** | In each of the subject areas for DA’s, Billbacks & Bad Bottle, there is a Vendor No. setting allowing the user to use an alternative Vendor code that will be used in the creation of the corresponding Chargeback Credit Memo document created during the Chargeback process routine |
| **Vendor Posting Group** | In each of the three subject areas, the user is given the flexibility to use an alternative posting group that can be used to deviate from the normal posting group setup on the vendor card. |
| **Payment Terms Code** | Each of the subject areas can have a custom payment term that will be used when creating the chargeback credit memo. |
| **Dimension Group Code** | Dimension Group Codes can used to group large number of Chargeback Purchase Credit Memo lines by a specific dimension. |
| **Depletion Allowance Description** | This allows the user to define an alternative posting description that will be used in ledger entries for DA’s |

## 7.2.        Blanket Purchase Order Synchronization

Blanket Purchase Orders can be seen as contracts, when using standard Business Central. You can setup agreements with your vendors in regard to quantities that will be provided throughout a certain period.

Standard Business Central allows you to enter these contracts, but it has a very loose control when it comes to mixing Purchase Orders with existing Blanket Orders.

**365WineTrade** enhances this functionality by offering 2 new checks, available from the [Wine Setup](#_Wine_Setup):

·       **Allow Multiple Blanket Purchase Orders per Vendor per Item**: Specifies whether users can enter one same item, for one same vendor, across different Blanket Purchase Orders. The acceptable values are:

o   **Not Allowed**: BC will throw an error message if you enter an item on a Blanket Order, and this item already exists on another Blanket Order for the same vendor.

o   **Ask**: BC will warn you about the item existing on another Blanket Order, and it will let you choose whether to continue or to stop.

o   **Allowed and Do Not Ask**: BC will not let you know if this item is in other Blanket Orders for the same vendor

·       **Link Purchase Orders to Blanket Purchase Orders**: When entering a Purchase Order, if BC detects that a Blanket Order already exists for the same item and for the same vendor, it will act depending on this setting. The acceptable values are:

o   **Ask**: BC will ask if the user wants to link the current Purchase Order line to the existing Blanker Order line. User may say yes or no.

o   **Automatically with Warning**: BC will automatically link the Purchase Order line to the existing Blanket Order line, and it will throw a warning message.

o   **Automatically without Warning**: BC will automatically link the Purchase Order line to the existing Blanket Order line, and no warnings will be thrown.

## 7.3.        Purchase Orders

**365WineTrade** adds 3 new features to the Purchase Order Process:

·       [Freight Forwarder](#_Freight_Forwarders) code (under Shipping and Payment FastTab), rolled down from the Vendor Card

·       [Pickup Address](#_Pickup_Addresses_1) selection (under Shipping and Payment FastTab), also rolled down from the Vendor Card

·       [Purchase Order Consolidations](#_Purchase_Order_Consolidations_2), described on the next section

## 7.4.        Purchase Order Consolidations

**365WineTrade** offers a basis functionality to consolidate Purchase Orders, so that they can be watched over in a batch, received in a batch, and posted in batch.

Consolidations can be done for both International and Domestic Orders.

To assign a Purchase Order to a Purchase Consolidation, simply select a **Consolidation No.** on the Purchase Order header:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image069.png)

Figure 7‑2: Purchase Consolidation fields on the Purchase Order header

When you select a **Consolidation No.**, BC will automatically lookup fields **Port of Departure**, **Port of Entry**, **Container No.** and **Shipped**, from the Consolidation Header. **Please note**: All purchase lines will be added to the Consolidation. It is not possible to split purchase lines between different Consolidation headers. If this a need, please consider acquiring **Western Computer’s Inbound Container Extension**, which is a much more advanced version of this functionality.

When selecting a Consolidation No., you can also choose to create a new Consolidation right from the Lookup dialog:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image070.png)

Figure 7‑3: Lookup +New action on the Consolidation No. field

To see a list of all current consolidations, go to the **365WineTrade** Menu, **Purchasing**, **Purchase Consolidations**. You will be taken to the following list:

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image071.png)

Figure 7‑4: List of Purchase Consolidations

The card for a Purchase Consolidation is shown below:

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image072.png)

Figure 7‑5: Purchase Consolidation Card, FastTab General

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image073.png)

Figure 7‑6: Purchase Consolidation Card, FastTab Purchase Lines

Table 7‑3: Purchase Consolidation fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Container No.** | No. that can be used for tracking the container. This is usually provided by the shipping agent |
| **Freight Forwarder Code** | Code of Freight Forwarder assigned to this Consolidation |
| **Customs Broker Code** | Code of Customs Broker assigned to this Consolidation |
| **Vessel No.** | Vessel No., usually provided by the shipping agent |
| **Shipped** | Manual flag to indicate if a consolidation has shipped from its Port of Departure. This field does not hold any intelligence; it is informational only |
| **Description** | Provides 100 characters for description. Can be used alternatively to hold last status updates |
| **Expected Receipt Date** | Date to be used for planning purposes. Updating this field will update all Purchase Orders and Lines associated with this consolidation |
| **Port of Departure** | Code of Port of Departure. There is no table associated with this field, it is a freeform text field |
| **Port of Entry** | Code of Port of Departure. There is no table associated with this field, it is a freeform text field |

### 7.4.1.     Receiving and Invoicing a Purchase Consolidation

When you are ready to receive a Purchase Consolidation, you should enter the quantities to receive on each line, and then run action **Posting**, **Post Batch**…

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image074.png)

Figure 7‑7: Post Batch... action on a Purchase Consolidation

This action will take you to BC standard Batch Post Purchase Orders job, where you can set the following options:

![Graphical user interface, text, application, chat or text message
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image075.png)

Figure 7‑8: Batch Post Purchase Orders

Table 7‑4: Batch Post Purchase Orders options

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Receive** | Determines if you want to Receive the Purchase Order lines on this consolidation |
| **Invoice** | Determines if you want to Invoice the Purchase Order lines on this consolidation |
| **Posting Date** | If you want to replace the Posting Date, indicate the new Posting Date on this option |
| **Replace Posting Date** | Uses the Posting Date above on the posted invoice |
| **Replace Document Date** | Uses the Posting Date above as Document Date on the posted invoice |
| **Calc. Inv. Discount** | Determines if BC should Calculate Invoice Discounts again |

This job task will also be automatically filtered to the current Consolidation No.:

![Table
Description automatically generated with medium confidence](365WineTrade_Users%20Guide%20-%20Base.fld/image076.png)

Figure 7‑9: Purchase Order table filters

Users may change these filters if needed, but usually, users should not need to change this.

Once Purchase Lines are received, the Quantities Received will be updated on the Consolidation Lines.

If a Purchase Consolidation is fully received and invoiced, then the header and lines will be turned into history (Posted Purchase Consolidations). If a Purchase Consolidation is only partially received and invoiced, then lines will be removed from the open Consolidation as they get posted.

Lastly, if needed, users can choose to reopen a Purchase Consolidation to add more lines to it.

**Please Note**: If users reopen a Purchase Consolidation, the historical lines will not be brought over to the reopened document. They will remain as posted, but without a Posted Purchase Consolidation header. Once the Consolidation gets fully posted again, then it will be converted into history again, and all lines will be, once again, grouped under the Posted Purchase Consolidation.

  

# 8.   Processing Sales Orders

**365WineTrade** is embedded in the Sales Order Processing of Business Central. This section and those following will provide an overview on how processing a Sales Order is affected by this module. This documentation does not cover the base BC Sales Order entry process steps.

The following fields are introduced by the **365WineTrade** on the Sales Order module:

Table 8‑1: Summary of fields created and/or affected by 365WineTrade

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **FastTab General** |     |
| **Order Type Code** | Impacts the behavior of a few fields (Location Code, Purchasing Code, etc.). Impacts [Sales Order Charges](#_Pickup_Addresses) and impacts the [Sales Order Review](#_Sales_Order_Reviews) process. Refer to section [Order Types](#_Brand_Item_Registration) |
| **Co-op Code** | This feature is to be used with **365****WineTrade** **US Compliance** extension. Please refer to that User Guide for more details |
| **Review Status** | Displays the current status in the Sales Order Review Process. Status can be blank, Pending or Approved. Refer to section [Sales Order Reviews](#_Sales_Order_Reviews) |
| **FastTab Shipping and Billing** |     |
| **Ship-to** | This standard field has been changed to include a new option **Pickup Address**. Refer to section [Pickup Addresses](#_Pickup_Addresses_1) |
| **Delivery Instructions** | This field can be automatic populated from a Customer Card, or from a Ship-to Address (Ship-to Addresses take precedence over Customer Cards). It can also be manually changed at the Sales Order Level. **Please note**: This field does not print in any standard BC reports. Customizations are needed to have this printed. |
| **FastTab 365WineTrade** |     |
| **Credit Class Code** | Defaults from the Customer Card. Refer to section [Credit Classes](#_Approval_Users) |
| **Sales Region Code** | Defaults from the Customer Card. Can be changed manually. Refer to section [Sales Regions](#_Sales_Regions) |

The following FactBoxes are also added to BC by **365WineTrade**:

Table 8‑2: 365WineTrade FactBoxes on the Sales Order Page

|     |     |
| --- | --- |
| **FactBox** | **Purpose** |
| **Order Reviews** | Refer to section [Sales Order Reviews](#_Sales_Order_Reviews) |
| **Order Line Reviews** | Refer to section [Sales Order Reviews](#_Sales_Order_Reviews) |

The following fields are mandatory for entering new lines:

·       Order Type Code

·       Sales Region Code

## 8.1.        Sales Line Quantity

**365WineTrade** does not implement any special methods or format for handling the field Quantity. As a base BC feature, the default Unit of Measure on a Sales Line will be transferred from the field **Sales Unit of Measure** from the Item Card. Users can then choose to keep the Sales Unit of Measure or alternate to other units of measure set up for the Item.

![](365WineTrade_Users%20Guide%20-%20Base.fld/image077.png)

Figure 8‑1: Sales Line Quantity in different UoMs

Standard BC allows you to enter any Quantity on a quantity field, be it an integer or a decimal quantity. **365WineTrade** introduces a special setup that can prevent entry of decimal quantities for specific Units of Measure (please refer to section [Units of Measure](#_States)). When this special feature is enabled, this is how BC will behave for Sales Lines, Purchase Lines and Journal Lines:

Table 8‑3: Sales Line Quantity Entry rules

|     |     |
| --- | --- |
| **Scenario** | **Behavior** |
| **No UoMs are set up as non-fractional** | You can enter decimal quantities for both Bottle and Case Units of Measure. They will be recorded as decimal when posting the Item Ledger Entries. **Please note**: This setup may render results such as 1.37 Bottles |
| **Only Bottle UoM is set up as non-fractional;**<br><br>**Item Base UoM is Bottle or in Case** | You cannot enter a decimal quantity for the Bottle UoM.<br><br>You can enter a decimal quantity for the Case UoM, but BC will adjust this quantity to reflect a non-fractional Bottle UoM. For example, an Item with 12 bottles per case, 1 BT = 0.083 CS. If the user tries to enter 0.099 CS, BC will round it to the closest integer bottle; in this case 0.083 CS = 1 BT |
| **Both Bottle and Case UoMs are set up as non-fractional** | You cannot enter a decimal quantity for either the Bottle UoM, or for the Case UoM. |

Our recommended setup is that at least all the individual UoMs (Bottles, Cans, Kegs, etc.) are set up as non-fractional on the [Units of Measure setup](#_States).

## 8.2.        Releasing Sales Orders

The next step after entering all Sales Header information and Sales Lines information is to have the Sales Order released.

This is done using standard BC **Release** action from the **Actions** ribbon.

Releasing the Sales Order will trigger the [Sales Order Review](#_Sales_Order_Reviews) process, which is described in detail later in this documentation. This process is meant to request approval from users in a few different areas. If any Sales Order Reviews are needed, the order will be kept on status **Open** until all Order Reviews are approved or cleared. In this situation, field **Review Status** will show as **Pending**.

The table below describes the different Order Statuses and what they mean:

Table 8‑4: Sales Order Status and Review Status meanings

|     |     |
| --- | --- |
| **Status** | **Description** |
| **![](365WineTrade_Users%20Guide%20-%20Base.fld/image078.png)** | Sales Order entry is in progress. No user has tried to release this Order yet. |
| **![](365WineTrade_Users%20Guide%20-%20Base.fld/image079.png)** | Sales Order entry is finished, and a user has tried to release the Order. However, Sales Order Reviews are pending and must be approved or cleared. |
| **![](365WineTrade_Users%20Guide%20-%20Base.fld/image080.png)** | Sales Order entry is finished, and it’s officially considered released. If there were any Sales Order Reviews, they have been approved. |

## 8.3.        Shipping and Invoicing Sales Orders

**365WineTrade** may modify the process of Shipping a Sales Order, if you’re using either the [Bill & Hold](#_Automated_Processing_of_1) or [Salesperson Location](#_Salesperson_Location_2) processes. **365WineTrade** does not modify the process of Invoicing a Sales Order.

  

# 9.   Sales Order and Credit Reviews

Standard BC offers some level of Sales Order and Credit approvals based on workflows. **365WineTrade** Sales Order and Credit Reviews is a more comprehensive approval tool that is a replacement of the standard BC workflows, but it does operate in different ways. **365WineTrade** Sales Order and Credit Reviews offer more options for approval checks on items that require more logic, whereas base BC only offers triggers based on fields of the Sales Header.

Once users set up Sales Order Review Categories and link them to [Order Types](#_State_Liquor_Authority), BC will start checking them on any new entered Sales Order. Most Sales Order Reviews checks are done at time of Sales Order Releasing, but some specific ones will be tested as they happen (e.g., Sales Price changes). No matter when the Order Review type is tested, they will all be displayed to the user at time of releasing. If there are any Items to be approved, the **Status** on the Sales Order will still show as **Open**, and a new field called **Review Status** will show as **Pending**:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image079.png)

Figure 9‑1: Sales Order Status when there are pending order reviews

The Sales Order status will remain **Open**, for as long as there are Sales Order or Credit Reviews pending approval. Users then have the option to approve each review, and if done by mistake, they can un-approve reviews as well. Users cannot reject/decline approval items; instead, they must manually reopen the Sales Order and address the issues. **Please note**: Reopening the Sales Order will delete all Order Reviews, including the ones that have already been approved; anything that had been approved, will require approval again.

Once all review Items have been either approved, or cleared, then the Sales Order **Review Status** will automatically change to **Approved**, and the Sales Order **Status** will change to **Released**:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image080.png)

Figure 9‑2: Sales Order Status as released

**Please note**: Even if there were no Sales Order Reviews or Credit Reviews to be made to an order, Review Status will still show as **Approved**.

Once Sales Order Reviews are approved and the Sales Order is posted, all the Reviews will be moved to the Posted Invoice document, so that users can review them in the future, if needed.

You can find specific details to the steps above in the following sections.

## 9.1.        Order Review Types

Sales Order and Credit Review types are split into 2 areas: Sales Order Reviews and Credit Reviews. Sales Order Reviews are usually handled by the internal sales team which will review approvals needed for all aspects except for Credit aspects, such as Order entry issues. Credit Reviews are usually handled by the finance department. **365WineTrade** offers flexibility to handle these in 2 different dashboards (Sales Order Review and Credit Review), or they can all be handled from the Sales Order Review dashboard.

Sales Order Reviews support the following checks for approval, most of which, are very common to the wine industry:

·       Overdue Balance, Over Credit Limit, On Credit Hold

·       Sample Orders, Review Orders, Orders on Hold, Orders with Items for Review

·       Minimum Charge or Split-Case Charge Manually Deleted

·       Unit Price $0, Unit Price not $0, Unit Price manually changed

·       Lines with non-reserved quantities

·       Lines with Sample items

**365WineTrade** offers extension flexibility so that customers can add more review checks if they need additional approvals. **Please note**: This can only be done as a customization by the implementing partner. End users cannot dynamically create new review checks.

You can find more specific details on how each order review type works in the next section.

## 9.2.        Setting up Sales Order Reviews

You start setting up Sales Order Reviews by creating a Sales Order Review Category and then assigning these categories to [Sales Order Types](#_State_Liquor_Authority).

To review Sales Order Categories, go to the **365WineTrade** menu, **Setup**, **Order Review Categories**. You will be taken to the **Order Review Categories list**:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image081.png)

Figure 9‑3: Order Review Categories list

From this list you can create a new one or edit an existing one. In either case, you will be using the Order Review Category Card to determine which checks will be done for each review category:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image082.png)

Figure 9‑4: Order Review Category card

Table 9‑1: Order Review Category fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Review Type** | Refer to **Table 9‑2: Review Types** below |
| **Order** | Order in which this check will be performed |
| **Notification Type** | ·       **Stop**: Does not allow for approvals: it must be addressed by executing changes to the Sales Order. BC will throw an error message on screen and stop processing. If the check is done at time of releasing the order, the Review Status will **NOT** show as Pending.<br><br>·       **Warning**: Does not allow for approvals, but it does allow for further processing. BC will throw a message on screen, just for information. Since approvals can’t be done, BC may mark a Sales Order as released if all other approval types have been satisfied<br><br>·       **Review**: Generate an Order Review that will require approval before an order can be considered Released |
| **Message** | Message to be used when Notification Type is either Stop or Warning |
| **Amount** | Used for specific review types |
| **Comment** | Internal comment just for organization. Will not be displayed anywhere else |

Table 9‑2: Review Types

|     |     |     |
| --- | --- | --- |
| **Type** | **Area** | **Trigger** |
| **Credit Review** | Credit Review | When any of the Credit Review types below are triggered |
| **Overdue Balance** | Credit Review | When Customers have an overdue balance |
| **Over Credit Limit** | Credit Review | When Customers are over their credit limit |
| **On Credit Hold** | Credit Review | When sales orders have a [Credit Class](#_Approval_Users) set as on hold |
| **Order Minimum** | SO Review | When the total Sales Order amount is under the amount defined on the Amount field |
| **Order Type-Sample** | SO Review | When sales orders have an Order Type marked as Sample = True |
| **Order Type-Review** | SO Review | When set, will always stop orders for review with verbiage “Order Type-Review”. No special logic is checked. Usage is defined by the customer |
| **Order Type-Hold** | SO Review | When set, will always stop orders for review with verbiage “Order Type-Hold”. No special logic is checked. Usage is defined by the Customer. |
| **Delivery Charge Deleted** | SO Review | When a [Minimum Order Charge](#_Pickup_Addresses) is manually deleted |
| **Split-Case Charge Deleted** | SO Review | When a [Split Case Charge](#_Pickup_Addresses) is manually deleted |
| **Item Review** | SO Review | When the item is marked as Sales Order Review = True |
| **Unit Price $0** | SO Review | When the Sales Line Price is Zero |
| **Unit Price not $0** | SO Review | When the Sales Line Price is Not Zero |
| **Sales Price Change** | SO Review | When the Sales Line Price has been manually changed |
| **Non-Reserved Quantity** | SO Review | When the Sales Line has quantities that are not reserved from Inventory (using BC’s standard Reservation system) |
| **Sales Line-Sample** | SO Review | When any Sales Line has a Sample Reason Code |
| **Salesperson Over Sample Budget** | SO Review | When a Salesperson shipping a sample is over their sample budget for the period. For more details, refer to section [Sample Management Setup](#_Sample_Management_Setup_1) |
| **Not Fully Allocated** | SO Review | If the Sales Order Line-item quantity has exceeded the available amount of Allocation quantity the system will produce a review message for approval. |
| **Delinquent or Inactive SLA License** | SO Review | Used when SLA integration is active to obtain current customer information such as delinquent AR with other companies or License is expired. Both conditions would block sales to this customer based on SLA |
| **In-Activ**e **SLA Licens**e | SO Review | Validated if a customers License from the customer card is still active. |
| **Delinquent SLA License** | SO Review | Validates if the License Fees are up to date. |

## 9.3.        Credit Classes

Credit Classes are used extensively on **365WineTrade** to keep accurate information about whether customers are in good standing or not. These Credit Classes, when properly setup, and used in conjunction with Credit Reviews, will cause **365WineTrade** to always stop Sales Orders from Customers who are currently set with any type of hold (e.g., Delinquent with an SLA, or just internally marked as On Hold).

Credit Classes can be set on the following levels:

·       [Customers](#_Credit_FastTab)

·       [Sales Orders](#_Processing_Sales_Orders_1)

When a new Sales Order is created, the Credit Class Code will default to the Sell-to Customer’s Credit Class Code. Changing the Customer’s Credit Class Code will cause BC to update the Credit Class Code for all Sales Orders currently existing for that Customer, whether Open or Released.

Ultimately for Credit Review purposes, the Credit Class on a Sales Order header will be the only determining criterion if the Order should be stopped or not.

To access the Credit Classes records, go to the **365WineTrade** Menu, **Credit**, **Credit Classes**. You will then be taken to the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image083.png)

Figure 9‑5: Credit Classes list

Table 9‑3: List of Credit Classes fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Credit Hold** | Determines that this Credit Class is to be considered On Hold |

## 9.4.        Approval Users

For a successful setup of Order Reviews, you also need to set up all approval users from the standard BC’s User Setup Page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image084.png)

Figure 9‑6: Flags for Sales Order Review and Credit Review Approvers

Setting up a user as a Sales Order Review approver or Credit Review approver will not limit their visibility on what needs to be approved; it only limits what entries they can approve. Sales Order Review approvers can see Credit reviews, and vice-versa, no matter what their permissions are. Users who are not approvers can also see these reviews, as well as view the Sales Order Review and Credit Review dashboards.

## 9.5.        Sales Order Review Approvals – Order by Order

Once the user tries to release a Sales Order, and its Sales Order Reviews and Credit Reviews are created, users can see them in the Order Reviews and Order Line Reviews FactBoxes of a Sales Order:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image085.png)

Figure 9‑7: Order Reviews and Order Line Reviews FactBoxes

As mentioned previously, some Review Types may be tested on the go as changes are happening (e.g., Sales Price Changes), and this may give users a cue that the order will stop for further approval. However, most Review Types are only tested at time of Sales Order release.

The few Review Types that are tested on the fly, even though they are displayed promptly, can only be approved once the user tries to release the Sales Order.

Once the order starts the approval process (Status = Open; Review Status = Pending), users can approve Items, by selecting 1 or more items on the FactBox (step 1), hitting action **Order Reviews** (step 2), and then **Approve** (step 3):

![](365WineTrade_Users%20Guide%20-%20Base.fld/image086.png)

Figure 9‑8: Steps to approve a review item from the Order Review FactBox

If a review has been approved by mistake, users can un-approve the entry:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image087.png)

Figure 9‑9: Un-approve Order Reviews

**Please note**: If you try to approve an Item and nothing happens, you have not been properly set up as an approver. Please review section [Approval Users](#_Approval_Users_1) above.

Once all items have been approved, the **Review Status** will change to **Approved**, and the order Status will change to **Released**.

## 9.6.        Sales Order Review Approvals – Multiple Documents

**365WineTrade** also offers a centralized dashboard for users to review all Sales Order Reviews that are currently pending. To access this view, go to the **365WineTrade** menu, **Accounts Receivable**, **Sales Order Review**. You will be taken to the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image088.png)

Figure 9‑10: Sales Order Review Dashboard

This dashboard is Sales Orders-centric: it’s optimized for the user to have a better visibility of Orders in the system. The area marked in a yellow box above, is the Filters area, where you can define what data you will see on the Sales Orders Headers area (blue box). Once you select a Sales Order from the headers list, then both the Sales Order Lines (green box) and FactBoxes (red box) will be updated accordingly.

This view can display all Sales Orders currently in the system. Therefore, getting familiar with the Filters Area and its capabilities is very much recommended.

### 9.6.1.     Sales Order Review Filters Area

![](365WineTrade_Users%20Guide%20-%20Base.fld/image089.png)

Figure 9‑11: Sales Order Review: Filters Area

Table 9‑4: Filters Area fields

|     |     |
| --- | --- |
| **Filter** | **Purpose** |
| **Review Code** | Enables user to apply a pre-set filter, also referred to as parameters. Please refer to section [Sales Order Review Parameter](#_Sales_Order_Review) below. |
| **View** | ·       **Review**: Apply filters from Review Code, and additionally, set a filter to see all Orders that have at least one Sales Order Review pending approval. Orders that have been fully approved will not show.<br><br>·       **Posting**: Apply filters from Review Code, and additionally, set a filter on Order Status = Released |
| **Show Credit Review** | If set to No, BC will narrow down the Sales Order list to show only reviews of type Sales Order Review. For more details, refer to Table 9‑2: Review Types for more details |
| **Date Filter** | Applies a filter where Shipment Date is equal to or before the date on this filter |

Filters are applied as soon as the values are changed. You do not need to refresh or press any other action to refresh the view.

### 9.6.2.     Sales Order Review Parameters

Since you can use this dashboard for multiple purposes other than just approving Order Reviews, you have the option of pre-setting some views using the Review Code field. When you look up on the Review Code field, you will be taken into a list of pre-set filters, also referred to as Parameters:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image090.png)

Figure 9‑12: Sales Order Review Parameters

Each one of these filters will display a **Code**, a **Description** and their **Parameters**, which contains a list of Sales Orders filters to be applied when using each code. If you want to change the parameters field, you can drill down on the hyperlink for the field’s content, and BC will present you with a Sales Order filter page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image091.png)

Figure 9‑13: Parameter filters

On this page, you can set up the different filters to be applied to the Sales Header table, when filtering the Sales Order Reviews list.

This gives you the flexibility of following different groups of orders, without having to set filters every time. **Please note**: This feature is very similar to BC’s standard Custom Saved Views. This dashboard, however, provides more functionality, as described below.

Once you’re done setting up the parameters (filters), you can select one of them, and your Sales Order Review dashboard will update to show just the Sales Orders matching the criteria of the filter.

### 9.6.3.     Sales Order List – Shortcut Actions, Lines and FactBoxes

This Sales Order Review dashboard offers the following shortcut Actions from the Sales Order List:

Table 9‑5: Sales Order list actions

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Process > View** | Shows the Sales Order Card |
| **Process > Post…** | Posts the Sales Order. As in standard BC, it will prompt if you desire to Ship, Invoice or Ship and Invoice |
| **Process > Release** | Attempts to release the Sales Order currently selected. **Please note**: This option does not release in batch, even if you have multiple Orders selected |
| **Process > Reopen** | Reopens the Sales Order |
| **Process > Post Batch…** | Executes standard BC Post Batch routine. **Please note**: This will not post the Orders that are currently selected. Instead, it will prompt a Sales Header filter page for you to fill out the necessary criteria |
| **Customer > Card** | Shows the Customer Card for the selected Sales Order |

Additionally, users can see all lines in each order by looking into the Sales Lines area (green box):

![](365WineTrade_Users%20Guide%20-%20Base.fld/image092.png)

Figure 9‑14: Sales Order Lines area

Lastly, the Sales Order FactBoxes serve 3 purposes:

Table 9‑6: Sales Order Review FactBoxes

|     |     |
| --- | --- |
| **FactBox** | **Purpose** |
| **Reviews** | Allows for users to approve reviews on the Order Level |
| **Line Reviews** | Enables users to approve reviews on the Line Level |
| **Contacts** | Displays a list of all contacts registered for the Customer. This is particularly helpful when your internal sales team needs to contact the Customer before adjusting orders |

## 9.7.        Credit Review Dashboard

The Credit Review Dashboard acts very similarly to the Sales Order Review dashboard, however, this one is Customer-centric (as opposed to being Sales Order-centric); instead of showing all Sales Orders Headers and Lines, this dashboard will show Customers and Sales Order Headers. You can access the Credit Review dashboard by clicking the **365WineTrade** menu, **Credit**, **Credit Review**. You will be taken to the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image093.png)

Figure 9‑15: Credit Review dashboard

The Filters Area acts similarly to the [Sales Order Review Filters Area](#_Sales_Order_Review_1). The only exception is that the list of Review Codes for Sales Order Reviews (also called Sales Order Review Parameters) is separated from the Review Codes for Credit Reviews (also called Credit Review Parameters). Therefore, each area (Sales Orders vs. Credit) can keep its own list of Review Codes. **Please note**: This is not optional. If you want both departments to have the same Review Codes, you will need to manually duplicate them.

### 9.7.1.     Credit Reviews List – Shortcut Actions, Sales Orders and FactBoxes

This Credit Review dashboard offers a wider variety of shortcut actions. These actions are listed below:

Table 9‑7: Customer list actions

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Process > Update Credit Reviews** | Manually refreshes the whole dashboard. **Please note**: Applying filters on the header will also refresh the whole dashboard |
| **Process > Cash Receipt Journal** | Displays standard BC Cash Receipt Journal |
| **Process > Sales Journal** | Displays standard BC Sales Journal |
| **Process > Statistics** | Displays standard BC Customer Statistics page for the Customer currently selected |
| **Report > …** | Offers a variety of standard BC reports, that can also be found directly from the Customer card |
| **Customer > Co-ops** | Displays a list of Co-ops for the Customer currently selected. |
| **Customer > Comments** | Displays standard BC Customer Comments for the Customer currently selected |
| **Customer > Contact** | Displays a list of standard BC Contacts for the Customer currently selected |
| **Actions > History > Ledger Entries** | Displays standard BC Customer Ledger Entries for the Customer currently selected |
| **Actions > Prices and Discounts > …** | Offers standard BC actions for Prices and Discounts, such as Invoice Discounts, Prices and Line Discounts, for the Customer currently selected. These can also be found from within the Customer Card |
| **Actions > Functions > Assign Tax Area** | Runs standard BC Assign Tax Area to Customer |
| **Navigate > …** | Offers standard BC navigate actions, that are usually also available from within the Customer Card |

The Sales Orders list also offers shortcut actions:

Table 9‑8: Credit Review Sales Order list shortcut actions

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Manage > View Document** | Displays the Sales Order Card |
| **Manage > Approve** | Approves all Credit Reviews for the Order. **Please note**: This will not approve Sales Order Reviews, only Credit Reviews. For more details on the different Review Types, please refer to Table 9‑2: Review Types |

Lastly, the Credit Review FactBoxes serve 4 purposes:

Table 9‑9: Sales Order Review FactBoxes

|     |     |
| --- | --- |
| **FactBox** | **Purpose** |
| **Sales Order Review** | Refers to the currently selected Sales Order. Enables users to approve reviews on the Order level. **Please note**: Credit Reviews can be only assigned to the Order header level; never to the Line level |
| **State Liquor Authority** | Refers to current state license type and status |
| **Contacts** | Refers to the currently selected Customer. Displays a list of all Contacts registered for the Customer. This is particularly helpful when your credit department needs to contact the Customer for collection inquiries and other matters |
| **Customer Statistics** | Refers to the currently selected Customer. Allows for you to access the Customer Card (by clicking the hyperlink on the Customer No. field). Additionally, it provides a financial summary for the Customer |

  

 

# 10.        Document Worksheets

Document Worksheets is a very powerful tool of the **365WineTrade** module, used for dispatching emails and/or printing documents in Batch. Out-of-the-box, Document Worksheets is flexible enough to handle reports linked to Customers and Vendors, such as Sales Order Confirmations, Purchase Order Confirmations, Customer Statements, Sales Invoices, etc.

**Please note**: BC currently has a limitation with printing multiple documents from the Cloud version. Therefore, printing from the Document Worksheet is currently not available.

To start using Document Worksheets, you will need to setup:

·       Document Groups

·       Email Reports

·       Email Body

·       Document Worksheet Templates

·       Document Worksheet Template Batches

These setups are described on the following sections.

## 10.1.     Document Groups

Document Groups are used in different areas of **365WineTrade** and their main purpose is to group documents in the system, as well as determine how these documents need to be handled in case they need to be emailed or exported out of Business Central. Document Groups also play a role in the [internal permissions system](#_365WineTrade_Internal_Permission_2) for **365WineTrade**.

To setup Document Groups, go to the **365WineTrade** menu, **Setup**, **Document Groups**. You will then be taken to the Document Groups list:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image094.png)

Figure 10‑1: Document Groups list

Table 10‑1: List of fields for Document Groups

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Zip Attachments** | Determines whether files will be compressed when emailed or exported |
| **Export Filename Format** | Determines the format that will be used when generating filenames. You can use a fixed value, or you can use the following variables to compose the filename:<br><br>%1 = Document Description  <br>%2 = Group Code<br><br>%3 = Source No.<br><br>%4 = Group Description<br><br>%5 = Current Date (yyyymmdd)<br><br>%6 = Current Date and Time (yyyymmdd\_hhmmss)<br><br>You can get Help on these variables directly from the interface, by clicking on the drill-down button on this field |
| **Permissions** | Permissions associated with this Document Group. For more information, refer to section [365WineTrade Internal Permission System](#_365WineTrade_Internal_Permission_2) |

## 10.2.     Email Reports

Email Reports are standard or customized Business Central reports that must be enabled for the Document Worksheet functionality. Currently, you can only enable reports related to Customers and Vendors.

In order to enable these reports, go to the **365WineTrade** menu, **Document Worksheets**, **Email Report Setup**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image095.png)

Figure 10‑2: Email Report Setup list

The page is initially started in View mode, so you must change it to Edit Mode before you can change data on it.

Table 10‑2: Email Report Setup fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Table Name** | Determines the table you’re currently selecting reports for. The only out-of-the-box options are Customer and Vendor tables |
| **Report Id** | Used for entering the ID of the Report object to be used with the selected Table Name. You may use custom reports, so long as you’re familiar with their Object Name or Object ID |

## 10.3.     Email Addresses

Once Email Reports are set up, you must set them up for all your Customers and/or Vendors. Each new Email Report that is set up, will display as a column when setting Email Addresses for Customer/Vendors:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image096.png)

Figure 10‑3: Email Addresses with Email Reports

For more information on how to set up Email Addresses per Customer, please visit section [Additional Actions and Navigation Options](#_State_Liquor_Authority_1). For more information on how to setup Email Addresses per Vendor, please visit section [Vendor Card](#_Vendor_Card).

## 10.4.     Email Body

You can pre-set templates for emails to be dispatched using Document Worksheets by using the Email Body setup. To do so, go to the **365WineTrade** menu, **Document Worksheets**, **Email Body List**. You will be taken to the list below:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image097.png)

Figure 10‑4: Email Bodies list

You can manage this list with standard BC actions such as **New**, **Edit List** and **Delete**. Once you create a new code, you can import an Email body using action **New**, **Import Body**. Similarly, you can export a current template by selecting a record and then clicking action **New**, **Export Body**.

To import a new body from scratch, you can create a template using Microsoft Word ®, and save it in a Web Page format (HTML file). **Please note**: The template file should only contain HTML text, without images.

## 10.5.     Document Worksheet Template

Once you have set up which reports can be used, you can create Document Worksheet Templates. Document Worksheet Templates is where users set up which report is run for each Document Worksheet (you can only run one type of document per worksheet). These templates also need to have batches assigned to them, just like BC’s standard Journal structure. This way, **365WineTrade** allows multiple document worksheet processing for different types of documents, for different users, at the same time.

To set up these templates, go to the **365WineTrade menu**, **Document Worksheets**, **Document Worksheet Templates**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image098.png)

Figure 10‑5: Document Worksheet Templates list

To add or modify a Document Worksheet, you will be taken to the Document Worksheet Card:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image099.png)

Figure 10‑6: Document Worksheet Template Card

Table 10‑3: Document Worksheet Template fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Source Table Name** | Use Customer for Sales Related documents, or Vendor for Purchase-related documents |
| **Document Group Code** | [Document Group](#_Document_Groups_1) assigned to this document. This field is mandatory. |
| **Send Type Filter** | Determines which outputs will be generated for documents run under this worksheet (E-Mail, Printer) |
| **Permissions** | Explicitly assigns which Permissions have access to this worksheet. Please see [365WineTrade Internal Permission System](#_365WineTrade_Internal_Permission_2) for more details |
| **Report ID** | Number of Report to be used with this Document Worksheet. **Please note**: Only reports properly set up as Email Reports will be listed here. If you don’t see a report on this list, please refer to section [Email Reports](#_Email_Reports) above |
| **Report Parameters** | Enables users to pre-set filters that will be applied prior to running the document report. You must set this field using the Drill-down button next to it. When you do, a Filters Page will pop up where you can define any special filters you want to apply, or you can just press Ok to leave them blank. **Please note**: This field is mandatory |
| **Report Table ID** | Once you set the **Report Parameters** above, BC will try to automatically identify which Table ID is used on this report. BC may not always be able to determine that information, so you will need to manually input the Table ID for the Data Item that relates to the Customer table. Please refer to your implementing partner if you need more help with this |
| **Report Field Name** | Looks up field names from the **Report Table ID** above. This is the linking field between the Customer/Vendor table, and the report. Please refer to your implementing partner if you need more help with this |
| **Document Option** | Select either Single or Multiple Documents |
| **Email Account Name** | Email Account to be used when dispatching documents as Emails |
| **Body Code** | [Email Body code](#_Email_Body) |
| **Email Option** | Choose if you want to send Single or Multiple attachments per Email |
| **Subject** | Email Subject Line to be used when dispatching documents as Emails. You can create some variables by using the Drill down button to the right of this field. Once you create a variable, you can use them as part of the Subject field. To use these variables, just insert them in the middle of the text. **E.g.:** Invoice for Customer %1, where %1 is a variable |
| **Parameters** | Just for convenience, it lists the variables created using the Drill down button to the right of the Subject Field. See field **Subject** above |

From the Actions ribbon, you can find the following actions:

Table 10‑4: Actions on Document Worksheet Template Card/List

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Template > Batches** | Enables users set up Batches for the current template. This is the same Batch concept as standard BC Journals |
| **Template > Report Parameters** | Enables users to pre-set filters that will be applied prior to running the document report |
| **Template > Permissions** | Explicitly assigns which Permissions have access to this worksheet. Please see [365WineTrade Internal Permission System](#_365WineTrade_Internal_Permission_2) for more details |
| **Functions > Clear Report Parameters** | Clears any pre-set filters on field **Report Parameters** |
| **Functions > Clear Email Account** | Clears the Email Account Name field |
| **Setup > Email Body Setup** | Quick access to setting up [Email Bodies](#_Email_Body) |
| **Setup > Email Report Setup** | Quick access to setting up [Email Reports](#_E-Mail_Reports) |

## 10.6.     Document Worksheet Template Batches

From the Document Worksheet Template, you can access its batches by clicking action **Template**, **Batches**. BC will display the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image100.png)

Figure 10‑7: Document Worksheet Batches

## 10.7.     Using the Document Worksheet

Once everything is set up, you can start using the Document Worksheet. To do so, go to the **365WineTrade** menu, **Document Worksheets**, **Document Worksheet.** You will be taken to the main page of Document Worksheet:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image101.png)

Figure 10‑8: Document Worksheet Page

To start working, you need to select a [Template Name](#_Document_Worksheet_Template) and a [Batch Name](#_Document_Worksheet_Template_1) on the heading part of the page (marked in red above). Some actions are available through the Document Lines actions (marked in blue above). The list marked in green displays all documents that have been generated as a result of action **Suggest Lines**. Suggesting Lines will list all documents that must be sent and will also attach a copy of the final PDF to the **Documents** FactBox (marked in purple above).

The following Document Lines actions are available:

Table 10‑5: Actions on the Document Worksheet Page

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Suggest Lines** | Runs the report associated with the selected Template and inserts one record per customer or vendor, depending on the settings of the Template. The actual PDF file will be stored as an attachment to its corresponding document line and can be accessed from action **View Attachments**, or from the **Documents** FactBox |
| **Send Documents** | Dispatches or prints the documents currently selected. Only documents with a blank **Date Sent** are processed. **Please note**: Printing in batch is currently not available from BC Cloud installations; therefore, documents that need to be printed will not really print, rather than they will remain on the list as placeholders |
| **View Attachments** | Shows up a popup window with all attachments for the currently selected line |
| **Reset Date Sent** | Resets field Date Sent for the lines currently selected so that they can be sent again |
| **Actions > Related Information > Email Addresses** | Displays all the email addresses associated with the currently selected Customer or Vendor |
| **Actions > Related Information > View Account** | Shows the Customer or Vendor Card associated with the current document |

## 10.8.     Document Worksheet Entries

Once documents are successfully sent using the **Send Documents** action, BC will store a copy of all documents that were transmitted in the Document Worksheet Entries history. To find this history, go to the **365WineTrade** menu, **Document Worksheets**, **Document Worksheet Entries**.

Documents also will remain on the original Document Worksheet until they are manually deleted.  

# 11.        Integrations to External Systems

**365WineTrade** has an out-of-the-box integration framework, that provides some elements and guidelines on how external systems should integrate with Business Central. This is not a mandatory framework, rather than just a best practice approach to make sure all your integrations are managed from one place.

This integration framework is composed of the following elements:

·       [**Sites**: Used for listing all the different integrations present in the system. Depending on the structure, you could have one Site for all operations with an external partner, or you could have multiple Sites for the same external partner. What determines how many Sites you’ll have per partner will be the design of the interface.](#_Sites_1)

·       [**Site Communications**: Used for more technical details on each Site, since it will store data such as username and passwords, URLs and other technical information.](#_Site_Communication)

·       [**Site Log**: Used to keep logs on communications established with each Site.](#_Site_Logs)

·       [**Site Order Queue**](#_Site_Order_Queue): This specialty element is used mainly when integrating Sales Order entry from external partners. External Systems may send processing data in an Order layout (with headers and lines), and this element will be the best place to store and process them.

You will find more details about each element, on the upcoming sections.

## 11.1.     Sites

Sites are used to link **365WineTrade** with external partners, such as SLAs, third party carriers, and any other type of partner that can provide integration with Business Central. These integrations are not limited only to API Webservices. Each Site must be set with its own Processing Codeunit ID, and this Processing Codeunit will be the business rule determining how each Site should behave. For more details, please consult with your implementing partner.

To setup Sites, go to menu **365WineTrade**, **Integration**, **Sites**. You will then be taken to the list below:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image102.png)

Figure 11‑1: 365WineTrade Sites

The following fields and actions are available:

Table 11‑1: List of fields for Sites

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Document Group Code** | Determines a document group for this Site |
| **Communication Code** | Determines the [Site Communication](#_Site_Communication) code for Sites that are fully integrated using API communication. Can be left blank for Sites that do not require further parameters |
| **Processing Codeunit** | Determines the Codeunit ID that will be handling processing for this Site. This Codeunit will be the main business rule driver for each site |
| **Allow Order Line Update** | Used in connection with Site Order Queues. This allows for edition directly on the Site Order Queue lines subpage |

Table 11‑2: List of actions for Sites

|     |     |
| --- | --- |
| **Action** | **Purpose** |
| **Run** | This is a generic function that can be used with custom interfaces. **Please note**: This action will not run for out-of-the-box codeunits and it will display an error message. |
| **Templates** | For future use |
| **Cross References** | This is a generic cross reference table that can be used with custom interfaces. This setup does not apply to any out-of-the-box processes |
| **Log** | Shows a history for every time the automated process ran |

## 11.2.     Site Communication

Site Communications are used for automated sites using API integrations. These integrations can be done using Webservices, or it can also integrate with Microsoft® Azure® Logic Apps. For more details on Logic Apps, please visit [https://azure.microsoft.com/en-us/services/logic-apps/](https://azure.microsoft.com/en-us/services/logic-apps/).

To set up these communications, go to the **365WineTrade** menu, **Integration**, **Site Communications**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image103.png)

Figure 11‑2: List of Site Communications

Table 11‑3: List of fields for Site Communications

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Communication Type** | Choose between blank, **Logic Apps** or **Website**.<br><br>**Please note**: Any integrations with Logic Apps must be custom developed. Most integrations with Webservices, other than NY SLA licensing Webservices, must be custom developed as well |
| **URL** | Determines the URL for the Webservice or Logic App |
| **Method** | Choose between GET, POST and PUT. It depends on the communication type and on the interface design |
| **App Token** | Reserved for future use |

### 11.2.1. Site Communication Parameters

For each [Site Communication](#_Site_Communication) record, you can determine additional parameters that can be passed to the Webservices or Logic Apps. To set them up, select a **Site Communication** record, then click on action **Parameters** from the **Actions** ribbon. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image104.png)

Figure 11‑3: Site Communication Parameters

Table 11‑4: Site Communication Fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Type** | Available types are:<br><br>·       Blank<br><br>·       Content-Type<br><br>·       Accept<br><br>·       User-Agent<br><br>·       Get File List<br><br>·       Get Files with Path<br><br>·       Get Files<br><br>·       Send Files<br><br>·       Custom Parameter |
| **Parameter** | Determines the name of the parameter |
| **Value** | Determines the value of the parameter |

## 11.3.     Site Logs

Each interaction with an automated [Site](#_Sites_1) will generate an entry on the Site Logs page. These logs are used for debugging purposes, but they can also be used for auditing purposes.

You can find the Site Logs page under the **365WineTrade** menu, **Integration**, **Site Log**. You are then taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image105.png)

Figure 11‑4: Site Log List

Table 11‑5: Site Log fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Request** | Determines if there’s a log for the Request that was made. If this reads Yes, you can drill down on it in order to download a file with the contents of the Request. This could be a JSON file, an XML file, or something similar |
| **Response** | Determines if there’s a log for the Response that was made. If this reads “Yes”, you can drill down on it in order to download a file with the contents of the Response. The type of this response can be easily determined by field **Response Type** below |
| **Response Type** | Determines the type of response that is stored on the Response field |
| **Status Code** | Code for status. This is determined per interface, but it’s usually a best practice to follow HTTP status codes |
| **Status Description** | Description for the **Status Code** above |
| **Date** | Date when the request and response were logged |
| **User Id** | User ID that triggered this request and response |

 

## 11.4.     Site Order Queue

If the current site relates to an interface that integrates Sales Orders, then the Site Order Queue will be the transitory place where Sales Orders will be imported to before they’re turned into real Sales Orders.

To see a list of all pending orders, you can go to the **365WineTrade** menu, **Integration**, **Site Order Queue**. You will then be taken to the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image106.png)

Figure 11‑5: Site Order Queue List

On this page, you can find the actions ribbon at the very top, followed by Order Headers (marked in red), followed by Order Lines (marked in blue).

All interfaces that are designed to work with this part of the Integrations framework, will import prospect Sales Orders into this area. From this page, you can give standard Business Central maintenance, using actions Edit List and Delete. You can also edit the lines, if needed, and if the Site has flag Allow Order Line Update enabled (for more details, refer to section [Sites](#_Sites_1) above).

When everything is good with a Sales Order, you can try to transform it into a real Sales Order using action **Create Sales Order(s)** on the actions ribbon. If everything is processed Ok, field **Date Created** will be populated with today’s date. If the order is not processed correctly, then fields **Error** and **Error Message** will tell you the reason there were issues.

**Please note**: The whole behavior for this depends on the interface design along with the rules programmed on the Processing Codeunit for the Site. Some interfaces may be designed to run completely manually, and may never try to create Sales Orders automatically, whereas some other interfaces may be designed to run fully automated with less manual intervention as possible. All these variables will be defined by the Functional and Technical consultant designing each interface that is needed.

  

# 12.        sam

## 12.1.     Bill & Hold Agreements

In some states and markets, Bill & Hold is a practice that allows distributors to sell goods to a customer, get paid for it, but not to have them shipped right away, most likely due to storage restrictions on the customer side. The party offering Bill & Hold arrangements, usually has a time limit on how long they store goods for, and sometimes, they can also charge storage fees from their customer.

**365WineTrade** supports the following aspects Bill & Hold arrangements:

·       Selling goods to a customer, on a Bill & Hold arrangement

·       Shipping goods that have been sold under a Bill & Hold arrangement

·       Keep track of expiration dates on Bill & Hold operations

·       Credit memos for all steps on the operation.

At this moment, **365WineTrade** does not offer an automated option to generate Bill & Hold Storage Fee invoices.

### 12.1.1. Bill & Hold Process

Bill & Hold inventory is held into regular BC locations. These locations are “virtual” locations, per physical location (eg. EAST-BH is the B&H location for location EAST). These “virtual” locations must have the setting **Bin Mandatory** enabled. Each customer under a Bill & Hold agreement is represented by bins on these “virtual” locations.

When a Bill & Hold Sales Order is processed, items are shipped out of the regular location. Then, the same items are brought back to these Virtual locations, via Item Journals. The bin codes where these items are put into, are the **Bill and Hold Bin Code** determined on each customer card.

This is the visualization of how goods flow from a regular location to a Bill & Hold location:

![A picture containing timeline
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image107.png)

Figure 12‑1: Bill & Hold flow of goods

Lastly, when items are brought back to the Bill & Hold Location, BC will also set field **Bill & Hold Expiration Date** on the Item Ledger Entries, following the Expiration Date formula defined on the card for the Bill & Hold location. This way, you will be able to keep track (through BC Filters and Views) of items that are expiring soon, or that are already expired on the Bill & Hold Location.

**Please note**: No report is provided for controlling expiration dates; BC does not issue any type of notification regarding items that are about to expire, or that had already expired, on the Bill & Hold Location; editing the expiration date is not possible.

Lastly, when entering regular Sales Orders for a customer that has Bill & Hold inventory, BC will warn the users.

### 12.1.2. Bill & Hold Setup

In order to setup Bill & Hold Arrangements, you will need the following setups in the system:

·       **B&H Virtual Location**: You will need a new virtual location to hold Bill & Hold inventory. This Location must be marked as **Bin Mandatory** = True, and it must be marked as a **Bill & Hold Location** = True. Optionally, you can setup the **Bill & Hold Expiration Date Calculation** formula.

o   Each customer that you have Bill & Hold agreements with, must be set as a **Bin Code** under this location. The **Bin Code** must match the **Customer Code**.

·       **Regular Inventory Location**: On your regular inventory location, you will need to indicate what is the Virtual Bill & Hold Location, by setting field **Bill & Hold Location Code**.

·       **Customer**: On each customer that you have a Bill & Hold agreement with, you will need to setup their Bill and Hold Bin Code (under the [365WineTrade FastTab](#_365WineTrade_FastTab_1))

·       **Order Types**: You will need to add the following [Order Types](#_State_Liquor_Authority) to your system:

o   **BH-SALES**

§  Bill and Hold Type = Sales

§  Location Code = regular inventory location code

§  Purpose: to be used when selling goods to a customer, under a Bill & Hold agreement

o   **BH-SHIP**

§  Bill and Hold Type = Shipment

§  Location Code = Bill & Hold Location Code

§  Purpose: to be used when shipping good that were sold to a Bill & Hold Location

o   **BH-REVERSE**

§  Bill and Hold Type = Sales

§  Purpose: to be used for Credit Memos from the Bill & Hold location to the regular location

o   **BH-RET-BH**

§  Bill and Hold Type = blank

§  Purpose: to be used for Credit Memos when goods were sold under Bill & Hold agreement, and the customer wants to ship them back to their Bill & Hold storage. On this scenario, customers will still want the product, but at a future date

o   **BH-RET-PHYS**

§  Bill and Hold Type = blank

§  Purpose: to be used for Credit Memos when goods were sold under Bill & Hold agreement, but they will return to the regular inventory location. On this scenario, customers will no longer want the product

The diagram below illustrates the different Order Types:

![Diagram
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image108.png)

Figure 12‑2: Bill & Hold Order Types

### 12.1.3. Bill & Hold Order Processing

To process Bill & Hold orders, please follow these short guidelines:

#### Selling to a Bill & Hold Location (Invoice #1)

Start a new Sales Order, select your customer, and make sure to select **Order Type = BH-SALES**. Enter your items and quantities, proceed with releasing, shipping, and invoicing.

Goods will be sold as a regular Sales Invoice, that will generate COGS and Accounts Receivable. Goods will also be put back into the Bill & Hold virtual location, with cost zero.

#### Shipping from a Bill & Hold Location (Invoice #2)

Start a new Sales Order, select your customer, and make sure to select **Order Type = BH-SHIP**. Use function “Select Bill & Hold Items…” on the Lines subform. This will help you pick items from the Bill & Hold Location:

![Graphical user interface, text, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image109.png)

Figure 12‑3: Select Bill and Hold Items from the Sales Line functions

Alternatively, you can enter Item Nos. manually. Proceed with releasing, shipping, and invoicing.

Goods will be sold with Zero cost and Zero price. BC will generate Ledger Entries for this transaction, but they should net to zero, with a zero accounts-receivable as well.

#### Credit Memo: Reversing a Bill & Hold Sales

Start a new Credit Memo/Return Order, use function Copy Document, to copy the Posted Sales Invoice for the original sale ([Invoice #1](#_Selling_to_a)). Make sure Location Code = regular inventory location. Set Order Type = BH-REVERSE. Make sure this document has prices and costs associated with it. Proceed with releasing, receiving, and invoicing.

Goods will be taken out from the Bill & Hold Location, with zero cost and price. Goods will be put back into the regular inventory location, and it will generate a reversing COGS and Accounts Receivable.

#### Credit Memo: Reversing a Bill & Hold Shipment, bringing goods back to Bill & Hold Location

Start a new Credit Memo/Return Order, use function Copy Document, to copy the invoice that was used to SHIP the goods ([Invoice #2](#_Shipping_from_a)). Change **Order Type** to **BH-RET-BH**. Adjust quantities if it is a partial return. Proceed with releasing, receiving, and invoicing.

Goods will be brought back into the Bill & Hold location, with Zero Price and Zero Cost.

#### Credit Memo: Reversing a Bill & Hold Shipment, bringing goods back to regular inventory Location

Start a new Credit Memo/Return Order, use function Copy Document, to copy the invoice that was used to SELL the goods ([Invoice #1](#_Selling_to_a)). Change **Order Type** to **BH-RET-PHYS**. Adjust quantities if it is a partial return. Proceed with releasing, receiving, and invoicing.

Goods will be brought back into the Bill & Hold location, with price and cost associated with it.

## 12.2.     Salesperson Location

**365WineTrade** offers the option of tracking inventory shipped to a Salesperson, so that managers do not lose visibility of how much stock a salesperson may be keeping on their remote location.

To setup this feature, you need a dedicated virtual Location, with option **Bin Mandatory** enabled. Each Salesperson will be setup as a Bin in this location. This location will also have a special flag (**Salesperson Location**) enabled:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image110.png)

Figure 12‑4: Salesperson Location flag on the Location Card

You also need to setup each salesperson as a customer, and on their customer card, you need to indicate their Salesperson Location code and Salesperson Bin code:

![Chart
Description automatically generated with medium confidence](365WineTrade_Users%20Guide%20-%20Base.fld/image111.png)

Figure 12‑5: Salesperson Location fields on the Customer Card

Once these setups are done, all sales orders shipped to this customer will generate a positive adjustment entry on the Salesperson Location code:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image112.png)

Figure 12‑6: Item Ledger Entry of a Sales Order Shipped to a Salesperson

On the screenshot above, the 1st entry shows the original BC shipment, that depletes inventory. The 2nd entry shows the Salesperson Location entry, showing the positive adjustment, bringing those quantities back into the Salesperson location.

If these goods need to be invoiced to another customer at some point, and the salesperson will be responsible for delivering them, the salesperson can enter a regular Sales Order, using his Location and Bin Code for issuing the order.

Lastly, the best way to see all quantities on the Salesperson Location, per Salesperson, is to view the standard Bin Contents page (search for term “Bin Contents”):

![Graphical user interface, text, application, email
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image113.png)

Figure 12‑7: The Bin Contents page showing the salesperson inventory for fictitious rep Benjamin Chiu

## 12.3.     Sample Management Setup

**365WineTrade** comes with a Sample Management system that allows users to track Salesrep Sample Budget amounts vs. Realized amounts.

The basic setup can be found under the **365WineTrade** menu, **Setup**, **Sample Management Setup**. You will be taken to the following page:

![Graphical user interface, application, table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image114.png)

Figure 12‑8: Sample Management Setup

Table 12‑1: List of fields for Sample Management Setup

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Budget Item No.** | Dummy Item No. that will be used to hold Budget information on the standard Sales Budget setup in Business Central. This item must be Blocked in order to be used on this setup |
| **Sample Amount Type** | Determines if Sample Amounts will be tracked by Item Price or Item Cost |
| **Sample Reason Codes** | Provides a list of Sample Reason Codes that will be entered on every Sample Sales Line. |
| **Do Not Ship to Salesperson Location** | Determines that if Samples are being shipped to a Salesperson, that it should not trigger the [Salesperson Location](#_Salesperson_Location_2) tracking feature. This would apply for personal purchases that do not require tracking |
| **Exclude from Sample Budget** | Determines that Samples invoiced with this code will not be included in the amount Realized that is used for comparison with the Budget |

### 12.3.1. Setting Up Sample Budget

To setup Sample Budgets, you will use BC’s Sales Budgets functionality. You can find the Sales Budgets from the Search Bar:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image115.png)

Figure 12‑9: Searching for Sales Budgets

Once you open it, you need to select an existing budget, or create a new one, and click on action Edit Budget:

![Graphical user interface, application, table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image116.png)

Figure 12‑10: List of Sales Budgets

Once in the Budget page, these will be the ideal filters you need to set:

·       FastTab General:

o   **Show as Lines**: Customer

o   **Show as Columns**: Period

o   **Show Value as**: Sales Amount or Cost Amount, depending on what your budget is going to be based on. This has to follow what you setup on the [Sample Management Setup](#_Sample_Management_Setup_1)

o   **View by**: Month

·       FastTab Filters:

o   **Customer Filter**: A filter for all Salespeople Customer Nos.

o   **Item Filter**: **Budget Item No.** defined on the [Sample Management Setup](#_Sample_Management_Setup_1)

§  If this filter is missing, BC will not be able to find estimated budget correcly

You should end up with a page set like this, where you can enter the Sample Budget amounts per Salesperson, directly on the Matrix:

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image117.png)

Figure 12‑11: Sample Budget overview

![Graphical user interface, application
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image118.png)

Figure 12‑12: Sample Budget, FastTab Filters showing how to filter on Customers, and most importantly, on the Budget Item No.

### 12.3.2. Sample Sales Orders Budget Check

When entering a sales order for a Salesrep, you may choose to ship some lines as samples, by setting field Sample Reason Code:

![Table
Description automatically generated](365WineTrade_Users%20Guide%20-%20Base.fld/image119.png)

Figure 12‑13: Fields Sample Reason Code and Line Discount % on Sales Lines

When you fill out a **Sample Reason Code**, BC will automatically fill out the **Line Discount %** to 100%. This cannot be edited.

At this moment, BC will also determine the sample amount for that line, and it will check if the total sample amount for the period has not been reached. For this comparison, BC will gather the following figures:

·       Sample Budget: Sum of all Item Budget Entries setup on Sales Budgets

·       Sample Amount Realized: Sum of Posted Invoices + Credit Memos + Released Sample Sales Lines + Current SO Sample Sales Lines

If the Amount Realized is greater than the Amount Budgeted, then BC may throw an [Order Review Types](#_Order_Review_Types) if this is setup, so that users can take actions if the Salesperson has gone over their allowance.

## 12.4.     Data Processing

When implementing a new installation of Business Central with (or without) **365WineTrade**, it is customary to use the Configuration Packages module for data migration. Some data, however, cannot be handled out-of-the-box, and that’s when the Data Processing tasks come in handy.

In this current version, there’s only one Data Processing Task available. This feature may be expanded in the future if new special tasks are needed. Developers are also encouraged to extend this functionality for any Data Processing needs that can’t be processed by regular Configuration Packages.

To access Data Processing tasks, go to the **365WineTrade** menu, **Setup**, **Data Processing**. You will be taken to the following list:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image120.png)

Figure 12‑14: List of Data Processing tasks for the version 1.0.0.2

### 12.4.1. Import Customer Delivery Instructions

This Data Processing task is used to import Delivery Instructions into Customer Cards and Customer Ship-to Addresses Cards. Programmatically, these fields are of type BLOB that cannot be imported or exported using Configuration Packages, therefore the need for having them imported using a special Data Processing task.

To run this Data Processing task, select it from the list, then click the **Actions** ribbon, then **Run**.

BC will display a processing report. Under FastTab **General**, you can select if you want to Import or Export Template. We suggest you run Export Template first, which will generate a Microsoft® Excel file with 3 columns:

·       Customer No.

·       Ship-to Address Code

·       Delivery Instructions

Once you fill out this template, then you can save the file and Import it using the same task.

  

 

# 13.        365WineTrade Internal Permission System

Due to the nature on how documents are managed in **365WineTrade**, system administrators cannot rely 100% on standard BC Permissions in order to grant or deny access to documents, as this setup is usually restrictive of ALL data. Administrators cannot easily choose selectively which records to grant or deny access to.

**365WineTrade** internal permission system offers system administrators a finer level of setup: They can define visibility permissions per [Document Group](#_Document_Groups_1).

To start setting up these permissions, you can use the search bar to look for **Document Groups**. On each Document Group, you can see how many Permissions are assigned to it, by looking at column Permissions:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image121.png)

Figure 13‑1: Document Group permissions

To set up Permissions, you can either click on **Permissions** on the Actions ribbon, or you can drill down into the **Permissions** column. You will then be taken to the following page:

![](365WineTrade_Users%20Guide%20-%20Base.fld/image122.png)

Figure 13‑2: Wine Permissions

From this page you can set up which users, profiles, permission sets and/or user groups have access to the current document group.

Table 13‑1: Wine Permissions fields

|     |     |
| --- | --- |
| **Field** | **Purpose** |
| **Type** | You can choose from: **Profile**, **Permission Set**, **User Group**, **User**. These are all standard BC security entities |
| **Read** | Specifies that you can delete documents for the selected [Document Group](#_Document_Groups_1) |
| **Update** | Specifies that you can update documents for the selected [Document Group](#_Document_Groups_1) |
