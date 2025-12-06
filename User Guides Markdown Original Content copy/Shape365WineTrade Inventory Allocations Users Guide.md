_Microsoft Dynamics__®_ _365 Business Central_ 

![Shape](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image003.png)365WineTrade Inventory Allocations  
Users Guide 

Last Update: July 10, 2024

  

**Change Log:** 

|     |     |     |
| --- | --- | --- |
| **Date** | **Name** | **Description** |
| 2/26/2024 | Maurice Tisseur | After some additional testing of the Allocation automated expiry feature, this guide was updated to correctly reflect what the system reaction will be. The changes are limited to Page 18 of this document. |
| 7/10/2024 | Maurice Tisseur | Section 4.1 Allocation Journals was updated to include further clarification on the Transaction Types “Taken”. These are used by the system exclusively and not available to be used in an Allocation Journal. |
|     |     |     |
|     |     |     |
|     |     |     |

  

Table of Contents

[1. Introduction. 4](#_Toc171692055)

[2. Dependencies and Assumptions 4](#_Toc171692056)

[3. Setups 5](#_Toc171692057)

[3.1. Allocation Setup. 5](#_Toc171692058)

[3.1.1. Automatic Reservation Setup. 6](#_Toc171692059)

[3.2. Master Data Setup. 7](#_Toc171692060)

[3.2.1. Item Allocation Setup. 8](#_Toc171692061)

[3.2.2. Customer Allocation Setup. 9](#_Toc171692062)

[3.2.3. Other Allocation Setups 9](#_Toc171692063)

[3.3. Allocation Code and List 10](#_Toc171692064)

[3.3.1. Master Data Specific Allocation Card. 11](#_Toc171692065)

[3.3.2. Allocation Card Based on Filters. 12](#_Toc171692066)

[3.3.3. Wildcard Allocation Cards 13](#_Toc171692067)

[3.3.4. Unspecified Allocation Cards (Open Pools) 14](#_Toc171692068)

[3.4. Inheritance Path. 15](#_Toc171692069)

[3.5. Allocation Journal Batches. 17](#_Toc171692070)

[4. Transactions. 19](#_Toc171692071)

[4.1. Allocation Journals 19](#_Toc171692072)

[4.1.1. Allocations vs. Reservations 19](#_Toc171692073)

[4.1.2. Reservation System Integration. 21](#_Toc171692074)

[4.2. Sales Line Allocation Entries. 21](#_Toc171692075)

[4.3. Sales Line Reviews. 22](#_Toc171692076)

[4.4. Allocation Ledger Entries. 23](#_Toc171692077)

[4.5. Allocation Report 23](#_Toc171692078)

  

# 1.   Introduction

The **365WineTrade** add-on for Business Central is designed to add specific features to support the challenges of wines and spirits manufacturers and distributors.

The **365WineTrade Inventory Allocations** add-on provides extended functionality for allocating items, that is not native to Business Central. These are the key features of this extension:

·       Multiple Allocation Source: Users are able to allocate quantities (on hand or not), for the following records in the system:

o   Customers

o   Sales Regions, States and Countries

o   Salespersons

o   Gen. Business Posting Groups and Customer Posting Groups

o   Customer Price Groups

o   Vendors and Brands

·       Multiple Allocation Paths: Users are able to determine different ways to consume allocations, depending on the customer, or on them item

·       Allocation Journal: Users have an easy way of recording new allocations, or giving maintenance to current allocations, through the use of an Allocation Journal

·       Allocation Consumption Tracing: Users are able to track which sales orders consumed from which allocations

·       Mandatory Allocations: Users have the option of setting up items that require allocation

·       Integration with BC Reservation Entries: Users have the option of enable an integration with the Reservation Entry system, so that each Allocation Entry is supported by an existing Quantity on Hand. This ensures that allocations represent real quantity on hands, which is more applicable for Wine and Spirits Distributors

·       Automatic expiration of allocations

·       Automatic blocking of certain types of Business Central reservations

# 2.   Dependencies and Assumptions

The minimum required version of BC for this version of **365WineTrade**, is v18, also known as Business Central 2021 release Wave 1.

This documentation assumes that users are familiar with Business Central’s basic navigation capabilities such as creating/viewing/editing/deleting records, filtering, and sorting, as well as executing functions from the Actions and Navigate ribbons.

This documentation also assumes that users are familiar with their respective modules and functionalities, such as entering Sales Orders, entering Purchase Orders, processing Payment/Receipt/General Journals, etc.

  

# 3.   Setups

## 3.1.        Allocation Setup

The general Allocation Setup can be found under menu **365WineTrade**, **Inventory Allocations**, **Allocation Setup**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image004.png)

Figure 3‑1: Allocation Setup, FastTabs General and Automatic Reservation Setup

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image005.png)

Figure 3‑2: Allocation Setup, Allocation Source FastTab

Table 3‑1: Allocation Setup Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Default Inheritance Code** | Defines the standard path that will be used to consume allocations. For more details, refer to section [Inheritance Path](#_Inheritance_Path_1) |
| **Inheritance Code Precedence** | Determines if the system should pick the Inheritance Code setup on the Customer Card or on the Item Card in case both have Inheritance Codes. For more details, refer to section [Inheritance Path](#_Inheritance_Path_1) |
| **Default Allocation Reservation Integration** | Determines if Allocation entries must have a supporting Reservation Entry when allocations are created from the Allocation Journals<br><br>**Disabled** – Users cannot use the reservation system<br><br>**Mandatory** – Users must reserve quantities prior to posting Allocation Journal Entries<br><br>For more details, refer to section [Reservation System Integration](#_Reservation_System_Integration_1) |
| **Expiration Job Queue Frequency** | Determines if there will be a Job Queue running to automatically expire Allocation Entries or not. Options are either **Never**, or **Daily** |
| **Expiration Journal Batch** | Allocation Journal Batch to be used when allocation entries are to be expired |
| **Allocation Source** | Determines prefixes to be used on allocation codes when they are automatically created from each master data |
| **Automatic Reservation Setup** | Determines which combinations of automatic reservations are allowed or not. Refer to section [Automatic Reservation Setup](#_Automatic_Reservation_Setup) below |

### 3.1.1.     Automatic Reservation Setup

When items and/or customers are setup to Always reserve quantities in standard BC, there is no out-of-box way of preventing certain automatic reservations from being done, such as, reserving Sales Order from a Purchase Order, or from a Transfer Order. With this, it becomes a challenge to use the standard reservation system, when users need to ensure all the time, that a sales lines did not get automatically reserved from a supply document that is not currently received in the system.

With **365WineTrade Inventory Allocations**, you can prevent these reservations from happening automatically.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image006.png)

Figure 3‑3: Automatic Reservation Setup

Table 3‑2: Automatic Reservation Setup Fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Reserve From** | Determines the Table Id whose reservation should be restricted from. Common values are:<br><br>39 – Purchase Lines<br><br>5741 – Transfer Lines |
| **Reserve For** | Determines the Table Id whose reservation should be restricted for. Common value is:<br><br>37 – Sales Line |
| **Allowed** | Determines if the reservation combination is allowed or not. Values are:<br><br>Yes – Standard BC behavior<br><br>Yes with Message – If an automatic reservation is done for such combination, warn the user with a message<br><br>No – If an automatic reservation is done for such combination, BC will delete it and throw an error message |
| **Message** | Message to be used with option “Yes with Message” from above |

**Note**: If the company is using strict date handling on both purchase receiving and sales shipment sides, BC will handle this out-of-box by comparing the Expected Receipt Date on the Purchase Document vs. the Shipment Date on the Sales Document.

## 3.2.        Master Data Setup

**365WineTrade Inventory Allocations** offer a centralized view called Master Data Setup, that shows all the system records that need and can be allocated. To access the Master Data Setup, you can go to menu **365WineTrade**, **Inventory Allocations**, **Allocation Master Data Setup:**

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image007.png)

Figure 3‑4: Allocation Master Data Setup page

Each one of these options will take the user to a specialized page that will display only allocation-related fields. For example, the Item Allocation Setup will show the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image008.png)

Figure 3‑5: Item Allocation Setup list

### 3.2.1.     Item Allocation Setup

In order to allocate Items, they need to be individually setup. You can setup which items to allocate, from the **Item Allocation Setup**, inside the **Master Data Setup**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image008.png)

Figure 3‑6: Item Allocation Setup list

Table 3‑3: Item Allocation Setup fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Allocate** | Determines if the item can be allocated or not. This setting is required for all items that require allocation |
| **Allocation is Current** | This field is just for information and does not carry any intelligence. Users can use this field to identify which allocations are still valid in the system, for reporting purposes only, for example. |
| **Allocation Reservation Integration** | Overrides the general [Allocation Setup](#_Allocation_Setup) option, if the value is not **System Default** |
| **Full Allocation Required** | Prevents items from being placed on a Sales Order if there’s not enough automatic allocations to be consumed for the requested quantity. **Please note**: You should only use this option for items that are critical, that you do not want any manual shuffling of allocations. This option will not let users pick manual allocation codes on Sales Order level. |
| **Allocation Inheritance Code** | Determines the [Inheritance Path](#_Inheritance_Path_1) to be used when looking for allocations for this item |

### 3.2.2.     Customer Allocation Setup

If you want to use allocation per specific customers, you need to set them up, from the **Customer Allocation Setup**, inside the **Master Data Setup**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image009.png)

Figure 3‑7: Customer Allocation Setup list

Table 3‑4: Customer Allocation Setup fields

|     |     |
| --- | --- |
| **Field** | **Description** |
| **Allocate** | Determines if the customer will be allocated or not. This setting is not mandatory per customer, as you may create different types of [Allocation Codes](#_Allocation_Code_and) |
| **Allocation Code** | Determines the [Allocation Code](#_Inheritance_Path) for this customer. When clicking field Allocate, BC will determine the Allocation Code automatically based on the [Allocation Source](#AllocationSource) setup and the Customer No. |
| **Allocation Inheritance Code** | Determines the [Inheritance Path](#_Inheritance_Path_1) to be used when looking for allocations for this customer |

### 3.2.3.     Other Allocation Setups

As mentioned previously, **365WineTrade Inventory Allocations** allows for allocations to be done by the following entities:

·       Sales Regions, States and Countries

·       Salespersons

·       Gen. Business Posting Groups and Customer Posting Groups

·       Customer Price Groups

·       Vendors and Brands

To setup allocation per each one of these entities, you can do so from the **Master Data Setup** page. Their setup fields follow very closely the [Customer Allocation Setup](#_Customer_Allocation_Setup) fields.

## 3.3.        Allocation Code and List

In **365WineTrade Inventory Allocations**, an Allocation Code is the main record that will hold allocated quantities against it. For example, an Allocation Code can be for a Customer, a Vendor, a Brand, a Salesperson, a group of Salespeople, one or more states, or even, a generic pool.

There are 4 types of Allocations Codes:

·       **Master Data Specific**: Allocation codes that represent exactly 1 master data in the system. E.g.: Allocation Code for a specific Customer.

·       **Based on Filters**: Allocation codes that represent 1 or more master data in the system, based on filters. E.g.: Allocation Code for NY-Tri-State area (comprised by NY, NJ, and CT).

·       **Wildcard Allocation Codes**: Allocation codes that do not hold allocation quantities itself, but when put into an [Inheritance Path](#_Inheritance_Path), will be used to search for similar Allocation Codes. E.g.: Allocation Code for Sales Reps

·       **Unspecified Allocations Codes**: Allocation codes that are not linked to any specific master data. They can be either consumed using an Inheritance Path, or they can be manually consumed on the [Sales Order Allocation Entries](#_Sales_Line_Allocation).

These are the Master Data entities that you can allocate items against:

·       Customers

·       Sales Regions, States and Countries

·       Salespersons

·       Gen. Business Posting Groups and Customer Posting Groups

·       Customer Price Groups

·       Vendors and Brands

To access the Allocation List, you can go to menu **365WineTrade**, **Inventory Allocations**, **Allocation List:**

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image010.png)

Figure 3‑8: Allocation List

From this list you can see details for each Allocation Code, such as:

·       Which master data is this allocation linked to (via fields **Source**, **Based On-Type** and **Based On-Criteria**)

·       Allocation totals (via fields **Total Allocated**, **Allocated Qty Remaining**, **Total Taken**, **Total on Sales Orders**)

·       Allocation subtotals per item (via **Actions** Ribbon > **Allocation Subtotals**)

·       Allocation Ledger Entries (via **Actions** Ribbon > **Ledger Entries**)

An Allocation Code card looks like the picture below:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image011.png)

Figure 3‑9: Allocation Code card

Each field will be described with details on the following sub-sections.

### 3.3.1.     Master Data Specific Allocation Card

This type of Allocation Card defines 1 unique Master Data in the system, and it is the most common type of allocation card. This is also the type of allocation card that is created automatically when you choose to Allocate it from the [Master Data Setup](#_Master_Data_Setup).

Common examples for this type of allocation cards are Allocations for specific Customers, Allocations for specific Salespeople, Allocation for specific States.

Figure 3‑10: Master Data Specific Allocation card for a Customer

For an allocation card to be considered a Master Data Specific, it must have the following values:

·       Source: **Not blank**

·       Based On-Type: **No.**

·       Based On-Criteria: **Not blank**

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image012.png)

**Please note**: Field **Applies-to** is only applicable for Sources State and Country.

### 3.3.2.     Allocation Card Based on Filters

This type of Allocation Card defines 1 or more Master Data in the system, based on filters.

Common examples for this type of allocation cards are Allocations for a group of States, or a group of Gen. Business Posting Groups / Customer Posting Groups.

![Graphical user interface
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image013.png)

Figure 3‑11: Allocation Card Based on Filters for a group of states

For an allocation card to be considered Based on Filters, it must have the following values:

·       Source: **Not blank**

·       Based On-Type: **Filter**

·       Based On-Criteria: **Not blank**

**Please note**: Field **Applies-to** is only applicable for Sources State and Country. Note on the example above that this allocation card applies-to the Ship-to Address. This means that when looking for allocations to deplete, BC will only use this allocation code, if the Sales Order Ship-to State falls within this filter.

### 3.3.3.     Wildcard Allocation Cards

This type of Allocation Card is mainly used with Inheritance Paths. Usually, quantities are never allocated against this type of allocation card. Instead, Wildcard Allocation codes will be put into an Inheritance Path to search for multiple allocation cards that may satisfy an allocation request.

Common examples for this type of allocation cards are Allocations for any Salesperson, or Allocations for any Salespeople.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image014.png)

Figure 3‑12: Wildcard Allocation Card for Salesreps

For an allocation card to be considered a Wildcard Allocation, it must the following values:

·       Source: **Not blank**

·       Based On-Type: **Blank**

·       Based On-Criteria: **Blank**

#### Wildcard Allocation Example

Consider the following allocation cards:

1 Allocation Card for Salesperson JO – Jim Olive

1 Allocation Card for Salesperson BC – Benjamin Chiu

1 Allocation Card for Salesperson HR – Helena Ray

If you do not use a Wildcard Allocation card, when you setup the [Inheritance Path](#_Inheritance_Path_1) to consume allocations from these salespeople, you would need to set it up as follows:

![Chart
Description automatically generated with low confidence](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image015.png)

Figure 3‑13: Inheritance Path with Salesperson Specific Allocation Codes

In the event a new salesperson is setup in the system, they would need to be manually added to the Inheritance Sequence; if they are not added, their allocations will never be automatically consumed.

If you use a Wildcard Allocation card instead, the process is simplified. Your Inheritance Path will look as follows:

![Waterfall chart
Description automatically generated with medium confidence](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image016.png)

Figure 3‑14: Inheritance Path with a Wildcard Allocation Code

Whenever a new salesperson is setup in the system, their Allocation Code does not need to be added to the Inheritance Path, as the Wildcard Allocation SALESREPS will automatically look for their allocation card if the Salesperson Code on the Sales Order matches their Salesperson Code.

Wildcards can be used for any type of source. Customer Wildcards are not needed, as BC will always look for Customer Allocations first, no matter the inheritance path.

### 3.3.4.     Unspecified Allocation Cards (Open Pools)

Unspecified Allocation Cards (also known as Open Pools) are to be used as a big catch-all situation, in case no other allocation cards could be consumed, and they are usually setup as the last allocation code in an [Inheritance Path](#_Inheritance_Path_1).

The most common scenario for using Open Pools is when you do not want to allocate specific items to specific master data, but still, you want to have some level of control over unclaimed quantity on hand.

When you use Open Pools, you must manually allocate quantities against it, as new quantities are purchased in the system. BC does not have the ability of automatic allocating new quantities to existing open pools. This can be useful in situations where you do not want to sell new inventory right away without properly allocating them against your customers, salespeople, etc. Using an Open Pool will ensure that somebody allocated open quantities correctly before they’re placed into sales orders.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image017.png)

Figure 3‑15: Unspecified Allocation Card (Open Pool)

For an allocation card to be considered Unspecified, or Open Pool, it must have the following values:

·       Source: **Blank**

·       Based On-Type: **Blank**

·       Based On-Criteria: **Blank**

## 3.4.        Inheritance Path

In **365WineTrade Inventory Allocations**, Inheritance Paths determine in which order allocations will be searched for, when an allocated item is entered into a sales order.

After setting up Allocation Codes, you will need to determine at least one Inheritance Path so that BC knows in which order to look for allocations. If no default Inheritance Paths are setup, then BC will only look for [Customer Allocations](#_Master_Data_Specific).

This is especially useful when you have Allocation Codes that may overlap based on different Master Data entities.

Consider the scenario below:

**1 Allocation Code for Tri-State Area of New York (NY, NJ and CT)**:

·       Allocating **36 bottles** of item FR-ALH-02-18 – Ma Vin 2018.

**1 Allocation Code for Salesperson JO** – Jim Olive

·       Allocation **60 bottles** of item FR-ALH-02-18 – Ma Vin 2018

Also, consider that Customer **10000 – Wines of New Zealand**, is **located** in **NY** State, and its **Salesperson** is **Jim Olive**.

**Question**: When entering a sales order for customer Wines of New Zealand, for 12 bottles of item FR-ALH-02-18 – Ma Vin 2018, which allocation code should be depleted: The Tri-State Area allocation, or the Salesperson allocation?

The answer for this will be determined with an Inheritance Path. You can setup an inheritance Path that will consume the Tri-State allocations first, and then it will consume the Salesperson allocations next; or vice-versa.

You can find the Allocation Inheritance Codes List under menu **365WineTrade**, **Inventory Allocations**, **Allocation Inheritance Codes List**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image018.png)

Figure 3‑16: The Allocation Inheritance Codes List

The **Inheritance Sequence** on the Actions Ribbon will give you a detailed list of how allocations are to be searched for.

In the example scenario above, if we wanted BC to first deplete Jim’s allocation, and then the NY-Tristate Area allocation, we can define the **Inheritance Path** with the following **Inheritance Sequence**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image019.png)

Figure 3‑17: Allocation Inheritance Sequence for SALESREPFIRST

BC will search allocation codes using the Sequence field, from lower to higher. This field has to be input manually when setting up sequences, and it’s advised you enter ranges in 100’s, so that you can insert allocation codes in between 2 other allocation codes, if needed.

If we wanted BC to actually deplete the NY Tristate allocations first, then we can setup the Inheritance Sequence as follows:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image020.png)

Figure 3‑18: Allocation Inheritance Sequence for STATEFIRST

In this inheritance path, see how we used a [Wildcard Allocation](#_Wildcard_Allocation_Cards) for Sales Reps. As described on the previous session, when a Wildcard Allocation is used, BC will not look for one specific allocation code (e.g. SALESREP-JO). Instead, it will look for all allocations codes with the same Source, that matches the information from the Sales Order. Therefore, if the SALESREPS allocation code has Source **Salesperson**, then, when used in an inheritance path, BC will look for any allocation code with a **Salesperson** Source, that matches the current sales order Salesperson. For more details, please review the [Wildcard Allocation Cards](#_Wildcard_Allocation_Cards) section.

Inheritance Paths can be determined in 3 levels:

·       Globally, on the [Allocation Setup](#_Wine_Setup)

·       [Per Item](#_Item_Allocation_Setup)

·       [Per Customer](#_Customer_Allocation_Setup)

BC will choose the Inheritance Path as follows:

·       If both Customer and Item has **Allocation Inheritance Codes**:

o   BC will choose the **Inheritance Code** based on field **Inheritance Code Precedence** defined on the [Allocation Setup](#_Wine_Setup)

·       If only the Customer has an **Allocation Inheritance Code**, then this one will be used

·       If only the Item has an **Allocation Inheritance Code**, then this one will be used

·       If Customer and Item do not have Allocation Inheritance Codes, then the default one setup on the [Allocation Setup](#_Wine_Setup) will be used

·       If no **Default Inheritance Code** is setup, then BC will not search for additional allocation codes to satisfy an allocation need. It will only use the Customer Allocation Code. For more details, refer to section [Sales Line Allocation Entries](#_Sales_Line_Allocation)

**Please note**: BC will always look for and consume Customer Allocations, before looking for additional quantities from the Inheritance Path. Therefore, you should never add Customer Allocation Codes to the Inheritance Path.

## 3.5.        Allocation Journal Batches

[Allocation Journals](#_Allocation_Journals) is how users will post quantities to Allocation Codes. Before using them, you need to setup Allocation Journal Batches.

To do so, go to the **365WineTrade** menu, **Inventory Allocations**, **Allocation Journal Batches**. You will be taken to the following list:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image021.png)

Figure 3‑19: Allocation Journal Batches list

If you’re using automatic allocation expiration (as defined on the [Allocation Setup](#_Wine_Setup) card), it’s advised that you create one specific Allocation Journal Batch, with an specific **Posting Document No. Series**, like shown on the screenshot above.

There are two approaches to posting expired allocation entries manual vs automatic.

The automatic approach is handled via the setting in the allocation setup page. For automatic expiry of allocation entries, the “Expiration Job Queue Frequency” must be set to “Daily”. Each day, the system will review expired allocation entries and post automatically reversing entries to expired allocations. The second approach is still somewhat automated however it requires a user to run the task manually. When the job queue frequency is set to “Never” the user will now be required to manually run the task “Expire Allocation Ledger Entries”. This job will also review allocation ledger entries for expiry dates that have passed and automatically post reversing allocation journal entries to expired ledger entries.

![](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image022.png)

**Note: For allocation entries to be expired through this automated process “Expiry Dates” must be set on the initial allocation entry. If no expiry date has been posted with the entry, then the automated expiry process will overlook these allocation ledger entries.**

  

# 4.   Transactions

## 4.1.        Allocation Journals

Allocation Journals is how users will post quantities to Allocation Codes. Any maintenance to quantities that have been already allocated, will need to be managed using Allocation Journals. Users can work with multiple Journal Batches in case they need to work on allocation planning for extended period of times.

An Allocation Journal entry allows for the following operations (aka Transaction Types):

·       **Initial**: This is the very first allocation done against a new Allocation Code

·       **Adjustment**: This will be sequential positive and negative adjustments done against an Allocation Code. The quantity field will need to have the correct sign for this type of transaction

·       **Transfer**: This will allow for users to move quantities from an Allocation Code to another

·       **Taken, Taken/Inherited, Taken/Not Allocated, Taken/Manual**: These types are used by the system to record that an allocation has been consumed. Transaction Type with Taken associated with the name can only be used by the system and not permitted in an Allocation Journal manual entry. This information is presented here for informational purposes only. These types have the same effect as a negative adjustment, and can be used for statistical purposed to determine how many allocations end up being used

·       **Expired**: This will record that an allocation entry was explicitly expired. This type has the same effect as a negative adjustment, and can be used for statistical purposes to determine how many allocations never end up being used

To start using the Allocation Journals, you can go to the **365WineTrade** menu, **Inventory Allocations**, **Allocation Journal**. You will be taken to a page that resembles a standard BC general journal:

![Graphical user interface, application
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image023.png)

Figure 4‑1: Allocation Journal Lines

Once allocation journal lines are created, and ready to be allocated, users will need to use action **Post…** on the actions ribbon. These allocation journal lines will then be removed from the Allocation Journal Batch, and they will be converted into [Allocation Ledger Entries](#_Allocation_Ledger_Entries). Any transaction sitting on an Allocation Journal is not considered an allocation until it is posted, but they may commit inventory quantities if the [Reservation System Integration](#_Reservation_System_Integration) is enabled, and users have reserved quantities for the Journal Line. Because of this, you should not leave lines hanging on these journals for long if they have reservation entries for them.

 

### 4.1.1.     Allocations vs. Reservations

Two terms that are often confusing when using the **365WineTrade Inventory Allocations** for the first time, is **Allocations** and **Reservations**.

**Reservations** are a Business Central user-generated link between Supply and Demand. Users can link quantities from Inventory on Hand to some quantities on Sales Orders, for example, using Reservations. This way, BC will ensure that inventory is reserved for such Sales Order, and that no other Sales Orders consume that inventory.

**Reservations** can only exist for Supply and Demand that exist in the system. For example, you cannot reserve quantity for a Sales Order (**existing demand**), from a Purchase Order that is not yet entered in the system (**unknown supply**). Similarly, you cannot reserve existing Inventory on Hand (**existing supply**) for customers if there is no current Sales Orders open for them (**unknown demand**).

**Allocations** is a **365WineTrade** entity used to link Quantities (on hand or not) to Allocation Codes (aka Customers, Vendors, Brands, States, Salespeople, etc). They were created to cover the gap between **Reservations** and the Wine Industry, where it is common to allocate Quantity on Hand (**existing supply**) for future orders that are not yet entered in the system (**unknown demand**). They also cover a gap for Wineries, that have sales orders from customers (**existing demand**), but no real quantity on hand (**unknown supply**).

The **365WineTrade Inventory Allocations** module was designed in a way that allocations by themselves are not a firm demand in Business Central, and they do not commit inventory, meaning that Sales Orders may consume quantities that were allocated for other customers. This may work for users who do soft allocations for their customers and do not really hold back sales in case an item is fully allocated but not fully sold.

There are other users that require that allocations be committing, and quantities should not be depleted if they have not been properly allocated for the Sales Order that is requesting it. For these users, you should turn on setting Allocation Reservation Integration on the [Allocation Setup](#_Wine_Setup).  

### 4.1.2.     Reservation System Integration

When you choose to integrate the Reservation System with the **365WineTrade Inventory Allocations**, you have the following 3 options to choose from on the Allocation Setup:

·       **Disabled**: No reservations can be done for an allocation entry

·       **Reserve when Possible**: You can pick and choose which allocation entries will have a supporting reservation entry (see more details below)

·       **Mandatory**: Users must always reserve quantities against an allocation entry (see more details below)

These settings can also be defined on the [Item card](#_Item_Allocation_Setup) in case some Items require special reservation handling.

When an allocation entry has a supporting Reservation Entry linked to it, this means that the quantity for that allocation is now a firm demand that cannot be used for any other demand in the system. Users will only be able to sell this reserved quantity when:

·       Either the allocation is allocated to a Sales Order and ultimately posted

·       Or the allocation is undone using the Allocation Journals

When the **Allocation Reservation Integration** setting is set to **Mandatory** (either globally or on the item level), Reservation Entries for Allocation Entries cannot be cancelled using standard Business Central procedures. This is by design so that the Allocation System can remain reliable.

As seen on the next section, when Allocation Entries have Reservation Entries linked to them, they will be automatically assigned to the Sales Order, when BC detects that the Allocation Entry can be consumed by such Sales Order. If these allocation entries are removed from the Sales Order, prior to being posted, their previously linked reservations entries shall be re-attached to them.

## 4.2.        Sales Line Allocation Entries

When users enter items into Sales Orders, that’s when **365WineTrade Inventory Allocations** determine if there are any allocation codes that need to be consumed in order to fulfill the current order.

If so, BC will automatically create Sales Line Allocation Entries to let users know which allocation entries are going to be consumed in order to fulfill the current order. If these allocation entries have reservation entries linked to them then these reservation entries will be automatically assigned to the Sales Line.

In order to detect if a Sales Line got any quantities allocated for it, users can check field “Allocated Quantity” on the Sales Line:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image024.png)

Figure 4‑2: Field Allocated Quantity on a Sales Order Line

Users can also go into the Sales Line **Actions** ribbon, **Line, Related Information, Allocation Entries**:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image025.png)

Figure 4‑3: Accessing Sales Line Allocations from the Sales Lines functions

This will take users to the following page:

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image026.png)

Figure 4‑4: Sales Line Allocation Entries

From this page, users can:

·       Check exactly which Allocation Codes are being used to fulfill the current order

·       Manually change or delete any allocations calculated by the system

When the Sales Order is posted, these lines will be transferred to an Allocation Journal and they will be posted and converted into [Allocation Ledger Entries](#_Allocation_Ledger_Entries).

## 4.3.        Sales Line Reviews

**365WineTrade Inventory Allocations** integrates with the Sales Order review functionality from **365WineTrade Base**.

On the Sales Order Review Category Cards, a new Review Type is added:

·       **Not Fully Allocated**

![Graphical user interface, application
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image027.png)

Figure 4‑5: Not Fully Allocated Review Type

When used, this review type will be triggered for all sales lines that have an **Allocated Quantity** less than the total Quantity for the Sales Line.

For more information on the Sales Order Review process, please refer to the **365WineTrade Base** documentation.

## 4.4.        Allocation Ledger Entries

Once Allocation lines are posted from an Allocation Journal (or from a Sales Order), they become historical Allocation Ledger Entries. Just like any regular ledger entry in Business Central, these entries cannot be modified. They hold important information about existing allocations such as remaining quantities. For _Taken_ entries, they also hold information on which sales orders and which allocation codes were consumed.

To find the Allocation Ledger Entries, go to the **365WineTrade** menu, **Inventory Allocations**, **Allocation Ledger Entries:**

![Graphical user interface, table
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image028.png)

Figure 4‑6: Allocation Ledger Entries list

Very similar to BC’s Item Ledger Entries, an entry marked as **Open** means that the line is a positive allocation quantity that is yet to be consumed. The **Remaining Qty** field will show how many quantities are still available to be consumed.

## 4.5.        Allocation Report

The Allocation Report can be used to get an overview of all current allocations per item:

The report can be accessed under the 365WineTrade menu.

![A screenshot of a computer
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image029.png)

Figure 4‑7: Allocation Report Menu

![A screenshot of a report
Description automatically generated](365WineTrade%20Users%20Guide%20-%20Inventory%20Allocations.fld/image030.png)

Figure 4‑8: Allocation Report