# The App Interface

## Opening the app

Open [apps.geoglows.org/previews/aquiferx](https://apps.geoglows.org/previews/aquiferx){:target="_blank"} in a current version of
Chrome, Edge, Firefox or Safari. Nothing needs to be installed. **Sign in** connects your GEOGLOWS account, which is shared by the apps on
apps.geoglows.org; nothing in Aquifer Analyst requires it.

![Aquifer Analyst on opening](../../static/images/aquiferx/app-home.webp)

The window has a **control panel** on the left and the **map** on the right. Selecting a well opens a **chart panel** under the map. Drag
the bar between the map and the chart to give either one more room.

## Control panel

![The control panel with a region and an aquifer open](../../static/images/aquiferx/app-panel.webp){ align=right width="260" }

From top to bottom:

- **GEOGLOWS logo.** Opens apps.geoglows.org, where the other GEOGLOWS apps are listed.
- **Sign in.** Your GEOGLOWS account, as above.
- **Settings** (the gear). Light or dark colors, the size of map labels, how much space My Data takes in the browser, and deleting all of
  My Data. See [Sample Data and My Data](my-data.md#settings).
- **Sample Data / My Data.** Which set of regions the tree and the map show. Sample Data holds three ready-made regions that cannot be
  changed; My Data holds the regions you add. In My Data, three buttons sit under the switch: **Add Data**, **Back up** and **Restore**,
  with a line saying when you last backed up. See [Sample Data and My Data](my-data.md).
- **Regions.** The tree of regions. Click a region to open it and list its aquifers, and an aquifer to show its wells. Under an aquifer
  are the water table maps and gap-filling models saved for it. Every row has a menu, the three dots that appear when you point at it,
  with the actions for that item.
- **Data type.** Shown only when the open region holds more than one kind of measurement, such as water levels and nitrate. It picks
  which one the map, the chart and the analyses use.
- **Show on map.** Turns the wells on and off, and labels each aquifer or well with its name or ID. The label size is in Settings.
- **Filter wells.** Hides wells with fewer than a given number of measurements, or wells never measured between two years. See
  [Exploring a Region](exploring.md#filtering-wells).

## Map

The bar along the top of the map shows where you are: **Home**, then the open region, aquifer and well. Click any step to go back to it.

On the map itself:

- **Zoom** with the **+** and **−** buttons, the mouse wheel, or a pinch on a trackpad. Drag to pan.
- **Basemap**, the button at the top right, switches the background between OpenStreetMap and six Esri maps: topographic, imagery,
  streets, light gray, dark gray and terrain.
- **Click** a region's outline to open it, an aquifer to show its wells, and a well to plot it. Clicking an empty spot inside the open
  aquifer clears the selected wells, and clicking a part of the region outside every aquifer goes back to the region.
- **Search wells**, the box at the top left once an aquifer is open, finds a well by name or ID. Use the arrow keys and **Enter**, or
  click a match, to select it and zoom to it.
- **The legend** explains the colors of the well markers, which change when trends are shown.

## Analysis buttons

Three buttons at the top right start the analyses. Each appears once there is something for it to work on:

- **Analyze Trends** (the line icon), once a region is open, colors wells and aquifers by how fast their water levels are changing. See
  Part 3.
- **Spatial Analysis** (the grid icon), once an aquifer is open, interpolates maps of the water table. See Part 5.
- **Impute Gaps** (the wand icon), once an aquifer is open and water table elevation is the data type, fills the gaps in well records.
  See Part 4.

## Chart panel

![The chart panel](../../static/images/aquiferx/app-chart.webp)

The chart panel plots the measurements of the selected wells. Along its top:

- **GSE** adds a line for each well's ground surface elevation.
- **PCHIP** draws a smooth curve through the measurements. Part 3 explains the method.
- **Trend Line** and **MAvg** add a straight-line trend and a moving average.
- **View/Edit** opens a table of the selected well's measurements, where you can correct or delete them.
- **Export CSV** downloads what the chart shows.
- The arrows open the chart in a larger window.

The right end says which data type is plotted and in what unit.
