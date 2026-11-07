"""Build the practice files for Part 2 of the Aquifer Analyst training from public data.

    python3 make-practice.py [cache-dir]

Needs shapely and geopandas. Downloads, once, into cache-dir (default .cache/ beside this script):

  - Monterey County's outline, from the US Census Bureau's cartographic boundary file of counties
    (1:500,000, 2024), which follows the shoreline
  - groundwater basin and subbasin outlines from California DWR's Bulletin 118 map service
  - wells and water levels from DWR's Periodic Groundwater Level Measurements (data.cnra.ca.gov)
  - water quality results for wells around the Pajaro Valley from the Water Quality Portal

and writes practice/:

  monterey-region.geojson        the outline of Monterey County
  monterey-aquifers.geojson      the nine Bulletin 118 basins and subbasins that lie wholly inside it
  monterey-wells.csv             DWR's monitoring wells in those aquifers that have water levels, with
                                 their depths where DWR gives them
  monterey-water-levels.csv      their water levels, one row per measurement
  pajaro-region.geojson          the outline of the Pajaro Valley subbasin
  pajaro-water-quality.csv       water quality samples from its wells, one row per sample, with each
                                 well's ID, name, location and, where the portal gives it, depth

and the same files as docs/static/files/aquiferx/aquifer-analyst-practice.zip. The counts in the zip's
README come from the data, so they stay right when the sources change.
"""
import csv
import json
import sys
import urllib.parse
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point, mapping, shape

here = Path(__file__).parent
cache = Path(sys.argv[1]) if len(sys.argv) > 1 else here / '.cache'
cache.mkdir(exist_ok=True)
out = here / 'practice'
out.mkdir(exist_ok=True)
for old in out.iterdir():
    old.unlink()

UA = {'User-Agent': 'aquifer-analyst-docs'}


def fetch(name, url, data=None, headers=None):
    """The file at url, downloaded once into the cache."""
    p = cache / name
    if not p.exists():
        print('downloading', name)
        req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
        with urllib.request.urlopen(req, timeout=600) as r:
            p.write_bytes(r.read())
    return p


def ckan_sql(name, sql_template, page=20000):
    """Every row of a query of data.cnra.ca.gov's datastore, a page at a time."""
    p = cache / name
    if not p.exists():
        rows, off = [], 0
        while True:
            q = sql_template + f' LIMIT {page} OFFSET {off}'
            url = 'https://data.cnra.ca.gov/api/3/action/datastore_search_sql?' + urllib.parse.urlencode({'sql': q})
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=600) as r:
                rec = json.load(r)['result']['records']
            rows += rec
            print(name, off, len(rec))
            if len(rec) < page:
                break
            off += page
        p.write_text(json.dumps(rows))
    return json.loads(p.read_text())


def round_coords(geom, nd=6):
    """A GeoJSON geometry with its coordinates rounded to nd decimals (about 0.1 m)."""
    def r(c):
        return [round(c[0], nd), round(c[1], nd)] if isinstance(c[0], float) else [r(x) for x in c]
    g = mapping(geom)
    return {'type': g['type'], 'coordinates': r(json.loads(json.dumps(g['coordinates'])))}


def num(v):
    """A number as text without trailing zeros: '747.50000' -> '747.5'; empty when there is none"""
    if v is None or str(v).strip() == '':
        return ''
    return ('%.7f' % float(v)).rstrip('0').rstrip('.')


def write_geojson(path, features):
    path.write_text(json.dumps({'type': 'FeatureCollection', 'features': [
        {'type': 'Feature', 'properties': props, 'geometry': round_coords(geom)} for props, geom in features]}))


# ---------------------------------------------------------------------------------------------
# Outlines

zp = fetch('cb_2024_us_county_500k.zip', 'https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_500k.zip')
counties = gpd.read_file(f'zip://{zp}', where="STATEFP='06' AND COUNTYFP='053'").to_crs(4326)
county = counties.geometry.iloc[0]
write_geojson(out / 'monterey-region.geojson', [({'name': 'Monterey County', 'geoid': '06053'}, county)])

