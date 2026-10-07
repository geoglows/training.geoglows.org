"""GRACE inter-satellite ranging over a mass anomaly: three-stage pass plus range signal."""
import math
from common import C, text, line, svg_doc, save

W, H = 1200, 600
PW = 360           # panel width
GAP = 30
X0 = (W - 3 * PW - 2 * GAP) / 2
ORBIT_Y = 150
SURF_Y = 262
D = 120            # nominal separation in px
MASS_X = PW / 2


def satellite(cx, cy, label):
    """A small satellite: body plus two solar wings."""
    s = [f'<g transform="translate({cx:.1f},{cy:.1f})">',
         f'<rect x="-15" y="-7" width="30" height="14" rx="3" fill="{C["darkgray"]}"/>',
         f'<rect x="-11" y="-4" width="22" height="8" rx="1.5" fill="{C["gold"]}"/>',
         f'<rect x="-6" y="-17" width="12" height="9" fill="{C["navy"]}" stroke="white" stroke-width="0.8"/>',
         f'<rect x="-6" y="8" width="12" height="9" fill="{C["navy"]}" stroke="white" stroke-width="0.8"/>',
         '</g>',
         text(cx, cy + 34, label, 12, fill=C["gray"])]
    return "\n".join(s)


def ground(px):
    """Curved ground surface with a buried water mass at the panel centre."""
    x1, x2 = px, px + PW
    mx = px + MASS_X
    g = [f'<path d="M{x1},{SURF_Y + 14} Q{mx},{SURF_Y - 14} {x2},{SURF_Y + 14} L{x2},{SURF_Y + 70} '
         f'L{x1},{SURF_Y + 70} Z" fill="{C["ground"]}" stroke="none"/>',
         f'<path d="M{x1},{SURF_Y + 14} Q{mx},{SURF_Y - 14} {x2},{SURF_Y + 14}" fill="none" '
         f'stroke="{C["groundline"]}" stroke-width="1.5"/>',
         f'<ellipse cx="{mx}" cy="{SURF_Y + 30}" rx="62" ry="18" fill="url(#massgrad)"/>',
         text(mx, SURF_Y + 35, "extra water mass", 12, fill="white", weight="bold"),
         ]
    return "\n".join(g)


def pull(sx, sy, mx, my, strength):
    """Gravity pull arrow from a satellite toward the mass, length scaled by strength."""
    dx, dy = mx - sx, my - sy
    L = math.hypot(dx, dy)
    ln = 22 + 34 * strength
    return line(sx + dx / L * 52, sy + dy / L * 52, sx + dx / L * (52 + ln), sy + dy / L * (52 + ln),
                "blue", 2.2, head=True)


def orbit_y(px, x):
    """y of the quadratic orbit arc at x within panel starting at px."""
    t = (x - (px + 6)) / (PW - 12)
    return (1 - t) ** 2 * (ORBIT_Y + 8) + 2 * t * (1 - t) * (ORBIT_Y - 8) + t * t * (ORBIT_Y + 8)


