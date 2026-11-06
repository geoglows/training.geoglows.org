# Preparing Your Files

A region in Aquifer Analyst is built from four kinds of file: an outline of the region, outlines of the aquifers in it, a table of
wells, and tables of measurements. For regions in the United States, wells and measurements can also be downloaded from the USGS and
the Water Quality Portal instead (see [Wells](wells.md), [Measurements](measurements.md) and [Water Quality](water-quality.md)).

Column names in your files do not have to follow any convention. Each importer shows which column it will use for each field, guessed
from common names, and you can change any of them.

## Outlines

The region outline and the aquifer outlines are polygons, in either of two formats:

- **GeoJSON** (`.geojson` or `.json`), with Polygon or MultiPolygon features
- **a zipped shapefile** (`.zip`) holding the `.shp`, `.shx` and `.dbf` files, and the `.prj` file that says what coordinate system
  the shapefile uses

A region outline can have more than one feature; together they make up the region. An aquifer file has one feature per aquifer, with an
attribute holding the aquifer's name and, if you have them, an attribute holding its ID.

The app keeps every outline in longitude and latitude (WGS 84). A zipped shapefile is converted from whatever system its `.prj` file
describes; without a `.prj`, its coordinates are read as longitude and latitude. GeoJSON should be in longitude and latitude already,
as the GeoJSON standard requires. If your outlines are in a projected system, such as UTM or a state plane, zip them as a shapefile with
their `.prj`, or reproject them in QGIS before importing.

## Tables

Wells and measurements come as CSV files: plain text, one row per line, with a header row naming the columns. Commas or tabs both work;
the app decides which from the header row. Spaces at the start and end of a cell are ignored, and a cell in quotes can hold a comma.

From Excel, use **Save As** and pick **CSV UTF-8**.

### Wells

| Field | Needed | What it holds |
|-------|--------|---------------|
| Well ID | yes | An identifier unique within the region |
| Well name | no | A name for labels and charts; the ID is used when there is none |
| Latitude | yes | Latitude, or the northing (Y) in a projected system |
| Longitude | yes | Longitude, or the easting (X) in a projected system |
| Ground surface elevation | no | In the region's unit; looked up from an elevation model when the file has none |
| Aquifer ID | no | Which aquifer each well is in; the app can work this out from the locations instead |

```
Well ID,Well Name,Latitude,Longitude
373236113111401,(C-37-12)34abb- 1,37.543312,-113.189117
373338113431502,(C-37-17)14dcd- 2,37.560531,-113.721633
373347113102801,(C-37-12)23cbd- 1,37.563034,-113.175228
```

Coordinates in a projected system are converted when you import the file; [Wells](wells.md#uploading-a-wells-file) explains how to
pick the system.

### Measurements

A measurements file has a date and a value on each row, and a way to tell which well the value belongs to: a well ID that matches a
well already in the region, or a well name or coordinates, which the app matches to the wells it has or uses to make new ones.

The values can be laid out in either of two ways. In **long form**, each row holds one measurement:

```
Well ID,Date,WTE (ft)
373236113111401,03/22/1940,5464.98
373236113111401,04/13/1940,5466.3
373236113111401,12/02/1940,5460.35
```

In **wide form**, each row is one sample, with a column for each thing measured. Water quality data often comes this way:

```
Station,Latitude,Longitude,Date,pH,Temperature (deg C),TDS (mg/L),Hardness (mg/L)
34.00S/08.00E-21DDA01,42.604958,-121.760719,2019-10-24,8.3,12,110,27.8
34.00S/08.00E-21DDA01,42.604958,-121.760719,2022-03-09,8.3,12.3,107,27.9
34.00S/08.00E-23AAA01,42.616364,-121.720992,2019-11-20,7.8,12.1,131,47.5
```

The importer offers every column it has not used for the well or the date as a column of data, and suggests what each one holds: water
level, one of the standard water quality parameters, or a new type of your own (see [Measurements](measurements.md#data-columns)). A
unit in parentheses after the name, as in `TDS (mg/L)`, helps it check that the values are in the unit the app expects.

**Water levels** are water table elevations, in the region's unit, measured from the same datum as the ground surface elevations. If your
file holds depth to water below the ground instead, the importer can convert it, using each well's ground surface elevation.

**Water quality values** must be in the unit the app uses for that parameter, listed in the [catalog](water-quality.md#the-catalog).
Convert them before importing if they are not, for example arsenic in mg/L to µg/L.

**A value that is not a number**, such as `<0.05`, `ND` or `dry`, is skipped when the app reads the region, so it never appears on a
chart or in an analysis. If results below a detection limit matter to your work, decide how to record them and enter numbers before
importing.

### Dates

Every date needs a day, month and year, all in one format throughout the file. The importer reads these formats:

| Format | Example |
|--------|---------|
| YYYY-MM-DD | `2024-01-15` |
| MM/DD/YYYY | `01/15/2024` |
| DD/MM/YYYY | `15/01/2024` |
| M/D/YYYY | `1/15/2024` |
| D/M/YYYY | `15/1/2024` |

A two-digit year is read as 1950 to 1999 from `50` to `99`, and 2000 to 2049 from `00` to `49`.

The importer guesses the format from the first dates in the file. A date such as `03/04/2020` could be either March 4 or April 3; if
any of the dates it looks at has a first number over 12, it reads the file as day first, and otherwise as month first. Check the
**Date Format** it picked before saving, and change it if your file puts the day first.

## Units

Each region measures lengths in feet or in meters, chosen when you create it. Ground surface elevations and water table elevations in your
files must be in that unit. Elevations the app looks up or downloads are converted to it. The unit can be changed only until the region
has wells.
