# Where Each One Is Trustworthy

Neither dataset wins everywhere. [Why the Two Datasets Differ](why-they-differ.md) accounts for the disagreement; this page says which series to
quote for which question, and gives the diagnostic to run when you want to decide for yourself in a region the tables below do not cover.

## Agreement follows the size of the signal

Grouping the 1° land cells by how much the GRACE groundwater actually moves:

| GRACE GWSa standard deviation | median correlation | median RMS difference | cells |
|---|---:|---:|---:|
| under 5 cm | 0.19 | 4.58 cm | 5,854 |
| 5–15 cm | 0.51 | 8.32 cm | 7,110 |
| over 15 cm | 0.77 | 27.32 cm | 2,171 |

A quiet cell correlating at 0.2 is two small signals failing to line up, and it carries no information about whether either dataset is sound. The
aquifers anyone would analyse sit in the bottom row. Read the correlation alongside the amount of water in play, never on its own.

## For the size of a trend, use GRACE

Averaged over the 37 WHYMAP large groundwater basins, the 2.2 GWSa trend runs about a quarter of the GRACE one — a median ratio of 0.26 across
the basins losing storage and 0.33 across those gaining it, so the flattening goes both ways:

| Basin | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|---|---:|---:|---:|
| Ganges-Brahmaputra | −1.53 | −0.44 | 0.29 |
| Indus | −1.45 | −0.21 | 0.14 |
| California Central Valley | −1.37 | −0.24 | 0.18 |
| North Caucasus | −1.03 | −0.68 | 0.66 |
| North China Plain | −0.67 | −0.25 | 0.38 |
| Arabian | −0.65 | −0.10 | 0.16 |
| Tarim | −0.55 | −0.06 | 0.11 |
| Ogallala (High Plains) | −0.45 | −0.22 | 0.49 |
| Sahara Septentrional | −0.44 | −0.10 | 0.23 |

Trends in cm/yr, area-weighted over each basin, February 2003 to June 2026.

Pumping is absent from the Catchment physics, so depletion reaches the 2.2 groundwater store only through the monthly GRACE correction, and that
correction is spread across the surface, root zone and profile stores rather than landing in groundwater alone. Between corrections the model
relaxes toward its own water balance.

Scanlon et al. (2018) found the same flattening in open-loop models, comparing seven of them against three GRACE solutions over 186 river basins
and 2002–2014: the models badly understate the large decadal trends GRACE sees, in both directions, which they attribute to irrigation and other
human use being outside the model physics. 2.2 is a model with GRACE assimilated rather than an open-loop run, so the correction pulls it part of
the way back, and the ratios above are what is left.

Three basins disagree on sign — the Amazon, the Congo and the Pechora — all of them places where the trend is small beside the seasonal cycle.

## For the shape of the seasonal cycle, check SMa against TWSa first

The two datasets can differ in the size of the seasonal swing and in its timing. Across the 37 WHYMAP basins the 2.2 seasonal amplitude runs a
median 1.23 times the GRACE one; across the 31 USGS principal aquifers, 1.52. In a few places it is several times larger:

| Aquifer | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|---|---:|---:|---:|
| Willamette Lowland | 4.8 | 33.3 | 7.0 |
| Parisian Basin | 3.0 | 17.3 | 5.7 |
| Denver Basin | 1.2 | 4.7 | 4.0 |
| Northern Atlantic Coastal Plain | 2.9 | 9.9 | 3.4 |
| Bassin Sénégalo-Mauritanien | 5.8 | 18.7 | 3.2 |

Peak to trough of the GWSa climatology in cm, trend removed, February 2003 to June 2026.

Timing can part company as well. In the Northern Atlantic Coastal Plain the GRACE GWSa peaks in June and the 2.2 GWSa in February, four months
apart, and the two seasonal cycles correlate at −0.54. The Sahara Septentrional is half a year apart; the Indus runs March against September.

Comparing the seasonal size of SMa against that of TWSa tells you which regions will do this. Across the WHYMAP basins the ratio between those two
amplitudes correlates at −0.65 with how well the two groundwater cycles agree, and at −0.83 across the USGS aquifers. Every region whose seasonal
cycles run opposite has soil moisture swinging as hard as total water, or harder:

| Aquifer | TWSa amplitude | SMa amplitude | SMa / TWSa | seasonal r |
|---|---:|---:|---:|---:|
| Ogaden-Juba | 2.0 | 3.3 | 1.70 | −0.74 |
| Upper carbonate | 7.2 | 9.9 | 1.37 | −0.60 |
| Sahara Septentrional | 0.5 | 0.7 | 1.35 | −0.83 |
| Cambrian-Ordovician | 9.9 | 11.4 | 1.15 | −0.38 |
| Indus | 5.7 | 6.3 | 1.11 | −0.39 |
| Northern Atlantic Coastal Plain | 7.9 | 8.4 | 1.06 | −0.54 |

