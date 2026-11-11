"""Draw the Part 3 diagram of the curves a chart can draw through a well's measurements.

    python3 curves.py

Uses the Utah Sample Data in the aquiferx repo beside this one (../aquiferx), and scipy, whose PchipInterpolator is the
method the app's chart uses. Writes an editable SVG to docs/static/images/aquiferx/diagrams/ and a 2x PNG next to the
pages' other images, with the helpers of diagrams.py.

  chart-curves.png   ten readings of (C-35-16)29ccd- 1, 1952 to 1957, joined by straight lines, a cubic spline and PCHIP
"""
import csv
from datetime import date, datetime
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator

from diagrams import C, FONT, line, path, save, svg_doc, text

HERE = Path(__file__).resolve().parent
UTAH = HERE.parents[2] / 'aquiferx' / 'public' / 'data' / 'utah'
WELL = '374320113401001'                       # (C-35-16)29ccd- 1, in Escalante Valley-Beryl-Enterprise
FIRST, LAST = date(1952, 1, 1), date(1957, 12, 31)


def parse(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        return datetime.strptime(s, '%m/%d/%Y').date()


def year(d):
    start = date(d.year, 1, 1)
    return d.year + (d - start).days / (date(d.year + 1, 1, 1) - start).days


def chart_curves():
    rows = sorted((parse(r['date']), float(r['value'])) for r in csv.DictReader(open(UTAH / 'data_wte.csv'))
                  if r['well_id'] == WELL)
    pts = [(year(d), v) for d, v in rows if FIRST <= d <= LAST]
    xs = np.array([p[0] for p in pts])
    ys = np.array([p[1] for p in pts])
    t = np.linspace(xs[0], xs[-1], 600)
    curves = [
        ('Straight lines', np.interp(t, xs, ys), 'gray', 1.5, '5 4'),
        ('Cubic spline', CubicSpline(xs, ys, bc_type='natural')(t), 'orange', 2, None),
        ('PCHIP', PchipInterpolator(xs, ys)(t), 'blue', 2.5, None),
    ]

    W, H = 900, 430
    L, R, T, B = 78, 24, 56, 54                 # plot margins
    x0, x1 = 1952, 1958
    lo = min(c[1].min() for c in curves)
    hi = max(c[1].max() for c in curves)
    y0, y1 = 5 * np.floor(lo / 5) - 5, 5 * np.ceil(hi / 5) + 5
    X = lambda x: L + (x - x0) / (x1 - x0) * (W - L - R)
    Y = lambda y: H - B - (y - y0) / (y1 - y0) * (H - T - B)

    body = []
    for yv in np.arange(y0, y1 + 0.1, 10):
        body.append(line(L, Y(yv), W - R, Y(yv), col='lightgray', w=1))
        body.append(text(L - 8, Y(yv) + 4, f'{yv:,.0f}', size=12, anchor='end', fill='gray'))
    for xv in range(x0, x1 + 1):
        body.append(line(X(xv), H - B, X(xv), H - B + 5, col='gray', w=1))
        body.append(text(X(xv), H - B + 20, str(xv), size=12, anchor='middle', fill='gray'))
    body.append(line(L, H - B, W - R, H - B, col='gray', w=1))
    body.append(f'<text transform="translate(20 {(T + H - B) / 2:.0f}) rotate(-90)" font-family="{FONT}" font-size="12" '
                f'text-anchor="middle" fill="{C["gray"]}">Water table elevation (ft)</text>')

    for name, v, col, w, dash in curves:
        d = 'M' + ' L'.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in zip(t, v))
        body.append(path(d, stroke=col, w=w, dash=dash))
    for a, b in pts:
        body.append(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="4.5" fill="{C["navy"]}" stroke="white" stroke-width="1.5"/>')

    # Legend along the top
    lx = L
    for name, _, col, w, dash in curves:
        body.append(line(lx, 28, lx + 30, 28, col=col, w=w + 0.5, dash=dash))
        body.append(text(lx + 38, 32, name, size=13, fill='darkgray'))
        lx += 38 + 9 * len(name) + 34
    body.append(f'<circle cx="{lx + 6:.1f}" cy="28" r="4.5" fill="{C["navy"]}"/>')
    body.append(text(lx + 18, 32, 'Measurements', size=13, fill='darkgray'))

    # Where the spline leaves the readings: the two-year gap, 1953 to 1955
    gap = (t > xs[3]) & (t < xs[4])
    k = np.argmin(curves[1][1][gap]) if curves[1][1][gap].min() < min(ys[3], ys[4]) else np.argmax(curves[1][1][gap])
    tx, ty = t[gap][k], curves[1][1][gap][k]
    above = ty - ys.max()
    body.append(text(X(tx), Y(ty) - 12, f'in the two-year gap the spline rises {above:.0f} ft above the highest reading',
                     size=12, anchor='middle', fill='orange', italic=True))

    save('chart-curves', svg_doc(W, H, '\n'.join(body),
                                 'Three curves through ten readings of a well: straight lines, a cubic spline and PCHIP'))
    print('readings', len(pts), 'spline range', round(curves[1][1].min(), 1), round(curves[1][1].max(), 1),
          'readings range', ys.min(), ys.max())


if __name__ == '__main__':
    chart_curves()
