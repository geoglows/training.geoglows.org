# Why the Two Datasets Differ

The app serves two groundwater records for the same month in the same cell, and they do not agree. This page covers where the disagreement comes
from. [Where Each One Is Trustworthy](trusting-each-one.md) covers which one to believe, and [Known Artifacts](known-artifacts.md) covers the
places where one of them is simply wrong.

[Deriving Groundwater Storage](../gldas/deriving-groundwater.md) gives both constructions in full. In short:

- **The GRACE route.** JPL measures total water storage. The app subtracts GLDAS 2.1's soil moisture, snow and canopy water, and reads the
  remainder as groundwater.
- **The GLDAS 2.2 route.** NASA runs the Catchment land surface model with GRACE assimilated into it, and the model reports a groundwater state
  directly. Nothing is subtracted.

## What already differs before any water is counted

| | GRACE route | GLDAS 2.2 |
|---|---|---|
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

GRACE never measured water. It measured the distance between two satellites, to a few microns, as they fell around the Earth and were pulled by
the mass beneath them. Recovering a map of mass from that record is underdetermined — many different mass distributions fit the same orbits — so
each processing center imposes further assumptions to arrive at a single answer. JPL and CSR impose different ones.

| | JPL | CSR |
|---|---|---|
| Solved on | 3° equal-area spherical caps | equal-area geodesic grid, 1° at the equator |
| Delivered on | 0.5° | 0.25° |
| Regularization | constraint informed by a land surface model | constraint derived from GRACE data alone, parameter chosen by an L-ribbon |
| Coastlines | a CRI filter separates land from ocean inside a straddling mascon | coastal tiles split in two along the coastline |
| Scale factors | published, and JPL recommends applying them | CSR states the mascons do not need them |

Scanlon et al. (2016) compared the CSR and JPL mascons against each other and against the rescaled spherical harmonics over 176 river basins, and
found total-water time series correlating mostly above 0.9, with trends the part that still diverges. That matches what the two datasets do here:
over the 37 WHYMAP basins the TWSa series correlate at a median 0.87, and 15 of the 37 exceed 0.9. Agreement falls off as the region gets smaller,
and cell by cell across the globe the median TWSa correlation is 0.75.

## Splitting the difference into its two causes

Both datasets satisfy the same water balance, TWSa = GWSa + SMa + SWEa + CANa. Writing REST for everything that is not groundwater, the difference
between the two groundwater series is therefore fixed by two other differences:

$$ d_{GW} = d_{TWS} - d_{REST} $$

Each term can be measured. Cell by cell, area-weighted medians over 2003-02 to 2026-06:

| | RMS | median share of the d<sub>GW</sub> variance |
|---|---:|---:|
| d<sub>GW</sub>, the groundwater difference you see | 6.42 cm | — |
| d<sub>TWS</sub>, the two GRACE solutions disagreeing | 5.73 cm | 0.85 |
| d<sub>REST</sub>, the column partitioned differently | 3.38 cm | 0.32 |

The shares exceed 1 together because the two differences are partly correlated.

Averaged over a basin the balance shifts. Per-basin medians are 0.72 for d<sub>TWS</sub> and 0.32 for d<sub>REST</sub>, and in 11 of the 37 basins
the partition is the larger of the two. Averaging cancels much of the per-cell noise in the GRACE solutions while leaving the systematic
difference in how the column is divided, so the larger the region, the more the disagreement is about the partition and the less it is about JPL
against CSR.

Groundwater disagrees more than total water does throughout. Cell by cell the medians are 0.42 for GWSa against 0.75 for TWSa; by basin, 0.61
against 0.87. The further a quantity sits from the raw measurement, the more the two constructions drift apart.

## What the literature says about the subtraction

Getirana, Kumar and Rodell (2025) argue that the residual method — subtracting modelled soil moisture, snow and canopy water from GRACE TWS and
reading the remainder as groundwater — rests on an assumption that does not hold: that the models represent every non-groundwater store in
separate, physically meaningful compartments. They ask users to weigh what model simplifications and conventions do to the result, and they
recommend data assimilation and models with a fuller representation of the subsurface.

That critique applies to the GRACE route in this app, and the two sections of [Where Each One Is Trustworthy](trusting-each-one.md) on seasonal
cycles put numbers on one case of it. It does not make the GRACE route useless. Scanlon et al. (2018) compared seven global models against three
GRACE solutions across 186 river basins and found the models badly understating the large decadal trends that GRACE sees, in both directions,
which is a reason to keep the measurement in the picture rather than to hand the question to a model. The two papers point in the same direction:
take the partition from the better-posed model and the magnitude of change from the measurement.

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
