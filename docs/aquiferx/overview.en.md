# Aquifer Analyst Overview

## What the app does

Aquifer Analyst works with groundwater monitoring data: the water levels and water quality measured in wells. It organizes those
records by region and aquifer, plots them, fills the gaps in them, and turns them into maps of the water table and estimates of how much
water an aquifer has gained or lost.

It complements the [GRACE Regional Analyst](../grace/overview.md). GRACE measures changes in groundwater storage from space, but at a
resolution of about 300 km, which limits it to large basins and aquifer systems. For smaller aquifers, Aquifer Analyst estimates the same
quantity from the wells themselves: it interpolates the measured water levels into maps of the water table and turns the change in those
maps into a record of storage change over time, the basis for judging whether an aquifer is being used sustainably. In a large aquifer with
a good monitoring network the two apps overlap, and comparing them is a useful check on both.

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
- fill the gaps in well records month by month from the wells whose readings rise and fall with each well's own
- interpolate maps of the water table by kriging or inverse distance weighting, animate them through time, draw cross sections through
  them, and compute how much water the aquifer has gained or lost

## What this training covers

**Part 1, Getting Started,** is a tour of the app:

- [The App Interface](start/interface.md): the panel, the map and the chart, and what each control does.
- [Sample Data and My Data](start/my-data.md): the ready-made regions, where your own data is kept, and backing it up.
- [Exploring a Region](start/exploring.md): opening regions and aquifers, selecting wells, and filtering what the map shows.

**Part 2, Adding Your Data,** covers getting your own records into the app:

- [Preparing Your Files](data/preparing-files.md): what each file needs to hold, and the formats, dates and units the app reads.
- [Regions and Aquifers](data/regions-aquifers.md): the Add Data window, creating a region, and adding its aquifers.
- [Wells](data/wells.md): uploading a wells file, coordinate systems, ground elevations, and downloading wells from the USGS.
- [Measurements](data/measurements.md): uploading measurements, how rows find their wells, and downloading USGS water levels.
- [Water Quality](data/water-quality.md): the parameter catalog, custom data types, and downloading from the Water Quality Portal.
- [Editing and Exporting](data/editing.md): correcting and deleting measurements, and exporting what the chart shows.

**Part 3, Time Series and Trends,** covers the well chart and the trends of water levels:

- [The Time Series Chart](timeseries/chart.md): the curve between measurements, ground surface elevation, the moving average, trend
  lines and zooming.
- [Trends](timeseries/trends.md): how Analyze Trends rates each well and aquifer, the trend window, and the classes.

**Part 4, Filling Gaps,** fills the gaps in well records from neighboring wells:

- [Gaps in Well Records](imputation/gaps.md): why records have gaps, what Impute Gaps produces, how close its values come, and what
  it can and cannot know.
- [Running an Imputation](imputation/running.md): the wizard, its options and the run.
- [How MC+LNN Works](imputation/method.md): the neighbors, the matrix completion, the reservoirs and the readout, in full.
- [Reading the Results](imputation/results.md): the model on the chart, managing saved models, and using them for water table maps.

**Part 5, Water Table Maps,** covers interpolating the water table between wells, the two interpolation methods, and the storage change
and cross sections built from the maps.
