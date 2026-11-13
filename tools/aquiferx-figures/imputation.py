"""Draw the Part 4 figures of how Impute Gaps fills a well's record.

    python3 imputation.py

Uses the saved model and the readings of the Utah Sample Data in the aquiferx repo beside this one (../aquiferx).
Writes editable SVGs to docs/static/images/aquiferx/diagrams/ and 2x PNGs next to the pages' other images, with the
helpers of diagrams.py.

  impute-network.png   MC+LNN's steps for one well: neighbors and anchors, SoftImpute, the inputs of a month, the 18
                       fixed reservoirs, the ridge readout
  impute-gap.png       (C-36-16) 3ddc- 1 around its 1961-1971 gap: readings, the saved series (PCHIP and MC+LNN), the
                       PCHIP curve across the gap; below, the readings of its 15 neighbors, standardized
"""
import csv
import json
from datetime import date, datetime
from pathlib import Path

import numpy as np

from diagrams import C, FONT, OUT, line, path, save, svg_doc, text

HERE = Path(__file__).resolve().parent
UTAH = HERE.parents[2] / 'aquiferx' / 'public' / 'data' / 'utah'
MODEL = UTAH / 'escalante_valley_beryl_enterprise' / 'model_wte_mc_lnn.json'
WELL = '374041113373501'                       # (C-36-16) 3ddc- 1, in Escalante Valley-Beryl-Enterprise
AQUIFER = '17'
GAP_DAYS = 183                                 # gaps this long or longer are MC+LNN's


def box(x, y, w, h, title, lines, col):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="white" stroke="{C[col]}" stroke-width="2"/>',
           text(x + w / 2, y + 24, title, size=14, anchor='middle', weight='bold', fill=col)]
    for k, s in enumerate(lines):
        out.append(text(x + w / 2, y + 46 + 18 * k, s, size=12, anchor='middle', fill='darkgray'))
    return out


def arrow(x1, y1, x2, y2, col='gray'):
    ang = np.arctan2(y2 - y1, x2 - x1)
    a = [(x2 - 10 * np.cos(ang) + 5 * np.sin(ang), y2 - 10 * np.sin(ang) - 5 * np.cos(ang)),
         (x2 - 10 * np.cos(ang) - 5 * np.sin(ang), y2 - 10 * np.sin(ang) + 5 * np.cos(ang))]
    return [line(x1, y1, x2 - 8 * np.cos(ang), y2 - 8 * np.sin(ang), col=col, w=1.8),
            path(f'M{x2:.1f},{y2:.1f} L{a[0][0]:.1f},{a[0][1]:.1f} L{a[1][0]:.1f},{a[1][1]:.1f} Z', stroke=col, w=1, fill=col)]


def network():
    W, H = 940, 640
    body = []
    # Row 1: the monthly records, the neighbors and anchors, SoftImpute
    body += box(30, 40, 250, 110, 'Monthly records', ['every well of the aquifer with', 'readings in 10 months or more,', 'gaps left blank'], 'navy')
    body += box(345, 40, 250, 110, 'Neighbors and anchors', ['the 15 wells that track the well', 'best (largest |r|), and the 60', 'most complete other wells'], 'navy')
    body += box(660, 40, 250, 110, 'SoftImpute', ["fills the neighbors' blanks", 'from the patterns all 75 share;', 'the well itself is never a row'], 'teal')
    body += arrow(280, 95, 345, 95) + arrow(595, 95, 660, 95)
    # Row 2: the well's readings, the inputs of a month
    body += box(30, 215, 250, 110, "The well's readings", ['averaged by month; they choose', 'the neighbors and are what', 'the regression is fitted to'], 'green')
    body += arrow(200, 215, 400, 150, col='green')
    body += box(345, 215, 565, 110, 'The inputs of a month (18)', ['15 completed neighbor records, standardized',
                                                                 'season: sin and cos of the calendar month',
                                                                 'trend: \u22121 to 1 across the model\'s months'], 'gold')
    body += arrow(785, 150, 785, 215)
    # Row 3: the readout, the reservoirs
    body += box(30, 390, 250, 110, 'Ridge regression', ['maps the reservoirs\' states to', 'the well\'s level; penalty chosen', 'by 6-block cross-fitting'], 'orange')
    body += box(345, 390, 565, 110, '18 reservoirs of 64 units, weights fixed', ['memory \u03c1 = 0.5, 0.9 and 0.99, each run forward and backward',
                                                                     'in time, with 3 draws of the weights; each month a new',
                                                                     'state from the inputs and the state before'], 'purple')
    body += arrow(627, 325, 627, 390) + arrow(345, 445, 280, 445) + arrow(155, 325, 155, 390, col='green')
    # Row 4: the estimate
    body += box(30, 555, 250, 70, 'MC+LNN estimate', ['every month, average of 3 draws'], 'blue')
    body += arrow(155, 500, 155, 555)
    body.append(text(345, 580, 'Only the regression is fitted. Before the first reading and after the last,', size=12,
                     fill='darkgray', italic=True))
    body.append(text(345, 598, 'a second regression, on inputs without the trend, gives the estimate.', size=12,
                     fill='darkgray', italic=True))
    save('impute-network', svg_doc(W, H, '\n'.join(body),
                                   'MC+LNN for one well: neighbors completed by SoftImpute, fed with the season and a trend '
                                   'through 18 fixed reservoirs, and a ridge regression fitted to the well'))


