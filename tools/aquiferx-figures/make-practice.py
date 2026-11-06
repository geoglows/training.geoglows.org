"""Build the practice files the Part 2 screenshots import, from the app's Sample Data.

    python3 make-practice.py ../../../aquiferx/public/data

Writes practice/:
  sw-utah-region.geojson       outline of three Southwest Utah aquifers, merged
  sw-utah-aquifers.geojson     the three aquifers, with a NAME attribute and no ID
  sw-utah-wells.csv            their wells with 30 or more water levels, without ground elevations
  sw-utah-water-levels.csv     those wells' water levels, one row per measurement
  klamath-region.geojson       the Oregon sample's outline
  klamath-water-quality.csv    the Oregon sample's water quality, one row per sample, with locations
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from shapely.geometry import mapping, shape
from shapely.ops import unary_union

src = Path(sys.argv[1])
out = Path(__file__).parent / 'practice'
out.mkdir(exist_ok=True)

# Southwest Utah: Cedar Valley, Parowan Valley and Escalante Valley-Beryl-Enterprise
AQUIFERS = {'15', '16', '17'}
aq = json.loads((src / 'utah/aquifers.geojson').read_text())
feats = [f for f in aq['features'] if str(f['properties']['aquifer_id']) in AQUIFERS]
outline = unary_union([shape(f['geometry']) for f in feats]).buffer(0.01).simplify(0.002)
(out / 'sw-utah-region.geojson').write_text(json.dumps({
    'type': 'FeatureCollection',
    'features': [{'type': 'Feature', 'properties': {'NAME': 'Southwest Utah'}, 'geometry': mapping(outline)}],
}))
(out / 'sw-utah-aquifers.geojson').write_text(json.dumps({
    'type': 'FeatureCollection',
    'features': [{'type': 'Feature', 'properties': {'NAME': f['properties']['aquifer_name']}, 'geometry': f['geometry']}
                 for f in feats],
}))

levels = [r for r in csv.DictReader(open(src / 'utah/data_wte.csv')) if r['aquifer_id'] in AQUIFERS]
counts = Counter(r['well_id'] for r in levels)
keep = {w for w, n in counts.items() if n >= 30}
wells = [r for r in csv.DictReader(open(src / 'utah/wells.csv')) if r['well_id'] in keep]
with open(out / 'sw-utah-wells.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Well ID', 'Well Name', 'Latitude', 'Longitude'])
    for r in wells:
        w.writerow([r['well_id'], r['well_name'].strip(), round(float(r['lat']), 6), round(float(r['long']), 6)])
with open(out / 'sw-utah-water-levels.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Well ID', 'Date', 'WTE (ft)'])
    for r in levels:
        if r['well_id'] in keep:
            w.writerow([r['well_id'], r['date'], r['value']])

# Upper Klamath: water quality, one row per well and date with a column per parameter
(out / 'klamath-region.geojson').write_text((src / 'oregon/region.geojson').read_text())
PARAMS = [('ph', 'pH'), ('temperature', 'Temperature (deg C)'), ('tds', 'TDS (mg/L)'),
          ('hardness', 'Hardness (mg/L)'), ('alkalinity', 'Alkalinity (mg/L)'),
          ('dissolved_oxygen', 'Dissolved Oxygen (mg/L)')]
by_id = {r['well_id']: r for r in csv.DictReader(open(src / 'oregon/wells.csv'))}
samples = defaultdict(dict)
for code, _ in PARAMS:
    for r in csv.DictReader(open(src / f'oregon/data_{code}.csv')):
        samples[(r['well_id'], r['date'])][code] = r['value']
with open(out / 'klamath-water-quality.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Station', 'Latitude', 'Longitude', 'Date'] + [h for _, h in PARAMS])
    for (wid, date), vals in sorted(samples.items(), key=lambda kv: (by_id[kv[0][0]]['well_name'], kv[0][1])):
        well = by_id[wid]
        w.writerow([well['well_name'], well['lat'], well['long'], date] + [vals.get(c, '') for c, _ in PARAMS])

for p in sorted(out.iterdir()):
    print(p.name, p.stat().st_size)

# The same files as a download for readers, linked from Preparing Your Files
README = """Practice files for Aquifer Analyst, Part 2 of the training at training.geoglows.org

Southwest Utah, a region with three aquifers (Cedar Valley, Parowan Valley and
Escalante Valley-Beryl-Enterprise), in feet:
  sw-utah-region.geojson       the region outline
  sw-utah-aquifers.geojson     the aquifer outlines, named in a NAME attribute
  sw-utah-wells.csv            wells with long water level records, without ground elevations
  sw-utah-water-levels.csv     their water table elevations, one row per measurement

Upper Klamath, a single-unit region in Oregon, in feet:
  klamath-region.geojson       the region outline
  klamath-water-quality.csv    water quality samples, one row per sample, with each
                               well's name and location (the import creates the wells)

The data come from the USGS and the Oregon sample region that ship with the app.
"""
import zipfile
dest = Path(__file__).parents[2] / 'docs/static/files/aquiferx/aquifer-analyst-practice.zip'
dest.parent.mkdir(parents=True, exist_ok=True)
def entry(name):   # a fixed date, so a rebuild with the same data makes the same zip
    return zipfile.ZipInfo(f'aquifer-analyst-practice/{name}', date_time=(2026, 1, 1, 0, 0, 0))
with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr(entry('README.txt'), README, zipfile.ZIP_DEFLATED)
    for p in sorted(out.iterdir()):
        z.writestr(entry(p.name), p.read_bytes(), zipfile.ZIP_DEFLATED)
print(dest.relative_to(Path(__file__).parents[2]), dest.stat().st_size)
