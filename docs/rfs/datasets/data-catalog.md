## Summary

There are 3 primary kinds of river datasets provided by the River Forecast System. All these data are available for free.

1. **Hydrography**: GIS data for stream and catchment locations around the world.
2. **Retrospective Simulation**: Hourly river discharge data since January 1940.
3. **Forecasts**: 15-day streamflow forecasts generated every day at midnight.

[River Forecast System v2](https://geoglows.org){:target="_blank"} © 2024 by [Dr Riley Hales](https://hales.app){:target="_blank"} is licensed
under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}

## Table of datasets

All RFS V2 datasets are sponsored by the AWS Open Data Sponsorship Program. This makes datasets publicly available and available at no cost. You **do
not need** an AWS account, credit card, or a username and password to use this AWS service. Read more on
the [Registry of Open Data](https://registry.opendata.aws/geoglows-v2/) and
the [AWS Data Exchange](https://aws.amazon.com/marketplace/pp/prodview-aboaljwcz64zs)

The data are stored in 2 buckets. The first holds the model configuration files, gis data, retrospective simulation data, and other data which are
essentially static. The second bucket holds the daily forecasts produced by that model as arranged by GEOGLOWS.

- Forecasts: [http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}
- GIS + Retro: [https://rfs-v2.s3-us-west-2.amazonaws.com/index.html](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html){:target="_blank"}

| Dataset                              | File Format(s)      | Bucket URI and Path                                                                                                                          | AWS Region |
|--------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Daily Forecasts                      | Zarr                | [s3://geoglows-v2-forecasts/](https://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}                           | us-west-2  |
| Hydrography - VPUs                   | GeoPackage (sqlite) | [s3://rfs-v2/hydrography/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#hydrography/){:target="_blank"}                              | us-west-2  |
| Hydrography - Global                 | GeoPackage (sqlite) | [s3://rfs-v2/hydrography-global/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#hydrography-global/){:target="_blank"}                | us-west-2  |
| Hydrography - Supplementary Tables   | Parquet             | [s3://rfs-v2/tables/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#tables/){:target="_blank"}                                        | us-west-2  |
| Retrospective - Hourly Average       | Zarr                | [s3://rfs-v2/retrospective/hourly.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}               | us-west-2  |
| Retrospective - Daily Average        | Zarr                | [s3://rfs-v2/retrospective/daily.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}                | us-west-2  |
| Retrospective - Monthly Average      | Zarr                | [s3://rfs-v2/retrospective/monthly-timeseries.zarre](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}  | us-west-2  |
| Retrospective - Yearly Average       | Zarr                | [s3://rfs-v2/retrospective/yearly-timeseries.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}    | us-west-2  |
| Retrospective - Yearly Maximums      | Zarr                | [s3://rfs-v2/retrospective/yearly-maximums.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}      | us-west-2  |
| Retrospective - Return Periods       | Zarr                | [s3://rfs-v2/retrospective/return-periods.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}       | us-west-2  |
| Retrospective - Flow Duration Curves | Zarr                | [s3://rfs-v2/retrospective/flow-duration-curves.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"} | us-west-2  |

## Code and Technical References

- TDX-Hydro post-processing preparation for hydrological
  modeling: [https://github.com/geoglows/tdxhydro-postprocessing](https://github.com/geoglows/tdxhydro-postprocessing){:target="_blank"}
- Forecast computation scripts: [https://github.com/geoglows/geoglows_ecflow](https://github.com/geoglows/geoglows_ecflow){:target="_blank"}
- Retrospective weekly update scripts: [https://github.com/geoglows/retrospective-update](https://github.com/geoglows/retrospective-update){:target="_blank"}
- river-route Python Package for Matrix Muskingum Routing: [https://github.com/rileyhales/river-route](https://github.com/rileyhales/river-route){:target="_blank"}

## Downloading data from the command line interface (recommended)

The fastest way to download GEOGLOWS data using the AWS Command Line Interface. If you are not familiar with programming or command line tools, please
skip to the next section on downloading data with a web browser.

Using the CLI will download data faster than the through the browser and is recommended for downloading large amounts of data. Please refer to the AWS
instructions for downloading data from S3. You may need to add the --no-sign-request flag on your copy or sync commands.

## Downloading data with a web browser

The simplest way to browse the GEOGLOWS V2 datasets is by using the websites which let you browse the datasets available. This is not the fastest way.
For better performance downloading data, you should use the command line interface instructions.

RFS allows users to download global streamflow data directly from AWS. This provides access to both retrospective simulation data and 15-day
streamflow forecasts. These datasets are hosted in S3 buckets, optimized for time series analysis and bulk downloads.

Users can easily access and analyze these data using **Python** and **Jupyter notebooks**, with detailed tutorials available.

![Collab](../../static/images/image5.png)

The following Collab notebooks demonstrate how to access the data from the AWS bucket using Python:

- [Access GEOGLOWS retrospective simulation data from AWS S3](https://colab.research.google.com/drive/19f8n-YMqGxL_qcn3aw5yv4oYUFFlB8IK)
- [Access GEOGLOWS river forecast data from AWS S3](https://colab.research.google.com/drive/1tOuybiHK3HuxwL0MHDhGRbU65-yaolGs)
