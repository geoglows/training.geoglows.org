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

`gapfill_example.py` draws `gap-filling-example.png` (Python with pandas and matplotlib) from `data/northern_midwest_filled.csv`, the
app's seasonal fill of a Northern Midwest Aquifer System export.

## App screenshots

`shots.mjs` drives the GRACE Regional Analyst in headless Chrome with puppeteer-core and saves full-resolution PNGs.

```
cd ../../../webapp-grace-groundwater && npx vite --port 5199 --strictPort   # in another terminal
npm install puppeteer-core
mkdir -p raw && node shots.mjs raw                  # all shots
node shots.mjs raw region,global                    # or a subset: home, panel, region, cv, global, modals, gapfill, recharge
```

The pages use WebP copies resized to 1800 px wide (quality 86), saved to `docs/static/images/grace/app-*.webp`.