AQUIFERS = ['3-004.01', '3-004.02', '3-004.04', '3-004.05', '3-004.08', '3-004.09', '3-004.10', '3-007', '3-006']
PAJARO = '3-002.01'
where = 'Basin_Subbasin_Number IN (' + ','.join(f"'{n}'" for n in AQUIFERS + [PAJARO]) + ')'
b118 = json.loads(fetch('b118.geojson', 'https://gis.water.ca.gov/arcgis/rest/services/Geoscientific/'
                        'i08_B118_CA_GroundwaterBasins/FeatureServer/0/query?' + urllib.parse.urlencode({
                            'where': where, 'outFields': 'Basin_Subbasin_Number,Basin_Subbasin_Name',
                            'outSR': 4326, 'f': 'geojson'})).read_text())
basins = {f['properties']['Basin_Subbasin_Number']: (f['properties']['Basin_Subbasin_Name'], shape(f['geometry']).buffer(0))
          for f in b118['features']}


def short_name(b118_name):
    """'SALINAS VALLEY - 180/400 FOOT AQUIFER' -> '180/400 Foot Aquifer', the name DWR's well records use"""
    return b118_name.split(' - ')[-1].title()


for n in AQUIFERS:     # the nine lie inside the county; the rest of the Pajaro Valley lies outside it
    assert basins[n][1].intersection(county).area / basins[n][1].area > 0.99, n
write_geojson(out / 'monterey-aquifers.geojson',
              [({'aquifer_id': n, 'aquifer_name': short_name(basins[n][0])}, basins[n][1]) for n in AQUIFERS])
write_geojson(out / 'pajaro-region.geojson', [({'name': 'Pajaro Valley', 'b118': PAJARO}, basins[PAJARO][1])])

# ---------------------------------------------------------------------------------------------
# Monterey County: DWR's wells and water levels

STATIONS = 'af157380-fb42-4abf-b72a-6f9f98868077'
MEASUREMENTS = 'bfa9f262-24a1-45bd-8dc8-138bc8107266'
stations = ckan_sql('dwr-stations.json', f'SELECT * FROM "{STATIONS}" WHERE county_name = \'Monterey\' ORDER BY _id')
levels = ckan_sql('dwr-measurements.json',
                  f'SELECT m.site_code, m.msmt_date, m.gwe, m.wlm_qa_desc FROM "{MEASUREMENTS}" m '
                  f'JOIN "{STATIONS}" s ON s.site_code = m.site_code WHERE s.county_name = \'Monterey\' ORDER BY m._id')

# Measurements DWR rates Good, with a groundwater elevation; it also lists visits with no measurement
# and measurements it rates Questionable
good = defaultdict(list)
dropped = {'No measurement': 0, 'Questionable': 0}
for r in levels:
    if r['wlm_qa_desc'] == 'Good' and r['gwe'] is not None:
        good[r['site_code']].append((r['msmt_date'][:10], r['gwe']))
    else:
        dropped[r['wlm_qa_desc']] = dropped.get(r['wlm_qa_desc'], 0) + 1
wells = sorted((s for s in stations if s['basin_code'] in AQUIFERS and good[s['site_code']]), key=lambda s: s['site_code'])
for s in wells:
    assert county.contains(Point(s['longitude'], s['latitude'])), s['site_code']
with open(out / 'monterey-wells.csv', 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['Well ID', 'Well Name', 'Latitude', 'Longitude', 'GSE', 'Well Depth', 'Aquifer ID'])
    for s in wells:
        w.writerow([s['site_code'], s['well_name'].strip(), num(s['latitude']), num(s['longitude']), num(s['gse']), num(s['well_depth']), s['basin_code']])
