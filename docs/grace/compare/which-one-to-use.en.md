# Which One to Use

Neither dataset wins everywhere. [What the Differences Look Like](examples.md) shows the cases this advice is drawn from,
[Exploring the Differences in the App](exploring.md) shows how to put your own region on the same footing, and
[How Far This Is Validated](validation.md) says how much weight the advice can carry.

## The short answer

| What you want | Use | Because |
|:---|:---|:---|
| A depletion or recovery rate, in cm/yr or km³/yr | GRACE | 2.2 flattens trends to roughly a quarter |
| The shape and timing of the seasonal cycle | 2.2 where soil moisture swings as hard as total water, otherwise either | the subtraction can flip the timing |
| A region a few cells across | 2.2 | averaged on 0.25° where the other is on 1° |
| An unbroken monthly series | 2.2 | the model runs through the GRACE gaps |
| Recharge by the WTF method | GRACE | Barbosa et al. (2025), plus the risk of a flipped season |
| An uncertainty figure per cell | GRACE | 2.2 publishes none |
| Anything before February 2003 | GRACE | the 2.2 record starts there |
| A result you mean to publish | both | and say where they agree and where they do not |

Two independent answers that agree are hard to explain away. Where they disagree, plot the pieces: a gap that lives in soil moisture is a
different problem from one that lives in total water.

## The check to run before trusting a seasonal cycle

One comparison tells you whether the GRACE route's seasonal timing can be trusted in your region, and it takes a minute in the app.

1. Open your region and plot **SMa** and **TWSa** for the GRACE dataset.
2. Compare the height of their seasonal cycles, low month to high month.
3. If soil moisture swings about half as far as total water or less, the GRACE groundwater cycle has a shape of its own. Either dataset will
   do for seasonal questions.
4. If soil moisture swings as far as total water or further, the subtraction is cancelling most of the signal. Prefer 2.2 for the shape and
   timing of the cycle, and do not read the month of the GRACE peak as the month the water table is highest.

Across 299 aquifers that ratio predicts the agreement between the two seasonal cycles at a correlation of −0.75. Below 0.7 the median agreement
is 0.93; above 1.0 it is −0.39.

For the answer without the arithmetic, set **Color by** to **GRACE vs GLDAS 2.2: agreement** and look at the color of your region: brown means
the two cycles run opposite, which is what a cancelling subtraction produces (see
[Exploring the Differences in the App](exploring.md#the-agreement-map)).

## Before treating a large difference as a result

1. Plot snow water (**SWEa**). Ice and snow explain most of the extremes, and a groundwater cycle shaped like the snow cycle upside down is the
   snow term.
2. Plot total water (**TWSa**) for both datasets. Where the totals agree and only the groundwater disagrees, the two are dividing the column
   differently and the satellite measurement itself is not in question.
3. Compare the seasonal swing of soil moisture (**SMa**) against total water, as above.
4. Check how much water is actually moving. Below about 5 cm of variation the two datasets correlate at a median of 0.19, and that number says
   nothing about either one.
5. Ask whether a river, a floodplain, a lake or a reservoir could account for the water.

The three comparison maps run steps 3 and 4 over every region in a set at once, which is the quick way to see whether your region is an outlier
or one of many (see [Exploring the Differences in the App](exploring.md)).

## What GWSa is good for, in either dataset

Both datasets answer regional questions about direction and rate: is storage in this aquifer declining, how fast, and did the decline slow after
a policy change or a run of wet years. Neither is suited to decisions at the scale of a well field or a single irrigation district, and neither
says anything about water levels or water quality. Both average storage change over an area far larger than a well field, and both put surface
water into the groundwater term.

Where monitoring wells exist, compare the trend with storage change estimated from the wells. That comparison is the strongest check available on
either dataset, and agreement between the two strengthens both.

## References

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
