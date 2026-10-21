# What the Differences Look Like

[Why the Two Datasets Differ](why-they-differ.md) sets out the two causes. This page shows what they produce, in named aquifers on five
continents, with both datasets drawn on the same axes every time.

Every series here is the area-weighted average over the region, which is what the app's regional view plots, over the 281 months both datasets
provide. A **seasonal cycle** is the average shape of a year after the long-term trend is removed, and a **swing** is the height from its lowest
month to its highest. The first half of the page covers real disagreements about groundwater. The second covers places where one of the two is
not reporting groundwater at all.

## Where the two agree

Four aquifers, four continents, nothing in dispute:

![Monthly groundwater records from both datasets over the Parecis Basin, the Taurus-Zagros, the Deccan Plateau and the Khorat Plateau, tracking each other closely](../../static/images/grace/compare-agreement.png)

| Aquifer | Monthly r | Seasonal r | Swing, GRACE | Swing, 2.2 |
|:---|:---:|:---:|:---:|:---:|
| Parecis Basin, Brazil | 0.94 | 0.97 | 35.3 cm | 37.7 cm |
| Taurus–Zagros, Iraq and Iran | 0.92 | 0.96 | 13.7 cm | 10.7 cm |
| Deccan Plateau, India | 0.91 | 0.94 | 26.5 cm | 22.5 cm |
| Khorat Plateau, Thailand and Laos | 0.89 | 0.95 | 27.7 cm | 31.1 cm |

Nothing a water manager would conclude in these four changes with the choice of dataset. They cover a wet tropical basin, a semi-arid mountain
front, a monsoon plateau and a monsoon lowland, and all four are falling or rising in both records at once — the Deccan gains in both
(+0.64 and +0.37 cm/yr), the Taurus–Zagros loses in both (−0.73 and −0.43).

What they have in common is the ratio that runs through the rest of this page: in each, the models' soil moisture cycle is about 0.4 of the
total water cycle. The subtraction removes less than half of what GRACE measured and leaves a groundwater signal with a clear shape of its own.

## Where the trend differs

The two datasets can see the same wet and dry years and still sit on lines that drift steadily apart:

![Both datasets over the Central Valley, the Disi aquifer, the Coastal Plain of Veracruz and the Tarim Basin, with fitted trend lines diverging in each](../../static/images/grace/compare-trend.png)

| Aquifer | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|:---|:---:|:---:|:---:|
| Central Valley, California | −1.37 | −0.24 | 0.18 |
| Saq–Ram (Disi), Jordan and Saudi Arabia | −1.08 | −0.11 | 0.10 |
| Coastal Plain of Veracruz, Mexico | −1.21 | −0.06 | 0.05 |
| Tarim Basin, China | −0.55 | −0.06 | 0.11 |
| Ganges-Brahmaputra | −1.53 | −0.44 | 0.29 |
| Indus | −1.45 | −0.21 | 0.14 |
| North China Plain | −0.67 | −0.25 | 0.38 |
| Ogallala (High Plains) | −0.45 | −0.22 | 0.49 |

Trends in cm/yr, area-weighted, February 2003 to June 2026. Across the 37 WHYMAP basins the 2.2 trend runs a median 0.26 of the GRACE one where
storage is falling and 0.33 where it is rising, so the flattening goes both ways.

The Central Valley is the clearest case because wells can settle it. Over the record the GRACE route loses 32 cm and 2.2 loses 6 cm: a basin in
serious depletion against one drifting gently down. The Central Valley study found the GRACE record tracking a well-based storage history in
timing while running several times too small, and calibrated a scale factor of about 5 to match it (see
[Central Valley](../case-studies/central-valley.md)). Against the wells, 2.2 is the furthest of the three.

The cause sits in how 2.2 is built. The Catchment model has no pumping in it: nobody irrigates in the model world, so the model by itself will
never deplete an aquifer. Depletion reaches 2.2's groundwater only through the monthly correction GRACE applies to the model, and that correction
gets spread across the model's surface, root-zone and deep stores rather than landing on groundwater alone. Between corrections the model drifts
back toward its own water balance.

Disi makes the same point without irrigation districts in the picture. It is a fossil aquifer under the Jordanian and Saudi desert, pumped for
cities and for farms that recharge almost nothing. GRACE has it falling 25 cm over the record and 2.2 has it falling 3 cm.

## Where the swing differs

The timing can agree almost perfectly while the size of the seasonal cycle does not:

![The Senegalo-Mauritanian Basin and the Nu River Valley, each showing the two groundwater cycles beside the total water and soil moisture cycles the GRACE route subtracts](../../static/images/grace/compare-amplitude.png)