n_levels = 0
same_day = 0
with open(out / 'monterey-water-levels.csv', 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['Well ID', 'Date', 'WTE (ft)'])
    for s in wells:
        rows = sorted(good[s['site_code']])
        same_day += len(rows) - len({d for d, _ in rows})
        for d, v in rows:
            w.writerow([s['site_code'], d, num(v)])
        n_levels += len(rows)
first = min(d for s in wells for d, _ in good[s['site_code']])
last = max(d for s in wells for d, _ in good[s['site_code']])
per_aquifer = {n: sum(1 for s in wells if s['basin_code'] == n) for n in AQUIFERS}

# ---------------------------------------------------------------------------------------------
# Pajaro Valley: water quality from the Water Quality Portal

pajaro = basins[PAJARO][1]
x0, y0, x1, y1 = pajaro.bounds
bbox = f'{x0 - 0.01:.2f},{y0 - 0.01:.2f},{x1 + 0.01:.2f},{y1 + 0.01:.2f}'
# Columns of the file: the portal's characteristic, the unit the app keeps it in, and the units it is
# reported in here with the factor to that unit
PARAMS = [
    ('pH', 'pH', {'std units': 1}),
    ('Temperature, water', 'Temperature (deg C)', {'deg C': 1}),
    ('Specific conductance', 'Specific Conductance (uS/cm)', {'uS/cm @25C': 1}),
    ('Total dissolved solids', 'TDS (mg/L)', {'mg/l': 1}),
    ('Chloride', 'Chloride (mg/L)', {'mg/l': 1}),
    ('Nitrate', 'Nitrate (mg/L as N)', {'mg/l as N': 1, 'mg/l asNO3': 14.0067 / 62.0049}),
]
q = {'bBox': bbox, 'siteType': 'Well', 'mimeType': 'csv', 'zip': 'no'}
st_csv = fetch('wqp-stations.csv', 'https://www.waterqualitydata.us/data/Station/search?' + urllib.parse.urlencode(q))
res_csv = fetch('wqp-results.csv', 'https://www.waterqualitydata.us/data/Result/search?' + urllib.parse.urlencode(
    {**q, 'characteristicName': ';'.join(p for p, _, _ in PARAMS), 'dataProfile': 'resultPhysChem'}))
sites = {r['MonitoringLocationIdentifier']: r for r in csv.DictReader(open(st_csv))
         if pajaro.contains(Point(float(r['LongitudeMeasure']), float(r['LatitudeMeasure'])))}
assert {r['HorizontalCoordinateReferenceSystemDatumName'] for r in sites.values()} <= {'NAD83', 'WGS84'}
assert {r['WellDepthMeasure/MeasureUnitCode'] for r in sites.values()} <= {'ft', ''}
# One row per routine sample (field replicates left out), with a column per parameter. Where a
# sample has nitrate as N and as the nitrate ion, as N is kept; a result below the detection limit,
# which has no value, leaves its cell empty.
samples = defaultdict(dict)
for r in csv.DictReader(open(res_csv)):
    if r['MonitoringLocationIdentifier'] not in sites or r['ActivityTypeCode'] != 'Sample-Routine':
        continue
    units = next(u for c, _, u in PARAMS if c == r['CharacteristicName'])
    unit, value = r['ResultMeasure/MeasureUnitCode'], r['ResultMeasureValue']
    if unit not in units or not value:
        continue
    key = (r['MonitoringLocationIdentifier'], r['ActivityStartDate'])
    have = samples[key].get(r['CharacteristicName'])
    if have and have[1] == 1:
        continue
    samples[key][r['CharacteristicName']] = (float(value) * units[unit], units[unit])
with open(out / 'pajaro-water-quality.csv', 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['Well ID', 'Station', 'Latitude', 'Longitude', 'Well Depth', 'Date'] + [h for _, h, _ in PARAMS])
    for (sid, date), vals in sorted(samples.items(), key=lambda kv: (sites[kv[0][0]]['MonitoringLocationName'], kv[0][1])):
        s = sites[sid]
        w.writerow([sid, s['MonitoringLocationName'], num(s['LatitudeMeasure']), num(s['LongitudeMeasure']),
                    num(s['WellDepthMeasure/MeasureValue']), date] +
                   [('%.4g' % vals[c][0]) if c in vals else '' for c, _, _ in PARAMS])
