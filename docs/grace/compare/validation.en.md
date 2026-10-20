# How Far This Is Validated

[Which One to Use](which-one-to-use.md) makes recommendations. This page says what they rest on, so you can judge how much weight to put on each
one.

## What the comparison on these pages establishes

The numbers in [Why the Two Datasets Differ](why-they-differ.md) and [What the Differences Look Like](examples.md) come from comparing the two
published datasets against each other. That establishes how they differ, by how much, and through which term. It settles nothing about which one
is closer to the water table, because neither is being measured against water levels anywhere in that comparison.

Two datasets disagreeing tells you at least one is wrong. It does not tell you which.

## Where wells have actually been consulted

Two studies have compared these datasets against observed groundwater levels. Both are the work of our group with collaborators, both are
published, and both are single regions.

### California's Central Valley

Stevens et al. (2025) built a storage record from wells in the USGS and California Department of Water Resources databases, gap-filled with a
machine-learning scheme and converted to storage with the specific yield map of the USGS Central Valley Hydrologic Model. At a 75-month record
threshold (572 wells) the well-based curve matched that calibrated model closely, at r² = 0.87 and RMSE 9.04 km³.

Against that record the app's GRACE groundwater tracked the timing well — r² = 0.725 over 2002–2021 — and ran several times too small. The study
calibrated a scale factor of about 5 (± 1.0) to bring it into line. GLDAS 2.2, which loses 6 cm over the record where the GRACE route loses 32,
is the furthest of the three from what the wells show.

See [Central Valley](../case-studies/central-valley.md) for the method and the figures.

### The Volta Basin

Barbosa et al. (2025) estimated recharge with the water table fluctuation method from both datasets and compared the result against wells:

| Source | Recharge |
|:---|:---:|
| GRACE route, WTF method 1 | 5.8 cm/yr |
| GRACE route, WTF method 2 | 10.7 cm/yr |
| Wells in the Nasia sub-basin, specific yield 0.05 | 10.4 cm/yr |
| Obuobie et al. (2012), an earlier independent estimate | 8.6 cm/yr |
| GLDAS 2.2, WTF method 1 | 17.4 cm/yr |
| GLDAS 2.2, WTF method 2 | 36.1 cm/yr |

The GRACE route brackets the well-based figure. GLDAS 2.2 runs well above every other estimate. That study is the basis for recommending GRACE
for recharge.

See [Volta Basin](../case-studies/volta.md), which also shows Lake Volta accounting for about half the basin's storage signal.

## The evidence behind each recommendation

### 2.2 flattens trends

The strongest support comes from the team that built GLDAS 2.2. Li et al. (2019) validated the assimilation against in-situ data from about
4,000 wells and found it improved on the model alone: errors down 36% and correlation up 16% at the regional scale, and 10% and 22% at
individual points. They also state its limit plainly — the assimilation **cannot compensate for the absence of a groundwater withdrawal scheme in
the Catchment model in areas of heavy pumping.** That is the mechanism behind every row of the trend table, stated by the product's own authors.

Scanlon et al. (2018) found the same shortfall across models generally: seven global land surface and water resource models against GRACE over
186 river basins, 2002–2014, with the model medians greatly underestimating both the large declining trends GRACE sees (≤ −0.5 km³/yr) and the
large rising ones (≥ 0.5 km³/yr). Summed over basins the models gave a negative land storage trend where GRACE gave a positive one.

What this does not establish is the size of the correct trend. It supports preferring GRACE over 2.2 for a rate of change; it does not say the
GRACE figure is right. The Central Valley is the one place where wells have been consulted, and there GRACE itself was several times too small.

### The residual method is structurally shaky

Getirana, Kumar and Rodell (2025) examine the assumption behind the GRACE route: that a land surface model's soil moisture, snow and canopy
stores are distinct, physically meaningful compartments holding exactly the water those labels imply. They argue that model simplifications and
naming conventions break that assumption, and recommend models that represent the subsurface more completely with data assimilation — which
describes GLDAS 2.2.

This is an argument from how models are built rather than a measurement against wells. The soil-moisture ratio pattern across 299 aquifers in
[What the Differences Look Like](examples.md) is consistent with it, but consistency is not confirmation: no well record establishes that the 2.2
seasonal timing is the correct one in any of those aquifers.

### The two GRACE solutions agree at basin scale and diverge on trends

Scanlon et al. (2016) compared the CSR and JPL mascon products across 176 river basins and found their total water records tracking each other
closely, with long-term trends the part that still diverges. This is why the construction difference matters most for trends and least for
timing, and the two datasets in this app behave the same way.

### Comparing any of this against wells is harder than it sounds

Chen, Famiglietti, Scanlon and Rodell (2016) note that converting well levels to storage requires a specific yield for each well, which is itself
uncertain even where the monitoring network is dense. Bhanja et al. (2016) carried out such a comparison across India. Both the Central Valley and
Volta studies above depend on a specific yield, so their agreement carries that uncertainty with it.

## How much weight each recommendation carries

| Recommendation | Rests on | Strength |
|:---|:---|:---|
| Use GRACE for the size of a trend | Li et al. (2019) on the missing withdrawal scheme, Scanlon et al. (2018) across 186 basins, plus the measured ratios here | strong on direction, weak on magnitude |
| Use GRACE for recharge | Barbosa et al. (2025) against wells in one basin | one region, one method |
| Prefer 2.2 for seasonal shape where soil moisture swings as hard as total water | Getirana et al. (2025) on construction, plus the pattern across 299 aquifers | mechanism is well argued, no well record confirms which timing is right |
| Use 2.2 for small regions and unbroken series | the published grids and record periods | a fact about the products, not a finding |
| Report both where it matters | — | a practice, not a result |

## What is still unvalidated

None of the studies above evaluated these two app datasets against each other, and none used this app. Direct well-based validation reaches the
Central Valley and the Volta Basin and stops there — two regions out of the hundreds the app covers, both in the work of one group.

In particular, nothing here establishes:

- which dataset has the seasonal timing right in any aquifer with a shallow water table
- whether the GRACE route's scale problem in the Central Valley generalises to other narrow aquifers
- how either dataset performs in the humid tropics, in permafrost, or anywhere surface water is a large part of the signal
- an uncertainty for GLDAS 2.2 at all, since NASA publishes none and it is a single model run rather than an ensemble

Treat the recommendations as reasoning from how each dataset is constructed and from measured behaviour, supported by the literature on each
mechanism, rather than as a validated ranking. Where you have wells, use them: that comparison beats everything on this page.

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
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., and Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
- Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., and Pulla, S. T. (2025).
  Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.
  *Environmental Modelling & Software*, 186, 106368.
  [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}
