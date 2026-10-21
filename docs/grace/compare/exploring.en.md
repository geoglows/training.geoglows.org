# Exploring the Differences in the App

[What the Differences Look Like](examples.md) works through named aquifers one at a time. The app will do the same arithmetic for every region
in a set at once, and for every land cell, by coloring the map with a comparison between the two datasets in place of the value of either.

## Turning it on

A comparison needs both datasets, so the app offers one only while the **Displayed layer** is **Groundwater Storage Anomaly (GWSa)**, the
quantity both datasets carry as a product of their own. With GWSa displayed, the **Color by** dropdown in the header holds four choices: the
trend in GWSa, which works on one dataset at a time, and three comparisons.

| Color by | The question it answers |
|:---|:---|
| GRACE vs GLDAS 2.2: trend difference | do the two disagree about how fast storage is changing |
| GRACE vs GLDAS 2.2: agreement | do the two see the same months as wet and the same months as dry |
| GRACE vs GLDAS 2.2: seasonal swing | do the two agree on how far the annual cycle swings |

Each is one axis of disagreement, and a map of one says little about the other two. Across the 322 aquifer and basin outlines the published
data cover, the median region's two trends differ by 0.27 cm/yr over the whole record, its two monthly series correlate at 0.69, and its GRACE
seasonal cycle swings 0.73 times as far as 2.2's.

Picking a comparison turns on **Also show GLDAS 2.2** in the control panel and holds it there, so the chart carries both series for whatever you
click next. The regional view colors region outlines, the global view colors cells, and the measure stays selected when you move between them.
[Trend and Difference Analysis](../app/trends.md) gives the mechanics: the class boundaries, the minimum record a region needs, and how a
region's cells are averaged.

## The trend difference map

