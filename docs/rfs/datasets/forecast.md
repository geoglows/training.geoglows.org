## Terms and Vocabulary

- **IFS**: Integrated Forecast System. The name of the coupled meteorology and land surface model used to generate forcings for the RFS results.

---

RFS produces ensemble streamflow forecasts using IFS data from the ECMWF. Daily forecasts are calculated at the ECMWF Supercomputing facility in
Bologna, Italy and are available by 12 PM UTC. Flows are reported in cubic meters per second. The forecast has a **3-hour time step**, where each flow
value represents the average flow that occurred in the river during the previous 3 hours. Below is an example graph showing all the ensemble members.

![image](../../static/images/img17.png)

Each forecast includes a **50+1 member ensemble** meaning there is **1 baseline (control)** prediction and **50 perturbations** (slight variations) of
the baseline condition.

Each day's forecast is initialized using the 24-hour mean value from the ensemble members on the previous day as the initial condition. The IFS data
have a spatial resolution of about 9 kilometers horizontally at the equator. The grid of IFS runoff values are mapped to RFS catchment boundaries
using GIS zonal statistics methods.

| Model Property           | Retrospective Simulation |
|--------------------------|--------------------------|
| Earliest Date            | 01 July 1940             |
| Simulation Type          | Ensemble                 |
| Ensemble Members         | 50+1                     |
| Lead time                | 15 Days                  |
| Time Step                | 3 hourly average         |
| Update Frequency         | Daily at 00:00 UTC       |
| Bulk Download Available  | Yes                      |
| Query & Subset Available | Yes                      |

## Interpreting an Ensemble Forecast

Each ensemble member has an equal probability of occurring. Therefore, forecasts are best understood by looking at summaries of the ensembles rather
than individual members.

Forecast plots are designed to help users interpret the range of possible outcomes and uncertainties. The most commonly used forecast plot includes
the median, the 20th percentile, and the 80th percentile. These represent 60% of the probability distribution within the ensemble members and provide
insight into the potential variability of future streamflow. This approach allows users to see the range of probable scenarios for their streams.

In the following example forecast plot, there are 3 areas to focus on:

- **Black Line:** The median of the 51 ensemble members (the "best guess" of river flow at each 3-hour period)
- **Blue Lines:** The 20th and 80th percentile values
- **Blue Shaded Area:** Represents the middle 60% of values from the ensemble predictions

![image](../../static/images/img8.png)

**How to interpret this graph**

1. The **black line** represents the best estimate of future river flow.
2. The **blue shaded region** represents the uncertainty in the prediction. The narrower the blue region, the more confident the model is. The true
   flow is more likely than not to fall within the blue shaded area.
