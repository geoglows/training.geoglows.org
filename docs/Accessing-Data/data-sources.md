# How to get results from the REST API
To use the REST API, a request must be made to the server. The majority of the request commands use the reach_id as a parameter. The reach_id is a unique identifier for each river segment in the model. The reach_id can be found by using the `geoglows.get_reach_id()` function. The reach_id is used to get the forecasted streamflow, historical simulation, and return periods.

Once the reach_id is obtained, use the following base URL to make requests to the server:

* Base URL: [geoglows.ecmwf.int/api/v2](geoglows.ecmwf.int/api/v2) 

Then use the following paths to get the desired data and replace `{reach_id}` with the reach_id obtained from the `geoglows.get_reach_id()` function. 

* `/dates`
* `/forecast/{reach_id}`
* `/forecaststats/{reach_id}`
* `/forecastensembles/{reach_id}`
* `/forecastrecords/{reach_id}`
* `/retrospective/{reach_id}`
* `/returnperiods/{reach_id}`
* `/dailyaverages/{reach_id}`
* `/monthlyaverages/{reach_id}`
* `/annualaverages/{reach_id}`
* `/hydroviewer/{reach_id}`
* `/getReachID`

# How to get results using geoglows python package

The data module provides functions for requesting forecasted and historical data river discharge simulations.
The data can be retrieved from the REST data service hosted by ECMWF, or it can be retrieved from the repository
sponsored by the AWS Open Data Program. The speed and reliability of the AWS source is typically better than
the REST service.

In general, each function requires a river ID. The name for the ID varies based on the streams network dataset. 
It is called LINKNO in GEOGLOWS which uses the TDX-Hydro streams dataset. This is the same as a reach_id or 
common id (COMID) used previously. The LINKNO can be found by using the `geoglows.get_reach_id()` function. 

## Forecasted Streamflow
* `geoglows.data.forecast()`
* `geoglows.data.forecast_stats()`
* `geoglows.data.forecast_ensembles()`
* `geoglows.data.forecast_records()`

## Historical Simulation
* `geoglows.data.retrospective()`
* `geoglows.data.return_periods()`
* `geoglows.data.daily_averages()`
* `geoglows.data.annual_averages()`