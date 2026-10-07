# Case Studies

The three studies below were carried out by the Brigham Young University team that developed the GRACE Regional Analyst and its predecessor,
the GRACE Groundwater Subsetting Tool (GGST). Each used the same GRACE and GLDAS water balance as the app, combined with other data, to answer
practical questions about a real aquifer, and each shows a different side of working with GRACE: estimating recharge where wells are scarce,
accounting for a large surface reservoir, and correcting for leakage in a narrow, heavily pumped valley. The figures are reproduced from the
papers.

## Niger: storage change and recharge in the Iullemeden and Chad Basins

!!! cite "Paper"
    Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). **Evaluating groundwater storage change
    and recharge using GRACE data: A case study of aquifers in Niger, West Africa.** *Remote Sensing*, 14(7), 1532.
    [doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}

The study was carried out under the NASA SERVIR West Africa project with the AGRHYMET Regional Centre in Niamey. It follows the same workflow as
the app: derive GWSa for each aquifer, fill the gaps in the record, and estimate annual recharge with the water table fluctuation method.

### Setting and data

Southern Niger overlies two large sedimentary basins. The Iullemeden Basin in the west covers about 620,000 km² and receives 550–650 mm of rain a
year; the study analyzed its Continental Intercalaire and Continental Terminal aquifers. The Lake Chad Basin in the east covers about
2.5 million km² and receives 200–400 mm a year; the study analyzed its Manga and Korama aquifers. Nearly all rain falls between June and
September, and monitoring wells are few.

![Selected aquifers of the Iullemeden and Chad basins](../../static/images/grace/papers/niger-fig4-study-aquifers.webp)

*Selected aquifers of the Iullemeden and Chad basins. Barbosa et al. (2022), Fig. 4, CC BY 4.0.*

GWSa was computed in GGST from JPL mascon TWSa and the mean of the GLDAS Noah, VIC and CLSM models, relative to the 2004–2009 mean, for April
2002 to September 2021. Missing months were filled by seasonal decomposition: each missing value is the trend at that month plus the average
seasonal and residual values for that calendar month.

![Measured and imputed GWSa](../../static/images/grace/papers/niger-fig7-gwsa-imputed.webp)

*Measured (black) and imputed (red) GWSa data showing that visually, the imputed data honor the long-term trend and seasonal variation present
in the data. Barbosa et al. (2022), Fig. 7, CC BY 4.0.*

### Storage change

In the Iullemeden Basin, storage rose slightly from 2002 to 2011 and much faster from 2011 to 2021, reaching a total increase of more than 10 cm
of water. In the Chad Basin, storage declined slightly through 2011 and rose from 2011 to 2020. Rainfall increased over the same period, but the
correlation between storage and rainfall was low (0.2 for Iullemeden and 0.35 for Chad, with a 7-month lag), so the authors suggest that land
use change also contributed.

![Groundwater storage anomalies in the Iullemeden basin region](../../static/images/grace/papers/niger-fig10-gwsa-iullemeden.webp)

*Groundwater storage anomalies in the Iullemeden basin region. Barbosa et al. (2022), Fig. 10, CC BY 4.0.*

### Recharge

The authors applied the water table fluctuation method to each year of the filled GWSa record. Method 1 counts only the visible seasonal rise
and gives a lower estimate; Method 2 adds the drainage the rise offset and gives an upper estimate.

![Estimated recharge values in the Iullemeden basins](../../static/images/grace/papers/niger-fig17-recharge-iullemeden.webp)

*Estimated recharge values in the Iullemeden basins. Barbosa et al. (2022), Fig. 17, CC BY 4.0.*

The paper compared its averages with earlier studies in Niger (its Table 1):

| Source | Region | Method | Period | Recharge (cm/yr) |
|---|---|---|---|---|
| Barbosa et al. (2022) | Iullemeden Basin | WTF, GRACE | 2002–2011 | 4.0–7.3 |
| Barbosa et al. (2022) | Iullemeden Basin | WTF, GRACE | 2012–2021 | 4.5–9.2 |
| Barbosa et al. (2022) | Chad Basin | WTF, GRACE | 2002–2011 | 2.9–5.4 |
| Barbosa et al. (2022) | Chad Basin | WTF, GRACE | 2012–2021 | 4.1–7.6 |
| Bromley et al. (1997) | Southwest Niger | Chloride mass balance | 1992 | 1.3 |
| Leduc et al. (1997) | Southern Niger | WTF, wells | 1991 | 5–6 |
| Leduc et al. (2001); Favreau et al. (2002) | Southwest Niger | Radioisotopes (¹⁴C and ³H) | 1950s–2000s | 0.1–0.5 |
| Leduc et al. (2001) | Southwest Niger | WTF, wells | 1990s–2000s | 2–5 |
| Vouillamoz et al. (2008) | Southwest Niger | WTF, wells | 1990s–2000s | 2–5 |