Regions where the two agree sit between 0.4 and 0.6.

GWSa on the GRACE route is TWSa − SMa − SWEa − CANa. Where the model's soil moisture cycle is as large as the measured total-water cycle and close
to it in phase, the remainder peaks when soil moisture is at its driest, and the groundwater cycle left behind is the small difference of two large
similar numbers. In the Northern Atlantic Coastal Plain that puts the GRACE peak four months after the water table there is actually highest, while
2.2's February peak falls where late-winter recharge would put it. A shallow water table is the likely reason: part of what GLDAS 2.1 counts as
soil moisture is groundwater, and subtracting it removes the signal twice. Getirana, Kumar and Rodell (2025) make the general form of this
argument, that the models' compartments are not the physically separate stores the subtraction assumes them to be.

**Prefer 2.2 for seasonal shape where SMa swings as hard as TWSa.** You can run the check in the app: plot SMa and TWSa for the region and compare
the height of their seasonal cycles.

## For recharge, use GRACE

Barbosa et al. (2025) ran the water table fluctuation method on both datasets in the Volta Basin and got 17.4 and 36.1 cm/yr from 2.2 against 5.8
and 10.7 cm/yr from GRACE, with wells giving a median of 10.4. They recommend 2.2 for trends and not for recharge (see
[Volta Basin](../case-studies/volta.md)). A flipped seasonal phase is a second reason for the same conclusion: the method reads a trough and a
peak off the series, and if their months are wrong the recharge estimate is wrong with them.

## Summary

| What you want | Use | Because |
|---|---|---|
| A depletion or recovery rate, in cm/yr or km³/yr | GRACE | 2.2 flattens trends to roughly a quarter |
| The shape and timing of the seasonal cycle | 2.2 where SMa swings as hard as TWSa, otherwise either | the subtraction can invert the phase |
| A region a few cells across | 2.2 | averaged on 0.25° where the other is on 1° |
| An unbroken monthly series | 2.2 | the model runs through the GRACE gaps |
| Recharge by the WTF method | GRACE | Barbosa et al. (2025), plus the phase risk |
| An uncertainty figure per cell | GRACE | 2.2 publishes none |
| Anything before February 2003 | GRACE | the 2.2 record starts there |
| A result you mean to publish | both | and say where they agree and where they do not |

Two independent answers that agree are hard to explain away. Where they disagree, plot the components: a divergence that lives in SMa is a
different problem from one that lives in TWSa.

## How far any of this is validated

The numbers on this page come from comparing the two published datasets against each other, which establishes how they differ and why, and
settles nothing about which is closer to the water table. The independent support for the recommendations is indirect:

- **Models understate trends.** Scanlon et al. (2018), seven global models against three GRACE solutions over 186 basins.
- **The residual method is structurally shaky.** Getirana, Kumar and Rodell (2025), on the models' stores not being the separable compartments the
  subtraction needs.
- **The two mascon solutions agree at basin scale and diverge on trends.** Scanlon et al. (2016), CSR and JPL over 176 basins.
- **In-situ comparison is harder than it sounds.** Chen, Famiglietti, Scanlon and Rodell (2016) note that converting well levels to storage needs
  a specific yield per well, which is itself uncertain even where the monitoring network is dense. Bhanja et al. (2016) carried out such a
  comparison across India.

None of those studies evaluated these two datasets against each other, and none used this app. Direct well-based validation here extends only to
the [Central Valley](../case-studies/central-valley.md) and Barbosa et al.'s Volta wells. Treat the recommendations above as reasoning from
construction and from measured behaviour, supported by the literature on each mechanism, rather than as a validated ranking.

## References

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
- Bhanja, S. N., Mukherjee, A., Saha, D., Velicogna, I., and Famiglietti, J. S. (2016). Validation of GRACE based groundwater storage anomaly
  using in-situ groundwater level measurements in India. *Journal of Hydrology*, 543, 729–738.
  [doi:10.1016/j.jhydrol.2016.10.042](https://doi.org/10.1016/j.jhydrol.2016.10.042){:target="_blank"}
- Chen, J., Famiglietti, J. S., Scanlon, B. R., and Rodell, M. (2016). Groundwater Storage Changes: Present Status from GRACE Observations.
  *Surveys in Geophysics*, 37, 397–417. [doi:10.1007/s10712-015-9332-4](https://doi.org/10.1007/s10712-015-9332-4){:target="_blank"}
- Getirana, A., Kumar, S., and Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., and Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
