# Trend and Difference Analysis

## What the analysis does

**Analyze** in the header colors each region outline, in the regional view, or each grid cell, in the global view, by one number summarizing the
whole record in place of the value for the month on the time control. The analysis is on when the app opens; **Hide** turns it off and returns
the map to the monthly anomaly.

**Color by**, beside the button, chooses the number. One measure works on whichever dataset is selected, and three compare the two datasets
against each other:

| Color by | What it computes | Both datasets | Window |
|:---|:---|:---:|:---:|
| Trend in GWSa | least-squares slope of the monthly values, in cm/yr | no | yes |
| GRACE vs GLDAS 2.2: trend difference | the GRACE slope minus the 2.2 slope | yes | yes |
| GRACE vs GLDAS 2.2: agreement | Pearson correlation of the two monthly series | yes | no |
| GRACE vs GLDAS 2.2: seasonal swing | the GRACE seasonal swing divided by 2.2's | yes | no |

The trend entry names whatever is displayed, so it reads **Trend in GWSa** on the default layer and **Trend in SMa** on soil moisture. The three
comparisons appear only while groundwater (GWSa) is displayed, because that is the only quantity both datasets derive in their own right: the
2.1 route's soil moisture, snow and canopy water come from the three land surface models with no GRACE in them, so calling a comparison against
them "GRACE vs GLDAS 2.2" would name a dataset that is not in it.

Every measure needs at least 24 months of data in the window, and the three comparisons need 24 months both datasets report; a region or cell
with fewer is shown as **Insufficient data**. [Exploring the Differences in the App](../compare/exploring.md) covers what the three comparisons
mean, their class boundaries and how to read them. The rest of this page is about the trend.

## Trend classification

Under **Trend in GWSa**, or the trend in whatever else is displayed, each region or cell is colored by the rate at which that layer has been
rising or falling.

![Aquifers in the Global Aquifers set classified by their groundwater storage trend over the last five years](../../static/images/grace/app-home.webp)

In the regional view, above, each aquifer or basin gets one trend from the average of its cells (see
[Regional View](regional-view.md#the-landing-page)). That is the better guide for a particular aquifer.

![Groundwater storage trend over the last five years for every 1° cell, in the global view](../../static/images/grace/app-global-trends.webp)

The global view, above, classifies every land cell — 15,159 of them on the GRACE dataset's 1° grid and 17,346 on GLDAS 2.2's, which carries a
slightly larger land mask — so it shows where storage is changing regardless of aquifer boundaries: rising across the Sahel and East Africa,
falling across much of the Middle East, northern India and Brazil.

The trend is the slope of a straight line fitted by least squares to the monthly values in the window, in cm per year. Months with no GRACE
data are skipped rather than filled, which affects the GRACE dataset only; GLDAS 2.2 has a value in every month.

Trends are computed on whichever dataset is selected, so the classification changes when you switch. Two differences matter when comparing the
two maps. GLDAS 2.2 starts in February 2003 against GRACE's April 2002, so the **All** window covers ten fewer months. And a 2.2 trend is a
trend in a model state that GRACE corrects monthly, which inherits GRACE's resolution however fine the model grid looks.

| Class | Trend (cm/yr) |
|:---|:---:|
| Extreme decline | less than −2 |
| Decline | −2 to −0.5 |
| Static | −0.5 to +0.5 |
| Increase | +0.5 to +2 |
| Extreme increase | more than +2 |

The legend counts the regions or cells in each class. For reference, a trend of −2 cm/yr sustained over 100,000 km² is a loss of 2 km³ of water
a year.

### Gain factors and trend magnitudes

This section is about the GRACE dataset. GLDAS 2.2 is unaffected: no gain factor is applied to it, and the GRACE solution assimilated into it is
CSR's rather than JPL's.

The TWSa the app serves has JPL's gain factors applied (see
[Deriving Groundwater Storage](../gldas/deriving-groundwater.md#gain-factors)), and those factors flow straight into the trends, because a
constant multiplier on a time series multiplies its slope. JPL attaches a caution to this use: the factors are dominated by the annual cycle,
and the GRACE-FO Level-3 Handbook says they "can potentially introduce biases in frequency bands outside the annual component, in particular for
longer term trends," for which factors derived per averaging kernel would be needed. No such factors are published for this product, so the app
applies the standard ones throughout and reports one value of GWSa everywhere rather than one number for the map and a different one for the
trend.

In practice this moves most trends very little. Over the app's default five-year window the median cell's groundwater trend shifts by
0.12 cm/yr and the median trend magnitude goes from 0.95 to 0.93 cm/yr; over the whole record the median shift is 0.05 cm/yr. About 15% of cells
cross a class boundary over five years and 10% over the whole record — nearly all of them cells already sitting close to the ±0.5 or ±2 cm/yr
lines, where a small change in slope moves the label. The exceptions are glaciated cells, in Svalbard, Novaya Zemlya and the Patagonian
icefields, where a large factor is applied to an enormous ice signal and the trend can move by tens of cm per year. Those cells were never
groundwater. Treat a class as a summary rather than a measurement, and read the trend magnitude and the time series together.

## The analysis window

The **Window** stepper in the header sets how far back the fit reaches from the most recent month: 5, 10, 15 or 20 years, or **All** for the
whole record since 2002. The classification and the legend update when you change it.

Agreement and the seasonal swing always use the whole record, so the stepper dims under those two. A correlation over five years asks a
different question from one over twenty, and a seasonal cycle estimated from five years rests on five values per calendar month. The setting is
kept while the stepper is dimmed and comes back when you return to a trend.

Storage in most regions swings between wet and dry years, so a short window can capture one swing rather than the long-term direction. In
California's Central Valley, groundwater storage declined from 2002 through the drought of 2021–2022, then recovered partly after the very wet
winter of 2022–2023. The 5-year trend is an increase; the 20-year trend is a decline. Both are correct for their windows. Look at the time
series before drawing conclusions from a trend class, and compare more than one window.

## Fitted lines on the chart

When a region or cell is selected and a trend is showing, the chart adds the fitted line as a dashed line over the window, and the legend reports
the slope, for example "GWSa trend +2.25 cm/yr (last 5 yr)". Each plotted component gets its own trend line.

The trend difference draws both fits, one per dataset, and reports under the chart title the number the map was colored with. Agreement and the
seasonal swing have no line to draw, so the chart shows none and reports the measure under its title alone.

## How the region classification is computed

To classify every region in a set at once, under any of the four measures, the app averages the cells whose centers fall inside each region,
weighted by the cosine of latitude. This is faster than the overlap-weighted average used for the chart of a selected region (see
[Regional View](regional-view.md#which-cells-are-averaged)), and the two can differ slightly for small or narrow regions. The trend in the chart
legend, and the measure under the chart title, are computed from the chart's own series. A region too small to contain any cell center is
classified using the cell at its center.
