"""GRACE / GRACE-FO record timeline with the months that have no solution."""
import pathlib
import pandas as pd
from common import C, text, line, svg_doc, save

csv = pathlib.Path(__file__).resolve().parents[2] / "tools/grace-figures/data/sample_iullemeden.csv"
df = pd.read_csv(csv, parse_dates=["Date"])
months = df["Date"]
missing = set(df.loc[df["TWSa"].isna(), "Date"])

W, H = 1200, 300
L, R = 70, W - 40
y0, y1 = 2002, months.max().year + 1


def xof(ts):
    return L + (ts.year + (ts.month - 1) / 12 - y0) / (y1 - y0) * (R - L)


out = [text(L, 34, "The GRACE and GRACE-FO record", 17, anchor="start", weight="bold", fill=C["navy"])]

# mission bars
bar_y = 70
grace_end = pd.Timestamp("2017-07-01")
fo_start = pd.Timestamp("2018-06-01")
out += [
    f'<rect x="{xof(pd.Timestamp("2002-04-01")):.1f}" y="{bar_y}" width="{xof(grace_end) - xof(pd.Timestamp("2002-04-01")):.1f}" height="30" rx="5" fill="{C["navy"]}"/>',
    text((xof(pd.Timestamp("2002-04-01")) + xof(grace_end)) / 2, bar_y + 20, "GRACE (2002–2017)", 14, weight="bold", fill="white"),
    f'<rect x="{xof(fo_start):.1f}" y="{bar_y}" width="{R - xof(fo_start):.1f}" height="30" rx="5" fill="{C["teal"]}"/>',
    text((xof(fo_start) + R) / 2, bar_y + 20, "GRACE Follow-On (2018–present)", 14, weight="bold", fill="white"),
]
gx0, gx1 = xof(grace_end), xof(fo_start)
out += [
    f'<rect x="{gx0:.1f}" y="{bar_y - 6}" width="{gx1 - gx0:.1f}" height="128" fill="{C["orange"]}" opacity="0.12"/>',
]

# month strip
strip_y = 128
mw = (R - L) / ((y1 - y0) * 12)
for ts in months:
    col = C["orange"] if ts in missing else C["blue"]
    out.append(f'<rect x="{xof(ts):.2f}" y="{strip_y}" width="{mw * 0.82:.2f}" height="26" fill="{col}"/>')
out += [
    text(L - 10, strip_y + 18, "months", 12, anchor="end", fill=C["gray"]),
]

# axis
ax_y = 172
out.append(line(L, ax_y, R, ax_y, "gray", 1))
for yr in range(y0, y1 + 1):
    x = L + (yr - y0) / (y1 - y0) * (R - L)
    out.append(line(x, ax_y, x, ax_y + (6 if yr % 2 else 10), "gray", 1))
    if yr % 2 == 0:
        out.append(text(x, ax_y + 26, str(yr), 12, fill=C["darkgray"]))

# gap callout
gm = (gx0 + gx1) / 2
out += [line(gm, ax_y + 36, gm, strip_y + 30, "orange", 1.2),
        text(gm, ax_y + 52, "11-month gap between missions", 13, weight="bold", fill=C["orange"]),
        text(gm, ax_y + 70, "(July 2017 – May 2018)", 12, fill=C["orange"])]

# legend
lx, ly = L, H - 26
out += [f'<rect x="{lx}" y="{ly - 11}" width="14" height="14" fill="{C["blue"]}"/>',
        text(lx + 22, ly, "monthly solution available", 12, anchor="start"),
        f'<rect x="{lx + 210}" y="{ly - 11}" width="14" height="14" fill="{C["orange"]}"/>',
        text(lx + 232, ly, f"no solution ({len(missing)} of {len(months)} months, the gap between missions plus single months lost to battery management)", 12, anchor="start")]

print(save("grace-timeline", svg_doc(W, H, "\n".join(out), "GRACE and GRACE-FO data record")))
