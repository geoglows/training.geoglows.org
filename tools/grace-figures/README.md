# GRACE documentation figures

Scripts that generate the diagrams and app screenshots used in `docs/grace/`.

## Diagrams

Each `*.py` script (except `common.py`) writes an editable SVG to `docs/static/images/grace/diagrams/` and renders a 2x PNG next to the
pages' other images with Inkscape. They need Python 3.11+ with `pandas` and `shapely`, and Inkscape at
`/Applications/Inkscape.app` (change `INKSCAPE` in `common.py` elsewhere).

```
python mission.py        # mission geometry: altitude, separation, ranging, GPS
python ranging.py        # GRACE satellite ranging over a mass anomaly
python timeline.py       # GRACE / GRACE-FO record and missing months
python waterbalance.py   # storage components and the water balance
python pipeline.py       # processing chain from NASA inputs to app layers
python leakage.py        # grid sizes and signal leakage
python averaging.py      # region averaging with the 35% overlap rule
python wtf.py            # water table fluctuation method, conceptual
```

Edit the SVGs directly in Inkscape for one-off changes, but rerunning a script overwrites its SVG.

`compare_examples.py` draws the six worked examples on the Comparing the Two Datasets pages (`compare-agreement.png`,
`compare-amplitude.png`, `compare-phase.png`, `compare-trend.png`, `compare-artifact-ice.png`, `compare-artifact-amazon.png`). It needs
pandas and matplotlib, and reads `data/compare_*.csv`, which `data/export_compare_series.py` in webapp-grace-groundwater writes from the
published stores:

```
cd ../../../webapp-grace-groundwater && data/.venv/bin/python -I data/export_compare_series.py
cd -  &&  python compare_examples.py
```

Each CSV is one region's monthly area-weighted mean of both datasets' GWSa, TWSa and SMa, plus GRACE SWEa, which is the series the app's
regional view plots. Regenerate the CSVs after a data rebuild and the figures follow.

`gapfill_example.py` draws `gap-filling-example.png` (Python with pandas and matplotlib) from `data/northern_midwest_filled.csv`, the
app's seasonal fill of a Northern Midwest Aquifer System export.

`seasonal_model.py` refits the app's seasonal model (`src/gapFill.js` in webapp-grace-groundwater) to the same file, checks that it matches
the app's fill, and draws the four figures on the Seasonal Model page: `seasonal-decomposition.png`, `seasonal-levels.png`,
`seasonal-breakpoints.png` and `seasonal-gap-correction.png`. It also refits `data/central_valley_gwsa.csv`, an app export, for
`seasonal-gap-correction-cv.png`, the Central Valley's gap between the missions. It prints the breakpoints, the BIC of each fit, the
seasonal levels and the residuals either side of the mission gap, which are the numbers the Gaps and Gap Filling page quotes.

`holdout.mjs` produces the two RMSE tables on that page. It hides observed months, refits, and compares the app's seasonal model against the
trend and seasonal cycle alone and against linear interpolation. It imports `src/gapFill.js` directly rather than reimplementing it, so the
tables cannot drift from what the app does, and its PRNG is seeded so a rerun reproduces them.

```
node holdout.mjs <dir>     # <dir> holds one Download CSV export per region
```

Both read data regenerated from the app after a rebuild. `data/northern_midwest_filled.csv` is an export plus the app's own
trend/seasonal/filled columns; `data/central_valley_gwsa.csv` is the GWSa columns of an export.

## App screenshots

`shots.mjs` drives the GRACE Regional Analyst in headless Chrome with puppeteer-core and saves full-resolution PNGs.

```
cd ../../../webapp-grace-groundwater && npx vite --port 5199 --strictPort   # in another terminal
npm install puppeteer-core
mkdir -p raw && node shots.mjs raw                  # all shots
node shots.mjs raw region,global                    # or a subset: home, panel, region, cv, global, modals, gapfill, recharge
```

The pages use WebP copies resized to 1800 px wide (quality 86), saved to `docs/static/images/grace/app-*.webp`.
