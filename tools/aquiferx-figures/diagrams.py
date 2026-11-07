"""Draw the Preparing Your Files diagrams from the practice files.

    python3 diagrams.py

Run make-practice.py first. Writes editable SVGs to docs/static/images/aquiferx/diagrams/ and renders 2x PNGs next to the
pages' other images with Inkscape. Needs shapely, and Inkscape at /Applications/Inkscape.app (change INKSCAPE elsewhere).

  files-map.png     the Monterey County practice region: outline, aquifers, wells, and one well's water levels
  files-links.png   the four files, a few rows of each, and the columns that tie them together
"""
import csv
import json
import math
import subprocess
from datetime import date
from pathlib import Path

from shapely.geometry import Point, shape

HERE = Path(__file__).resolve().parent
PRACTICE = HERE / 'practice'
OUT = HERE.parents[1] / 'docs' / 'static' / 'images' / 'aquiferx'
INKSCAPE = '/Applications/Inkscape.app/Contents/MacOS/inkscape'

# Same palette and type as the GRACE diagrams
FONT = 'Helvetica, Arial, sans-serif'
MONO = 'Menlo, Consolas, monospace'
C = dict(
    navy='#1f3a5f', blue='#2b6cb0', teal='#2c7a7b', orange='#dd6b20', gray='#718096', darkgray='#4a5568',
    lightgray='#e2e8f0', gold='#b7791f', sky='#f7fafc', faint='#edf2f7', green='#2f855a', purple='#6b46c1',
)
# Neighboring aquifers in different colors
AQ_COLOR = {'3-004.01': 'green', '3-004.02': 'purple', '3-004.09': 'gold', '3-004.04': 'gold', '3-004.10': 'blue',
            '3-004.08': 'gold', '3-004.05': 'green', '3-006': 'blue', '3-007': 'green'}
WELL_ID = '367886N1216748W001'       # 13783, in the Langley Area: the well on the Editing page, measured
                                     # each winter, with a steady record and one bad value


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def text(x, y, s, size=14, anchor='start', weight='normal', fill='darkgray', font=FONT, italic=False):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" font-weight="{weight}"{st} '
            f'text-anchor="{anchor}" fill="{C.get(fill, fill)}">{s}</text>')


def tspan(s, fill=None, weight=None, font=None):
    a = ''
    if fill:
        a += f' fill="{C.get(fill, fill)}"'
    if weight:
        a += f' font-weight="{weight}"'
    if font:
        a += f' font-family="{font}"'
    return f'<tspan{a}>{esc(s)}</tspan>'


def line(x1, y1, x2, y2, col='darkgray', w=1.5, dash=None, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C.get(col, col)}" '
            f'stroke-width="{w}" stroke-linecap="round" opacity="{opacity}"{d}/>')


def path(d, stroke='darkgray', w=1.5, fill='none', fill_opacity=1, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="{C.get(fill, fill)}" fill-opacity="{fill_opacity}" stroke="{C.get(stroke, stroke)}" '
            f'stroke-width="{w}" stroke-linejoin="round"{ds}/>')


def svg_doc(w, h, body, title):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
            f'<title>{esc(title)}</title>\n<rect width="{w}" height="{h}" fill="white"/>\n{body}\n</svg>\n')


def save(name, svg):
    (OUT / 'diagrams').mkdir(parents=True, exist_ok=True)
    src = OUT / 'diagrams' / f'{name}.svg'
    src.write_text(svg)
    png = OUT / f'{name}.png'
    subprocess.run([INKSCAPE, str(src), '--export-type=png', f'--export-filename={png}', '--export-dpi=192',
                    '--export-background=white'], check=True, capture_output=True)
    print('saved', png.name)


# ---------------------------------------------------------------- data

region = shape(json.loads((PRACTICE / 'monterey-region.geojson').read_text())['features'][0]['geometry'])
aq_feats = json.loads((PRACTICE / 'monterey-aquifers.geojson').read_text())['features']
aquifers = {f['properties']['aquifer_id']: (f['properties']['aquifer_name'], shape(f['geometry'])) for f in aq_feats}
wells = list(csv.DictReader(open(PRACTICE / 'monterey-wells.csv')))
wells_by_id = {w['Well ID']: w for w in wells}
levels = [r for r in csv.DictReader(open(PRACTICE / 'monterey-water-levels.csv')) if r['Well ID'] == WELL_ID]