In the Senegalo-Mauritanian Basin both datasets rise with the summer rains, both peak within a month of each other, and their cycles correlate at
0.94 — but 2.2 swings 3.2 times as far. The right-hand panel shows where the GRACE route's smaller swing comes from. Total water rises and falls
by 15.8 cm over the year and the models' soil moisture by 11.7 cm, so subtracting one from the other leaves a 5.8 cm remainder. The Nu River
Valley, on the China–Myanmar border, does the same thing: cycles correlating at 0.94, and swings of 11.8 cm against 31.5 cm.

The Catchment model inside 2.2 divides the same column differently and keeps a much larger share of the cycle in its groundwater store. Across
the 37 WHYMAP basins the 2.2 swing runs a median 1.23 times the GRACE one; across the 31 USGS principal aquifers, 1.52.

Neither swing can be checked against a well in these basins, so the honest reading is that the two datasets disagree about how a wet season is
shared between the soil and the aquifer beneath it.

## Where the cycles run opposite

In some regions the two do not merely differ in size. They peak in different seasons:

![Seasonal cycles from both datasets in six aquifers on five continents, each pair running close to opposite](../../static/images/grace/compare-phase.png)

| Aquifer | GRACE peaks | 2.2 peaks | Seasonal r | Soil moisture ÷ total water |
|:---|:---|:---|:---:|:---:|
| Baltic Devonian, Latvia and Estonia | August | March | −0.99 | 2.24 |
| Western Mountain, Israel and Palestine | August | March | −0.93 | 3.22 |
| Armorican Massif, France | August | February | −0.90 | 1.56 |
| Shabelle, Ethiopia and Somalia | September | December | −0.84 | 2.83 |
| Pilbara Craton, Australia | September | April | −0.65 | 1.40 |
| N. Atlantic Coastal Plain, USA | June | February | −0.54 | 1.06 |

The last column is the diagnostic, and it is the same quantity that made the agreeing aquifers agree. Where the models' soil moisture cycle is
small beside the measured total water cycle, the subtraction leaves a groundwater signal with its own shape. Where soil moisture swings as hard
as total water or harder, the two nearly cancel:

![The Atlantic Coastal Plain total water and soil moisture cycles almost on top of each other, and a scatter of the soil moisture ratio against seasonal agreement across 299 aquifers](../../static/images/grace/compare-phase-mechanism.png)

The left panel is the mechanism in one frame. In the Northern Atlantic Coastal Plain total water swings 7.9 cm over the year, the models' soil
moisture swings 8.4 cm, and the two curves sit almost on top of each other. Subtracting one from the other leaves the dashed remainder: small,
and shifted to peak when the soil is at its driest, which is midsummer. The groundwater cycle the GRACE route reports is the small difference
between two large similar numbers, so any error in either lands on it whole.

The right panel is the pattern across 299 aquifers in the app's region sets. Soil moisture divided by total water predicts how well the two
seasonal cycles agree, at a correlation of −0.75. Below a ratio of 0.7 the median seasonal agreement is 0.93; above 1.0 it is −0.39. Of the 59
aquifers whose cycles run opposite, 42 have soil moisture swinging harder than total water.

Shallow water tables are the likely reason the ratio climbs that high. Part of what the GLDAS 2.1 models count as soil moisture is water a
hydrologist would call groundwater, so the subtraction removes the groundwater signal twice. Getirana, Kumar and Rodell (2025) make the general
form of this argument — that a model's compartments are not the physically separate stores the subtraction assumes.

## Where a low agreement score means nothing

The **agreement** map asks whether the two records rise and fall together. In a cell where storage barely moves — a few centimetres either side
of normal, year after year — the two records have almost nothing to rise and fall with. Each one tracks its own small wobbles, the wobbles do not
line up, and the score comes out low whether or not anything is wrong with either dataset:

