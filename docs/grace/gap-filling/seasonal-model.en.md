# The Seasonal Model

## Why fill the gaps

The GRACE record is missing 35 of its months: scattered single months, mostly between 2011 and 2017, and the 11 months between the end of
GRACE and the start of GRACE-FO (see [The GRACE Mission](../background/grace-mission.md#the-record-and-its-gaps)). Trend analysis in the app
skips missing months. Analyses that work year by year need a value for every month. In the
[Recharge Analysis](../recharge/wtf-method.md), for example, a missing month at a seasonal peak or trough changes that year's result.

The **Seasonal model** option of the **Gap filling** control (see [Gap Filling](../app/gap-filling.md) in Part 2) estimates each missing month
from the rest of the record, following the approach of Barbosa et al. (2022). This page gives the model; the pages that follow give how it is
[fitted](fitting.md), how the [filled values](filling.md) are computed, and how [accurate](accuracy.md) they are.

## Trend, seasonal cycle and residual

The series is split into a long-term trend, a seasonal cycle that repeats every year, and a residual:

$$
y(t) = T(t) + S(m) + r(t)
$$

where *y*(*t*) is GWSa (or TWSa) in month *t*, *m* is the calendar month of *t* (January to December), *T* is the trend, *S* is the seasonal
cycle and *r* is the residual, the part of each month's value that the trend and the seasonal cycle don't explain.

## The trend

The trend is a continuous piecewise straight line with up to three breakpoints *b*<sub>1</sub>, …, *b*<sub>k</sub>, where its slope changes:

$$
T(t) = \beta \, t + \sum_{j=1}^{k} \gamma_j \max(t - b_j,\, 0)
$$

Time *t* is counted in months from the first observed month. Each hinge term max(*t* − *b*<sub>j</sub>, 0) is zero before its breakpoint and
rises one per month after it, so the slope is *β* before the first breakpoint, *β* + *γ*<sub>1</sub> after it, and so on. The line bends at each
breakpoint without jumping. A record with *k* = 0 has a single straight trend.

## The seasonal cycle

The seasonal cycle has one level for each calendar month, *α*<sub>Jan</sub>, …, *α*<sub>Dec</sub>. The full model for an observed month *i*
is

$$
y_i = \beta \, t_i + \sum_{j=1}^{k} \gamma_j \max(t_i - b_j,\, 0) + \alpha_{m_i} + \varepsilon_i
$$

The twelve levels also act as the intercept, so there is no separate constant term. The levels are fixed from year to year: the model has one
average annual cycle, and a wet year shows up in the residual rather than in *S*.

## Reference

Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
[doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
