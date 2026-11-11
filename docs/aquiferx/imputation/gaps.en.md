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
the well: an extreme learning machine (ELM), a kind of neural network that trains in a single step. Each well gets its own, trained on
the well's record to relate its water level to soil moisture in the aquifer's area, the year and the month.

The series are saved together as a model of the aquifer, which you can open on the chart (see [Reading the Results](results.md)) and
use in place of the readings for water table maps (Part 5). In Escalante the model covers 159 wells, and almost three quarters of
their months come from the ELM. The approach is that of Evans et al. (2020), who filled well records with an
ELM driven by Earth observation data, soil moisture among them, and found its estimates more accurate than kriging's.

[Running an Imputation](running.md) walks through the wizard, [How the Model Works](method.md) gives the method in full, and
[Reading the Results](results.md) covers the chart and the saved model.

## What the model can and cannot know

The model learns, for each well, how the water level followed soil moisture, the year and the month over the months the well was
read, and carries that relationship into the gaps. That suits a well whose level rises and falls with wet and dry years,
or that declines at a steady rate. A new well field pumping nearby, a canal lined, a recharge basin built or a pump switched off leaves
no mark on soil moisture, so a change of that kind during a gap does not show in the filled values. Before a well's first reading and
after its last, the model stretches a relationship learned from other years, sometimes across decades.

### Limits of the method

- **The fit statistics flatter it.** R² and RMSE are measured over the months the model learned from (see
  [How the Model Works](method.md#the-fit-statistics)), and with 500 hidden units it can follow even a short record closely: in
  Escalante the median R² is 0.955. They tell you how closely the model follows the record, and
  nothing about its values in the gaps.
- **Runs differ.** The model starts from random weights, so a second run gives different values in the gaps. Between two runs on
  Escalante, half the wells changed by more than 2.5 ft somewhere in their gaps, and one in ten by more than 12 ft.
- **The series can step.** Where it passes from PCHIP to the model, or back, the two rarely meet exactly. In Escalante half of these
  steps are under 1.3 ft, one in ten is over 7.5 ft, and the largest is 31 ft.
- **The model is jumpy.** Each month's value comes from that month's inputs alone, so it moves about twice as much from one month to
  the next as the PCHIP curve does. A moving average, on the chart or in Spatial Analysis, evens it out.

Treat the filled values as estimates: open the wells that matter most to you, compare the model with the readings on either side of
each gap, and leave out of a map, or use with care, a well whose model wanders.

## References

Evans, S., Williams, G. P., Jones, N. L., Ames, D. P., and Nelson, E. J. (2020). Exploiting Earth observation data to impute
groundwater level measurements with an extreme learning machine. *Remote Sensing*, 12(12), 2044.
