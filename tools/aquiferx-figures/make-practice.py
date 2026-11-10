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
  monterey-wells.csv             DWR's monitoring wells in those aquifers that have water levels
  monterey-water-levels.csv      their water levels, one row per measurement
  pajaro-region.geojson          the outline of the Pajaro Valley subbasin
  pajaro-water-quality.csv       water quality samples from its wells, one row per sample, with each
                                 well's ID, name and location

Aquifer Analyst takes one well at each place in an aquifer (wells within 10 m of each other), so
where the sources have more, such as nested wells finished at different depths, the files keep one:
in Monterey County the well whose water levels agree best with those of nearby wells, in the
Pajaro Valley the shallowest. The README lists the wells left out.

and the same files as docs/static/files/aquiferx/aquifer-analyst-practice.zip. The counts in the zip's
README come from the data, so they stay right when the sources change.
"""
import bisect
import csv
import json
import math
import statistics
import sys
import urllib.parse
import urllib.request
import zipfile
from collections import defaultdict
from datetime import date
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


COLOCATED_METERS = 10   # as in the app's utils/geo.ts


def meters(lat1, lng1, lat2, lng2):
    la1, lo1, la2, lo2 = map(math.radians, [float(lat1), float(lng1), float(lat2), float(lng2)])
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371000 * 2 * math.asin(math.sqrt(h))


def places(items, aquifer, lat, lng):
    """The groups of two or more items of one aquifer within COLOCATED_METERS of each other, chained,
    as the app's services/sharedLocations.ts finds them, each in the order of items"""
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, a in enumerate(items):
        for j in range(i + 1, len(items)):
            b = items[j]
            if aquifer(a) == aquifer(b) and meters(lat(a), lng(a), lat(b), lng(b)) < COLOCATED_METERS:
                parent[find(i)] = find(j)
    groups = defaultdict(list)
    for i, it in enumerate(items):
        groups[find(i)].append(it)
    return [g for g in groups.values() if len(g) > 1]


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
# and measurements it rates Questionable. Some measurements are in DWR's datastore twice, as two
# records next to each other that agree in every field; the second is a copy and is left out.
good = defaultdict(list)
dropped = {'No measurement': 0, 'Questionable': 0}
copies = defaultdict(int)
seen = set()
for r in levels:
    if r['wlm_qa_desc'] == 'Good' and r['gwe'] is not None:
        key = (r['site_code'], r['msmt_date'], r['gwe'])
        if key in seen:
            copies[r['site_code']] += 1
            continue
        seen.add(key)
        good[r['site_code']].append((r['msmt_date'][:10], r['gwe']))
    else:
        dropped[r['wlm_qa_desc']] = dropped.get(r['wlm_qa_desc'], 0) + 1
wells = sorted((s for s in stations if s['basin_code'] in AQUIFERS and good[s['site_code']]), key=lambda s: s['site_code'])
for s in wells:
    assert county.contains(Point(s['longitude'], s['latitude'])), s['site_code']

# One well at each place. Each water level of a well at a place is compared with the level estimated
# for its date from nearby wells of the same aquifer that stand alone: up to NEIGHBORS of them within
# RADIUS of the place, nearest first, each with a measurement within DAYS of the date, weighted by
# the inverse square of distance (50 m at least), and at least MIN_NEIGHBORS of them. The well whose
# levels lie closest to the estimates (the median of the differences, ignoring sign) is kept. A well
# with fewer than MIN_COMPARED such comparisons is not scored; where no well at a place is, the
# shallowest is kept, then the one with the most measurements.
RADIUS, DAYS, NEIGHBORS, MIN_NEIGHBORS, MIN_COMPARED = 8000, 45, 6, 3, 5
series = {s['site_code']: sorted((date.fromisoformat(d).toordinal(), float(v)) for d, v in good[s['site_code']]) for s in wells}
times = {k: [t for t, _ in v] for k, v in series.items()}
mplaces = places(wells, lambda s: s['basin_code'], lambda s: s['latitude'], lambda s: s['longitude'])
at_place = {s['site_code'] for g in mplaces for s in g}


def differences(site, neighbors):
    out = []
    for t, v in series[site]:
        pts = []
        for d, n in neighbors:
            k = bisect.bisect_left(times[n], t)
            near = min((series[n][j] for j in (k - 1, k) if 0 <= j < len(series[n])), key=lambda x: abs(x[0] - t))
            if abs(near[0] - t) <= DAYS:
                pts.append((d, near[1]))
                if len(pts) == NEIGHBORS:
                    break
        if len(pts) >= MIN_NEIGHBORS:
            wts = [1 / max(d, 50) ** 2 for d, _ in pts]
            out.append(v - sum(wt * y for wt, (_, y) in zip(wts, pts)) / sum(wts))
    return out


