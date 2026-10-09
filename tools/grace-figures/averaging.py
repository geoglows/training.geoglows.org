"""How the app averages grid cells over a region: overlap fraction, 35% threshold, area weights."""
from shapely.geometry import Polygon, box as sbox
from common import C, text, line, svg_doc, save, FONT

W, H = 1200, 420
gx, gy, cell = 50, 70, 64
cols, rows = 7, 5
region = Polygon([(0.7, 0.9), (2.6, 0.3), (4.9, 0.6), (6.3, 1.7), (6.1, 3.6), (4.6, 4.5), (2.4, 4.4), (0.9, 3.5), (0.4, 2.0)])

out = [text(gx, 36, "Averaging a region: which cells count, and how much", 17, anchor="start", weight="bold", fill=C["navy"]),
       '<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
       f'<line x1="0" y1="0" x2="0" y2="7" stroke="{C["gray"]}" stroke-width="1.2" opacity="0.5"/></pattern></defs>']

labels = []
for i in range(cols):
    for j in range(rows):
        frac = region.intersection(sbox(i, j, i + 1, j + 1)).area
        x, y = gx + i * cell, gy + j * cell
        if frac >= 0.35:
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{C["blue"]}" fill-opacity="{0.15 + 0.55 * frac:.2f}"/>')
            labels.append(text(x + cell / 2, y + cell / 2 + 5, f"{frac * 100:.0f}%", 13, weight="bold",
                               fill="white" if frac > 0.6 else C["navy"]))
        elif frac > 0:
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="url(#hatch)"/>')
            labels.append(text(x + cell / 2, y + cell / 2 + 5, f"{frac * 100:.0f}%", 12, fill=C["gray"]))
for i in range(cols + 1):
    out.append(line(gx + i * cell, gy, gx + i * cell, gy + rows * cell, "gray", 1))
for j in range(rows + 1):
    out.append(line(gx, gy + j * cell, gx + cols * cell, gy + j * cell, "gray", 1))
pts = " ".join(f"{gx + x * cell:.1f},{gy + y * cell:.1f}" for x, y in region.exterior.coords)
out.append(f'<polygon points="{pts}" fill="none" stroke="{C["orange"]}" stroke-width="3" opacity="0.85"/>')
# labels on top, each on a small rounded backing so the boundary line never cuts through them
for lab in labels:
    out.append(lab.replace("<text ", '<text paint-order="stroke" stroke="white" stroke-opacity="0.85" stroke-width="3.5" ', 1)
               if 'fill="white"' not in lab else lab)

# legend
lx, ly = gx + cols * cell + 60, 90
out += [f'<rect x="{lx}" y="{ly - 14}" width="22" height="22" fill="{C["blue"]}" fill-opacity="0.6"/>',
        text(lx + 32, ly + 2, "Used: at least 35% of the cell lies inside the region.", 13.5, anchor="start"),
        text(lx + 32, ly + 21, "Darker = larger share of the cell inside.", 12.5, anchor="start", fill=C["gray"]),
        f'<rect x="{lx}" y="{ly + 40}" width="22" height="22" fill="url(#hatch)" stroke="{C["lightgray"]}"/>',
        text(lx + 32, ly + 56, "Ignored: less than 35% inside. A sliver of a cell", 13.5, anchor="start"),
        text(lx + 32, ly + 75, "mostly describes somewhere else.", 13.5, anchor="start"),
        line(lx, ly + 106, lx + 22, ly + 106, "orange", 3),
        text(lx + 32, ly + 111, "Region boundary (preset, uploaded or drawn)", 13.5, anchor="start"),
        text(lx, ly + 160, "Each used cell is weighted by its overlap area aᵢ,", 13.5, anchor="start", weight="bold", fill=C["navy"]),
        text(lx, ly + 180, "measured on the ellipsoid:", 13.5, anchor="start", weight="bold", fill=C["navy"]),
        f'<rect x="{lx}" y="{ly + 196}" width="300" height="60" rx="8" fill="{C["sky"]}" stroke="{C["blue"]}"/>',
        f'<text x="{lx + 150}" y="{ly + 233}" font-family="{FONT}" font-size="19" text-anchor="middle" fill="{C["navy"]}">'
        f'x̄ = Σ aᵢ xᵢ  /  Σ aᵢ</text>',
        text(lx, ly + 286, "The ±1σ band is averaged the same way, which treats the", 12.5, anchor="start", fill=C["gray"]),
        text(lx, ly + 304, "errors in neighbouring cells as fully correlated.", 12.5, anchor="start", fill=C["gray"])]

print(save("grace-region-averaging", svg_doc(W, H, "\n".join(out), "Region averaging in the GRACE Regional Analyst")))
