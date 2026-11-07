# Aquifer Analyst documentation figures

Scripts that make the app screenshots used in `docs/aquiferx/`.

## Screenshots

`shots.mjs` drives Aquifer Analyst in headless Chrome with puppeteer-core and saves full-resolution PNGs to `raw/`, using the app's
Sample Data. It needs a local build of the app served on port 5198, from a clone of
[geoglows/aquiferx](https://github.com/geoglows/aquiferx):

```
cd ../../../aquiferx && npx vite build && npx vite preview --port 5198 --strictPort
```

Then, in this folder:

```
npm install puppeteer-core
node shots.mjs raw                      # every shot
node shots.mjs raw region,multiwell     # just these steps
./webp.sh                               # raw/*.png -> docs/static/images/aquiferx/*.webp
```

`AQX_URL` points the script at another address, such as the deployed preview. The steps are `home`, `region`, `menu`, `multiwell`,
`filter`, `datatype`, `mydata` and `settings` for Part 1, and `adddata`, `wq` and `edit` for Part 2; each names the shots it saves in
the script. The browser profile in `.chrome-profile/` keeps the app's remembered settings between runs, so every step that opens an
aquifer resets the data set and the well filters first.

The Part 2 steps import the files in `practice/`, which `make-practice.py` downloads and builds from public data: the Census
Bureau's county outlines, California DWR's Bulletin 118 basins and its periodic groundwater levels, and the Water Quality Portal
(`python3 make-practice.py`; it needs shapely and geopandas, and keeps the downloads in `.cache/`). It also writes the zip the pages
link to. `adddata` deletes everything in the browser profile's My Data and builds a Monterey County region from them; `wq` adds a
Pajaro Valley region; `edit` works in the Monterey County region, so run the three in that order. The water quality import looks up
ground elevations for the wells it makes, so it needs a network connection.

`webp.sh` writes WebP copies at quality 86, reduced to 1800 px wide when the PNG is wider, which is what the pages use.

## Diagrams

`diagrams.py` draws the two figures on Preparing Your Files from the files in `practice/`, so run `make-practice.py` first. It writes
editable SVGs to `docs/static/images/aquiferx/diagrams/` and renders 2x PNGs next to the pages' other images with Inkscape, the same way
as the GRACE diagrams. It needs shapely, and Inkscape at `/Applications/Inkscape.app`.

```
python3 diagrams.py     # files-map.png and files-links.png
```

The aquifer names on the map are placed by hand for the practice region, so check them if the practice files change.
