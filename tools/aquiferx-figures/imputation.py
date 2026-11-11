"""Draw the Part 4 figures of how Impute Gaps fills a well's record.

    python3 imputation.py

Uses the saved model and the readings of the Utah Sample Data in the aquiferx repo beside this one (../aquiferx).
Writes editable SVGs to docs/static/images/aquiferx/diagrams/ and 2x PNGs next to the pages' other images, with the
helpers of diagrams.py.

  impute-network.png   the extreme learning machine: 19 inputs for a month, 500 hidden units, one output
  impute-gap.png       (C-36-16) 3ddc- 1 around its 1961-1971 gap: readings, PCHIP, the gap and its pads, the model
"""
import csv
import json
from datetime import date, datetime
from pathlib import Path

import numpy as np

from PIL import Image

from diagrams import C, FONT, OUT, line, path, save, svg_doc, text

HERE = Path(__file__).resolve().parent
UTAH = HERE.parents[2] / 'aquiferx' / 'public' / 'data' / 'utah'
MODEL = UTAH / 'escalante_valley_beryl_enterprise' / 'model_wte_elm.json'
WELL = '374041113373501'                       # (C-36-16) 3ddc- 1, in Escalante Valley-Beryl-Enterprise
GAP_SIZE, PAD = 730, 180                       # the defaults the model was built with, in days


def circle(x, y, r, fill='white', stroke='navy', w=1.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C.get(fill, fill)}" stroke="{C.get(stroke, stroke)}" stroke-width="{w}"/>'