def panel(i, offset, sep_label, lead_note, trail_note, title):
    px = X0 + i * (PW + GAP)
    mx, my = px + MASS_X, SURF_Y + 30
    out = [f'<rect x="{px}" y="40" width="{PW}" height="{SURF_Y + 70 - 40}" rx="10" fill="{C["sky"]}" '
           f'stroke="{C["lightgray"]}"/>',
           text(px + 18, 66, f"{i + 1}", 18, anchor="start", weight="bold", fill=C["navy"]),
           text(px + 40, 66, title, 15, anchor="start", weight="bold", fill=C["navy"]),
           line(px + PW - 70, 61, px + PW - 22, 61, "gray", 1.5, head=True),
           text(px + PW - 46, 80, "flight", 11, fill=C["gray"]),
           ground(px),
           f'<path d="M{px + 6},{ORBIT_Y + 8} Q{mx},{ORBIT_Y - 8} {px + PW - 6},{ORBIT_Y + 8}" fill="none" '
           f'stroke="{C["gray"]}" stroke-width="1" stroke-dasharray="3 5"/>']
    cx = mx + offset
    tx, lx = cx - D / 2, cx + D / 2
    # strength falls off with horizontal distance from the mass
    st = lambda x: math.exp(-((x - mx) / 70) ** 2)
    ty, ly = orbit_y(px, tx), orbit_y(px, lx)
    out += [pull(tx, ty, mx, my, st(tx)), pull(lx, ly, mx, my, st(lx))]
    # ranging link
    out.append(line(tx + 16, ty, lx - 16, ly, "orange", 2, dash="5 4"))
    out += [satellite(tx, ty, "trailing"), satellite(lx, ly, "leading")]
    # separation bracket, above the satellites so the pull arrows stay clear
    by = ORBIT_Y - 50
    out += [line(tx, by - 6, tx, by + 6, "darkgray", 1.2), line(lx, by - 6, lx, by + 6, "darkgray", 1.2),
            line(tx, by, lx, by, "darkgray", 1.2),
            f'<rect x="{cx - 34}" y="{by - 11}" width="68" height="22" rx="4" fill="{C["sky"]}"/>',
            text(cx, by + 5, sep_label, 15, weight="bold", fill=C["orange"])]
    # notes
    out.append(text(px + PW / 2, SURF_Y + 96, lead_note, 13))
    out.append(text(px + PW / 2, SURF_Y + 115, trail_note, 13))
    return "\n".join(out), cx - mx


def signal_plot(markers):
    """Schematic range-change signature below the panels, aligned with along-track position."""
    top, h = 430, 130
    left, right = X0, W - X0
    mid = top + h / 2
    total = right - left
    # map along-track distance from the mass (px in panel units) onto the full plot width
    scale = total / (3 * PW + 2 * GAP) * 2.2
    cxp = (left + right) / 2
    pts = []
    for k in range(401):
        u = -1 + 2 * k / 400
        x = cxp + u * total / 2
        s = (x - cxp) / scale / 70
        y = (1 - 2 * s * s) * math.exp(-s * s)
        pts.append(f"{x:.1f},{mid + y * h * 0.38:.1f}")
    out = [text(left, top - 12, "Change in separation as the pair flies over the mass (schematic, exaggerated)", 14,
                anchor="start", weight="bold", fill=C["navy"]),
           line(left, mid, right, mid, "gray", 1, dash="4 4"),
           text(right, mid - 6, "nominal separation D", 12, anchor="end", fill=C["gray"]),
           f'<polyline points="{" ".join(pts)}" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>',
           text(left + 4, top + 14, "pair farther apart (+Δd)", 12, anchor="start", fill=C["darkgray"]),
           text(left + 4, top + h - 6, "pair closer together (−Δd)", 12, anchor="start", fill=C["darkgray"]),
           line(left, top + h + 18, right, top + h + 18, "gray", 1.2, head=True),
           text(cxp, top + h + 36, "flight direction / along-track position", 12, fill=C["gray"])]
    for i, off in enumerate(markers):
        x = cxp + off * scale
        s = off / 70
        y = mid - (-(1 - 2 * s * s) * math.exp(-s * s)) * h * 0.38
        out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{C["navy"]}"/>',
                text(x, y + 5, str(i + 1), 13, weight="bold", fill="white")]
    return "\n".join(out)


defs = (f'<defs><radialGradient id="massgrad" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0%" stop-color="{C["blue"]}"/><stop offset="100%" stop-color="{C["blue"]}" '
        f'stop-opacity="0.55"/></radialGradient></defs>')
p1, o1 = panel(0, -80, "D + Δd", "Leading satellite is pulled ahead first,",
               "so the pair drifts apart.", "Approaching")
p2, o2 = panel(1, 0, "D − Δd", "Leading satellite is held back while the",
               "trailing one is pulled forward: they close.", "Straddling the mass")
p3, o3 = panel(2, 80, "D + Δd", "Trailing satellite is now held back,",
               "so the pair drifts apart again.", "Departing")
body = "\n".join([defs, p1, p2, p3, signal_plot([o1, o2, o3])])
print(save("grace-ranging", svg_doc(W, H, body, "How GRACE senses a mass anomaly")))
