# Why the Two Datasets Differ

The app serves two groundwater records for the same month in the same cell, and they do not agree. This page covers where the disagreement comes
from. [Where Each One Is Trustworthy](trusting-each-one.md) covers which one to believe, and [Known Artifacts](known-artifacts.md) covers the
places where one of them is simply wrong.

[Deriving Groundwater Storage](../gldas/deriving-groundwater.md) gives both constructions in full. In short:

- **The GRACE route.** JPL measures total water storage. The app subtracts GLDAS 2.1's soil moisture, snow and canopy water, and reads the
  remainder as groundwater.
- **The GLDAS 2.2 route.** NASA runs the Catchment land surface model with GRACE assimilated into it, and the model reports a groundwater state
  directly. Nothing is subtracted.

These pages use the app's layer names throughout. **TWSa** is total water storage: every form of water held in the column at that place — soil
moisture, snow, water on leaves, surface water and groundwater together. **GWSa** is the groundwater part of it, **SMa** the soil moisture,
**SWEa** the snow and **CANa** the water held on vegetation. The *a* on each stands for anomaly: every value is a departure from that cell's own
2004–2009 average, in centimetres of water spread evenly over the cell. Zero means average conditions for that place, never an empty aquifer.

## What already differs before any water is counted

| | GRACE route | GLDAS 2.2 |
|:---|:---|:---|
| GRACE solution | JPL mascons, RL06.3 v04 CRI | CSR mascons, RL06 |
| Native GRACE footprint | 3° equal-area caps | 1° equal-area at the equator |
| Grid served | 1° | 0.25°, averaged to 1° for the global grid |
| Record begins | April 2002 | February 2003 |
| Missing months | the GRACE gaps, filled or flagged | none; the model runs through them uncorrected |
| Gain factors | JPL's, applied | none |
| Uncertainty layers | published per cell | none |
| Land cells on the 1° grid | 15,159 | 17,346 |

The record start and the land mask are bookkeeping, and they show up as missing data rather than as disagreement. Every other row changes the
numbers.

## Two groups, one pair of satellites

GRACE never measured water. Two satellites flew in formation, one ahead of the other, and the instrument between them measured their separation
to a few microns. Extra mass on the ground below — water, mostly — tugs on the leading satellite first and the trailing one a moment later,
changing that separation by a tiny amount. Months of those measurements can be turned back into a map of where mass was gained and lost.

That conversion has no single right answer. Many different arrangements of water on the ground fit the same orbit record equally well, so each
processing center adds assumptions of its own to settle on one. JPL and CSR add different assumptions. Both publish the result as **mascons**:
blocks of the Earth's surface, each given one water value per month.

| | JPL | CSR |
|:---|:---|:---|
| Blocks the answer is solved on | equal-area caps 3° across, about 300 km | equal-area tiles 1° across at the equator, about 110 km |
| Grid the files ship on | 0.5° | 0.25° |
| What steers the answer where GRACE alone is ambiguous | a land surface model | the GRACE data alone |
| Blocks that straddle a coast | a filter separates the land part from the ocean part | the block is split in two along the coastline |
| Correction factors | JPL publishes gain factors and recommends applying them | CSR states its mascons need none |

Both grids are finer than what GRACE can actually see. The satellites resolve features a few hundred kilometres across, whichever center
processes them, so the grid is how an answer gets packaged rather than how much detail it holds.

Scanlon et al. (2016) compared the two centers' products across 176 river basins and found their total-water records tracking each other closely,
with long-term trends the part that still diverges. The two datasets in this app behave the same way.

Agreement throughout these pages is measured as a **correlation**: one number between −1 and 1 saying how closely two monthly records rise and
fall together. At 1 they move in lockstep, at 0 there is no relationship, at −1 one rises whenever the other falls. A correlation says nothing
about whether the two agree on how much water there is — only on the timing and shape of the ups and downs.

Each correlation here covers the 281 months both datasets provide, February 2003 to June 2026. For a basin, each dataset is first averaged across
the basin, which is the series the app's regional view plots, and those two averages are compared. Trends are left in, so a decline both datasets
see counts toward their agreement.

Across the 37 WHYMAP basins the two total-water records correlate at a median of 0.87, and 15 of the 37 are above 0.9. Agreement weakens as the
area shrinks: comparing one 1° cell at a time, the median falls to 0.75, because averaging over a basin cancels month-to-month noise that a
single cell carries on its own.
## Where the difference comes from

