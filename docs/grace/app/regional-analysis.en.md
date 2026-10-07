## Choosing a region

The regional view starts with the outlines of the active region set on the map. There are three ways to analyze a region:

1. Click its outline on the map, or its name in the list in the control panel.
2. Upload a boundary from a GeoJSON file.
3. Draw a polygon on the map.

### Preset region sets

Pick a set from the drop-down under **Regions**. Type in **Filter regions…** to narrow the list.

| Region set | Regions | Source |
|---|---|---|
| Global Aquifers | 99 | Compiled by the GEOGLOWS team from several sources, with gaps filled from the WHYMAP and IGRAC sets below |
| Large Aquifer Systems (WHYMAP) | 37 | Large Aquifer Systems of the World, WHYMAP (BGR/UNESCO) |
| Transboundary Aquifers (IGRAC) | 155 | Transboundary Aquifers of the World 2025, UNESCO-IHP / IGRAC (CC BY-SA 3.0 IGO) |
| Principal Aquifers, USA (USGS) | 31 | Principal Aquifers of the United States, U.S. Geological Survey |
| Major River Basins (GRDC) | 456 | Major River Basins of the World, Global Runoff Data Centre (non-commercial use only) |
| My Regions | yours | Regions you have uploaded |

The attribution for the active set is shown under the list. Cite it if you publish results based on that set.

### Uploading a region

Click **Upload**, choose or drag in a GeoJSON file (`.geojson` or `.json`, up to 50 MB), give the region a name, and click **Analyze**.

![The Upload Region dialog](../../static/images/grace/app-upload.webp){ width="510" }

The file must contain Polygon or MultiPolygon features in WGS 84 longitude and latitude, which is the GeoJSON standard. If it has more than one
feature, they are merged into a single region. Holes in polygons are ignored.

!!! tip "Converting a shapefile"
    The app reads GeoJSON only. To convert a shapefile, open it in QGIS, right-click the layer, choose **Export → Save Features As…**, set the
    format to GeoJSON and the CRS to EPSG:4326. [mapshaper.org](https://mapshaper.org){:target="_blank"} does the same in a browser: import
    the `.shp`, `.dbf` and `.prj` files together and export as GeoJSON. Simplifying a very detailed boundary first makes the file smaller
    without changing the result, since the grid cells are 1° across.

Uploaded regions are saved in **My Regions**, where you can open them again or delete them with the × next to the name. They are stored in your
browser only: they are not shared with anyone, and they won't appear on another computer or in another browser.

### Drawing a region

Select **My Regions** in the region set drop-down, then click **Draw a polygon** on the map. Click to place each corner and double-click to
finish. The app analyzes the polygon straight away. Drawn polygons are not saved; upload a file if you want to keep a region.

## Reading the results

When you open a region, the map zooms to it and shows the anomaly cells for the displayed layer inside its boundary, and the chart shows the
region's average time series.

![Regional analysis of an uploaded region over Punjab and Haryana, India](../../static/images/grace/app-upload-result.webp)

### Which cells are averaged

The regional average uses every grid cell that has at least 35% of its area inside the region, and weights each one by the area of overlap.
Cells mostly outside the region are left out; cells on the edge count in proportion to how much of them is inside.

![How the app averages cells over a region](../../static/images/grace/grace-region-averaging.png)

TWSa is averaged on its 0.5° grid and the other layers on their 1° grid, each with its own overlap weights. A region smaller than about 35% of
one cell may have no cells that qualify; use a larger region or click the cell in the [global view](global-view.md) instead.

### The chart

The chart plots the region's average for each month in cm of liquid water equivalent, with zero (the 2004–2009 mean) drawn as a solid line.
When one component is plotted, a shaded band shows ±1σ. The band is averaged over the cells the same way as the values, which treats the errors
in neighboring cells as fully correlated. That is the cautious choice: errors that partly cancel between cells would give a narrower band.

Check other components under **Time series** to compare them on the same axes:

![GWSa compared with TWSa and SMa for the Iullemeden-Irhazer Aquifer System](../../static/images/grace/app-chart-compare.webp)

The uncertainty band is hidden when several components are plotted, to keep the chart readable. Hover over the chart to read values for a
month. The red dashed line follows the month shown on the map.

Comparing components shows what drives the groundwater signal. In the example above, soil moisture (green) has a strong seasonal cycle but no
long-term trend, while total water storage (orange) and groundwater (blue) rise together from about 2010, so the rise in total storage is
groundwater.

### Showing the grid

Turn on **Show cell boundaries** and **Show mascon boundaries** to see how the region relates to the grid and to GRACE's true resolution:

![Cell and mascon boundaries over the Iullemeden-Irhazer Aquifer System](../../static/images/grace/app-region-boundaries.webp)

Here the region spans parts of several mascons (purple), so its average draws on several independent GRACE values. A region inside a single mascon
is subject to the [leakage](../background/resolution-and-leakage.md) described in the background section.
