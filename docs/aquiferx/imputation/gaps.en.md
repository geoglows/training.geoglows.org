# Gaps in Well Records

A program measures a set of wells twice a year for a decade, loses its funding, and starts again years later with other wells; a well
goes dry or is replaced; a new monitoring network begins long after the old one stopped.
The records that result are runs of readings separated by gaps of months to decades, and they start and stop at different times.

In Escalante Valley-Beryl-Enterprise in the Utah sample, 289 of the 713 wells have five or more readings. Of those 289, 149 have a gap
of more than two years somewhere in their record, 116 have no readings after 1957, and 35 were read after 2020.

## Why gaps matter

The chart joins a well's readings with a PCHIP curve, and across a gap of years that curve is a smooth join that knows nothing of the
droughts, pumping seasons or recoveries in between (see [The Time Series Chart](../timeseries/chart.md#what-the-curve-can-tell-you)).
A water table map needs a value at each of its wells on the map's date, and Spatial Analysis reads that value off the curve, so a gap
carries straight into the maps. Before a well's first reading and after its last there is no curve at all, and the well drops out of
the maps for those dates. A run of maps over several decades then draws each year from a different set of wells, and some of the
change from one map to the next comes from wells joining and leaving.

## What Impute Gaps does

**Impute Gaps** gives each well of an aquifer a series of monthly water levels covering December 1957 to the latest month of the soil
moisture record. Where the readings are close together, a month's value is the PCHIP curve on the first of the month. In a gap longer
than a limit you set, two years to start with, and before a well's first reading and after its last, the value comes from a model of
the well: an extreme learning machine (ELM), a kind of neural network that trains in a single step. Each well gets its own, the
average of five ELMs trained on the well's record to relate its water level to soil moisture in the aquifer's area, the year and the
month. In each stretch it fills,
the model is shifted to meet the PCHIP curve at both ends, so the series carries on without a jump where one hands over to the other.

An ELM trains in one step because the weights of its hidden layer are drawn at random and only its output is fitted. Each run draws
new weights and so builds a new model of each well. Two runs give the same values in the months that follow PCHIP and different values
in the gaps, and averaging five ELMs narrows the difference: between two runs on Escalante, half the wells changed by more than 1.2 ft
somewhere in their gaps, and one in ten by more than 5.6 ft, where a single ELM per well gave 3.1 ft and 12 ft.

The series are saved together as a model of the aquifer, which you can open on the chart (see [Reading the Results](results.md)) and
use in place of the readings for water table maps (Part 5). In Escalante the model covers 159 wells, and almost three quarters of
their months come from the ELM. The approach is that of Evans et al. (2020), who filled well records with an
ELM driven by Earth observation data, soil moisture among them, and found its estimates more accurate than kriging's.

Each run also tests the model on readings it never saw. It hides five years of readings from the middle of each well's record, which
leaves a gap long enough for the model to fill, fits the well again without them, and compares the model and the PCHIP curve across
the gap with the hidden readings in the months the model fills. The chart gives the result for each well and Get Info for the aquifer (see
[Reading the Results](results.md#the-hidden-readings-check)).

[Running an Imputation](running.md) walks through the wizard, [How the Model Works](method.md) gives the method in full, and
[Reading the Results](results.md) covers the chart and the saved model.

## How close the filled values come

A gap-filling method can be tested by hiding readings that exist, filling them, and comparing. A Python copy of the app's method did
this for every well with eight or more readings in the four Sample Data aquifers: Escalante Valley-Beryl-Enterprise, East Shore Area
and Central Sevier Valley in Utah, and Williamson in Oregon. It hid 3, 5 or 10 years of a well's readings, from the middle of its
record or from the end, ran the method on the rest with the default Gap Size and Pad Size, and measured the RMSE against the hidden
readings in the months the model filled. A stretch hidden from the middle leaves a long gap, and there the model was compared with
the PCHIP curve across it. Past the last reading there is no curve, and the model was compared with the last reading held level.

| Hidden stretch | Wells | PCHIP across it, or the last reading | The model | Wells where the model came closer |
|---|--:|--:|--:|--:|
| 3 years, middle of the record | 217 | 2.1 ft | 2.6 ft | 48% |
| 5 years, middle | 202 | 2.9 ft | 3.6 ft | 37% |
| 10 years, middle | 163 | 3.4 ft | 4.8 ft | 36% |
| 3 years, end of the record | 243 | 3.4 ft | 3.1 ft | 43% |
| 5 years, end | 241 | 4.2 ft | 4.8 ft | 46% |
| 10 years, end | 203 | 6.4 ft | 6.6 ft | 45% |

The model is the app's: five ELMs averaged and shifted to meet the curve. The RMSEs are medians over the wells. In the long gaps, the PCHIP curve came closer to the hidden readings than the model at most
wells, and more so the longer the gap; past a well's last reading, the model did about as well as holding that reading level.
Central Sevier Valley was the exception: there the two came out about even in the long gaps, and with 10-year gaps the model was
closer. A heavier penalty λ, fewer hidden units and a plain linear fit of the same inputs all left the model short of PCHIP in the
long gaps.

These are four aquifers, three of them in Utah, and the model may do better where water levels follow wet and dry years more closely.
The check each run makes gives the same comparison for your own wells.

## What the model can and cannot know

The model learns, for each well, how the water level followed soil moisture, the year and the month over the months the well was
read, and carries that relationship into the gaps. That suits a well whose level rises and falls with wet and dry years,
or that declines at a steady rate. A new well field pumping nearby, a canal lined, a recharge basin built or a pump switched off leaves
no mark on soil moisture, so a change of that kind during a gap does not show in the filled values. Before a well's first reading and
after its last, the model stretches a relationship learned from other years, sometimes across decades.

### Limits of the method

- **R² and RMSE score the model on the months it was trained on.** They compare it with the PCHIP values it was fitted to, so they
  show how well it reproduces those months (see [How the Model Works](method.md#the-fit-statistics)). With 500 adjustable weights it
  can reproduce almost any record: in Escalante the median R² is 0.955, and wells with only 6 months of record score above 0.9.
  On readings they had not seen, the same fits missed by about twice their RMSE or more. The hidden-readings check measures that.
- **The model's line zigzags.** Its twelve month inputs let it draw a seasonal pattern, which it repeats in every year it fills, and
  the month's own soil moisture adds swings of its own. More than half of the years in Escalante's modeled wells have a single
  reading, so most records hold little of a real seasonal cycle for it to learn. Its value changes about 1.4 times as much from one month
  to the next as the PCHIP curve's. A single ELM refitted without the month inputs is half as rough, though in most tests no closer
  to the hidden readings. A moving average, on the chart or in Spatial Analysis, evens it out.

Treat the filled values as estimates. Look at the hidden-readings check in Get Info, and on the chart for the wells that matter most
to you. Where PCHIP came closer, maps from the readings may fill the long gaps better, though each well leaves those maps before
its first reading and after its last, where only the model gives it a value. Compare the model with the readings
on either side of each gap, and leave out of a map, or use with care, a well whose model wanders.

## References

Evans, S., Williams, G. P., Jones, N. L., Ames, D. P., and Nelson, E. J. (2020). Exploiting Earth observation data to impute
groundwater level measurements with an extreme learning machine. *Remote Sensing*, 12(12), 2044.