The ranges for this study run from Method 1 to Method 2. Method 1 falls within the range of earlier water table fluctuation studies; Method 2 is
higher, which the authors consider reasonable for a period when storage was accumulating. Chloride and isotope methods, which integrate over
much longer periods, give lower values.

### Conclusions

- Groundwater storage in both basins has been rising for the past decade, so the aquifers are not being overused and there is room for further
  development, provided storage continues to be monitored.
- Satellite data made this analysis possible where well records are too sparse to do it from the ground.
- Reporting both WTF methods brackets the likely recharge.

## Volta Basin: separating a large reservoir from groundwater

!!! cite "Paper"
    Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., Sanchez, J. L., Nelson, E. J., Ames, D. P., and
    Miller, A. W. (2025). **A multi-source approach to groundwater storage and recharge assessment in the Volta Basin.** *Science of The Total
    Environment*, 1001, 180421. [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}

### Setting and data

The Volta Basin covers about 400,000 km² in Ghana, Burkina Faso, Togo, Mali, Côte d'Ivoire and Benin. Lake Volta, behind the Akosombo Dam,
covers only about 2% of the basin but holds a large and variable volume of water.

![Volta Basin location](../../static/images/grace/papers/volta-fig1-study-area.webp)

*Volta Basin location. Barbosa et al. (2025), Fig. 1, CC BY 4.0.*

The study used JPL mascon TWSa and the GLDAS 2.1 ensemble for April 2002 to December 2022, the same water balance as the app, and added a
surface water term, SWSa, computed from Copernicus altimetry of Lake Volta:

```text
GWSa = TWSa − (SMa + SWEa + CANa + SWSa)
```

Gaps were filled by seasonal decomposition with a piecewise linear trend, the approach used in this training's
[gap-filling notebook](gap-filling.md). The study also compared the results with the groundwater storage computed directly by the GLDAS 2.2
Catchment model, with CHIRPS rainfall, and with 10 monitoring wells in the Nasia sub-basin.

### Why the lake matters

Lake Volta accounts for about half of the basin's total water storage change. Without the lake term, the derived GWSa follows the lake: from
2002 to 2012 it is almost entirely lake water. With the lake removed, groundwater storage changed little until about 2012 and then rose, for a
total gain of about 30 km³, or about 10 cm of water, over 2002–2022.

![SWSa from Lake Volta altimetry, and GWSa with and without the lake](../../static/images/grace/papers/volta-fig6-swsa-gwsa.webp)

*Surface water storage anomaly (SWSa) computed from Lake Volta altimetry data and groundwater storage anomaly (GWSa) found with and without
considering SWSa. Barbosa et al. (2025), Fig. 6, CC BY 4.0.*

