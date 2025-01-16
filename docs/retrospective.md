# Retrospective Data

The retrospective simulation in the GEOGLOWS Model provides a deterministic dataset with daily resolution, offering over 85 years of historical streamflow data from January 1, 1940, to the near present. Each of the 6 million river segments in the GEOGLOWS model has its own retrospective time series available for download. The plot below shows an example of the retrospective data for one river.

![image](image4.png)

---

The dataset is deterministic, which means that there is no ensemble, but rather just one best guess of the average flows over the time period. The flow values represent the average flow during the day listed in UTC time. All flow values are in cubic meters per second.

- The inputs to the hydrology model lag from real time by 5 days.
- Once a week, on Sunday at midnight UTC, the dataset is updated. On that Sunday, GEOGLOWS data will cover up until 5 days ago. On Saturday night, the lag will have accumulated to 12 days.

---

## Runoff Data and Flow Estimates

The runoff data is created by using the runoff data from the **ECMWF ERA5 reanalysis dataset** as an input to the GEOGLOWS model. Then, a modification of Muskingum-Cunge routing is applied to route the water through the stream network, providing the flow estimates.

- The inputs to the model are derived from reanalysis meteorology data, including **satellite and gauge-based measurements**, which are assimilated to reconstruct the best possible historical precipitation, evaporation, and other hydrological variables.
- No river gauge data are assimilated during the routing step, ensuring a **uniform model-driven approach**.

For more details, refer to the document: [01. ERA5_time period_updates.pdf](https://drive.google.com/file/d/10P53NdkSTfsGsyc-PSE5nVMYAvMCU1Q-/view?usp=sharing).



