## Download RFS forecast data for my river

If you only need to download data for a few rivers, or you do not want to write code, use the web app! Our apps lets you graphically
browse a map of rivers, view and downloading forecast or retrospective data, compare forecasts with the latest satellite imagery, and
finding links to more information. Visit [hydroviewer.geoglows.org](https://hydroviewer.geoglows.org){:target="_blank"} to get started.

## Get a list of IDs in my watershed

Every river in the RFS model has an attribute called "TerminalLink". The TerminalLink is the ID number of the river at the outlet of the
watershed a given river of interest is in. Every river in the watershed has the same outlet. You can filter the table of rivers to select only those
rivers which all drain to the same river. You may use the GIS datasets and perform that in ArcGIS or QGIS. You can find links to retrieve GIS files
for the streams using the Available Data page and the tutorial on Finding River Numbers Alternatively, you can do this in code by using the tables of
metadata for RFS using the model metadata table. You will need to download that table (about 250 MB) in order to solve this problem via code.

<script src="https://gist.github.com/rileyhales/e94f0c51090f26bc396e2289d41edefd.js"></script>

## Retrieve forecast for many rivers

The geoglows python package allows you to request data for many rivers simultaneously. You do not need to use for loops in your code to make
sequential requests for data for a single river. Prepare a list of all the river ID numbers you want to get data for. As an example, you could get a
list of all rivers in a watershed (see tutorial on this page). When using the geoglows python package, you can pass that entire list of rivers to the
functions to retrieve data.

<script src="https://gist.github.com/rileyhales/963be8a9cbbc179d99ed82fd5c61bf46.js"></script>

## Save the forecast records dataset

New forecasts are generated daily. The ensemble average flows predicted to occur in the 24 hours between new forecast are archived each day at the
start of a new forecast simulation. This dataset is referred to as the forecast record. It is continuously updated each day. This dataset is not
archived on an AWS bucket. It is only available from the REST service for convenience in plotting on the fly. However, the full ensemble streamflow
prediction is saved every day.

Please do not write code which loops through a list of rivers and downloads the forecast records each day. This is burdensome to the REST service and
is not as fast or efficient if the number of rivers is large. If you want to download a copy of these, you can retrieve them from AWS where the full
ensemble forecast is stored each day and calculate them using the tools available in the geoglows python package.

<script src="https://gist.github.com/rileyhales/11ac6df64593dabb641ad9f044b23e37.js"></script>

## Save a local copy of forecast or retrospective data

Many users want to keep copies of new forecasts on their own devices. In particular, some users are required to download data so they can be moved to
a secure compute environment or high performance compute center. You can use the geoglows Python package to retrieve either forecast or retrospective
data and save a copy.

<script src="https://gist.github.com/rileyhales/ec78fa1c1d6453c407faee8d9c72acea.js"></script>

By default, you download data as a DataFrame (tabular data). You have many options for saving DataFrames to disc such as Parquet, CSV, or Excel. If
you are storing large tables of data, such as retrospective or forecast ensemble streamflow for many rivers, we recommend the Parquet format. It will
be faster to read and write as well as more compressed than many other formats.

For more advanced users, you can also retrieve data as an Xarray Dataset suitable for higher dimensional data and file formats such as netCDF or Zarr.
You can also save Xarray datasets to disc in several formats. The right format depends on your anticipated use case. To specify the format of data to
download, use format='df' to retrieve tables of data (DataFrames) or format='xarray' to retrieve as a multidimension
dataset. Most users should use the default format, DataFrame.