![Every land cell sorted into the app's agreement classes by how much groundwater moves: where it barely moves 60% of cells come out Weak or Opposite, where it moves a lot 75% come out Close or Very close](../../static/images/grace/compare-signal-size.png)

Nearly 40% of land cells barely move, and 60% of those land in the app's **Weak** or **Opposite** classes. Above 15 cm the classes invert: three
quarters of cells come out **Close** or **Very close**, and 4% run opposite.

| How far GRACE groundwater ranges from normal | Cells | Opposite or Weak | Close or Very close | Median score |
|:---|:---:|:---:|:---:|:---:|
| under 5 cm | 5,854 | 60% | 11% | 0.19 |
| 5 to 15 cm | 7,110 | 32% | 40% | 0.51 |
| over 15 cm | 2,171 | 11% | 75% | 0.77 |

*Range from normal is the standard deviation of the cell's monthly values over the whole record.*

The aquifers anyone manages sit in the bottom row, where a low score does mean something. Before reading one as a disagreement, open the region
and look at the chart. Two flat lines with a little noise on them are not two datasets contradicting each other; there is nothing there to agree
about.

## Differences that are not groundwater

In the cases below one of the two records is reporting something real that is not groundwater. The app draws those cells like any other.

### Ice sheets and glaciers

![A single cell in east Greenland where the GRACE route falls 22 metres, and the Pascua Basin in Patagonia where it falls 3 metres](../../static/images/grace/compare-artifact-ice.png)

GRACE measures ice sheets and glaciers losing mass, year after year. No GLDAS model carries either, so none reports that loss as snow, and the
subtraction has nowhere to put it except groundwater.

One 1° cell in east Greenland, at 66.5°N 36.5°W, reports groundwater falling **22 metres** over the record — a straight line interrupted only by
the mission gap, in a place with no aquifer and no groundwater to lose. That line is the Greenland ice sheet. The same cell's snow water runs
303 cm above its baseline, because the model's snow accumulates without limit where it should be ice. The Pascua Basin, draining the Southern
Patagonian Icefield, does the same at 3 metres.

2.2 sidesteps the arithmetic without escaping the problem: its Catchment model has no ice either, and the GRACE correction it receives is spread
across all the model's stores, so it reports a much smaller number for the same reason it flattens trends elsewhere. Neither series means
anything as groundwater here. Two river basins in the app's own basin sets, Alsek and Santa Cruz, carry very large GWSa for this reason.

**How to recognise it.** Switch the displayed layer to snow water (SWEa). Where it runs to hundreds of centimetres, or the region sits on an ice
cap at any latitude, the groundwater layer is reporting ice.

### Surface water the models do not carry

![The Amazon seasonal cycles, the GRACE one more than twice as large, and the Amu Darya where GRACE falls four times as fast as 2.2](../../static/images/grace/compare-artifact-water.png)

No GLDAS model represents rivers, lakes, floodplains or reservoirs. On the GRACE route that water has nowhere to go in the subtraction, so it
lands in groundwater.

In the Amazon the timing is not in dispute — the two cycles correlate at 0.99, both peaking in May with the flood. The size is: the GRACE route
swings 40.8 cm against 18.1 cm, and the extra water is the river itself, rising and falling across the floodplain. The trends then point in
opposite directions, +0.31 against −0.40 cm/yr, so a reader asking whether Amazon groundwater is gaining or losing gets a different answer from
each dataset. The Congo behaves the same way.

The Amu Darya shows the same mechanism as a trend rather than a cycle. The GRACE route has storage falling 58 cm over the record against 2.2's
14 cm, and much of that is the Aral Sea and the irrigation canals feeding away from it — surface water leaving the basin, counted as groundwater.

**How to recognise it.** A GRACE groundwater cycle far larger than 2.2's, in a basin with a major river, a large lake or a large reservoir, is
usually surface water.

### Snow and frozen ground at high latitude

![The Indigirka and George river basins, where the GRACE groundwater cycle mirrors the snow water cycle inverted](../../static/images/grace/compare-artifact-frozen.png)

| Band | Typical gap | Average snow water | Cells |
|:---|:---:|:---:|:---:|
| 60°S–30°S | 5.92 cm | 0.33 cm | 540 |
| 30°S–0° | 8.48 cm | 0.01 cm | 2,428 |
| 0°–30°N | 7.41 cm | 0.02 cm | 3,094 |
| 30°N–60°N | 6.49 cm | 2.12 cm | 5,397 |
| 60°N–90°N | 7.75 cm | 18.91 cm | 3,700 |

The northernmost band carries the snow. In the Indigirka Basin in Siberia the GRACE groundwater swings 7.0 cm through the year against 2.2's 1.6,
and in the George River basin in northern Quebec 6.9 against 1.9. The dotted curve in each panel is the snow water cycle, and the GRACE
groundwater is close to its mirror image: where the model holds too much or too little snow, the error passes straight into the subtraction. Water
locked in seasonally frozen ground adds to it, since no GLDAS model keeps that as a store of its own.

**How to recognise it.** Plot snow water (SWEa) beside the groundwater. A groundwater cycle that is the snow cycle upside down is the snow term,
not an aquifer.

### Shallow water tables

Where the water table sits close to the surface, part of what the models count as soil moisture is groundwater, and subtracting it removes the
groundwater signal twice. This is the mechanism behind the opposed cycles above, and the ratio in that section is how to spot it.
