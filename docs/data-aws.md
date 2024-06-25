
| Dataset                                           | AWS S3 Bucket Link              | Location in Bucket  |
|---------------------------------------------------|---------------------------------|---------------------|
| Stream lines and catchments (geopackage)          | s3://geoglows-v2                | streams             |
| Living Atlas Optimized Streams                    | s3://geoglows-v2                | streams-global      |
| VPU (computational group) boundaries (geopackage) | s3://geoglows-v2                | streams-global      |
| Model Configuration Files for Simulations         | s3://geoglows-v2                | configs             |
| River Names, Locations, and TDX-Hydro Metadata    | s3://geoglows-v2                | tables              |
| TDX-Hydro modification files                      | s3://geoglows-v2                | tdxhydro-processing |
| Retrospective Discharge since 1940 (Zarr)         | s3://geoglows-v2-retrospective  | retrospective.zarr  |
| Retrospective Discharge since 1940 (netCDF)       | s3://geoglows-v2-retrospective  | retrospective       |
| Return period flow estimates (Zarr)               | s3://geoglows-v2-retrospective  | return-periods.zarr |
| Return period flow estimates (netCDF)             | s3://geoglows-v2-retrospective  | return-periods      |


# GEOGLOWS V2 Datasets
All GEOGLOWS V2 datasets are sponsored by the AWS Open Data Sponsorship Program. This makes our datasets publicly available and available at no cost to the consumer. You do not need an AWS account, credit card, or a user name and password to use this AWS service to access GEOGLOWS data. You can view our listing in the registry of open data and in the AWS Data Exchange.

* Registry of Open Data: https://registry.opendata.aws/geoglows-v2/

* AWS Data Exchange: https://aws.amazon.com/marketplace/pp/prodview-aboaljwcz64zs 

## Model Configs, GIS Data, Metadata
The stream network, model configuration files, and many supporting metadata files:

* http://geoglows-v2.s3-website-us-west-2.amazonaws.com/

### Additional code used in GEOGLOWS:

* TDX-Hydro post processing preparation for hydrological modeling: https://github.com/geoglows/tdxhydro-postprocessing 

* Forecast computation scripts: https://github.com/geoglows/geoglows_ecflow 

* Retrospective weekly update scripts: https://github.com/geoglows/retrospective-update 

* Version of RAPID (muskingum channel routing) software used: https://github.com/c-h-david/rapid/releases/tag/20240224 

## Forecast Data and Summaries
GEOGLOWS daily river forecasts are calculated at the ECMWF Supercomputing facility in Bologna, Italy. The forecasts are archived there as well as on AWS in S3. In addition, The forecast data are available through a data service.

* http://geoglows-v2-forecasts.s3-website-us-west-2.amazonaws.com/ 

## Retrospective Simulation and Return Periods (Historical Simulation)
GEOGLOWS restrospective (or historical simulation) data and return period estimates. The retrospective simulation is updated weekly. The retrospective simulation is based on the ERA5 dataset. New ERA5 data becomes available daily with approximately 1 week lag (minimum 5 days) from real time which means the least possible amount of lag is 1 week. Once a week, we use all the newly produced ERA5 data since the last simulation to extend the retrospective simulation as far as possible. You should notice the historical simulation alternates between 1-2 weeks of lag from real time. 

* http://geoglows-v2-retrospective.s3-website-us-west-2.amazonaws.com/

## Downloading data from the command line interface (recommended)
The fastest way to download GEOGLOWS data using the AWS Command Line Interface. If you are not familiar with programming or command line tools, please skip to the next section on downloading data with a web browser.

Using the CLI will download data faster than the through the browser and is recommended for downloading large amounts of data. Please refer to the AWS instructions for downloading data from S3. You may need to add the --no-sign-request flag on your copy or sync commands. 

* Buckets:

    * `s3://geoglows-v2`

    * `s3://geoglows-v2-forecasts`

    * `s3://geoglows-v2-retrospective`

* Region: us-west-2

## Downloading data with a web browser
The simplest way to browse the GEOGLOWS V2 datasets is by using the websites which let you browse the datasets available. This is not the fastest way. For better performance downloading data, you should use the command line interface instructions.

Model configurations and GIS datasets: http://geoglows-v2.s3-website-us-west-2.amazonaws.com/

Daily forecast outputs: http://geoglows-v2-forecasts.s3-website-us-west-2.amazonaws.com/ 

Retrospective (Historical) Simulations: http://geoglows-v2-retrospective.s3-website-us-west-2.amazonaws.com/


### Stop: This is not the recommended method for most users and applications.

Both the forecast and retrospective river discharge simulations are available for bulk downloads. However, this is not the most efficient method for many use cases. Downloading this data is free and you are welcome to do so, but we encourage you to first review the tutorials for Query Forecast Data and Query Retrospective Data before proceeding. Many use cases are satisfied by accessing data on-demand from web services.

The best way to access this data is via the AWS Command Line tools. You will be able to download multiple datasets simultaneously and at higher speeds than is possible via the web browser. Please visit the AWS tutorials for instructions https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html/

You may download GEOGLOWS datasets using a web browser. Links to browse these datasets are given in Available Data page.

### Forecast Data Download Instructions
New 15 day forecasts are produced each day and made available immediately via a web data service ([https://geoglows.ecmwf.int]) as well as on an AWS S3 bucket. The CLI command pattern for downloading forecast datasets is:

### Retrospective Data Download Instructions
The retrospective simulation datasets are organized by computational groups (VPUs). Please review the tutorial on Finding River Numbers for help identifying streams and VPU numbers. The CLI command pattern to use for downloading this data is:

`aws s3 cp s3://geoglows-v2-retrospective/retrospective/<vpu-number-here> </local/save/path> --recursive --no-sign-request`

Follow along with a tutorial notebook here:

* [https://colab.research.google.com/drive/1jU915e-OrSnawi_OJkEH7gj4Pznu4qzu?usp=share_link ]