# Retrospective Data

The retrospective simulation from RFS provides a deterministic dataset with daily resolution, offering over 85 years of historical streamflow data from January 1, 1940 to the near present. Each of the 6 million river segments in RFS has its own retrospective time series available for download. The plot below shows an example of the retrospective data for one river.

![image](../../static/images/retrospective_graph.png)

---

The dataset is deterministic, which means that there is no ensemble, but rather just one best guess of the average flows over the time period. The start of the time period is given in UTC time. The value given represents the average flow starting at that time until the next timestep. All flow values are in cubic meters per second.  

The inputs to RFS lag from real time by 5 days. Once a week, on Sunday at midnight UTC, the dataset is updated. On that Sunday, RFS will cover up until 5 days ago. On Saturday night, the lag will have accumulated to 12 days.  

The retrospective data is available in several different time increments. The data was calculated at an hourly temporal resolution. Then the hourly timesteps were averaged to provide a daily average, monthly average, and yearly average time series.   

The monthly average data is available in two different formats. One is optimized to read the entire time series for a single river or group of rivers, which is anticipated to be the most common use case. Another is optimized to read a bunch of rivers at a given timestep. 


---

## Runoff Data and Flow Estimates

The runoff data is created by using the runoff data from the **ECMWF ERA5 reanalysis dataset** as an input to RFS. Then, a modification of Muskingum-Cunge routing is applied using a method called RAPID to route the water through the stream network, providing the flow estimates.

The inputs to the model are derived from reanalysis meteorology data, including satellite and gauge-based measurements, which are assimilated to reconstruct the best possible historical precipitation, evaporation, and other hydrological variables. No river gauge data are assimilated during the routing step, ensuring a uniform model-driven approach.

## Return Period Calculations

The retrospective simulation is used to define return periods that establish warning levels for each simulated river segment. Streamflow values for return periods of 2, 5, 10, 25, 50 and 100 years are calculated for every stream reach in the model.