Neither dataset measures groundwater. Both arrive at it by subtraction: start from the total water stored in the column, then take away the water
held as soil moisture, snow and canopy. Whatever remains gets called groundwater.

The two groundwater series can therefore part company in two ways, and in no others.

1. **They start from a different total.** The app's GRACE layers carry JPL's solution and GLDAS 2.2 has CSR's built into it. Wherever those two
   disagree about total water, the groundwater they imply inherits that disagreement in full.
2. **They take a different amount away.** The three GLDAS 2.1 models the GRACE route averages, and the Catchment model inside 2.2, hold
   different amounts of soil moisture and snow for the same place in the same month. Taking more away leaves less groundwater behind.

Nothing else enters, so the three gaps are tied together exactly: the groundwater gap equals the total-water gap minus the subtraction gap.
Writing d for "the difference between the two datasets", TWS for total water and REST for everything in the column that is not groundwater,

$$ d_{GW} = d_{TWS} - d_{REST} $$

All three can be measured, which settles which cause dominates where.

**RMS** is the typical size of a gap, in centimetres of water: take the difference between the two datasets in each month, square it, average
over the record, take the square root. Each cell's fixed offset is removed first, so RMS measures disagreement that moves over time rather than a
constant distance between the two.

**Share** says how much of the groundwater gap one cause could account for on its own. Each gap swings around its own average by some amount, and
the share compares the size of one gap's swing against the groundwater gap's.

Both are medians over the land cells the two datasets share, from February 2003 to June 2026, with each cell counted in proportion to its area,
so a wide cell at the equator weighs more than a narrow one near a pole.

| The gap between the two datasets in | RMS | Share of the groundwater gap |
|:---|:---:|:---:|
| groundwater, which is what you see on screen | 6.42 cm | — |
| total water, JPL against CSR | 5.73 cm | 0.85 |
| the subtraction: soil, snow and canopy | 3.38 cm | 0.32 |

The two shares add to more than 1 because the gaps partly move together, so they do not divide the blame into clean percentages. Read them as an
ordering: in a typical 1° cell, the disagreement between JPL and CSR accounts for most of the groundwater gap, and the subtraction for about a
third of it.

Averaging over a basin changes that balance. Averaging cancels much of the cell-scale noise in the GRACE solutions while leaving the systematic
difference in how the column gets divided, so the larger the region, the more of the disagreement traces to the subtraction. Per-basin shares run
to a median 0.72 for total water and 0.32 for the subtraction, and in 11 of the 37 basins the subtraction is the larger cause.

Groundwater disagrees more than total water throughout. Cell by cell the two datasets' groundwater series correlate at a median 0.42, against
0.75 for total water; by basin, 0.61 against 0.87. Each step away from the raw measurement adds a modelling choice the two datasets make
differently.

## What the literature says about the subtraction

Getirana, Kumar and Rodell (2025) question the method behind the GRACE route. Subtracting a model's soil moisture and snow from a GRACE total
gives you groundwater only if the model's soil and snow compartments hold exactly the water those labels imply, and in many models they do not.
Soil layers stop at a fixed depth, what lies below gets handled by convention, and where the water table is shallow the water a model files under
soil moisture is the same water a hydrologist would call groundwater. Subtract it and the signal you were after goes with it. They recommend
models that carry a fuller subsurface with GRACE assimilated into them, which describes GLDAS 2.2.

The critique applies to the GRACE route in this app. The seasonal-cycle sections of [Where Each One Is Trustworthy](trusting-each-one.md) show
one case of it with numbers: along the Atlantic coastal plain, where water tables are shallow, the GRACE route puts its groundwater peak in the
wrong season.

It does not make the GRACE route useless. Scanlon et al. (2018) checked seven global land models against three GRACE solutions across 186 river
basins and found the models consistently too flat — where GRACE sees a large multi-year gain or loss, the models show a smaller one, in both
directions. A model is the better guide to how the column divides between soil, snow and groundwater; the satellites are the better guide to how
much the total has changed.

The two papers support the split these pages recommend: take the shape of the cycle and the division of the column from 2.2, and the size of a
long-term gain or loss from GRACE.
## References

- Getirana, A., Kumar, S., and Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Save, H., Bettadpur, S., and Tapley, B. D. (2016). High-resolution CSR GRACE RL05 mascons. *Journal of Geophysical Research: Solid Earth*,
  121, 7547–7569. [doi:10.1002/2016JB013007](https://doi.org/10.1002/2016JB013007){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., and Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
