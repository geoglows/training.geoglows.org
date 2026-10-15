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

## The GLDAS terms

The app takes snow water equivalent, canopy interception storage and soil moisture from each of the three GLDAS 2.1 models — Noah, VIC and the
Catchment model, described in [The GLDAS Land Surface Models](land-surface-models.md) — converts them from kg/m² to cm of water, and puts all
three on the same 1° grid (Noah is averaged from 0.25° up to 1°). Each model's anomaly is its value minus that cell's mean for 2004–2009, the
same baseline as GRACE.

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

Most factors are close to 1: about 83% fall between 0.5 and 1.5. A cell keeps the unscaled mascon value in two cases.

**Where JPL publishes no factor.** That is the ocean, which the GLDAS land mask removes anyway, and ice — all of Antarctica and 18% of land
above 60°N. The factors are not meant for ice, because CLM does not represent ice sheets or mountain glaciers. This covers 5.6% of the cells
the app draws.

**Where the factor is implausible**, meaning zero or negative, or greater than 3. This is 1,604 cells on the 0.5° grid, 0.74% of the total, and
it is the app's rule rather than JPL's — the file marks its whole range as valid and sets no bounds.

What these cells have in common is that the regression producing the factor had almost no signal to work with, so its slope is unstable. They
are coastal about three times as often as the cells that are kept (51% within two cells of water, against 19%) and carry year-round snow
thirteen times as often (18.5% against 1.4%). Nearly half are neither, sitting instead in arid interiors — the Kalahari, the Australian
interior, the Karoo, the Atacama — where CLM's storage variation is small enough that the fit divides by nearly nothing. Ice, coastline and
desert are the same failure in three settings, which is why a bound on the factor catches them where a glacier mask alone would not.

The factors in these cells run as far as 24 and −1.35. A negative factor reverses the sign of the anomaly; a factor of 24 turned −292 cm into
−7048 cm at Ellesmere Island. In the arid basins the exclusion is harmless either way — four of the Great Artesian Basin's 806 cells, moving its
series by 0.00 cm — because a small anomaly multiplied by a bad factor is still small.

It matters in at least one place a user would notice. One such cell falls inside the **North Caucasus Basin**, an aquifer in the app's own
region sets. Applying every factor doubled that basin's groundwater series: the standard deviation of its mean went from 13.3 cm unscaled to
23.5 cm, and sits at 13.6 cm once implausible cells are left alone. Nearly all of that apparent amplitude was a handful of degenerate cells
rather than signal. The gain the factors exist to restore survives the rule — California's Central Valley keeps all of it, 10.2 cm to 12.4 cm,
and the Congo nearly all, 7.6 cm unscaled to 7.9 cm against 8.1 cm with every factor applied.

Two glacier basins in the river basin sets, Alsek and Santa Cruz, carry very large GWSa whatever is done with the gain factors. GRACE sees ice
mass loss there and GLDAS does not model glaciers, so the water balance attributes it to groundwater. Those numbers are an artifact of the
method, not of the scaling.

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
[Resolution, Leakage and Small Regions](../mission/resolution-and-leakage.md)), or the uncertainty in the gain factors themselves, which JPL does not
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