wq_sites = {sid for sid, _ in samples}
wq_depth_wells = sum(1 for sid in wq_sites if num(sites[sid]['WellDepthMeasure/MeasureValue']))
depth_wells = sum(1 for s in wells if num(s['well_depth']))
wq_dates = sorted(d for _, d in samples)

# ---------------------------------------------------------------------------------------------

for p in sorted(out.iterdir()):
    print(p.name, p.stat().st_size)
print(f'{len(wells)} wells, {n_levels} water levels ({same_day} on a day the well already has one), {first} to {last}')
print('dropped', dropped, 'wells per aquifer', per_aquifer)
print(f'{len(wq_sites)} water quality wells, {len(samples)} samples, {wq_dates[0]} to {wq_dates[-1]}')

aquifer_lines = '\n'.join(f'    {n:<10} {short_name(basins[n][0]):<24} {per_aquifer[n]:>4} wells' for n in AQUIFERS)
README = f"""Practice files for Aquifer Analyst, Part 2 of the training at training.geoglows.org

Two regions in California built from public data, for practice in My Data. They are not
in the app's Sample Data. Lengths are in feet.

Monterey County, a region with nine aquifers
  monterey-region.geojson     the outline of the county, from the US Census Bureau's
                              cartographic boundary file of counties (1:500,000, 2024)
  monterey-aquifers.geojson   the nine groundwater basins and subbasins of California DWR's
                              Bulletin 118 that lie wholly inside the county. aquifer_id is the
                              Bulletin 118 number and aquifer_name the subbasin's name:
{aquifer_lines}
  monterey-wells.csv          the {len(wells)} monitoring wells in those aquifers that have water
                              levels in DWR's Periodic Groundwater Level Measurements, with
                              DWR's site code as the well ID, the ground surface elevation DWR
                              gives, the well depth DWR gives for {depth_wells} of them, and the
                              Bulletin 118 number of the subbasin DWR lists
  monterey-water-levels.csv   their {n_levels:,} groundwater elevations, {first[:4]} to {last[:4]}, one row
                              per measurement: the measurements DWR rates Good. {same_day:,} are a
                              second measurement of a well on the same day.

Pajaro Valley, a single-unit region
  pajaro-region.geojson       the outline of the Pajaro Valley subbasin (Bulletin 118 {PAJARO})
  pajaro-water-quality.csv    {len(samples):,} water samples from {len(wq_sites)} wells inside it, {wq_dates[0][:4]} to {wq_dates[-1][:4]},
                              from the Water Quality Portal (all collected by the USGS), one row
                              per sample with a column per parameter. Each row gives the well's
                              site ID in the portal, its name, its location and, for {wq_depth_wells}
                              of the wells, its depth, from which the import makes the wells.
                              Nitrate reported as the nitrate ion is converted to nitrate as N.
                              A result below the detection limit leaves its cell empty.

Downloaded and built by tools/aquiferx-figures/make-practice.py in the training.geoglows.org
repository.
"""
(out / 'README.txt').write_text(README)
dest = here.parents[1] / 'docs/static/files/aquiferx/aquifer-analyst-practice.zip'
dest.parent.mkdir(parents=True, exist_ok=True)


def entry(name):   # a fixed date, so a rebuild with the same data makes the same zip
    return zipfile.ZipInfo(f'aquifer-analyst-practice/{name}', date_time=(2026, 1, 1, 0, 0, 0))


with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out.iterdir()):
        z.writestr(entry(p.name), p.read_bytes(), zipfile.ZIP_DEFLATED)
print(dest.relative_to(here.parents[1]), dest.stat().st_size)
