"""GRACE / GRACE-FO mission geometry: altitude, separation, ranging, GPS and accelerometers."""
import math
from common import C, text, line, svg_doc, save, FONT

W, H = 1200, 600
CX, R = 600, 2600          # Earth drawn as a large circle centred far below the figure
SURF_TOP = 470             # y of the Earth's surface at the centre
ORBIT_R = R + 260          # orbit radius in drawing units (altitude exaggerated, not to scale)
cy = SURF_TOP + R


def on_circle(radius, ang_deg):
    a = math.radians(ang_deg)
    return CX + radius * math.sin(a), cy - radius * math.cos(a)


def arc(radius, a0, a1, **kw):
    x0, y0 = on_circle(radius, a0)
    x1, y1 = on_circle(radius, a1)
    attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<path d="M{x0:.1f},{y0:.1f} A{radius},{radius} 0 0 1 {x1:.1f},{y1:.1f}" {attrs}/>'


def satellite(x, y, ang, label):
    return "\n".join([
        f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})">',
        f'<rect x="-26" y="-10" width="52" height="20" rx="4" fill="{C["darkgray"]}"/>',
        f'<rect x="-20" y="-6" width="40" height="12" rx="2" fill="{C["gold"]}"/>',
        f'<rect x="-11" y="-26" width="22" height="15" fill="{C["navy"]}" stroke="white" stroke-width="1"/>',
        f'<rect x="-11" y="11" width="22" height="15" fill="{C["navy"]}" stroke="white" stroke-width="1"/>',
        '</g>',
        text(x, y + 48, label, 13, weight="bold", fill=C["navy"])])


out = [f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
       f'<stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eaf4fb"/></linearGradient>'
       f'<clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}"/></clipPath></defs>',
       f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#sky)"/>',
       '<g clip-path="url(#frame)">',
       f'<circle cx="{CX}" cy="{cy}" r="{R + 40}" fill="#dbeaf6" opacity="0.6"/>',          # atmosphere
       f'<circle cx="{CX}" cy="{cy}" r="{R}" fill="#cfe3f1" stroke="{C["blue"]}" stroke-width="1.5"/>',  # ocean
       # a band of land along the visible surface
       arc(R - 11, -30, 30, fill="none", stroke="#c9b98f", stroke_width="22"),
       arc(ORBIT_R, -22, 22, fill="none", stroke=C["gray"], stroke_width="1.5", stroke_dasharray="4 6"),
       '</g>']

# satellite positions on the orbit
a_trail, a_lead = -3.3, 3.3
tx, ty = on_circle(ORBIT_R, a_trail)
lx, ly = on_circle(ORBIT_R, a_lead)

# GPS satellites above, tracking both
for gx_, gy_ in [(170, 60), (1030, 52)]:
    out += [f'<g transform="translate({gx_},{gy_})"><rect x="-14" y="-8" width="28" height="16" rx="3" fill="{C["gray"]}"/>'
            f'<rect x="-40" y="-5" width="22" height="10" fill="{C["teal"]}"/><rect x="18" y="-5" width="22" height="10" fill="{C["teal"]}"/></g>']
    for sx, sy in [(tx, ty), (lx, ly)]:
        out.append(line(gx_, gy_ + 10, sx, sy - 30, "teal", 1, dash="3 5", opacity=0.55))
out += [text(215, 40, "GPS satellites track each", 12.5, anchor="start", weight="bold", fill=C["teal"]),
        text(215, 56, "satellite's position", 12.5, anchor="start", weight="bold", fill=C["teal"])]

# satellites on the orbit
out.append(line(tx + 28, ty + 1, lx - 28, ly + 1, "orange", 3, dash="7 5"))
out += [satellite(tx, ty, a_trail, "trailing satellite"), satellite(lx, ly, a_lead, "leading satellite")]
out.append(line(lx + 60, ly + 2, lx + 130, ly + 8, "gray", 1.6, head=True))
out.append(text(lx + 140, ly - 6, "flight direction", 12, anchor="start", fill=C["gray"]))

# separation dimension above the pair
dy = 70
out += [line(tx, ty - dy + 6, tx, ty - 34, "darkgray", 1), line(lx, ly - dy + 6, lx, ly - 34, "darkgray", 1),
        line(tx + 3, ty - dy + 12, lx - 3, ly - dy + 12, "darkgray", 1.4, head=True, tail=True),
        f'<rect x="{CX - 92}" y="{ty - dy - 10}" width="184" height="26" rx="5" fill="white" stroke="{C["lightgray"]}"/>',
        text(CX, ty - dy + 8, "about 220 km apart", 15, weight="bold", fill=C["darkgray"])]

# altitude dimension from the surface up to the trailing satellite
ax = tx - 120
gx, gy = on_circle(R, a_trail - 2.6)
ox, oy = on_circle(ORBIT_R, a_trail - 2.6)
out += [line(gx, gy, ox, oy + 8, "navy", 1.6, head=True, tail=True),
        f'<rect x="{ox - 205}" y="{(gy + oy) / 2 - 40}" width="190" height="72" rx="6" fill="white" stroke="{C["lightgray"]}"/>',
        text(ox - 110, (gy + oy) / 2 - 16, "about 500 km altitude", 14, weight="bold", fill=C["navy"]),
        text(ox - 110, (gy + oy) / 2 + 4, "GRACE sank to ~300 km", 12),
        text(ox - 110, (gy + oy) / 2 + 21, "by 2017; GRACE-FO ~490 km", 12)]

# ranging callout
out += [line(CX, ty + 4, CX, ty + 70, "orange", 1.2),
        f'<rect x="{CX - 175}" y="{ty + 70}" width="350" height="62" rx="6" fill="white" stroke="{C["orange"]}"/>',
        text(CX, ty + 92, "Microwave ranging link", 14, weight="bold", fill=C["orange"]),
        text(CX, ty + 111, "measures changes in separation of about 1 µm", 12.5),
        text(CX, ty + 126, "(GRACE-FO adds a more precise laser link)", 12.5)]

# accelerometer callout
out += [line(lx + 30, ly + 14, lx + 170, ly + 105, "darkgray", 1),
        f'<rect x="{lx + 100}" y="{ly + 105}" width="270" height="62" rx="6" fill="white" stroke="{C["lightgray"]}"/>',
        text(lx + 235, ly + 127, "Accelerometer in each satellite", 13.5, weight="bold", fill=C["darkgray"]),
        text(lx + 235, ly + 146, "measures air drag and other non-", 12.5),
        text(lx + 235, ly + 161, "gravitational forces, to be removed", 12.5)]

out += [text(CX, SURF_TOP + 70, "Earth", 15, weight="bold", fill=C["blue"]),
        text(W - 20, H - 14, "not to scale", 11.5, anchor="end", fill=C["gray"], italic=True)]

print(save("grace-mission-geometry", svg_doc(W, H, "\n".join(out), "GRACE mission geometry")))
