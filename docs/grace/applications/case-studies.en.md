## Groundwater storage and recharge in Niger

Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
[doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}

This study was carried out under the NASA SERVIR West Africa project with AGRHYMET, using GGST, the predecessor of the GRACE Regional Analyst.
It follows the same workflow as Part 3 of this training: derive GWSa for each aquifer, fill the gaps in the record, and estimate annual recharge
with the water table fluctuation method.

### Setting

Southern Niger overlies two large sedimentary basins: the Iullemeden Basin in the west, with the Continental Terminal, Continental Intercalaire
and Quaternary aquifers, and the Lake Chad Basin in the east, with the Manga, Quaternary and Korama aquifers. Both are in the Sahel, where nearly
all rain falls between June and September and monitoring wells are few.

### Storage change

GWSa rose in both basins over 2002–2021. The rise was larger in the Iullemeden Basin, from about −2 cm early in the record to about +12 cm by
2021, and smaller in the Chad Basin. In both basins the rise tracked increasing annual rainfall after the drought decades of the 1970s and 1980s,
and soil moisture, which has a strong seasonal cycle, showed no comparable trend. The same pattern is visible in the app today:

![GWSa, TWSa and SMa for the Iullemeden-Irhazer Aquifer System in the GRACE Regional Analyst](../../static/images/grace/app-chart-compare.webp)

### Recharge

After filling the gaps with a trend-plus-seasonal model, the authors applied the water table fluctuation method to each year of the GWSa record.
Method 1 counts only the visible seasonal rise (a lower estimate); Method 2 adds the drainage that the rise offset (an upper estimate).

| Basin | Period | Recharge, Method 1 – Method 2 (cm/yr) |
|---|---|---|
| Iullemeden | 2002–2011 | 4.0 – 7.3 |
| Iullemeden | 2012–2021 | 4.5 – 9.2 |
| Chad | 2002–2011 | 2.9 – 5.4 |
| Chad | 2012–2021 | 4.1 – 7.6 |

Recharge was higher in the second decade in both basins, consistent with the rising storage. The GRACE estimates fall within or slightly above
the range of earlier local studies in southwestern Niger, which used chloride mass balance, well hydrographs and isotope dating and found from
under 1 cm/yr (long-term, from isotopes) to 2–6 cm/yr (from water table fluctuations in wells).

### What the study shows

- GRACE can give a basin-wide record of storage change and recharge where wells are too sparse to do so.
- Filling the gaps matters for annual recharge: a missing month near a seasonal peak or trough changes that year's estimate.
- Method 1 and Method 2 bracket the likely recharge. Reporting both is more honest than choosing one.
- The results are averages over areas of hundreds of thousands of square kilometers. They describe the basin, not any particular well field.

To reproduce this analysis for any region, follow [Filling Gaps](gap-filling.md) and [Estimating Recharge](recharge-wtf.md) with a CSV
downloaded from the app.