![The Global Aquifers set colored by the difference between the two datasets' five-year groundwater trends](../../static/images/grace/app-diff-regions.webp)

Each region or cell is colored by the GRACE trend minus the 2.2 trend over the window in the header, in cm/yr. GRACE is always the left operand,
whichever dataset the panel is set to, so the sign of the difference never depends on a control somewhere else.

| Class | Difference (cm/yr) |
|:---|:---:|
| GRACE much lower | below −1 |
| GRACE lower | −1 to −0.25 |
| Trends agree | −0.25 to +0.25 |
| GRACE higher | +0.25 to +1 |
| GRACE much higher | above +1 |

Red marks the aquifers where the GRACE route has storage falling faster, which is the flattening [How Far This Is
Validated](validation.md#22-flattens-trends) sets out: the Catchment model behind 2.2 has no pumping in it, and depletion reaches its
groundwater store only through the monthly GRACE correction, spread across all of the model's stores. Blue marks the other direction, where
GRACE has storage rising faster. Across the 37 WHYMAP basins the 2.2 trend runs a median 0.26 of the GRACE one where storage is falling and
0.33 where it is rising, so both colors are the same effect.

The window matters more here than it does for a single trend. Shorter windows produce larger trends, and the gap between the two datasets grows
with them: over the Global Aquifers outlines the typical difference more than doubles, from 0.26 cm/yr over the whole record to 0.59 over the
last five years. The classification follows:

| Window | GRACE much lower | GRACE lower | Trends agree | GRACE higher | GRACE much higher |
|:---|:---:|:---:|:---:|:---:|:---:|
| last 5 years | 14 | 18 | 28 | 21 | 18 |
| last 10 years | 8 | 19 | 37 | 20 | 15 |
| last 15 years | 6 | 21 | 42 | 24 | 6 |
| last 20 years | 7 | 14 | 50 | 24 | 4 |
| whole record | 5 | 15 | 52 | 23 | 4 |

52 of the 99 aquifers agree over the whole record and 28 over the last five years. Both readings are correct for their window. A region that
changes class as you step the window is telling you that the two datasets differ about a recent swing, which is a smaller problem than
differing about the long-term direction.

## The agreement map

![The same aquifers colored by the correlation between the two monthly groundwater series](../../static/images/grace/app-diff-agreement.webp)

Agreement is the Pearson correlation of the two monthly series, over the months both datasets report. Months GRACE is missing are dropped from
both sides rather than filled, so the number is not affected by the gap-filling setting. The whole record is always used; the **Window** stepper
dims, because a correlation over five years asks a different question from one over twenty and the short answer is the noisier of the two.

| Class | Correlation | Aquifers in the Global Aquifers set |
|:---|:---:|:---:|
| Very close | above 0.8 | 28 |
| Close | 0.6 to 0.8 | 30 |
| Partial | 0.3 to 0.6 | 21 |
| Weak | 0 to 0.3 | 15 |
| Opposite | below 0 | 5 |

Read this map beside the anomaly map rather than on its own. A low correlation where little water moves says nothing about either dataset: below
about 5 cm of variation in GRACE groundwater the two correlate at a median of 0.19, and above about 15 cm they settle around 0.77 however much
more water is in play (see [Where a low correlation means nothing](examples.md#where-a-low-correlation-means-nothing)). The brown class, where
the two run opposite, is the case to take seriously, and it has a known mechanism: where the models' soil moisture cycle swings as hard as the
measured total water cycle, the subtraction behind the GRACE route cancels most of the groundwater signal and what remains can peak in the wrong
season (see [Where the cycles run opposite](examples.md#where-the-cycles-run-opposite)).

The weak and opposite classes sit mostly at high latitude on this map — the Siberian basins, the Baltic aquifers — which is the snow term rather
than an aquifer: no GLDAS model keeps seasonally frozen ground as a store, so an error in the models' snow passes straight into the GRACE
route's groundwater (see [Snow and frozen ground at high latitude](examples.md#snow-and-frozen-ground-at-high-latitude)).

## The seasonal swing map

![The same aquifers colored by the ratio of the two datasets' seasonal swings](../../static/images/grace/app-diff-swing.webp)

The swing is the height of the average year from its lowest month to its highest, after the long-term trend is removed, and this map colors each
region by the GRACE swing divided by the 2.2 swing. It is the same quantity the figures on the comparison pages plot, so a region's color here
and its numbers there agree.

| Class | Ratio | Aquifers in the Global Aquifers set |
|:---|:---:|:---:|
| GRACE much flatter | below 0.5 | 16 |
| GRACE flatter | 0.5 to 0.8 | 33 |
| Similar swing | 0.8 to 1.25 | 22 |
| GRACE swings more | 1.25 to 2 | 11 |
| GRACE swings much more | above 2 | 8 |

A ratio of two small numbers is unstable, so both swings have to exceed 1 cm for a region to be scored; nine of the 99 aquifers fall below that
and come back as **Insufficient data**, nearly all of them in the Sahara, on the Arabian Peninsula and in central Asia, where there is
too little annual cycle to take a ratio of. Of the 90 that are scored, 49 have the GRACE cycle flatter than 2.2's and 19 have it larger — the
pattern the amplitude cases show, with the GRACE route's swing cut by the soil moisture it subtracts. The aquifers where GRACE swings much
harder are mostly the ones where it is carrying something other than groundwater: a river, a floodplain, a reservoir or a snowpack the models do
not hold (see [Differences that are not groundwater](examples.md#differences-that-are-not-groundwater)).

## A cell is not a region

The global view answers the same three questions per 1° cell, and the answers come out far less settled than the regional ones:

| Share of the set in this condition | Global Aquifers, 99 outlines | 1° land cells |
|:---|:---:|:---:|
| trend difference beyond ±1 cm/yr, last 5 years | 32% | 44% |
| correlation below 0 | 5% | 18% |
| GRACE seasonal swing more than 1.25 times 2.2's | 21% | 45% |

One land cell in six has the two records running opposite, where five of the 99 aquifers do, and nearly half of all cells have the GRACE cycle
swinging harder than 2.2's, where the regional picture is the reverse.

![Every land cell colored by the difference between the two datasets' five-year groundwater trends](../../static/images/grace/app-diff-global.webp)

The map above is what that looks like: speckle over most of the land surface, red and blue cells alternating within a few hundred kilometres,
and the one large block of **Trends agree** lying across the Sahara and the Arabian Peninsula, where neither record moves much in five years.

A single cell carries the month-to-month noise that an area average removes, and on the GRACE side it also carries the gain factor applied to a
3° mascon, so one cell's value rests on the same measurement as its neighbors (see
[Resolution, Leakage and Small Regions](../mission/resolution-and-leakage.md)). Read the global comparison maps for where the large patterns
are, and the regional view for anything you mean to say about a particular aquifer.

## Reading a region against its chart

![The Central Valley with the trend difference showing: both datasets on the chart, each with its fitted line over the five-year window](../../static/images/grace/app-diff-chart.webp)

Clicking a region, or a cell in the global view, plots both datasets and puts the number behind that region's color under the chart title. The
Central Valley above reads "GWSa trend difference +1.92 cm/yr (last 5 yr)", with the two fitted lines in the legend at +3.40 and +1.43 cm/yr:
over the last five years both records have the valley recovering from the 2021–2022 drought and GRACE has it recovering more than twice as fast.
Over the whole record the same valley has GRACE losing 1.37 cm/yr against 2.2's 0.24 (see
[Where the trend differs](examples.md#where-the-trend-differs)), which is the window lesson in one region.

Under either trend measure each series also gets its fitted line as a dashed line. Agreement and a swing ratio have no line to draw, so the
chart reports the measure under its title and leaves the series plain.

The number under the title is the map's number, so it can differ slightly from the two slopes in the legend. Coloring every region in a set at
once averages the cells whose centers fall inside each outline, while the chart of the open region uses an overlap-weighted average of every cell
the outline touches (see [Regional View](../app/regional-view.md#which-cells-are-averaged)).

## What a large difference does and does not mean

A region colored at either extreme is a region to look into. It is not an error bar, and neither dataset is the truth the other is departing
from. Before treating a large difference as a result, run the checks in [Which One to Use](which-one-to-use.md#before-treating-a-large-difference-as-a-result):
plot snow water, compare the two totals, compare soil moisture against total water, check how much water is actually moving, and ask whether a
river, a lake or a reservoir could account for it.

Where the evidence does point one way, [How Far This Is Validated](validation.md) says how far. Two well comparisons and a 186-basin study
support preferring GRACE for the size of a trend and treating 2.2's as flattened. Nothing comparable settles the seasonal swing, so a region
colored **GRACE much flatter** is a disagreement about how a wet season is divided between the soil and the aquifer beneath it, with no
independent measurement to say which division is right.
