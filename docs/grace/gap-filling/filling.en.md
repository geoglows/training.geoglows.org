# Filling the Gaps

A gap is a run of one or more missing months between two observed months, *a* before it and *c* after it. The model alone, *T* + *S*, would
not meet the observed values at either end of the gap, because each observed month has its own residual. The filled value adds a residual
correction that is interpolated linearly across the gap:

$$
\hat{y}_g = T(t_g) + S(m_g) + r_a + \frac{t_g - t_a}{t_c - t_a}\,(r_c - r_a), \qquad r_a = y_a - T(t_a) - S(m_a), \quad r_c = y_c - T(t_c) - S(m_c)
$$

for each missing month *g* in the gap.

The correction gives the fill a sensible shape whatever the length of the gap:

- For a single missing month, the seasonal change from one month to the next is small, so the filled value is close to a straight line between
  its two neighbors.
- For a long gap, such as the 11 months between the missions, the filled months follow the trend and the seasonal cycle, rising and falling
  with the usual seasons, while the correction shifts them to meet the observed values at both ends.

Observed months are never changed. Months before the first observation or after the last are left empty, because there is no observed value on
the far side to anchor a correction to.

GWSa and TWSa are each filled from their own record, with their own trend and seasonal cycle. A filled GWSa value is therefore not exactly the
filled TWSa minus the GLDAS terms for that month. The GLDAS layers have no gaps and are never filled.

## Example: the Northern Midwest Aquifer System

For the Northern Midwest Aquifer System, the BIC selects three breakpoints, in September 2006, May 2013 and October 2017, which split the record
into four trend segments of +1.3, −0.7, +2.9 and −0.5 cm/yr:

![Observed GWSa for the Northern Midwest Aquifer System with the four-segment trend and the filled months in red](../../static/images/grace/gap-filling-example.png)

The single missing months between 2011 and 2017 sit close to their neighbors. Across the 11-month gap between the missions, the filled values
rise to 12.8 cm in September 2017 and fall to 4.8 cm in March 2018 before meeting the first GRACE-FO month, carrying on the region's annual
cycle. The app shows the same values with **Gap filling** set to **Seasonal model**:

![The same series in the app with Gap filling set to Seasonal model](../../static/images/grace/app-gap-fill-seasonal.webp)
