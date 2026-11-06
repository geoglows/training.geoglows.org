# Aquifer Analyst Overview

## What the app does

Aquifer Analyst works with groundwater monitoring data: the water levels and water quality measured in wells. It organizes those
records by region and aquifer, plots them, fills the gaps in them, and turns them into maps of the water table and estimates of how much
water an aquifer has gained or lost.

Everything in the app hangs on four levels:

- A **region** is the area you are studying, such as a state, a basin or a country. It has an outline and a length unit, feet or meters,
  that every elevation and depth in it uses.
- **Aquifers** divide a region into the units you want to analyze, each with its own outline. A region can also be treated as a single
  unit, in which case the whole region is one aquifer.
- **Wells** are points in an aquifer, each with an ID, a name, a location and a ground surface elevation.
- **Measurements** are dated values at a well. Water table elevation is the main one, and any number of water quality parameters, such as
  nitrate or total dissolved solids, can sit alongside it.

![The water table of the Escalante Valley-Beryl-Enterprise aquifer in Utah in 2019, interpolated from well records, and the
change in groundwater storage since 1940](../static/images/aquiferx/app-overview.webp)

The app is free and runs in a web browser at
[apps.geoglows.org/previews/aquiferx](https://apps.geoglows.org/previews/aquiferx){:target="_blank"}. It has no server of its own: the
regions you add are stored by your browser on your computer, and you keep a copy by downloading a backup. With it you can:

- explore three ready-made regions, Utah, Oregon and Arizona, without loading anything
- bring in your own regions, aquifer outlines, wells and measurements from CSV, GeoJSON and shapefiles, in the coordinate system they
  came in
- download wells and water levels from the USGS, and water quality samples from the Water Quality Portal
- plot the record of one well or several, with a smooth curve through the measurements, the ground surface, a trend line and a moving
  average
- classify wells and aquifers by how fast their water levels are rising or falling
- fill the gaps in well records with a machine learning model trained on each well's own history and on soil moisture
- interpolate maps of the water table by kriging or inverse distance weighting, animate them through time, draw cross sections through
  them, and compute how much water the aquifer has gained or lost

## What this training covers

**Part 1, Getting Started,** is a tour of the app:

- [The App Interface](start/interface.md): the panel, the map and the chart, and what each control does.
- [Sample Data and My Data](start/my-data.md): the ready-made regions, where your own data is kept, and backing it up.
- [Exploring a Region](start/exploring.md): opening regions and aquifers, selecting wells, and filtering what the map shows.

**Part 2, Adding Your Data,** covers getting your own records into the app: preparing the files, creating regions and aquifers, adding
wells and measurements, downloading from the USGS and the Water Quality Portal, and editing what you have loaded.

**Part 3, Time Series and Trends,** explains the chart, the curve it draws between measurements, and how the app classifies water level
trends.

**Part 4, Filling Gaps,** explains when filling gaps in well records is worthwhile, how to run it, and the model behind it in full.

**Part 5, Water Table Maps,** covers interpolating the water table between wells, the two interpolation methods, and the storage change
and cross sections built from the maps.
