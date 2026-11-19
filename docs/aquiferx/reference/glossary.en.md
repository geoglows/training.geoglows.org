# Glossary

Terms as Aquifer Analyst and this training use them, each with a link to the page that covers it.

## A–C

**Acre-foot (acre-ft).** The volume of water that covers one acre to a depth of one foot: 43,560 ft³, or about 1,233 m³. The storage
change chart's default unit in a region measured in feet (see [Storage Change](../spatial/storage.md#the-controls)).

**Active Wells.** A button on the card at the top right of an open set of maps. It colors the wells with a value on the date shown green
and the rest dark gray, to show which wells each map rests on (see [Viewing the Maps](../spatial/maps.md#what-the-map-shows)).

**Aquifer.** One of the units a region is divided into, with its own outline. Each well belongs to one aquifer, and gap filling, water
table maps and storage change work one aquifer at a time (see [Regions and Aquifers](../data/regions-aquifers.md)).

**Aquifer ID.** An aquifer's identifier, from the aquifer file or numbered by the app, and the column of a wells or measurements file
that says which aquifer each row belongs to (see [Preparing Your Files](../data/preparing-files.md#how-the-files-fit-together)).

**Back up.** Download all of My Data as one zip file, with a folder of plain files for each region. **Restore** loads such a file into
My Data (see [Sample Data and My Data](../start/my-data.md#backing-up-and-restoring)).

**Catalog.** The app's list of 38 standard water quality parameters, each with a fixed code and unit (see
[Water Quality](../data/water-quality.md#the-catalog)).

**Combined.** The checkbox on a model's chart that shows the series the model saved, colored by how each month was filled: PCHIP,
MC+LNN or a held reading (see [Reading the Results](../imputation/results.md#the-filled-series)).

**Contour.** A line on a map joining cells of equal value. The maps draw eight levels evenly spaced across the color scale, the same
levels on every date (see [Viewing the Maps](../spatial/maps.md#what-the-map-shows)).

**Coordinate system.** The system a file's coordinates are given in: longitude and latitude, or a projection such as a UTM zone, in
meters or feet. Each has an **EPSG code**, such as 4326 for longitude and latitude (WGS 84) and 26912 for NAD83 / UTM zone 12N. The
app keeps every location in longitude and latitude and converts the rest (see [Wells](../data/wells.md#coordinate-systems)).

**Cross section.** A profile of a set of maps along a straight line from A to A′, on the date shown, with the ground surface when
**GSE** is checked (see [Cross Sections](../spatial/cross-sections.md)).

**Custom data type.** A data type defined for a region, with a code, name and unit, for a parameter the catalog does not have (see
[Water Quality](../data/water-quality.md#custom-data-types)).

## D–H

**Data type.** What a measurement measures: water table elevation, a catalog parameter or a custom type. A region holds each type's
measurements in a file of their own, such as `data_nitrate.csv` (see [Water Quality](../data/water-quality.md#data-types)).

**Depth to water.** The distance from the ground surface down to the water in a well. Subtracted from the well's ground surface
elevation, it gives the water table elevation (see [Measurements](../data/measurements.md#data-columns)).

**Direct.** The temporal method that takes a well's value on a map date from a gap-filling model's value in that month (see
[Running a Spatial Analysis](../spatial/running.md#value-at-each-date)).

**EPSG code.** See *Coordinate system*.

**Gap.** A stretch of a well's record with no readings. Impute Gaps keeps the PCHIP curve across a gap under 6 months and fills a
longer one with MC+LNN (see [Gaps in Well Records](../imputation/gaps.md)).

**GeoJSON.** A text format for map features, in longitude and latitude, and one of the two formats for region and aquifer outlines
(see [Preparing Your Files](../data/preparing-files.md#outlines)).

**Ground surface elevation (GSE).** The elevation of the ground at a well, in the region's unit. **GSE** on the well chart and the cross
section draws it (see [Wells](../data/wells.md#ground-surface-elevation)).

**Hidden-readings check.** A test an Impute Gaps run can add: it hides five years of each well's readings, fills the well again without
them, and compares MC+LNN and the PCHIP curve with the hidden readings (see
[Reading the Results](../imputation/results.md#the-hidden-readings-check)).

**Hold.** Keeping a well on the maps beyond its record, with its first reading before the record and its last reading after it, up to a
set number of years, 10 to start with (see [Running a Spatial Analysis](../spatial/running.md#which-wells)).

## I–M

**IDW (inverse distance weighting).** An interpolation method that takes each cell's value as a weighted average over the wells, the
nearer ones weighted more (see [Interpolation Methods](../spatial/interpolation.md#inverse-distance-weighting)).

**Impute Gaps.** The analysis that gives each well of an aquifer a value for every month and saves the series as a model (see
[Gaps in Well Records](../imputation/gaps.md#what-impute-gaps-does)).

**Imputed Data.** The Data Source choice in Spatial Analysis that takes the wells' values from a gap-filling model in place of the
readings (see [Running a Spatial Analysis](../spatial/running.md#data-source)).

**Insufficient data.** The trend class of a well without readings at least two years apart in the trend window, and of an aquifer
with no well that has a rate (see [Trends](../timeseries/trends.md#the-classes)).

**Interval.** The time between one map of a set and the next: 1 year, 6 months or 3 months (see
[Running a Spatial Analysis](../spatial/running.md#dates)).

**Kriging.** The default interpolation method. It weights each well by how closely its value is expected to agree with the cell's,
from the distances between the cell and the wells and among the wells themselves (see
[Interpolation Methods](../spatial/interpolation.md#kriging)).

**Length unit.** Feet or meters, chosen when a region is created, for every elevation, depth and water level in it (see
[Regions and Aquifers](../data/regions-aquifers.md#creating-a-region)).

**Long form.** A measurements file with one measurement on each row. A **wide form** file has one sample on each row and a column for
each thing measured (see [Preparing Your Files](../data/preparing-files.md#measurements)).

**MC+LNN.** The method Impute Gaps uses for long gaps and beyond each record. Matrix completion (MC) completes the records of a well's
neighbors, reservoirs, a kind of liquid neural network (LNN), take those records month by month, and a regression fitted to the well's
readings turns the reservoirs' states into a water level for each month (see [How MC+LNN Works](../imputation/method.md)).

**MCM.** Million cubic meters, the storage change chart's default unit in a region measured in meters. One MCM is about 811 acre-ft.

**Model.** The result of a run of Impute Gaps: a monthly series for each well it fills, saved in the aquifer and listed under it in
the tree (see [Reading the Results](../imputation/results.md)).

**Moving average (MAvg).** A smoothed copy of a well's record, each value an average of the readings around it with Gaussian weights
over a window of months (see [The Time Series Chart](../timeseries/chart.md#moving-average)).

**My Data.** The regions you create, copy or restore, kept by your browser on your computer (see
[Sample Data and My Data](../start/my-data.md#my-data)).

## N–R

**Neighbors.** In MC+LNN, the 15 wells of the aquifer whose monthly levels correlate most strongly with a well's own, at any distance
(see [How MC+LNN Works](../imputation/method.md#neighbors)).

**Nested wells.** Wells finished at different depths in one borehole or a few feet apart (see
[Wells at One Place](../spatial/places.md)).

**Nugget.** In kriging, the part of the variation that appears between readings at almost the same place. Without it, the default,
a map passes through every well's value (see [Interpolation Methods](../spatial/interpolation.md#the-nugget)).

**PCHIP.** Piecewise cubic Hermite interpolating polynomial: the smooth curve the chart draws through a well's readings, which never
rises above the higher or falls below the lower of two neighboring readings. Maps made from the measurements take each well's value
from it (see [The Time Series Chart](../timeseries/chart.md#the-curve-between-measurements)).

**Place.** A spot where two or more wells of an aquifer stand closer together than a set distance, 20 m to start with. A set of maps
keeps one well at each place (see [Wells at One Place](../spatial/places.md)).

**Proximity threshold.** How close a row's coordinates must be to a well already in the region to match it when importing
measurements, 100 m to start with (see [Measurements](../data/measurements.md#how-rows-find-their-wells)).

**R².** One minus the mean squared miss of MC+LNN's test values divided by the variance of the well's readings. One is a perfect
fit (see [How MC+LNN Works](../imputation/method.md#the-fit-statistics)).

**Range.** In kriging, the distance that sets how fast the relation between well values fades with distance: a third of the diagonal
of the rectangle around the wells to start with (see [Interpolation Methods](../spatial/interpolation.md#the-covariance)).

**Raster Statistics.** The chart of the wells' values on each date of a set of maps: their mean and standard deviation, and, when
chosen, the median, quartiles and range (see [Viewing the Maps](../spatial/maps.md#raster-statistics)).

**Region.** The area you study, with an outline and a length unit. It holds the aquifers, wells and measurements (see
[Regions and Aquifers](../data/regions-aquifers.md)).

**Reservoir.** In MC+LNN, a network of random units, fixed once drawn, that takes the inputs month by month and keeps a fading memory of
them (see [How MC+LNN Works](../imputation/method.md#the-reservoirs)).

**Resolution.** The number of columns in a map's grid across the aquifer, 50 to start with (see
[Running a Spatial Analysis](../spatial/running.md#spatial)).

**RMSE.** Root mean square error: the square root of the mean of the squared differences between estimates and readings, in the
region's unit (see [How MC+LNN Works](../imputation/method.md#the-fit-statistics)).

## S–Z

**Sample Data.** The three regions that come with the app, Utah, Oregon and Arizona. They cannot be changed, and a copy in My Data can
(see [Sample Data and My Data](../start/my-data.md#sample-data)).

**Set of maps.** The maps one run of Spatial Analysis saves, one for each date, listed under the aquifer by the data type's code and
the title, such as `wte_kriging` (see [Viewing the Maps](../spatial/maps.md)).

**Shapefile.** A GIS format kept in several files. The app reads it zipped, with the `.shp`, `.shx`, `.dbf` and `.prj` files (see
[Preparing Your Files](../data/preparing-files.md#outlines)).

**Single-unit region.** A region that is one aquifer, its outline also the aquifer's (see
[Regions and Aquifers](../data/regions-aquifers.md#single-unit-or-with-aquifers)).

**Spatial Analysis.** The analysis that interpolates a set of maps of one aquifer, one for each date in a range (see
[Running a Spatial Analysis](../spatial/running.md)).

**Storage change.** The volume of water an aquifer has gained or lost since the first map of a set: the change in the water table,
cell by cell, times the cell's area and the storage coefficient (see [Storage Change](../spatial/storage.md)).

**Storage coefficient.** The volume of water an aquifer releases from a unit area as its water table falls by one unit; for an
unconfined aquifer, the specific yield. The storage change chart uses 0.1 to start with (see
[Storage Change](../spatial/storage.md#the-controls)).

**Temporal method.** How a well's value on a map date is taken from its record: PCHIP or a moving average of the readings, or Direct or
a moving average from a model (see [Running a Spatial Analysis](../spatial/running.md#value-at-each-date)).

**Test values.** MC+LNN's estimates at the months with readings, each predicted with that sixth of the record left out. R² and RMSE
compare them with the readings (see [Reading the Results](../imputation/results.md#mclnns-estimate)).

**Trend.** The rate at which a well's water level changes: the slope of a straight line fitted by least squares to its readings in the
trend window, in the region's unit per year (see [Trends](../timeseries/trends.md#the-trend-of-a-well)).

**Trend class.** Extreme Decline, Decline, Static, Increase, Extreme Increase or Insufficient data, by a well's or an aquifer's rate
(see [Trends](../timeseries/trends.md#the-classes)).

**Trend window.** How many years back from today Analyze Trends fits each well, 30 to start with (see
[Trends](../timeseries/trends.md#the-trend-window)).

**Truncate Low and Truncate High.** Options of Spatial Analysis that clip every map to a lowest and a highest value (see
[Running a Spatial Analysis](../spatial/running.md#spatial)).

**Variogram.** Half the mean squared difference between values a distance apart, as a function of that distance. **Variogram Model**
in Spatial Analysis chooses its shape: exponential, the default, spherical or Gaussian (see
[Interpolation Methods](../spatial/interpolation.md#the-covariance)).

**Water Quality Portal (WQP).** A US service that gathers water quality results from the USGS, the EPA and more than 400 state, tribal
and local agencies, and one of the download sources of Add Measurements (see
[Water Quality](../data/water-quality.md#downloading-from-the-water-quality-portal)).

**Water table elevation (WTE).** The elevation of the water in a well, in the region's unit, measured from the same datum as the ground
surface elevations. Every region has it as its built-in data type, code `wte` (see
[Preparing Your Files](../data/preparing-files.md#measurements)).

**Well depth.** How far the finished well goes below the ground, in the region's unit (see [Wells](../data/wells.md#well-depth)).

**WGS 84.** The system of longitude and latitude the app keeps every location in, EPSG code 4326.

**Wide form.** See *Long form*.
