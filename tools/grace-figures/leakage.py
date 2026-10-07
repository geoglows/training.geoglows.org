"""GRACE resolution versus region size, and signal leakage."""
import math
from common import C, text, line, svg_doc, save

W, H = 1200, 500
out = []

# ---------- panel A: grids and region size ----------
ax, ay, cell = 40, 90, 46          # 1 degree = 46 px; 9 x 6 degrees shown
cols, rows = 9, 6
out.append(text(ax, 40, "A. Grid sizes compared with region size", 16, anchor="start", weight="bold", fill=C["navy"]))
out.append(f'<rect x="{ax}" y="{ay}" width="{cols * cell}" height="{rows * cell}" fill="{C["sky"]}"/>')
# large basin
basin = [(0.6, 0.5), (3.4, 0.2), (6.8, 0.7), (8.4, 2.2), (8.1, 4.6), (6.0, 5.6), (3.0, 5.5), (0.9, 4.4), (0.3, 2.4)]
pts = " ".join(f"{ax + x * cell:.1f},{ay + y * cell:.1f}" for x, y in basin)
out.append(f'<polygon points="{pts}" fill="{C["teal"]}" fill-opacity="0.12" stroke="{C["teal"]}" stroke-width="2"/>')
# small aquifer
aq = [(4.2, 2.3), (5.1, 2.1), (5.6, 2.8), (5.3, 3.7), (4.4, 3.8), (3.9, 3.1)]
pts = " ".join(f"{ax + x * cell:.1f},{ay + y * cell:.1f}" for x, y in aq)
out.append(f'<polygon points="{pts}" fill="{C["orange"]}" fill-opacity="0.35" stroke="{C["orange"]}" stroke-width="2"/>')
# 1 degree grid
for i in range(cols + 1):
    out.append(line(ax + i * cell, ay, ax + i * cell, ay + rows * cell, "gray", 0.6, opacity=0.6))
for j in range(rows + 1):
    out.append(line(ax, ay + j * cell, ax + cols * cell, ay + j * cell, "gray", 0.6, opacity=0.6))
# 3 degree mascons
for i in range(0, cols + 1, 3):
    out.append(line(ax + i * cell, ay, ax + i * cell, ay + rows * cell, "navy", 2.4))
for j in range(0, rows + 1, 3):
    out.append(line(ax, ay + j * cell, ax + cols * cell, ay + j * cell, "navy", 2.4))
out.append(text(ax + 4.75 * cell, ay + 3.05 * cell, "aquifer", 12, weight="bold", fill="#9c4415"))
out.append(text(ax + 1.6 * cell, ay + 4.3 * cell, "river basin", 12, weight="bold", fill=C["teal"]))
# legend for panel A
ly = ay + rows * cell + 34
out += [line(ax, ly, ax + 30, ly, "navy", 2.4), text(ax + 38, ly + 4, "3° GRACE mascon (~330 km): the true resolution", 12.5, anchor="start"),
        line(ax, ly + 22, ax + 30, ly + 22, "gray", 1), text(ax + 38, ly + 26, "1° cell (~110 km): GWSa grid in the app", 12.5, anchor="start"),
        text(ax, ly + 52, "TWSa on finer grids repeats each mascon value; it adds no detail.", 12.5, anchor="start", italic=True, fill=C["gray"])]

# ---------- panel B: leakage profile ----------
bx, by, bw, bh = 540, 90, 620, 300
out.append(text(bx, 40, "B. Leakage: concentrated storage loss is spread out", 16, anchor="start", weight="bold", fill=C["navy"]))
zero = by + 70
out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{C["sky"]}"/>')
out.append(line(bx, zero, bx + bw, zero, "gray", 1.2))
out.append(text(bx + bw - 8, zero - 8, "no change", 12, anchor="end", fill=C["gray"]))
a0, a1 = bx + bw * 0.42, bx + bw * 0.58     # aquifer extent
out.append(f'<rect x="{a0:.1f}" y="{by}" width="{a1 - a0:.1f}" height="{bh}" fill="{C["orange"]}" opacity="0.12"/>')
out.append(text((a0 + a1) / 2, by + bh - 10, "aquifer", 12, weight="bold", fill="#9c4415"))
# true signal: deep narrow box
depth = 190
out.append(f'<path d="M{bx},{zero} L{a0:.1f},{zero} L{a0:.1f},{zero + depth} L{a1:.1f},{zero + depth} L{a1:.1f},{zero} L{bx + bw},{zero}" '
           f'fill="none" stroke="{C["navy"]}" stroke-width="2.5"/>')
# smoothed signal: same area, gaussian
width_true = a1 - a0
sigma = 95
amp = depth * width_true / (sigma * math.sqrt(2 * math.pi))
mid = (a0 + a1) / 2
pts = []
for k in range(301):
    x = bx + bw * k / 300
    pts.append(f"{x:.1f},{zero + amp * math.exp(-((x - mid) / sigma) ** 2 / 2):.1f}")
out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{C["orange"]}" stroke-width="3"/>')
# annotations
out += [text(a1 + 12, zero + depth - 6, "actual loss (pumping)", 12.5, anchor="start", weight="bold", fill=C["navy"]),
        text(bx + 20, zero + 150, "what GRACE sees", 12.5, anchor="start", weight="bold", fill=C["orange"]),
        line(bx + 90, zero + 136, a0 - 120, zero + 46, "orange", 1),
        line(a0 - 10, zero + 105, a0 - 80, zero + 105, "orange", 1.8, head=True),
        line(a1 + 10, zero + 105, a1 + 80, zero + 105, "orange", 1.8, head=True),
        text(a0 - 45, zero + 125, "signal leaks out", 12, fill=C["orange"]),
        text(a1 + 45, zero + 125, "signal leaks out", 12, fill=C["orange"]),
        text(bx - 8, zero + 4, "0", 12, anchor="end"),
        text(bx - 8, zero + depth + 4, "loss", 12, anchor="end")]
ny = by + bh + 34
out += [text(bx, ny, "Averaging over the aquifer alone underestimates the loss. Averaging over the whole", 12.5, anchor="start"),
        text(bx, ny + 20, "smeared area (a larger basin) recovers most of it, as long as storage outside the", 12.5, anchor="start"),
        text(bx, ny + 40, "aquifer is not changing in the opposite direction.", 12.5, anchor="start")]

print(save("grace-resolution-leakage", svg_doc(W, H, "\n".join(out), "GRACE resolution and leakage")))
