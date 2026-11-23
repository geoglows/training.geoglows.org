# Troubleshooting

Where the app shows a message, the heading quotes its start, so the browser's Find can take you to it.

## My Data and backups

### My Data is empty, or a region is missing

My Data is kept by one browser on one computer (see [Sample Data and My Data](../start/my-data.md#my-data)). Another browser, another
computer, or a private window does not see it, and a private window discards what was added in it when it closes. Clearing the
browser's data for the site removes it too. Restore your latest backup with **Restore**.

The app asks the browser to keep My Data when disk space runs low, and **Settings** says when the browser has agreed. A backup is the
only copy that survives clearing the browser's data, so back up after each session of work you would not want to repeat.

### Restore says "This file has no regions in it"

A backup holds one folder per region at the top of the zip file, each with a `region.json` in it. A zip that holds a folder of region
folders, which is what you get by unzipping a backup and compressing the folder it made, has no region at its top. Open the folder,
select the region folders themselves and compress those. The same message comes from a zip that is not a backup, such as a zipped
shapefile.

### Restore says "This file could not be read as a backup"

The file is not a zip file, or the download was cut short. Download or copy the backup again.

### Editing, Impute Gaps or Spatial Analysis offers Copy to My Data

Sample Data cannot be changed, and anything that would change a region, including saving a model or a set of maps in it, needs a copy
in My Data (see [Sample Data and My Data](../start/my-data.md#copying-a-sample-region)). Copy it and carry on in the copy.

### A save fails with "Failed to save"

The rest of the message gives the browser's reason. A message that mentions the quota means the browser has no more room for the
site. Free some disk space, or back up and delete regions, maps and models you no longer need. **Settings** gives how much space the
site is using.

## Outlines and coordinates

### An outline is refused: "the coordinates are not longitude and latitude"

The GeoJSON file holds projected coordinates, such as UTM meters, and does not say what system they are in. Zip the layer as a
shapefile with its `.prj` file, or save it in longitude and latitude (WGS 84) from QGIS or ArcGIS, and add it again (see
[Preparing Your Files](../data/preparing-files.md#outlines)).

### An outline is refused: "…which could not be looked up"

The GeoJSON file names its coordinate system, and the app could not fetch the system's definition from epsg.io. Check the internet
connection and try again, or use one of the two formats above.

### Wells land outside the region

The coordinate preview reads *outside region*, or a notice says wells fall outside every aquifer and will be skipped. Check, in this
order:

1. **The columns.** **Edit Column Mapping** in Add Wells, or the Columns panel in Add Measurements, shows which column was taken for the
   latitude and which for the longitude. Swapped, they put the wells far from the region.
2. **The signs.** Longitudes west of Greenwich and latitudes south of the equator are negative. A file that leaves off the minus sign
   puts the wells on the other side of the world.
3. **The coordinate system.** Projected coordinates, such as UTM eastings and northings, need their system chosen in the
   **Coordinate system** menu or by its EPSG code (see [Wells](../data/wells.md#coordinate-systems)).

**Auto-detect** tries coordinate systems only, so it cannot fix the first two.

### Wells are skipped because they fall outside every aquifer

With **Assign by location**, a well goes to the aquifer whose outline it falls inside, and a well inside none is skipped. When the
wells are where they should be, the aquifer outlines do not cover them. Add an aquifer for those wells, or give the file an Aquifer ID
column and choose **Use aquifer_id column from CSV**, which places each well by its ID whatever its location.

### Save Wells or Save Measurements stays off: wells inside more than one aquifer outline

Overlapping outlines, as where an aquifer is split by depth, can't place a well by its location. Download the list the notice offers,
give each well its aquifer, and add the wells from a file with an Aquifer ID column (see
[Wells](../data/wells.md#wells-inside-two-aquifer-outlines)).

## Tables

### The importer finds one column, or splits the columns in odd places

The app tells commas, tabs and semicolons apart by the first line of the file, which must be the header row. A title or a note above
the header leaves it guessing, and so does a separator it does not read, such as `|`. Delete any lines above the header, and save the
table from the spreadsheet as CSV.

### Values are skipped as "not a number"

A value such as `<0.05`, `ND` or `dry` is not a number, and the summary after saving counts them and shows a few. Write decimals
with a point unless the file is separated by semicolons, and decide how to record results below a detection limit before importing (see
[Preparing Your Files](../data/preparing-files.md#measurements)).

### The dates come out wrong

A date such as `03/04/2020` can be March 4 or April 3. The importer reads a file of such dates as day first when one of them has a first
number over 12 or when they are written with points, so a file that puts the day first can be read month first. Check **Date Format**
in the Columns panel before saving. Measurements already saved with the wrong dates can be replaced by importing the file again with
the right format and **Replace all**, when the file holds all of the region's measurements of those types (see
[Measurements](../data/measurements.md#measurements-already-in-the-region)).

### Dates that "can't be read" or "could not be read"

Before saving, a notice in the Columns panel counts the dates the chosen **Date Format** can't read, and their rows are skipped. The
summary after saving counts them again. A date in another order, such as `2024-01-15` under DD/MM/YYYY, needs the
right format chosen. A date with a month name, such as `15-Jan-2024`, needs the month written as a number, and one naming a day the
month does not have, such as `31.04.2024`, needs correcting. **Download the details** lists each skipped row with its row number in the
file (see [Measurements](../data/measurements.md#saving) and [Preparing Your Files](../data/preparing-files.md#dates)).

### "No measurements match existing wells. Import cannot proceed."

With **The file has well names or coordinates** off, each row's well ID must equal the ID of a well already in the region. Compare a few
IDs in the file with the region's: point at a well on the map to see its ID. A spreadsheet that opened the file may have changed them,
dropping the leading zeros of `0123` or writing a long number such as `373236113111401` as `3.73236E+14`. Keep the IDs as text in the
spreadsheet. When the file also has well names or coordinates, turn the box on, and rows find their wells by those or make new ones (see
[Measurements](../data/measurements.md#how-rows-find-their-wells)).

### Depths to water are skipped: the well has no ground surface elevation

Converting a depth to an elevation needs the well's ground surface elevation. Add the wells with their elevations, or let the
elevation lookup fill them, before importing the depths (see [Wells](../data/wells.md#ground-surface-elevation)). For wells already in
the region without one, choose **Look up missing elevations** in the region's menu, or add a wells file that has their elevations with
**Append**. Then add the file of depths again with **Add new only**, which adds the depths skipped before and leaves the rest as they
are.

### A unit warning appears under a data column

The column name gives a unit that differs from the catalog's for that parameter, such as `Arsenic (mg/L)` where the catalog uses µg/L.
The app does not convert the units of your files, so convert the values before importing (see
[Water Quality](../data/water-quality.md#the-catalog)).

## Downloads

### USGS or Water Quality Portal is not offered

Both serve the United States only, and the importers offer them when the region's center is in the United States.

### "Max retries exceeded — you may be rate-limited"

Without an API key the USGS service answers 30 requests an hour. Get a free key with **Get a free key**, paste it in **API Key** and
download again (see [Wells](../data/wells.md#downloading-wells-from-the-usgs)).

### "USGS request timed out"

The USGS service did not answer in time, three times in a row. Try again later, or set **Download Scope** to **Selected Aquifer**.

### "This area contains more than … USGS wells — too many to download at once"

Set **Download Scope** to **Selected Aquifer** and download each aquifer in turn.

### "No USGS site IDs found"

**USGS Levels** downloads water levels for wells whose IDs are USGS site numbers, with or without the `USGS-` prefix, or IDs of another
agency in the same form. Add the wells with a [USGS well download](../data/wells.md#downloading-wells-from-the-usgs) first.

### USGS water levels are dropped for wells without an elevation

The USGS reports depth to water, and the app converts it with each well's ground surface elevation. The **Data Quality Report** counts
the records of wells without one. Give those wells an elevation as described [above](#depths-to-water-are-skipped-the-well-has-no-ground-surface-elevation)
and download again.

### "This query matches … results — too large to download at once"

The Water Quality Portal download stops above 250,000 results. Shorten the dates, pick fewer parameters, or set the scope to one
aquifer.

### "WQP request failed after retries"

The portal did not answer. Check the connection, try again later, or narrow the query as above.

### Fewer Water Quality Portal results than the estimate

**Estimate** counts the whole rectangle around the region, and the download keeps only sites inside the aquifer outlines. The cleanup
then drops results that are not numbers, such as those below a detection limit, results for the wrong sample fraction, and results in
units it cannot convert with certainty. The **WQP cleanup** note counts each (see
[Water Quality](../data/water-quality.md#downloading-from-the-water-quality-portal)).

### The elevation lookup failed

The panel reads *The lookup failed* with the reason, and wells saved now get no elevation. The lookup needs an internet connection.
Click **Try again** and wait until it finishes before **Save Wells**.

## Trends and the chart

### Analyze Trends is grayed out

Trends are rates of a water level. Choose **Water Table Elevation** in the panel's **Data type** list.

### Wells show Insufficient data

A well needs readings in the trend window at least two years apart. Lengthen the window with **+**, since it always ends today (see
[Trends](../timeseries/trends.md#the-trend-window)).

### The chart draws straight lines between readings

**PCHIP** is unchecked, or more than 25 wells are selected, when the chart joins the readings with straight lines to stay quick.

## Gap filling and maps

### Impute Gaps is not at the top right

The button appears once an aquifer is open with **Water Table Elevation** as the data type.

### Next stays off in the first step of a wizard

No wells qualify: the line under **Min Observations / Well** and **Min Time Span / Well** counts none. Lower the two settings. In
Spatial Analysis, Next also stays off while **Start Year** is after **End Year**.

### The title reads *Name already exists*

The aquifer already has a model, or a set of maps of that data type, with that title. Give the new one another title.

### A model is struck through and marked *older method*

It was made before November 2026 by a method Impute Gaps no longer uses, and it can't be opened. Delete it and run Impute Gaps again
(see [Reading the Results](../imputation/results.md#managing-models)). Maps made from it keep working.

### A well reads *PCHIP and held readings only*

MC+LNN needs a well with readings in at least 12 months and neighbors that track it. Pointing at the band gives the reason for that
well (see [Gaps in Well Records](../imputation/gaps.md#limits-of-the-method)).

### Spatial Analysis fails: "Every timestep came out empty"

No well has a value on any map date. Check that the years cover the wells' readings, and lower the well settings.

### Log Interpolation can't be checked

The logarithm of zero or a negative number does not exist, and some of the values are zero or below.

### A map has a spot of high or low values around one well

Without a nugget, kriging passes through every well's value, so one reading far from those of the wells around it shows as a spot on
that date's map. Select the well and look at its record on the chart, and check the reading with **View/Edit** (see
[Editing and Exporting](../data/editing.md#the-measurement-table)).

### The storage curve jumps in one year

Wells joining or leaving the maps move the surface though the water has not moved. Turn on **Active Wells** and step across the jump to
see which wells changed (see [Storage Change](../spatial/storage.md#reading-the-curve) and the
[East Side case study](../case-studies/east-side.md#a-step-that-is-not-water)).

### The cross section has a gap

The line runs outside the aquifer's outline there, where the maps have no cells.

### The cross section reads *Ground surface unavailable*

The ground surface is read from elevation tiles over the internet. Check the connection, then uncheck **GSE** and check it again to
read it once more.