def rings(geom):
    polys = geom.geoms if geom.geom_type == 'MultiPolygon' else [geom]
    for p in polys:
        yield p.exterior.coords
        for r in p.interiors:
            yield r.coords


class Projection:
    """Plate carree scaled by cos(latitude), fitted to a box."""

    def __init__(self, bounds, box):
        lon0, lat0, lon1, lat1 = bounds
        self.k = math.cos(math.radians((lat0 + lat1) / 2))
        bx, by, bw, bh = box
        sx = bw / ((lon1 - lon0) * self.k)
        sy = bh / (lat1 - lat0)
        self.s = min(sx, sy)
        w = (lon1 - lon0) * self.k * self.s
        h = (lat1 - lat0) * self.s
        self.x0 = bx + (bw - w) / 2
        self.y0 = by + (bh - h) / 2
        self.lon0, self.lat1 = lon0, lat1

    def __call__(self, lng, lat):
        return self.x0 + (lng - self.lon0) * self.k * self.s, self.y0 + (self.lat1 - lat) * self.s

    def d(self, geom):
        out = []
        for ring in rings(geom):
            pts = [self(x, y) for x, y in ring]
            out.append('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z')
        return ' '.join(out)


# ---------------------------------------------------------------- figure 1: the map

def files_map():
    W, H = 960, 470
    body = []
    body.append(text(30, 36, f'Monterey County: one region, nine aquifers, {len(wells)} wells', 17, weight='bold', fill='navy'))

    proj = Projection(region.bounds, (110, 60, 500, 395))
    body.append(path(proj.d(region), stroke='darkgray', w=2, fill='sky'))
    for aid, (name, g) in aquifers.items():
        col = AQ_COLOR[aid]
        body.append(path(proj.d(g), stroke=col, w=1.4, fill=col, fill_opacity=0.25))

    hi = None
    for wl in wells:
        x, y = proj(float(wl['Longitude']), float(wl['Latitude']))
        if wl['Well ID'] == WELL_ID:
            hi = (x, y)
            continue
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{C["navy"]}" stroke="white" stroke-width="0.5"/>')
    hx, hy = hi
    body.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="6.5" fill="{C["orange"]}" stroke="white" stroke-width="1.5"/>')

    # Aquifer names, with a leader to a point inside each outline: (id, label x, label y, anchor, lon, lat)
    for aid, lx, ly, anchor, lon, lat in LABELS:
        name, g = aquifers[aid]
        col = AQ_COLOR[aid]
        tx, ty = proj(lon, lat)
        ex = lx + (4 if anchor == 'start' else -4)
        body.append(line(ex, ly - 4, tx, ty, col, 1.2))
        body.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="3" fill="{C[col]}" stroke="white" stroke-width="1"/>')
        body.append(text(lx + (8 if anchor == 'start' else -8), ly, esc(name), 12.5, weight='bold', fill=col, anchor=anchor))

    # The region outline, from its eastern edge
    ring_pts = [proj(x, y) for r in rings(region) for x, y in r]
    lx, ly = 340, 206
    bx, by = min(ring_pts, key=lambda p: (p[0] - lx) ** 2 + (p[1] - ly) ** 2)
    body.append(line(bx + 2, by, lx - 4, ly - 4, 'darkgray', 1))
    body.append(text(lx, ly, 'Region outline', 13, weight='bold'))

    # The orange well's record
    cx0, cy0, cw, ch = 700, 132, 230, 160
    body.append(text(650, 98, 'Measurements at the orange well', 14, weight='bold', fill='orange'))
    body.append(text(650, 117, 'Water table elevation, ft', 13))
    pts = [(date.fromisoformat(r['Date']), float(r['WTE (ft)'])) for r in levels]
    t0, t1 = date(1955, 1, 1), date(2030, 1, 1)
    v0, v1, dv = -10, 30, 10
    def px(d):
        return cx0 + (d - t0).days / (t1 - t0).days * cw
    def py(v):
        return cy0 + ch - (v - v0) / (v1 - v0) * ch
    for v in range(v0, v1 + 1, dv):
        y = py(v)
        body.append(line(cx0, y, cx0 + cw, y, 'lightgray', 1))
        body.append(text(cx0 - 6, y + 4, f'{v:,}'.replace('-', '−'), 12, anchor='end', fill='gray'))
    for yr in range(1960, 2031, 20):
        x = px(date(yr, 1, 1))
        body.append(line(x, cy0 + ch, x, cy0 + ch + 4, 'gray', 1))
        body.append(text(x, cy0 + ch + 18, yr, 12, anchor='middle', fill='gray'))
    for d, v in pts:
        body.append(f'<circle cx="{px(d):.1f}" cy="{py(v):.1f}" r="1.8" fill="{C["orange"]}" fill-opacity="0.8"/>')

    # Key
    rows = [
        ('region', 'Region: the study area'),
        ('aquifer', 'Aquifers: inside the region'),
        ('well', 'Wells: each in one aquifer'),
        ('meas', 'Measurements: dated values at a well'),
    ]
    for j, (kind, label) in enumerate(rows):
        x, y = 650, 362 + j * 24
        if kind == 'region':
            body.append(f'<rect x="{x}" y="{y - 10}" width="22" height="13" fill="{C["sky"]}" stroke="{C["darkgray"]}" stroke-width="2"/>')
        elif kind == 'aquifer':
            for k, col in enumerate(['green', 'purple', 'blue', 'gold']):
                body.append(f'<rect x="{x + k * 5.5:.1f}" y="{y - 10}" width="5.5" height="13" fill="{C[col]}" fill-opacity="0.3" stroke="{C[col]}" stroke-width="1"/>')
        elif kind == 'well':
            body.append(f'<circle cx="{x + 11}" cy="{y - 3.5}" r="3.5" fill="{C["navy"]}"/>')
        else:
            for k in range(4):
                body.append(f'<circle cx="{x + 3 + k * 5.3:.1f}" cy="{y - 2 - k * 1.6:.1f}" r="1.8" fill="{C["orange"]}"/>')
        body.append(text(x + 32, y + 1, esc(label), 13))

    save('files-map', svg_doc(W, H, '\n'.join(body), 'How a region, its aquifers, wells and measurements fit together'))


