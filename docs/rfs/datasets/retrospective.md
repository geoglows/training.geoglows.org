## Terms and Vocabulary

- **ERA5**: The fifth generation of ECMWF atmospheric reanalysis of the global climate. It is the most recent reanalysis dataset produced by the
  European
  Centre for Medium-Range Weather Forecasts (ECMWF). It is available from 1940 to present and is updated daily with a 5-day lag.
- **Reanalysis**: A modeled product which incorporates in situ and/or remote sensing data to provide the best possible estimate of historical
  hydrometeorology conditions. Reanalysis data are used as inputs to the RFS model.

---

## Overview

The retrospective simulation from RFS is an 85+ year deterministic model simulation at hourly resolution beginning 1 January 1940. The retrospective
simulation and many derivative products are updated weekly. It is based on the ERA5 dataset. New ERA5 are produced each day with 5 days of lag from
real time so the least amount of lag possible is 5 days. Once a week, all new ERA5 data since the last simulation are used to extend the retrospective
simulation bringing the lag back down to 5 days.

![image](../../static/images/retrospective_graph.png)

The dataset is deterministic and based on reanalysis land surface modeling which means that there is only 1 value per timestep unlike the forecasts.
The retrospective simulation provides hourly average flows which are resampled to daily, monthly, and yearly averages. Flows are reported as the
average that occurred over the following interval (hour, day, month, or year). Dates are reported at the start of an interval in UTC +00:00 time
zone (e.g. "left aligned" dates). The value given represents the average flow starting at that time until the next timestep. All values are in cubic
meters per second.

The monthly average data is available in two different formats. One is optimized to read the entire time series for a single river or group of rivers,
which is anticipated to be the most common use case. Another is optimized to read a bunch of rivers at a given timestep.

| Model Property           | Retrospective Simulation   |
|--------------------------|----------------------------|
| Earliest Date            | 01 January 1940            |
| Simulation Type          | Deterministic              |
| Ensemble Members         | 1                          |
| Lag time                 | 5-12 Days from present     |
| Time Step                | Hourly average             |
| Update Frequency         | Weekly on Sunday 00:00 UTC |
| Bulk Download Available  | Yes                        |
| Query & Subset Available | Yes                        |

---

## Runoff Data and Flow Estimates

The runoff data is created by using the runoff data from the **ECMWF ERA5 reanalysis dataset** as an input to RFS. Then, a modification of
Muskingum-Cunge routing is applied using a method called RAPID to route the water through the stream network, providing the flow estimates.

The inputs to the model are derived from reanalysis meteorology data, including satellite and gauge-based measurements, which are assimilated to
reconstruct the best possible historical precipitation, evaporation, and other hydrological variables. No river gauge data are assimilated during the
routing step, ensuring a uniform model-driven approach.

## Return Period Calculations

The retrospective simulation is used to define return periods that establish warning levels for each simulated river segment. Streamflow values for
return periods of 2, 5, 10, 25, 50 and 100 years are calculated for every stream reach in the model.



