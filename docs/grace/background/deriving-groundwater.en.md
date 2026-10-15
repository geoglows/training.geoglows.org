# Deriving Groundwater Storage

## The water balance

GRACE measures the total change in water stored in a column of the Earth. To isolate groundwater, the app subtracts the parts of that total that
can be estimated by other means:

![Terrestrial water storage components](../../static/images/grace/grace-water-balance.png)

TWSa is the sum of the anomalies of every store in the column: snow water equivalent (SWEa), water held on vegetation canopies (CANa), soil
moisture (SMa), groundwater (GWSa) and surface water in rivers, lakes and reservoirs. Land surface models estimate the first three well. Removing
them leaves groundwater:

$$
\mathrm{GWSa} = \mathrm{TWSa} - (\mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa})
$$

The app leaves surface water out of the balance, so any change in surface water storage ends up in GWSa. Over most of the world surface water
changes are small next to the other terms. In regions with large reservoirs, wetlands, or rivers with big floods (the Amazon, the Ganges and
Brahmaputra, the Caspian Sea, Lake Victoria, Lake Volta), GWSa includes those changes and overstates the seasonal swing in groundwater. In the Volta Basin, for example, the lake accounts for about half
of the total storage signal ([case study](../case-studies/volta.md)).

## GLDAS land surface models

NASA's Global Land Data Assimilation System (GLDAS) runs land surface models forced with observed precipitation, radiation and meteorology to
estimate how much water the land surface stores each month. The app uses three GLDAS version 2.1 models, which differ in how they represent soil
layers and runoff:

| Model | Grid | Soil moisture used |
|---|---|---|
| Noah | 0.25° | four layers, 0–200 cm |
| VIC (Variable Infiltration Capacity) | 1° | three layers, depths vary by location |
| CLSM (Catchment Land Surface Model) | 1° | total soil profile |

From each model the app takes snow water equivalent, canopy interception storage and soil moisture, converts them from kg/m² to cm of water, and
puts all three models on the same 1° grid (Noah is averaged from 0.25° up to 1°). Each model's anomaly is its value minus that cell's mean for
2004–2009, the same baseline as GRACE.

The three models often disagree, particularly about deep soil moisture. Rather than choose one, the app averages them: SWEa, CANa and SMa are each
the mean of the three models, and the spread between the models (their standard deviation) is used as the uncertainty of each term.

## Processing chain

![GRACE Regional Analyst processing chain](../../static/images/grace/grace-processing.png)

GRACE TWSa is averaged from 0.5° to 1° and combined with the model ensemble to give GWSa on a 1° grid. The app serves five layers: GWSa, SMa, SWEa
and CANa at 1°, and TWSa at 0.5° as JPL distributes it. Using 1° for the derived layers follows the usual practice of combining GRACE with model data at
the coarser of the two grids; reporting GWSa at 0.5° would give an impression of detail that neither dataset has.

No gaps are filled. Each monthly value in the app is the published JPL value, scaled as described below, combined with the GLDAS ensemble for
that month.

### Gain factors

The mascon solution is natively 3°, and the 0.5° file repeats each mascon's value across all 36 of its cells, so the published grid on its own
carries no detail finer than a mascon. JPL ships a grid of **gain factors** in the same file to recover some of that detail. They are derived by
putting the CLM land surface model through the same processing GRACE goes through and estimating, cell by cell, the multiplier that restores the
model's original amplitude. The correction is a single multiplication, with the factor constant in time:

$$
g'(x,y,t) = g(x,y,t) \times s(x,y)
$$

JPL does not apply this scaling before distributing the data; the GRACE-FO Level-3 Handbook states that users must apply it, and its own
groundwater example follows the same TWSa-minus-GLDAS approach this app uses and lists the multiplication as a pre-processing step. The app
applies the factors to TWSa at 0.5°, before TWSa is averaged to 1°, since the structure they add is finer than a 1° cell.

Every factor is applied as JPL distributes it. About 83% fall between 0.5 and 1.5, and 1.3% of cells sit outside the range 0 to 3, including
several hundred that are negative and so reverse the sign of the anomaly in that cell. JPL marks the full range as valid and sets no bounds, and
excluding the extremes changes a basin average by at most 0.2 cm, so the app does not second-guess them. Cells with no factor at all keep the
mascon value: the ocean, which the GLDAS land mask removes anyway, and ice — all of Antarctica and 18% of land above 60°N — which the factors
are not meant for, because CLM does not represent ice sheets or mountain glaciers.

What the factors do not do is make the 0.5° grid 36 independent measurements. The underlying mascon is still one estimate, and the factors
redistribute its amplitude using a model's idea of how storage varies within it. The handbook is explicit that the models behind them carry
biases and "typically do not include groundwater or human activities in their simulations," so a heavily pumped aquifer is exactly where the
redistribution is least informed by the thing being measured.

## Uncertainty

Each layer in the app comes with a one-standard-deviation (1σ) uncertainty, which the time series chart draws as a band around the line:

- **TWSa:** JPL's published uncertainty for each mascon and month, multiplied by the same gain factor as the data, so the band stays in
  proportion to the value it describes.
- **SWEa, CANa, SMa:** the standard deviation across the three GLDAS models.
- **GWSa:** the four combined, treating them as independent:

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

The uncertainty band captures the measurement error in GRACE and the disagreement between models. It doesn't capture errors the three models
share, the effect of leaving out surface water, leakage from outside a region (see
[Resolution, Leakage and Small Regions](resolution-and-leakage.md)), or the uncertainty in the gain factors themselves, which JPL does not
publish. The true uncertainty is larger than the band shows.

One caution about combining them: JPL's TWSa uncertainty is a measurement error, while the three GLDAS terms are the spread across NOAH, VIC and
CLSM, which measures how much the models disagree rather than how wrong they are. Adding them in quadrature treats the two as comparable. Over
most basins the model spread dominates — in the Congo, 3.1 cm from GRACE against 5.7 cm combined.

## What GWSa is good for

GWSa is best used to answer regional questions about direction and rate: is storage in this aquifer declining, how fast, and did the decline
slow after a policy change or a run of wet years? It is not suited to decisions at the scale of a well field or a single irrigation district,
and it says nothing about water levels or water quality. Where monitoring wells exist, compare the GRACE trend with storage change estimated from
the wells; agreement between the two strengthens both.

## References

- Rodell, M., et al. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}
- GLDAS data at the NASA GES DISC: [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"}
