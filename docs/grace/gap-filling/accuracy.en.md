# Fill Accuracy

The fill was tested on months that do have data. Some observed months are hidden, the model is refitted without them, and the filled values
are compared with the real ones. There are two tests:

- **Single months:** 10% of the observed months (26 months), chosen at random through the record, are hidden together.
- **Long gaps:** an 11-month block is hidden, to mimic the gap between the missions. This is repeated for six blocks spread through the
  record.

Each test compares the seasonal model with two simpler fills: the trend and seasonal cycle without the residual correction, and linear
interpolation between the neighboring observed months. The table gives the root-mean-square error (RMSE) of each, in cm, with the median ±1σ
GRACE uncertainty of the region for comparison:

**Single months** (RMSE, cm):

| Region | ±1σ | Seasonal model | Trend + seasonal | Linear |
|---|---|---|---|---|
| Northern Midwest Aquifer System | 4.4 | 1.3 | 2.4 | 1.1 |
| Volta basin | 3.9 | 1.6 | 2.5 | 2.0 |
| Iullemeden-Irhazer Aquifer System | 1.9 | 0.9 | 1.1 | 0.8 |
| California Central Valley | 3.4 | 3.1 | 5.3 | 3.3 |

**11-month blocks** (RMSE, cm):

| Region | ±1σ | Seasonal model | Trend + seasonal | Linear |
|---|---|---|---|---|
| Northern Midwest Aquifer System | 4.4 | 1.5 | 2.3 | 4.7 |
| Volta basin | 3.9 | 2.6 | 2.4 | 5.1 |
| Iullemeden-Irhazer Aquifer System | 1.9 | 1.4 | 1.4 | 1.7 |
| California Central Valley | 3.4 | 4.2 | 4.8 | 5.2 |

Three results stand out:

- For single months, the seasonal model is about as good as linear interpolation, as expected: across one month, the residual correction makes
  the two nearly the same.
- For 11-month gaps, linear interpolation cuts straight through a whole seasonal cycle, and its error is two to three times that of the
  seasonal model in regions with a strong cycle (4.7 against 1.5 cm for the Northern Midwest).
- In the first three regions the error of the seasonal model is well below the GRACE uncertainty. California's Central Valley fills less
  well, with errors above the uncertainty, because its storage is driven by multi-year droughts and wet years that no average seasonal cycle
  can predict inside a long gap.

The error of a filled value comes from the model rather than from GRACE, so the app doesn't draw the uncertainty band for filled months. In a
region like the Central Valley, treat results that depend on filled months with extra caution, such as recharge for the years the
[Recharge Analysis](../recharge/results.md#the-table) marks as using filled months.