# Where each aquifer's name goes on the map, placed for this map: (id, label x, label y, anchor, lon, lat of
# the leader's end, inside the outline)
LABELS = [
    ('3-004.09', 330, 84, 'start', -121.635, 36.786),
    ('3-004.01', 330, 108, 'start', -121.746, 36.741),
    ('3-004.02', 330, 132, 'start', -121.629, 36.723),
    ('3-004.04', 390, 252, 'start', -121.32, 36.40),
    ('3-004.05', 500, 304, 'start', -120.95, 36.05),
    ('3-006', 262, 452, 'end', -121.05, 35.90),
    ('3-004.10', 96, 150, 'end', -121.79, 36.667),
    ('3-004.08', 96, 182, 'end', -121.805, 36.603),
    ('3-007', 96, 216, 'end', -121.80, 36.50),
]


# ---------------------------------------------------------------- figure 2: the files and their links

def files_links():
    W = 960
    CARD_W, CARD_H, STEP_X, STEP_Y = 740, 112, 60, 150
    X0, Y0 = 30, 62
    body = []
    body.append(text(30, 36, 'The four files and the columns that tie them together', 17, weight='bold', fill='navy'))

    def card(i, color, title, kind):
        x, y = X0 + i * STEP_X, Y0 + i * STEP_Y
        body.append(f'<rect x="{x}" y="{y}" width="{CARD_W}" height="{CARD_H}" rx="6" fill="white" stroke="{C["lightgray"]}" stroke-width="1.5"/>')
        body.append(f'<rect x="{x}" y="{y}" width="7" height="{CARD_H}" rx="3" fill="{C[color]}"/>')
        body.append(text(x + 20, y + 24, esc(title), 15, weight='bold', fill='navy'))
        body.append(text(x + 20 + len(title) * 8.6 + 10, y + 24, esc(kind), 13, fill='gray'))
        return x, y

    def link(i, segments):
        """Elbow from card i-1 down into card i, with a sentence in the gap above card i."""
        px, py = X0 + (i - 1) * STEP_X, Y0 + (i - 1) * STEP_Y
        cx, cy = X0 + i * STEP_X, Y0 + i * STEP_Y
        ex = px + 30
        body.append(path(f'M{ex},{py + CARD_H} L{ex},{cy + CARD_H / 2} L{cx},{cy + CARD_H / 2}', 'gray', 1.5))
        body.append(f'<path d="M{cx - 7},{cy + CARD_H / 2 - 4} L{cx},{cy + CARD_H / 2} L{cx - 7},{cy + CARD_H / 2 + 4} z" fill="{C["gray"]}"/>')
        body.append(text(cx + 4, cy - 12, ''.join(tspan(s, f, w) for s, f, w in segments), 13)
                    .replace('<text ', '<text xml:space="preserve" ', 1))

    def table(x, y, cols, rows, widths, key=None):
        """A few rows of a file. key maps a column index to the color its values are drawn in."""
        key = key or {}
        xs = [x]
        for w in widths[:-1]:
            xs.append(xs[-1] + w)
        for j, c in enumerate(cols):
            col = key.get(j)
            body.append(text(xs[j], y, esc(c), 12, weight='bold', fill=col or 'darkgray', font=MONO))
        for r, row in enumerate(rows):
            for j, v in enumerate(row):
                col = key.get(j)
                body.append(text(xs[j], y + 18 + r * 17, esc(v), 12, fill=col or 'darkgray', font=MONO,
                                 weight='bold' if col else 'normal'))

    def thumb(geoms, x, y, w, h):
        proj = Projection(region.bounds, (x, y, w, h))
        for g, col, fill, op in geoms:
            body.append(path(proj.d(g), stroke=col, w=1.2, fill=fill, fill_opacity=op))

    # 1. Region outline
    x, y = card(0, 'darkgray', 'Region outline', 'GeoJSON, or a zipped shapefile')
    body.append(text(x + 20, y + 52, 'One or more polygons that together make the study area.', 13))
    body.append(text(x + 20, y + 72, 'You give the region its name when you create it, and choose', 13))
    body.append(text(x + 20, y + 90, 'feet or meters for all its elevations.', 13))
    thumb([(region, 'darkgray', 'sky', 1)], x + CARD_W - 110, y + 12, 92, 88)

    # 2. Aquifer outlines
    link(1, [('Each aquifer lies inside the region. A ', None, None), ('single-unit', None, 'bold'),
             (' region has none: its outline is its one aquifer.', None, None)])
    x, y = card(1, 'teal', 'Aquifer outlines', 'GeoJSON, or a zipped shapefile')
    table(x + 20, y + 52, ['aquifer_id', 'aquifer_name'],
          [[aid, aquifers[aid][0]] for aid in ('3-004.01', '3-004.02', '3-007')], [100, 200], key={0: 'teal'})
    thumb([(region, 'lightgray', 'sky', 1)] + [(g, C[AQ_COLOR[aid]], C[AQ_COLOR[aid]], 0.3) for aid, (_, g) in aquifers.items()],
          x + CARD_W - 110, y + 12, 92, 88)
    body.append(text(x + 330, y + 70, 'One polygon per aquifer. Without', 13))
    body.append(text(x + 330, y + 88, 'IDs, they are numbered 1, 2, 3.', 13))

    # 3. Wells
    link(2, [('Each well is in one aquifer: the one its ', None, None), ('Aquifer ID', 'teal', 'bold'),
             (' names, or the outline it falls inside.', None, None)])
    x, y = card(2, 'navy', 'Wells', 'CSV, one row per well')
    ex = [WELL_ID, '367386N1216740W001', '360137N1208920W001']
    rows = [[w['Well ID'], w['Well Name'], w['Latitude'], w['Longitude'], w['GSE'], w['Well Depth'], w['Aquifer ID']]
            for w in (wells_by_id[e] for e in ex)]
    table(x + 20, y + 52, ['Well ID', 'Well Name', 'Latitude', 'Longitude', 'GSE', 'Well Depth', 'Aquifer ID'], rows,
          [148, 112, 76, 92, 48, 88, 90], key={0: 'orange', 6: 'teal'})

    # 4. Measurements
    link(3, [('Each measurement is at one well: the one its ', None, None), ('Well ID', 'orange', 'bold'),
             (' names, or found by name or coordinates.', None, None)])
    x, y = card(3, 'orange', 'Measurements', 'CSV, one row per measurement')
    rows = [[r['Well ID'], r['Date'], r['WTE (ft)']] for r in levels[:3]]
    table(x + 20, y + 52, ['Well ID', 'Date', 'WTE (ft)'], rows, [148, 100, 80], key={0: 'orange'})
    body.append(text(x + 380, y + 70, 'Or one row per sample, with a', 13))
    body.append(text(x + 380, y + 88, 'column for each data type.', 13))

    H = Y0 + 3 * STEP_Y + CARD_H + 24
    save('files-links', svg_doc(W, H, '\n'.join(body), 'The four files of a region and the columns that link them'))


if __name__ == '__main__':
    files_map()
    files_links()