def network():
    W, H = 900, 560
    xi, xh, xo = 250, 520, 760                 # input, hidden and output columns
    top = 92

    # The 19 inputs of one month, in groups
    groups = [
        ('Soil moisture', ['this month', '1-year mean', '3-year mean', '5-year mean', '10-year mean'], 'teal'),
        ('Year', ['scaled 0 to 1'], 'purple'),
        ('Month of the year', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 'gold'),
        ('Constant', ['1'], 'gray'),
    ]
    inputs = []
    y = top
    body = []
    for name, items, col in groups:
        y0 = y
        for k, it in enumerate(items):
            inputs.append((xi, y, col))
            if name == 'Month of the year':
                if k in (0, 11):
                    body.append(text(xi - 14, y + 4, it, size=11, anchor='end', fill='gray'))
            else:
                body.append(text(xi - 14, y + 4, it, size=12, anchor='end', fill='darkgray'))
            y += 19
        body.append(text(28, (y0 + y - 19) / 2 + 4, name, size=13, weight='bold', fill=col))
        if name == 'Month of the year':
            body.append(text(28, (y0 + y - 19) / 2 + 22, '1 for the month,', size=11, fill='gray', italic=True))
            body.append(text(28, (y0 + y - 19) / 2 + 37, '0 for the others', size=11, fill='gray', italic=True))
        y += 10
    bottom = y - 29

    # Hidden units: a few drawn, the rest elided
    shown = 12
    hy = list(np.linspace(top + 6, bottom - 6, shown + 1))
    gap_at = shown // 2
    hidden = [(xh, v) for k, v in enumerate(hy) if k != gap_at]
    out = (xo, (top + bottom) / 2)

    for (x1, y1, _) in inputs:
        for (x2, y2) in hidden:
            body.append(line(x1 + 6, y1, x2 - 9, y2, col='gray', w=0.6, opacity=0.25))
    for (x2, y2) in hidden:
        body.append(line(x2 + 9, y2, out[0] - 16, out[1], col='orange', w=1.6, opacity=0.85))
    for (x1, y1, col) in inputs:
        body.append(circle(x1, y1, 6, fill='white', stroke=col, w=1.8))
    for (x2, y2) in hidden:
        body.append(circle(x2, y2, 9, fill='faint', stroke='navy'))
    gy = hy[gap_at]
    for d in (-8, 0, 8):
        body.append(circle(xh, gy + d, 1.8, fill='navy', stroke='navy', w=0))
    body.append(circle(out[0], out[1], 16, fill='white', stroke='orange', w=2.5))

    # Labels
    body.append(text(xi, 40, '19 inputs for each month', size=14, anchor='middle', weight='bold', fill='navy'))
    body.append(text(xh, 40, '500 hidden units', size=14, anchor='middle', weight='bold', fill='navy'))
    body.append(text(xh, 60, 'each: max(0, weighted sum of the inputs + b)', size=12, anchor='middle', fill='darkgray'))
    body.append(text(xo, 40, 'Water level', size=14, anchor='middle', weight='bold', fill='navy'))
    body.append(text(xo, 60, 'z-score for the month', size=12, anchor='middle', fill='darkgray'))
    body.append(text(out[0] + 26, out[1] - 6, 'weighted sum', size=12, fill='darkgray'))
    body.append(text(out[0] + 26, out[1] + 10, 'of the units', size=12, fill='darkgray'))

    ly, lx = bottom + 40, 330
    body.append(line(lx, ly, lx + 28, ly, col='gray', w=1.5, opacity=0.6))
    body.append(text(lx + 36, ly + 4, 'weights and b: random, drawn once per well, never fitted', size=12, fill='darkgray'))
    body.append(line(lx, ly + 24, lx + 28, ly + 24, col='orange', w=2))
    body.append(text(lx + 36, ly + 28, 'weights β: fitted to the well by ridge regression, λ = 100', size=12, fill='darkgray'))

    save('impute-network', svg_doc(W, H, '\n'.join(body),
                                   'The extreme learning machine: 19 inputs for a month, 500 hidden units with random '
                                   'weights, and one output whose weights are fitted'))
    # Its 228 faint lines make a large PNG; 256 colors look the same at a fifth of the size
    png = OUT / 'impute-network.png'
    Image.open(png).convert('RGB').quantize(256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(png, optimize=True)


def parse(s):
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return datetime.strptime(s, '%m/%d/%Y').date()


def year(d):
    start = date(d.year, 1, 1)
    return d.year + (d - start).days / (date(d.year + 1, 1, 1) - start).days


def gap_figure():
    model = json.loads(MODEL.read_text())
    rows = sorted((parse(r['date']), r['pchip'], r['model']) for r in model['data'] if r['well_id'] == WELL)
    reads = sorted((parse(r['date']), float(r['value'])) for r in csv.DictReader(open(UTAH / 'data_wte.csv'))
                   if r['well_id'] == WELL)
    x0, x1 = 1958, 1975
    rd = [(year(d), v) for d, v in reads if x0 <= year(d) <= x1]
    mo = [(year(d), p, m) for d, p, m in rows if x0 <= year(d) <= x1]
    # The gap: the two readings either side of the longest interval in the window
    pairs = [(a, b) for a, b in zip(reads, reads[1:]) if (b[0] - a[0]).days > GAP_SIZE and x0 <= year(a[0]) <= x1]
    (ga, _), (gb, _) = pairs[0]

    vals = [v for _, v in rd] + [p for _, p, _ in mo if p is not None] + [m for _, _, m in mo]
    y0, y1 = 5 * np.floor(min(vals) / 5) - 5, 5 * np.ceil(max(vals) / 5) + 5
    W, H = 900, 440
    L, R, T, B = 78, 24, 70, 54
    X = lambda x: L + (x - x0) / (x1 - x0) * (W - L - R)
    Y = lambda y: H - B - (y - y0) / (y1 - y0) * (H - T - B)

    body = []
    # The gap, and the pads at its ends
    pa, pb = year(ga) + PAD / 365.25, year(gb) - PAD / 365.25
    body.append(f'<rect x="{X(year(ga)):.1f}" y="{T}" width="{X(year(gb)) - X(year(ga)):.1f}" height="{H - T - B}" '
                f'fill="{C["faint"]}"/>')
    for a, b in ((year(ga), pa), (pb, year(gb))):
        body.append(f'<rect x="{X(a):.1f}" y="{T}" width="{X(b) - X(a):.1f}" height="{H - T - B}" fill="{C["orange"]}" '
                    f'fill-opacity="0.15"/>')
    for yv in np.arange(y0, y1 + 0.1, 10):
        body.append(line(L, Y(yv), W - R, Y(yv), col='lightgray', w=1))
        body.append(text(L - 8, Y(yv) + 4, f'{yv:,.0f}', size=12, anchor='end', fill='gray'))
    for xv in range(x0, x1 + 1):
        body.append(line(X(xv), H - B, X(xv), H - B + 5, col='gray', w=1))
        if xv % 2 == 0:
            body.append(text(X(xv), H - B + 20, str(xv), size=12, anchor='middle', fill='gray'))
    body.append(line(L, H - B, W - R, H - B, col='gray', w=1))
    body.append(f'<text transform="translate(20 {(T + H - B) / 2:.0f}) rotate(-90)" font-family="{FONT}" font-size="12" '
                f'text-anchor="middle" fill="{C["gray"]}">Water table elevation (ft)</text>')

    # The model over every month, then PCHIP where it is kept
    body.append(path('M' + ' L'.join(f'{X(t):.1f},{Y(m):.1f}' for t, _, m in mo), stroke='blue', w=1.6))
    seg = []
    for t, p, _ in mo + [(None, None, None)]:
        if p is not None:
            seg.append(f'{X(t):.1f},{Y(p):.1f}')
        elif seg:
            body.append(path('M' + ' L'.join(seg), stroke='orange', w=2.6))
            seg = []
    for t, v in rd:
        body.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="4" fill="{C["navy"]}" stroke="white" stroke-width="1.2"/>')

    # Labels
    mid = (X(year(ga)) + X(year(gb))) / 2
    body.append(text(mid, T + 18, f'gap of {(gb - ga).days / 365.25:.0f} years, longer than the Gap Size of {GAP_SIZE} days',
                     size=12, anchor='middle', fill='darkgray', italic=True))
    body.append(text(X(year(ga)) + 4, T + 36, f'pad, {PAD} days', size=11, fill='darkgray'))
    body.append(text(X(year(gb)) - 4, T + 36, f'pad, {PAD} days', size=11, anchor='end', fill='darkgray'))
    lx = L
    for name, col, w in (('PCHIP, kept', 'orange', 2.6), ('Model', 'blue', 1.6)):
        body.append(line(lx, 30, lx + 30, 30, col=col, w=w + 0.5))
        body.append(text(lx + 38, 34, name, size=13, fill='darkgray'))
        lx += 38 + 9 * len(name) + 34
    body.append(f'<circle cx="{lx + 6:.1f}" cy="30" r="4.5" fill="{C["navy"]}"/>')
    body.append(text(lx + 18, 34, 'Readings', size=13, fill='darkgray'))

    save('impute-gap', svg_doc(W, H, '\n'.join(body), f'The model filling a {(gb - ga).days / 365.25:.0f}-year gap in a '
                                                      'well record, between the pads of PCHIP at its ends'))
    print('gap', ga, gb, 'readings in window', len(rd))


if __name__ == '__main__':
    network()
    gap_figure()
