# Gap-Filling Method

## Why fill the gaps

The GRACE record is missing 35 of its months: scattered single months, mostly between 2011 and 2017, and the 11 months between the end of
GRACE and the start of GRACE-FO (see [The GRACE Mission](../background/grace-mission.md#the-record-and-its-gaps)). Trend analysis in the app
handles gaps by skipping them. Analyses that work year by year, such as estimating recharge with the
[water table fluctuation method](../recharge/wtf-method.md), need a value for every month: a missing month at a seasonal peak or trough changes that
year's result.

The app fills the gaps with a seasonal model (see [Gap Filling](../app/gap-filling.md) in Part 2). This page describes that model and how well it
works.

## Method

The app fills gaps with a statistical model of the series, following the approach of Barbosa et al. (2022):

```text
GWSa(t) = trend(t) + seasonal(month of t) + residual(t)
```

1. **Trend.** A piecewise straight line, allowed to bend at up to three breakpoints, captures the long-term rise or decline. The model
   chooses the number and position of the breakpoints automatically, adding a breakpoint only when it improves the fit substantially (by the
   Bayesian information criterion), and keeps every segment at least three years long.
2. **Seasonal cycle.** One value for each calendar month, the average departure from the trend in that month. Together with the trend this gives
   the model value for any month.
3. **Residual.** The difference between the observed value and the model in the months on either side of a gap. The model interpolates the
   residual linearly across the gap and adds it to the model value, so the filled months join the observed record smoothly at both ends.

Observed months are never changed.

For the Northern Midwest Aquifer System, the model finds three breakpoints, in September 2006, May 2013 and October 2017, splitting the
record into four trend segments of +1.3, −0.7, +2.9 and −0.5 cm/yr:

![Observed GWSa for the Northern Midwest Aquifer System with the four-segment trend and the filled months in red](../../static/images/grace/gap-filling-example.png)

For a single missing month, the filled value is close to a straight line between its neighbors. For the 11-month gap between missions, it
follows the seasonal cycle and the trend, which a straight line can't. The app shows the same filled values with the **Seasonal model**
option, without the trend:

![The same series in the app with Gap filling set to Seasonal model](../../static/images/grace/app-gap-fill-seasonal.webp)

## How good is the fill?

The fill was tested by hiding months that do have data, filling them, and comparing the result with the real values, in two
tests: hiding 10% of the months one at a time, and hiding 11-month blocks at several places in the record to mimic the gap between missions. For
the Iullemeden-Irhazer Aquifer System, the filled values are typically within about 1 to 1.5 cm of the truth in both tests, smaller than the
GRACE uncertainty of about 2 cm. Regions with large year-to-year swings, such as California's Central Valley, fill less well, because no model
can predict an unusually wet or dry year inside a long gap.

In regions like these, treat results that depend on filled months with extra caution, such as recharge for the years the
[Recharge Analysis](../recharge/results.md#the-table) marks as using filled months.

## Reference

Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
[doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