The app's GWSa for this basin corresponds to the green curve, because the app does not subtract surface water (see
[Deriving Groundwater Storage](../background/deriving-groundwater.md#the-water-balance)).

GLDAS 2.2, which assimilates GRACE, showed the same trend but much larger seasonal swings, so the authors recommend it for trends but not for
recharge estimates.

![GWSa for the Volta Basin from the GLDAS 2.2 CLSM model](../../static/images/grace/papers/volta-fig7-gldas22-vs-grace.webp)

*Groundwater storage anomaly (GWSa) for Volta Basin derived from the GLDAS 2.2 CLSM model. Barbosa et al. (2025), Fig. 7, CC BY 4.0.*

### Recharge

Applied to the GRACE GWSa for 2010–2020 (the years before 2010 had no clear seasonal cycle), the water table fluctuation method gave average
recharge of 5.8 cm/yr (Method 1) and 10.7 cm/yr (Method 2). Wells in the Nasia sub-basin gave a median of 10.4 cm/yr, assuming a specific
yield of 0.05, and an earlier study by Obuobie et al. (2012) gave 8.6 cm/yr. GLDAS 2.2 gave 17.4 and 36.1 cm/yr, far above the other estimates.

![Boxplot of recharge in the Volta Basin](../../static/images/grace/papers/volta-fig8-recharge-boxplot.webp)

*Boxplot of recharge in the Volta Basin estimated with the WTF Methods 1 and 2 using GRACE data, using the new dataset from GLDAS V2.2, WTF
using observation well data, and from a prior study by Obuobie et al. (2012). Barbosa et al. (2025), Fig. 8, CC BY 4.0.*

### Conclusions

- Groundwater storage in the basin rose by about 30 km³ over 2002–2022, mostly after the early 2010s.
- In a basin with a large reservoir, leaving surface water out of the balance assigns the reservoir's changes to groundwater.
- GRACE-based recharge agrees with well-based estimates and earlier studies, so GRACE can support recharge estimates where monitoring is
  sparse.

**For app users:** before reading GWSa as groundwater in a basin with a large lake, reservoir or wetland, check how much of the storage signal
the surface water accounts for, and remove it if it is large.

## California's Central Valley: correcting GRACE with well data

!!! cite "Paper"
    Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., and Pulla, S. T. (2025).
    **Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.**
    *Environmental Modelling & Software*, 186, 106368.
    [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}

### Setting

California's Central Valley is about 700 km long and 80 km wide, about 52,000 km², and one of the most heavily pumped aquifer systems in the
world. It is narrower than a single 3° GRACE mascon (about 333 × 264 km at that latitude), and the pumping decline is concentrated in the valley
while the surrounding mountains behave differently. That makes it a textbook case of [leakage](../background/resolution-and-leakage.md#leakage):
averaged over the valley, GRACE understates the storage loss.

### An independent estimate from wells

The study built a storage record from well data for 1960–2020:

![Groundwater storage analysis using in situ data](../../static/images/grace/papers/cv-fig3-workflow.webp)

*Groundwater storage analysis using in situ data. (a) wells with data gaps are identified, (b) data gaps are imputed using a multi-step machine
learning algorithm featuring Earth observations, (c) temporal and then spatial interpolation is used to generate time-varying water level
rasters, (d) water levels rasters are combined with storage coefficients to estimate groundwater storage change at each time interval.
Reprinted from Stevens et al. (2025), Fig. 3, © 2025 Elsevier, reused under the authors' rights.*

1. Wells from USGS and California Department of Water Resources databases were screened by record length; the study compared thresholds of
   150, 75 and 50 months with observations (181, 572 and 921 wells).
2. Gaps in each well's record were filled in two steps: a machine learning model (an extreme learning machine) driven by the Palmer Drought
   Severity Index and GLDAS soil moisture, then an iterative refinement using the three best-correlated neighboring wells.
3. The filled records were kriged into monthly water level surfaces on a 0.1° grid.
4. Changes in water level were converted to changes in storage with the specific yield map of the USGS Central Valley Hydrologic Model (CVHM).

Using the 75-month threshold, the well-based storage curve matched CVHM closely (r² = 0.87, RMSE 9.04 km³).

### Calibrating GRACE

The GRACE GWSa for the valley, converted to volume, tracked the well-based curve in timing but was much smaller. Multiplying it by a scale factor
corrected for the leakage. The best factor was about 5 (± 1.0); with it, GRACE and the wells agreed with r² = 0.725, a mean error of −14.4 km³
and an RMSE of 21.2 km³ over 2002–2021.

![Comparison of the well-based storage curve with GRACE scaled by 5](../../static/images/grace/papers/cv-fig11-grace-75obs.webp)

*Comparison of Iterative Well Imputation to GRACE using 75 observation-month threshold dataset. Reprinted from Stevens et al. (2025), Fig. 11,
© 2025 Elsevier, reused under the authors' rights.*

With the factor applied, the GRACE storage losses agree with most published estimates for the same periods:

| Published study | Period | Published loss | GRACE × 5 in this study |
|---|---|---|---|
| Famiglietti et al. (2011) | Oct 2003 – Mar 2010 | 20.3 km³ | 26.7 km³ |
| Scanlon et al. (2012) | Oct 2006 – Mar 2010 | 31 km³ | 31.1 km³ |
| Xiao et al. (2017) | Apr 2002 – Sep 2016 | 64.6 km³ | 70.7 km³ |
| Ojha et al. (2018) | Dec 2006 – Jan 2010 | 21.3 km³ | 53.2 km³ |

### Conclusions

- Gap-filled well records can produce a storage history that agrees with a calibrated regional groundwater model.
- That history gives a direct way to calibrate a leakage scale factor for GRACE, about 5 for the Central Valley.
- Once calibrated, GRACE can track storage change in the valley going forward, and the same approach could be used in data-poor regions with
  some well records.

**For app users:** for a small or narrow aquifer, the GRACE average from the app captures the timing and direction of storage change but can
understate its size several times over. A scale factor calibrated against wells corrects that, for that aquifer only.

To repeat the Niger and Volta analyses for any region, set **Gap filling** to **Seasonal model** and open the
[Recharge Analysis](../recharge/opening.md).