def parse(s):
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return datetime.strptime(s, '%m/%d/%Y').date()


def year(d):
    start = date(d.year, 1, 1)
    return d.year + (d - start).days / (date(d.year + 1, 1, 1) - start).days


def monthly(rows):
    """Each well's readings averaged by calendar month: {well: {month index from 1940-01: level}}"""
    out = {}
    for r in rows:
        d = parse(r['date'])
        out.setdefault(r['well_id'], {}).setdefault((d.year - 1940) * 12 + d.month - 1, []).append(float(r['value']))
    return {w: {k: float(np.mean(v)) for k, v in mm.items()} for w, mm in out.items()}


def neighbors(raw, well, k=15):
    """The app's choice: the k wells of the matrix (10+ months) with the largest |r| over 8 or more shared months"""
    tgt, cand = raw[well], []
    for w, s in raw.items():
        shared = [t for t in tgt if t in s]
        if w == well or len(s) < 10 or len(shared) < 8:
            continue
        a, b = np.array([tgt[t] for t in shared]), np.array([s[t] for t in shared])
        if b.std() > 1e-9:
            cand.append((abs(np.corrcoef(a, b)[0, 1]), w))
    return [w for _, w in sorted(cand, reverse=True)[:k]]


def gap_figure():
    model = json.loads(MODEL.read_text())
    series = model['data'][WELL]
    rows = [r for r in csv.DictReader(open(UTAH / 'data_wte.csv')) if r['aquifer_id'] == AQUIFER]
    reads = sorted((parse(r['date']), float(r['value'])) for r in rows if r['well_id'] == WELL)
    raw = monthly(rows)
    nb = neighbors(raw, WELL)
    sy, sm = int(series['start'][:4]), int(series['start'][5:7])
    months = [(year(date(sy + (sm - 1 + i) // 12, (sm - 1 + i) % 12 + 1, 1)), v, c)
              for i, (v, c) in enumerate(zip(series['values'], series['source']))]
    x0, x1 = 1958, 1975
    rd = [(year(d), v) for d, v in reads if x0 <= year(d) <= x1]
    mo = [m for m in months if x0 <= m[0] <= x1]
    pairs = [(a, b) for a, b in zip(reads, reads[1:]) if (b[0] - a[0]).days > 3 * 365 and x0 <= year(a[0]) <= x1]
    (ga, _), (gb, _) = pairs[0]
    # The PCHIP curve across the gap: the chart's curve through the readings, from scipy
    from scipy.interpolate import PchipInterpolator
    tr = np.array([year(d) for d, _ in reads]); vr = np.array([v for _, v in reads])
    across = [(t, float(PchipInterpolator(tr, vr)(t))) for t in np.linspace(year(ga), year(gb), 120)]

    vals = [v for _, v in rd] + [v for _, v, _ in mo] + [v for _, v in across]
    y0, y1 = 5 * np.floor(min(vals) / 5) - 5, 5 * np.ceil(max(vals) / 5) + 5
    W, H = 900, 620
    L, R = 78, 24
    T1, B1 = 70, 330          # top panel: the well
    T2, B2 = 380, 570         # bottom panel: the neighbors
    X = lambda x: L + (x - x0) / (x1 - x0) * (W - L - R)
    Y = lambda y: B1 - (y - y0) / (y1 - y0) * (B1 - T1)

    body = []
    for top, bot in ((T1, B1), (T2, B2)):
        body.append(f'<rect x="{X(year(ga)):.1f}" y="{top}" width="{X(year(gb)) - X(year(ga)):.1f}" height="{bot - top}" '
                    f'fill="{C["faint"]}"/>')
        body.append(line(L, bot, W - R, bot, col='gray', w=1))
        for xv in range(x0, x1 + 1):
            body.append(line(X(xv), bot, X(xv), bot + 5, col='gray', w=1))
            if xv % 2 == 0:
                body.append(text(X(xv), bot + 20, str(xv), size=12, anchor='middle', fill='gray'))
    for yv in np.arange(y0, y1 + 0.1, 10):
        body.append(line(L, Y(yv), W - R, Y(yv), col='lightgray', w=1))
        body.append(text(L - 8, Y(yv) + 4, f'{yv:,.0f}', size=12, anchor='end', fill='gray'))
    body.append(f'<text transform="translate(20 {(T1 + B1) / 2:.0f}) rotate(-90)" font-family="{FONT}" font-size="12" '
                f'text-anchor="middle" fill="{C["gray"]}">Water table elevation (ft)</text>')

    # The PCHIP curve across the gap, dashed; the saved series by source; the readings
    body.append(path('M' + ' L'.join(f'{X(t):.1f},{Y(v):.1f}' for t, v in across), stroke='gray', w=1.6, dash='6 4'))
    seg, cur = [], None
    for k, (t, v, c) in enumerate(mo + [(None, None, None)]):
        if c != cur and seg:
            body.append(path('M' + ' L'.join(seg), stroke='orange' if cur == 'p' else 'blue', w=2.4))
            seg = seg[-1:] if c else []
        cur = c
        if t is not None:
            seg.append(f'{X(t):.1f},{Y(v):.1f}')
    for t, v in rd:
        body.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="4" fill="{C["navy"]}" stroke="white" stroke-width="1.2"/>')
    mid = (X(year(ga)) + X(year(gb))) / 2
    body.append(text(mid, T1 + 18, f'no readings for {(gb - ga).days / 365.25:.0f} years', size=12, anchor='middle',
                     fill='darkgray', italic=True))

    # The neighbors, each standardized over its whole record, in the window
    z = []
    for w in nb:
        pts = [(1940 + (t // 12) + (t % 12) / 12, v) for t, v in sorted(raw[w].items()) if x0 <= 1940 + (t // 12) + (t % 12) / 12 <= x1]
        if len(pts) > 1:
            v = np.array([p for _, p in pts]); mu, sd = np.median(v), np.std(v) or 1
            z.append([(t, (p - mu) / sd) for t, p in pts])
        else:
            z.append([(t, 0.0) for t, _ in pts])
    za, zb = -3, 3
    Z = lambda v: B2 - (min(max(v, za), zb) - za) / (zb - za) * (B2 - T2)
    for pts in z:
        if len(pts) > 1:
            body.append(path('M' + ' L'.join(f'{X(t):.1f},{Z(v):.1f}' for t, v in pts), stroke='teal', w=1, fill='none')
                        .replace('<path ', '<path opacity="0.45" ', 1))
        for t, v in pts:
            body.append(f'<circle cx="{X(t):.1f}" cy="{Z(v):.1f}" r="2.4" fill="{C["teal"]}"/>')
    body.append(f'<text transform="translate(20 {(T2 + B2) / 2:.0f}) rotate(-90)" font-family="{FONT}" font-size="12" '
                f'text-anchor="middle" fill="{C["gray"]}">Level, scaled</text>')
    read_in_gap = sum(any(year(ga) < t < year(gb) for t, _ in pts) for pts in z)
    body.append(text(L + 6, T2 - 12, f'Its 15 neighbors, each scaled over these years; {read_in_gap} of them were read during the gap',
                     size=13, fill='darkgray'))

    # Legend
    lx = L
    for name, col, w, dash in (('PCHIP', 'orange', 2.4, None), ('MC+LNN', 'blue', 2.4, None),
                               ('PCHIP across the gap', 'gray', 1.6, '6 4')):
        body.append(line(lx, 30, lx + 30, 30, col=col, w=w + 0.5, dash=dash))
        body.append(text(lx + 38, 34, name, size=13, fill='darkgray'))
        lx += 38 + 8 * len(name) + 30
    body.append(f'<circle cx="{lx + 6:.1f}" cy="30" r="4.5" fill="{C["navy"]}"/>')
    body.append(text(lx + 18, 34, 'Readings', size=13, fill='darkgray'))

    save('impute-gap', svg_doc(W, H, '\n'.join(body), f'MC+LNN filling a {(gb - ga).days / 365.25:.0f}-year gap in a '
                                                      "well record, from neighbors read during the gap"))
    print('gap', ga, gb, 'readings in window', len(rd), 'neighbors read in the gap', read_in_gap)


if __name__ == '__main__':
    network()
    gap_figure()