def depth_of(v):
    return float(v) if num(v) else None


monterey_kept = []   # per place: [(station, measurements, comparisons, median difference)], the kept one first
for g in mplaces:
    o = g[0]
    neighbors = sorted((meters(o['latitude'], o['longitude'], s['latitude'], s['longitude']), s['site_code'])
                       for s in wells if s['basin_code'] == o['basin_code'] and s['site_code'] not in at_place)
    neighbors = [x for x in neighbors if x[0] <= RADIUS]
    rows = []
    for s in g:
        diffs = differences(s['site_code'], neighbors)
        rows.append((s, len(series[s['site_code']]), len(diffs), statistics.median(abs(x) for x in diffs) if diffs else None))
    scored = [r for r in rows if r[2] >= MIN_COMPARED]
    if scored:
        kept = min(scored, key=lambda r: r[3])
    else:
        kept = min(rows, key=lambda r: (depth_of(r[0]['well_depth']) is None, depth_of(r[0]['well_depth']) or 0, -r[1]))
    monterey_kept.append([kept] + [r for r in rows if r is not kept])
monterey_left = {r[0]['site_code'] for p in monterey_kept for r in p[1:]}
monterey_left_levels = sum(len(good[k]) for k in monterey_left)
wells = [s for s in wells if s['site_code'] not in monterey_left]

with open(out / 'monterey-wells.csv', 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['Well ID', 'Well Name', 'Latitude', 'Longitude', 'GSE', 'Aquifer ID'])
    for s in wells:
        w.writerow([s['site_code'], s['well_name'].strip(), num(s['latitude']), num(s['longitude']), num(s['gse']), s['basin_code']])
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
n_copies = sum(copies[s['site_code']] for s in wells)

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

# One well at each place, the rule of the app's water quality download at its first setting: the
# shallowest, when the portal gives every well there a depth and one is shallowest; otherwise the one
# with the most samples, then the longest span of samples, then the first by site ID.
n_samples = defaultdict(int)
sample_dates = defaultdict(list)
for sid, d in samples:
    n_samples[sid] += 1
    sample_dates[sid].append(date.fromisoformat(d).toordinal())
pplaces = places([sites[sid] for sid in sorted(n_samples)], lambda s: '0',
                 lambda s: s['LatitudeMeasure'], lambda s: s['LongitudeMeasure'])
pajaro_kept = []   # per place: [(station, reason)], the kept one first
for g in pplaces:
    depth = {s['MonitoringLocationIdentifier']: depth_of(s['WellDepthMeasure/MeasureValue']) for s in g}
    pool = g
    if all(v is not None for v in depth.values()):
        pool = [s for s in g if depth[s['MonitoringLocationIdentifier']] == min(depth.values())]
    by_depth = len(pool) == 1

    def score(s):
        sid = s['MonitoringLocationIdentifier']
        return (n_samples[sid], max(sample_dates[sid]) - min(sample_dates[sid]))
    kept = max(pool, key=score)   # max keeps the first of equals
    rows = [(kept, '')]
    for s in g:
        if s is kept:
            continue
        rows.append((s, 'deeper' if by_depth or s not in pool else 'fewer samples' if score(s) < score(kept) else 'tie'))
    pajaro_kept.append(rows)
pajaro_left = {s['MonitoringLocationIdentifier'] for p in pajaro_kept for s, _ in p[1:]}
pajaro_left_samples = sum(n_samples[k] for k in pajaro_left)
samples = {k: v for k, v in samples.items() if k[0] not in pajaro_left}

with open(out / 'pajaro-water-quality.csv', 'w', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['Well ID', 'Station', 'Latitude', 'Longitude', 'Date'] + [h for _, h, _ in PARAMS])
    for (sid, d), vals in sorted(samples.items(), key=lambda kv: (sites[kv[0][0]]['MonitoringLocationName'], kv[0][1])):
        s = sites[sid]
        w.writerow([sid, s['MonitoringLocationName'], num(s['LatitudeMeasure']), num(s['LongitudeMeasure']), d] +
                   [('%.4g' % vals[c][0]) if c in vals else '' for c, _, _ in PARAMS])
wq_sites = {sid for sid, _ in samples}
wq_dates = sorted(d for _, d in samples)

# ---------------------------------------------------------------------------------------------

for p in sorted(out.iterdir()):
    print(p.name, p.stat().st_size)
