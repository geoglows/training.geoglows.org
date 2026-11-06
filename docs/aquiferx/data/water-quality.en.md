# Water Quality

## Data types

Every region has one built-in type of measurement, **water table elevation**, in the region's length unit. Anything else measured in a
well is another **data type**: one of the standard parameters in the app's **catalog**, or a **custom type** you define for a region. A
type belongs to a region once the region has measurements of it, and from then on it appears in the **Data type** list of the panel (see
[Exploring a Region](../start/exploring.md#data-types)). Each type's measurements are kept in their own file in the region,
`data_nitrate.csv` for nitrate.

## The catalog

The catalog holds 38 standard parameters, each with a fixed code and unit. Values imported for a catalog parameter must be in its unit;
the app does not convert units. **View Catalog** in Add Measurements, and **Browse Catalog** in the Custom Data Types window, list
them with the search box below.

For reference, the catalog also gives the US EPA drinking water standard and the WHO guideline value where one exists, in the
parameter's unit.

| Group | Parameter | Code | Unit | EPA | WHO |
|-------|-----------|------|------|-----|-----|
| Physical | pH | `ph` | — |  |  |
|  | Temperature | `temperature` | deg C |  |  |
|  | Specific Conductance | `conductivity` | µS/cm |  |  |
|  | Turbidity | `turbidity` | NTU |  | 5 |
|  | Total Dissolved Solids | `tds` | mg/L | 500 | 1000 |
|  | Hardness | `hardness` | mg/L |  |  |
| Nutrient | Nitrate | `nitrate` | mg/L | 10 | 50 |
|  | Nitrite | `nitrite` | mg/L | 1 | 3 |
|  | Ammonia | `ammonia` | mg/L |  |  |
|  | Phosphorus | `phosphorus` | mg/L |  |  |
|  | Total Nitrogen | `total_nitrogen` | mg/L |  |  |
|  | Total Phosphorus | `total_phosphorus` | mg/L |  |  |
| Major Ions | Calcium | `calcium` | mg/L |  |  |
|  | Magnesium | `magnesium` | mg/L |  |  |
|  | Sodium | `sodium` | mg/L |  | 200 |
|  | Potassium | `potassium` | mg/L |  |  |
|  | Chloride | `chloride` | mg/L | 250 |  |
|  | Sulfate | `sulfate` | mg/L | 250 |  |
|  | Bicarbonate | `bicarbonate` | mg/L |  |  |
|  | Carbonate | `carbonate` | mg/L |  |  |
| Minor Metals | Arsenic | `arsenic` | µg/L | 10 | 10 |
|  | Iron | `iron` | µg/L | 300 |  |
|  | Manganese | `manganese` | µg/L | 50 | 400 |
|  | Lead | `lead` | µg/L | 15 | 10 |
|  | Copper | `copper` | µg/L | 1300 | 2000 |
|  | Zinc | `zinc` | µg/L | 5000 |  |
|  | Chromium | `chromium` | µg/L | 100 | 50 |
|  | Selenium | `selenium` | µg/L | 50 | 40 |
| Minor Non-metals | Fluoride | `fluoride` | mg/L | 4 | 1.5 |
|  | Boron | `boron` | µg/L |  | 2400 |
|  | Silica | `silica` | mg/L |  |  |
| Microbiological | E. coli | `e_coli` | CFU/100mL | 0 | 0 |
|  | Fecal Coliform | `fecal_coliform` | CFU/100mL |  |  |
|  | Total Coliform | `total_coliform` | CFU/100mL |  | 0 |
| Other | Dissolved Oxygen | `dissolved_oxygen` | mg/L |  |  |
|  | Alkalinity | `alkalinity` | mg/L |  |  |
|  | Biochemical Oxygen Demand | `bod` | mg/L |  |  |
|  | Chemical Oxygen Demand | `cod` | mg/L |  |  |

The EPA column mixes kinds of standard. For most parameters it is the enforceable maximum contaminant level. For total dissolved solids,
chloride, sulfate, iron, manganese and zinc it is a secondary standard, set for taste, odor or staining, and for lead and copper it is the
action level for treatment. The nitrate and nitrite limits are on different bases: the EPA's are for nitrogen (10 mg/L nitrate as N), and
the WHO's for the whole ion (50 mg/L nitrate, about 11.3 mg/L as N).

## Custom data types

A parameter the catalog does not have, such as trichloroethylene or a lab's own index, can be imported as a **custom type**. In **Map
data columns** of Add Measurements, set the column's type to **+ New custom type** and fill in:

- **Code.** Lowercase letters, digits and underscores, up to 20 characters, such as `tce`. It names the type's file and cannot be a
  catalog code.
- **Name.** As it appears in the Data type list and on charts.
- **Unit.** As it appears beside the name.

A custom type is created only by importing data for it. Once it exists, other regions' imports suggest it for columns with the same name,
so codes stay consistent across your regions.

The gear on the **Measurements** card of the Add Data window opens **Custom Data Types**, which lists the region's custom types. There
you can rename one, change its unit, or delete it along with all its measurements. Changing the unit changes only the label shown with
the values.

## Downloading from the Water Quality Portal

![Water Quality Portal download, with two parameters picked and an estimate](../../static/images/aquiferx/data-wqp.webp){ align=right width="420" }

The [Water Quality Portal](https://www.waterqualitydata.us){:target="_blank"} (WQP) gathers results from the USGS, the EPA and more than
400 state, tribal and local agencies. For a region in the United States, the **Water Quality (WQP)** source in Add Measurements downloads
results for wells inside the region.

1. **Pick parameters** opens the list of catalog parameters the portal carries. Tick the ones you want and click **Apply**.
2. **Scope**, in a region with aquifers: all of them, or one.
3. **Start Date** and **End Date**: the last ten years unless you change them.
4. **Sources**: all agencies, or the USGS only.
5. **Estimate** asks the portal how many results and sites match. It counts the whole rectangle around the region, so the download, which
   keeps only wells inside the aquifer outlines, ends with fewer. A query over 250,000 results is refused; narrow the dates, the
   parameters or the scope.
6. **Download** fetches the results.

<div style="clear: both"></div>

![Choosing parameters to download](../../static/images/aquiferx/data-wqp-picker.webp){ align=right width="420" }

The portal often returns several results for one sample, and the download keeps one per well, date and parameter:

- **Non-numeric results** are dropped. A result below the detection limit, which the portal reports as text, is lost this way.
- **Sample fraction.** Where the catalog prefers one fraction, results for the other are dropped. It keeps filtered (dissolved) results
  for nitrate, nitrite, ammonia, phosphorus, the major ions, the metals, fluoride, boron and silica, and unfiltered results for total
  nitrogen and total phosphorus.
- **Duplicates.** Of the results left for a well, date and parameter, the first is kept.

A **WQP cleanup** note counts what was dropped at each step.

The results then go through the same [well matching](measurements.md#how-rows-find-their-wells) as an uploaded file. A portal site that is
also a USGS well, such as one from a [USGS well download](wells.md#downloading-wells-from-the-usgs), matches it by ID. Other sites match by
name or proximity or become new wells. **Save Measurements** saves them, as for an upload.

<div style="clear: both"></div>
