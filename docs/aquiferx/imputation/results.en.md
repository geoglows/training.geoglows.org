# Reading the Results

## Opening a model

A saved model appears in the tree under its aquifer, beside the aquifer's water table maps. In the Utah sample, Escalante
Valley-Beryl-Enterprise, East Shore Area and Central Sevier Valley each have one named `mc_lnn`, built with the default settings, and
so does Williamson in the Oregon sample. Click a model to open it and again to close it; a dot marks the open one. Pointing at it
shows its months, how many wells it fills and how many of them by MC+LNN, and when it was made.

With a model open and one well selected, the chart shows the model's series for that well in place of its readings. A band across
the top names the model, holds the **Combined** checkbox, and gives the well's R² and RMSE (see
[How MC+LNN Works](method.md#the-fit-statistics)) and the result of its hidden-readings check (below). For a well MC+LNN could not
fill, the band reads *PCHIP and held readings only*, and pointing at it gives the reason. A well the model left out reads *This well
is not in the model*, with the two settings it missed, and with two or more wells selected the chart goes back to the readings.

## The filled series

![The Escalante model on (C-36-16) 3ddc- 1 with Combined checked: PCHIP in red, MC+LNN in blue](../../static/images/aquiferx/impute-combined.webp)

With **Combined** checked, the chart shows the series the model saved, colored by how each month was filled: red for PCHIP, blue for
MC+LNN and dashed gray for a held reading, with the readings as green dots (see [How MC+LNN Works](method.md#the-saved-series)).
(C-36-16) 3ddc- 1 in Escalante was read 82 times from December 1953 to March 2026, and from 1979 on once a year, in March. Each gap
between those readings is a year long, so from 1979 MC+LNN fills eleven months of every year and PCHIP keeps the months with
readings. MC+LNN also fills the ten years before December 1953 and the months of 2026 after the last reading. At the scale of the
whole record the red, one month a year, barely shows; the figure in [Gaps in Well Records](gaps.md#what-impute-gaps-does) shows the
pieces over a few years.

## MC+LNN's estimate

![The same well with Combined unchecked: MC+LNN's estimate for every month beside the readings and their PCHIP curve](../../static/images/aquiferx/impute-separate.webp)

With **Combined** unchecked, as it is when a model opens, the chart shows MC+LNN's estimate for every month in blue, the PCHIP curve
through the readings in red, and the readings as green dots. In a gap of 6 months or more, the blue line is what the model saved. In a month with a
reading, it is the estimate made with that sixth of the record left out (see [How MC+LNN Works](method.md#the-readout)), so the
line jumps wherever the estimate misses the reading. At 3ddc- 1 it keeps within a few feet of the readings through 2012, and from
2013 on it spikes above them each March, by 1 ft in 2013 and 33 ft in 2026: fitted on the readings up to 2012, the regression did
not foresee how fast the well fell after it. Those misses make most of the well's RMSE of 6.77 ft. The saved series is not
affected, because in a month with a reading it keeps the PCHIP value.

A reading inside the model's months sits on the nearest first of the month, and a reading outside them keeps its date, so the axis
reaches out to it.

The chart's controls change while a model is on the chart:

- **MAvg** draws a moving average of the saved series as a dashed orange line, with its window in **months**, with the same Gaussian
  weights as on the readings' chart (see [The Time Series Chart](../timeseries/chart.md#moving-average)). It is offered with
  **Combined** checked.
- **GSE** draws the well's ground surface elevation, in either view.
- **PCHIP**, **Trend Line** and **View/Edit** are hidden until the model is closed.
- **Export CSV** downloads the well's monthly series as `<well>_model_<model>.csv`, with the columns Date, Value (the saved series),
  Filled by (PCHIP, MC+LNN or held reading) and MC+LNN (its estimate, empty for a well MC+LNN could not fill).

Pointing at the chart shows the month and each value to two decimals. Under the chart, **Processing Log** opens the log of the run that
made the model, with a line for each well and its check.

## The hidden-readings check

The last item in the band compares MC+LNN with readings it never saw (see
[How MC+LNN Works](method.md#the-hidden-readings-check)). For 3ddc- 1 it reads *Hidden readings: MC+LNN 1.22 · PCHIP 2.04 ft*: the
run hid five years of the well's record, the five readings from March 1979 to March 1983, filled the well again without them, and
compared that fill and the PCHIP curve across the gap with the hidden readings. The numbers are the RMSE of each, and pointing at the
item gives the dates and how many readings were scored. A well with too few readings around the middle of its record shows
*No hidden-reading check*.

Get Info gives the same comparison for the aquifer: how many wells were checked, at how many MC+LNN came closer than PCHIP, and the
median RMSE of each. For Escalante, MC+LNN came closer at 87 of the 109 wells checked, with a median RMSE of 1.47 ft against PCHIP's
2.39 ft.

The check covers a long gap in the middle of a record. Maps made from the measurements fill such a gap with the PCHIP curve, so where
MC+LNN came closer at most wells, maps made from the model fill those gaps better.

## Managing models

The three dots beside a model open its menu:

- **Edit** renames it, and its file with it.
- **Get Info** shows the model's title, code, aquifer and date; its settings (the months it covers, the wells it fills, the limit
  beyond each record, and PCHIP for gaps under 6 months and MC+LNN for longer ones); how many wells it fills, how many by MC+LNN and
  how many by PCHIP and held readings only, with the median R² and RMSE of the MC+LNN wells; and the hidden-readings check for the
  aquifer.
- **Delete** removes it, after you confirm.

Sample Data models can be opened and inspected but not renamed or deleted.

A model made before November 2026 used an older method, an extreme learning machine driven by soil moisture. It is listed struck
through, marked *older method*, and can no longer be opened. Clicking it offers to delete it; run Impute Gaps again to replace it.
Maps made from it keep working, since a map stores its own values.

## Using a model for water table maps

In Spatial Analysis, an aquifer with a saved model offers a **Data Source** choice, **Measurements** or **Imputed Data**. With
Imputed Data, each map takes its well values from the chosen model's saved series instead of from the readings: **Direct** takes the
series' value in the map's month, and **Moving Average** a moving average of it over a window you set. The wells on the maps are the
model's, and each keeps a value as long as its series runs, so the same wells stay on the maps from one year to the next. The
`kriging_mc_lnn` maps of Williamson, Central Sevier Valley and East Shore Area in the Sample Data were made this way with Direct.
Part 5 covers Spatial Analysis in full.

## Reading a model with care

- Start with the hidden-readings check, in Get Info for the aquifer and in the band for each well. It tests MC+LNN in a long gap,
  where the neighbors may be estimates themselves.
- Look at the wells that matter to you with **Combined** unchecked, and check how the blue line behaves next to the readings. Where
  it misses the readings by a wide margin in some stretch of the record, its values in the gaps of that stretch are doubtful too.
- R² and RMSE come from estimates made with a sixth of the record left out at a time. The first and last sixths are predicted from
  the rest alone, so a well whose level changed course late in its record can score poorly even where its gaps are filled well, as
  3ddc- 1 does.
- Values before a well's first reading and after its last follow the neighbors and the seasons, up to the limit you set. A change
  that reached the well and not its neighbors does not show in them.
- The same readings and settings always give the same model, so a second run changes nothing. To see how much a well depends on
  its readings, edit or remove a doubtful reading, of the well or of a neighbor, and run Impute Gaps again under a new title.