print(f'{len(wells)} wells, {n_levels} water levels ({same_day} on a day the well already has one, {n_copies} copies left out), {first} to {last}')
print(f'{len(mplaces)} places with more than one well: {len(monterey_left)} wells and {monterey_left_levels} water levels left out')
print('dropped', dropped, 'wells per aquifer', per_aquifer)
print(f'{len(wq_sites)} water quality wells, {len(samples)} samples, {wq_dates[0]} to {wq_dates[-1]}')
print(f'{len(pplaces)} places with more than one well: {len(pajaro_left)} wells and {pajaro_left_samples} samples left out')


def ft(v):
    return f'{depth_of(v):,.0f} ft' if depth_of(v) is not None else 'depth ?'


monterey_lines = []
for p in sorted(monterey_kept, key=lambda p: (AQUIFERS.index(p[0][0]['basin_code']), p[0][0]['well_name'].strip())):
    for i, (st, n, m, diff) in enumerate(p):
        how = f'{diff:5.1f} ft' if m >= MIN_COMPARED else f'{n} measurement{"s" if n != 1 else ""}, too few to compare'
        monterey_lines.append(f"    {p[0][0]['basin_code'] if i == 0 else '':<9} {'kept' if i == 0 else 'left out':<9}"
                              f"{st['well_name'].strip()[:22]:<23}{st['site_code']:<20}{ft(st['well_depth']):>9}  {how}")
pajaro_lines = []
for p in sorted(pajaro_kept, key=lambda p: p[0][0]['MonitoringLocationName']):
    for i, (st, why) in enumerate(p):
        sid = st['MonitoringLocationIdentifier']
        pajaro_lines.append(f"    {'kept' if i == 0 else 'left out':<9}{st['MonitoringLocationName']:<17}{sid:<22}"
                            f"{ft(st['WellDepthMeasure/MeasureValue']):>9}  {n_samples[sid]:>3} sample{'s' if n_samples[sid] != 1 else ''}"
                            + ('  (the same depth and samples as the kept well; it comes later by site ID)' if why == 'tie' else ''))
monterey_lines = '\n'.join(monterey_lines)
pajaro_lines = '\n'.join(pajaro_lines)

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
  monterey-wells.csv          {len(wells)} monitoring wells in those aquifers that have water levels
                              in DWR's Periodic Groundwater Level Measurements, one at each place
                              (see Wells left out, below), with DWR's site code as the well ID,
                              the ground surface elevation DWR gives, and the Bulletin 118 number
                              of the subbasin DWR lists
  monterey-water-levels.csv   their {n_levels:,} groundwater elevations, {first[:4]} to {last[:4]}, one row
                              per measurement: the measurements DWR rates Good. {same_day:,} are on a
                              day the well already has a measurement. DWR's datastore has
                              {n_copies:,} more records that repeat one of these in every field,
                              which are left out.

Pajaro Valley, a single-unit region
  pajaro-region.geojson       the outline of the Pajaro Valley subbasin (Bulletin 118 {PAJARO})
  pajaro-water-quality.csv    {len(samples):,} water samples from {len(wq_sites)} wells inside it, {wq_dates[0][:4]} to {wq_dates[-1][:4]},
                              from the Water Quality Portal (all collected by the USGS), one well
                              at each place (see Wells left out, below), one row per sample with
                              a column per parameter. Each row gives the well's site ID in the
                              portal, its name and its location, from which the import makes the
                              wells. Nitrate reported as the nitrate ion is converted to nitrate
                              as N. A result below the detection limit leaves its cell empty.

Wells left out

Aquifer Analyst takes one well at each place in an aquifer, because wells of one aquifer within
10 m of each other would be averaged into one value on a map. The sources have more than one well
at some places, mostly nested wells finished at different depths, and the files keep one.

Monterey County: {len(mplaces)} places, {len(monterey_left)} wells left out with their {monterey_left_levels:,} water levels. Each
place keeps the well whose water levels agree best with those of nearby wells in the same aquifer.
Every water level is compared with the level estimated for its date from up to {NEIGHBORS} wells of the
aquifer within {RADIUS // 1000} km that stand alone and were measured within {DAYS} days of it, weighted by the
inverse square of distance; the well with the smaller median difference (ignoring sign) is kept.
A well with fewer than {MIN_COMPARED} such comparisons is not scored. Depths are the ones DWR gives.

    aquifer            name                   site code                depth  median difference
{monterey_lines}

Pajaro Valley: {len(pplaces)} places, {len(pajaro_left)} wells left out with their {pajaro_left_samples} samples. Each place keeps the
shallowest well, by the depth the portal gives, as the app's water quality download does at its
first setting; where depths are missing or equal, the well with the most samples.

             station          site ID                  depth  samples
{pajaro_lines}

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
