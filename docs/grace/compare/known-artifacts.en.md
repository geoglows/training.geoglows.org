# Known Artifacts

Some of the largest differences between the two datasets are places where one of them, usually the GRACE route, is reporting water that is not
groundwater. The app draws those cells like any other. This page names them so you can recognise one on sight rather than reading it as a
finding.

## Ice sheets and glaciers

The twelve 1° cells where the two groundwater records differ most are all ice:

| Cell | RMS difference | correlation | mean \|SWEa\| |
|---|---:|---:|---:|
| 66.5°N, 36.5°W (east Greenland) | 1019 cm | −0.03 | 327 cm |
| 66.5°N, 35.5°W | 805 cm | 0.02 | 283 cm |
| 66.5°N, 37.5°W | 777 cm | 0.02 | 330 cm |
| 76.5°N, 67.5°W (Ellesmere and Baffin) | 739 cm | 0.13 | 9 cm |
| 78.5°N, 15.5°E (Svalbard) | 734 cm | 0.39 | 24 cm |
| 76.5°N, 68.5°W | 729 cm | 0.19 | 6 cm |

GRACE measures the ice sheet losing mass. No GLDAS model carries glaciers or ice sheets, so SWEa cannot absorb that loss and the subtraction
hands it to groundwater, producing metre-scale GWSa in cells that hold no aquifer. 2.2 avoids the arithmetic but not the underlying problem: its
Catchment run has no ice either, and the GRACE increment it receives is spread across the model's stores, so it reports a far smaller number for
the same reason that it flattens trends elsewhere. Neither series means anything as groundwater here.

Two river basins in the app's own basin sets, Alsek and Santa Cruz, carry very large GWSa for this reason (see
[Deriving Groundwater Storage](../gldas/deriving-groundwater.md)).

**How to recognise it.** Switch the displayed layer to SWEa. Where the mean absolute SWEa runs to hundreds of centimetres, or the region sits on
an ice cap at any latitude, the groundwater layer is reporting ice.

## Surface water the models do not carry

In the Amazon the GRACE seasonal amplitude of GWSa is 40.8 cm against 2.2's 18.1, and the GRACE trend is +0.31 cm/yr against 2.2's −0.40. The
Amazon's total water cycle is dominated by river channel and floodplain storage, which no GLDAS model represents. On the GRACE route that
storage has nowhere to go in the subtraction and lands in groundwater; the Congo behaves the same way, and the two datasets disagree on the sign
of the trend in both.

Any basin where a large river rises and falls seasonally over a wide floodplain will do some version of this.

**How to recognise it.** A GWSa seasonal cycle on the GRACE route that is far larger than 2.2's, in a humid basin with a major river, is usually
surface water.

## Snow and frozen ground at high latitude

RMS difference between the two groundwater records, by latitude band:

| Band | RMS difference | mean \|SWEa\| | cells |
|---|---:|---:|---:|
| 60°S–30°S | 5.92 cm | 0.33 cm | 540 |
| 30°S–0° | 8.48 cm | 0.01 cm | 2,428 |
| 0°–30°N | 7.41 cm | 0.02 cm | 3,094 |
| 30°N–60°N | 6.49 cm | 2.12 cm | 5,397 |
| 60°N–90°N | 7.75 cm | 18.91 cm | 3,700 |

The northernmost band carries the snow, and the Siberian basins show the GRACE route with the larger seasonal amplitude — the Pechora at 12.1 cm
against 2.2's 3.3, West Siberia at 14.0 against 4.6. Snow mass that the model's SWEa does not match, and water held in seasonally frozen ground
that neither model treats as a separate store, both end up in the GRACE residual.

The tropical band is the worst of the ice-free bands, and that is the floodplain storage above rather than anything frozen.

## Shallow water tables

Where the water table is close to the surface, part of what GLDAS 2.1 counts as soil moisture is in fact groundwater, and subtracting it removes
the groundwater signal twice. The clearest case is the Northern Atlantic Coastal Plain, where the GRACE GWSa seasonal cycle ends up four months
out of phase with 2.2's. [Where Each One Is Trustworthy](trusting-each-one.md) gives the diagnostic and the affected aquifers.

## Regions where little happens

Over 1° cells whose GRACE GWSa standard deviation is under 5 cm, the median correlation between the two datasets is 0.19. Two small signals that
fail to line up produce that number whether or not anything is wrong. Before reading a low correlation as a problem, check how much water is
moving: the same comparison gives 0.77 in cells with more than 15 cm of variability.

## A short checklist

Before treating a large difference as a result:

1. Plot SWEa. Ice and snow explain most of the extremes.
2. Plot TWSa for both datasets. If they agree and only the groundwater disagrees, the problem is in the partition, not the measurement.
3. Compare the seasonal size of SMa against TWSa. Where they are comparable, distrust the phase of the GRACE groundwater.
4. Check the size of the signal before reading anything into a correlation.
5. Ask whether a river, a floodplain or a reservoir could account for the water.
