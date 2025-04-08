## Overview

There are 6.25 million river segments modeled in the GEOGLOWS V2 datasets. These numbers are unique to the TDX-Hydro dataset and are different from
numbers in any other stream dataset and previous versions of the model. All ID numbers are 9 digits. As a reference, this table provides IDs of some
major rivers and their general locations.

| ID Number | Select Rivers and General Locations |
|-----------|-------------------------------------|
| 760021611 | Mississippi, USA                    |
| 160064246 | Nile, East Africa                   |
| 710462910 | Colorado, USA & Mexico              |
| 441057380 | Ganges, India                       |
| 430157411 | Mekong, Vietnam                     |
| 210406913 | Tiber, Italy                        |
| 621010293 | Amazon, Brazil                      |
| 130747391 | Congo, D.R. Congo                   |
| 640255644 | Parana, Argentina                   |

The RFS ID numbers are 9 digits longs. While large numbers are often delimited, often with a comma or period in various languages, any code you write
to retrieve data ***should not*** include any delimiters. These IDs are integers. Most programming languages will interpret quotes, periods, commas,
or other characters as something besides an integer which will make the retrieval process fail. For example, the number `123456789` ***should not***
be written as `123,456,789` or `123.456.789` or `"123456789"` or `"123,456,789"` or any other variation. Only the integer representation `123456789`
will work.

!!! warning "Users migrating from V1"
    RFS v2 is derived from a different source Digital Elevation Model (DEM) than v1 and has significantly more modeled streams. Because of the higher
    resolution and changes in placements of river channels, it is not possible to provide a mapping of all version 1 numbers to v2 numbers. We have
    outlined some steps below to map an old ID to a GEOGLOWS 2 ID.

## Using the Web App

The easiest way to find the ID of a river is to use the [RFS web app](https://hydroviewer.geoglows.org){:target="_blank"}. Click on a stream on
the map. To ensure you click on the exact stream you intended, the map will zoom in to a higher level of detail if you are zoomed out too far. After
clicking on a stream, the map will identify the river segment you clicked on and the ID will be presented to you in the pop-up window with charts
and other information.

## Using the Hydrography data

The Hydrography data is available in the [data catalog](../datasets/catalog.md){:target="_blank"}. You can download and view either
the streams or catchments in a GIS software such as ArcGIS or QGIS. You can click on features or use spatial analysis tools to select many rivers. The
ID numbers for those rivers are stored in the LINKNO attribute.

## Find Rivers with Lat/Lon

There are many methods to attempt to find a river ID given a latitude and longitude. None are perfect for all cases. There are several potential
errors from automated methods due to the accuracy and precision of your lat/lon points, the accuracy of the stream lines in that specific location,
if you want to snap to the nearest outlet or nearest stream arc, is your lat/lon close to a confluence where the GIS would get confused by having
multiple close choices nearby, etc. Automated methods should be considered imperfect and verified for accuracy against other sources such as a known 
upstream drainage area at the lat/lon of a gauge point, the name of the river, comparisons to imagery basemaps, or other means.

One method to start with is to load the streams GIS files for your area of interest into a GIS software. You can snap them to the nearest stream arc. 
In QGIS, the tool is called "Snap geometries to layer”. Use the algorithm to find the nearest point and insert extra vertices if required.

Another method is to download the catchment polygons and intersect them with a layer containing your lat/lon points. The GIS work is straightforward 
but is occasionally less accurate and requires larger file downloads.
