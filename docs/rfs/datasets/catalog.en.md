## Summary

There are 3 primary kinds of river datasets provided by the River Forecast System. All these data are available for free.

1. **Hydrography**: GIS data for stream and catchment locations around the world.
2. **Retrospective Simulation**: Hourly river discharge data since January 1940.
3. **Forecasts**: 15-day streamflow forecasts generated every day at midnight.

[The GEOGLOWS River Forecast System V2](https://www.geoglows.org){:target="_blank"} © [Dr. Riley Hales](https://hales.app) 2025 is licensed
under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}

## Table of datasets

All RFS V2 datasets are sponsored by the AWS Open Data Sponsorship Program. This makes datasets publicly available at no cost. You **do
not need** an AWS account, credit card, or a username and password to use this AWS service. Read more on
the [Registry of Open Data](https://registry.opendata.aws/geoglows-v2/) and
the [AWS Data Exchange](https://aws.amazon.com/marketplace/pp/prodview-aboaljwcz64zs).

When querying data from AWS, you may need to specify that you are accessing it anonymously if you don’t have an AWS account or prefer not to provide credentials.

The data are stored in 2 buckets. The first holds the model configuration files, gis data, retrospective simulation data, and other data which are
essentially static. The second bucket holds the daily forecasts produced by RFS.

- Forecasts: [http://geoglows-v2-forecasts.s3-website-us-west-2.amazonaws.com/index.html](http://geoglows-v2-forecasts.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}
- GIS + Retro: [http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}

| Dataset                              | File Format(s)      | Bucket URI and Path                                                                                                                                                                 | AWS Region |
|--------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Daily Forecasts                      | Zarr                | [s3://geoglows-v2-forecasts/](http://geoglows-v2-forecasts.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}                                                         | us-west-2  |
| Hydrography - VPUs                   | GeoPackage (sqlite) | [s3://geoglows-v2/hydrography/](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#hydrography/){:target="_blank"}                                                    | us-west-2  |
| Hydrography - Global                 | GeoPackage (sqlite) | [s3://geoglows-v2/hydrography-global/](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#hydrography-global/){:target="_blank"}                                      | us-west-2  |
| Hydrography - Supplementary Tables   | Parquet             | [s3://geoglows-v2/tables/](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#tables/){:target="_blank"}                                                              | us-west-2  |
| Retrospective - Hourly Average       | Zarr                | [s3://geoglows-v2/retrospective/hourly.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/hourly.zarr/){:target="_blank"}                         | us-west-2  |
| Retrospective - Daily Average        | Zarr                | [s3://geoglows-v2/retrospective/daily.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/daily.zarr/){:target="_blank"}                           | us-west-2  |
| Retrospective - Monthly Average      | Zarr                | [s3://geoglows-v2/retrospective/monthly-timeseries.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/monthly-timeseries.zarr/){:target="_blank"} | us-west-2  |
| Retrospective - Yearly Average       | Zarr                | [s3://geoglows-v2/retrospective/yearly-timeseries.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/yearly-timeseries.zarr/){:target="_blank"}   | us-west-2  |
| Retrospective - Yearly Maximums      | Zarr                | [s3://geoglows-v2/retrospective/yearly-maximums.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/yearly-maximums.zarr/){:target="_blank"}       | us-west-2  |
| Retrospective - Return Periods       | Zarr                | [s3://geoglows-v2/retrospective/return-periods.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/return-periods.zarr/){:target="_blank"}         | us-west-2  |
| Retrospective - Flow Duration Curves | Zarr                | [s3://geoglows-v2/retrospective/fdc.zarr](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html#retrospective/fdc.zarr/){:target="_blank"}                               | us-west-2  |

## Code and Technical References

- Forecast computation scripts: [https://github.com/geoglows/geoglows_ecflow](https://github.com/geoglows/geoglows_ecflow){:target="_blank"}
- Retrospective weekly update scripts: [https://github.com/geoglows/retrospective-update](https://github.com/geoglows/retrospective-update){:target="_blank"}

## Downloading data from the command line interface (recommended)

The fastest way to download RFS data using the AWS Command Line Interface. If you are not familiar with programming or command line tools, please
skip to the next section on downloading data with a web browser.

Using the CLI will download data faster than the through the browser and is recommended for downloading large amounts of data. Please refer to the AWS
instructions for downloading data from S3. You may need to add the `--no-sign-request` flag on your copy or sync commands.

## Downloading data with a web browser

The simplest way to browse the RFS V2 datasets is by using the websites which let you browse the datasets available. This is not the fastest way.
For better performance downloading data, you should use the command line interface instructions.

RFS allows users to download global streamflow data directly from AWS. This provides access to both retrospective simulation data and 15-day
streamflow forecasts. These datasets are hosted in S3 buckets, optimized for time series analysis and bulk downloads.
