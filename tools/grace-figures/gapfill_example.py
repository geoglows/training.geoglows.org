"""Gap-filling method figure: observed GWSa, the piecewise trend and the filled months (Iullemeden-Irhazer).

data/iullemeden_filled.csv is the notebook's output for docs/static/files/grace/sample_iullemeden.csv
(columns month, observed, trend, seasonal, filled, is_filled).
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import C, OUT

d = pd.read_csv(Path(__file__).parent / "data" / "iullemeden_filled.csv")
d["date"] = pd.to_datetime(d.month)
filled = d.is_filled == 1

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})
fig, ax = plt.subplots(figsize=(11, 4.4), dpi=200)
ax.axvspan(pd.Timestamp("2017-06-15"), pd.Timestamp("2018-05-15"), color=C["lightgray"], alpha=0.7, lw=0)
ax.text(pd.Timestamp("2017-12-01"), 19.6, "GRACE / GRACE-FO gap", ha="center", va="top", fontsize=9.5, color=C["gray"])

# observed: a solid line broken at the gaps
ax.plot(d.date, d.observed, color=C["navy"], lw=1.4, label="Observed", zorder=3)
# filled: a red line over each gap, joined to the observed month on each side
runs = (filled != filled.shift()).cumsum()[filled]
for k, (_, idx) in enumerate(runs.groupby(runs).groups.items()):
    seg = d.loc[idx.min() - 1:idx.max() + 1]
    ax.plot(seg.date, seg.filled, color=C["red"], lw=1.8, zorder=4, label="Filled months" if k == 0 else None)
ax.plot(d.date, d.trend, color=C["teal"], lw=2.2, alpha=0.9, label="Piecewise trend", zorder=2)

# slope of each trend segment, labelled along the bottom of the plot, clear of the data
bps = [0, 91, 241, len(d) - 1]
for a, b in zip(bps[:-1], bps[1:]):
    slope = (d.trend[b] - d.trend[a]) / (b - a) * 12
    mid = (a + b) // 2
    ax.text(d.date[mid], -3.6, f"trend {slope:+.1f} cm/yr", ha="center", va="bottom", fontsize=10, color=C["teal"],
            weight="bold")
for b in bps[1:-1]:
    ax.axvline(d.date[b], color=C["teal"], lw=0.8, ls=":", alpha=0.8)

ax.set_ylabel("GWSa (cm)")
ax.set_ylim(-4, 20.5)
ax.set_xlim(d.date.iloc[0] - pd.Timedelta(days=60), d.date.iloc[-1] + pd.Timedelta(days=60))
ax.grid(axis="y", color=C["lightgray"], lw=0.8)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
out = OUT / "gap-filling-example.png"
fig.savefig(out, facecolor="white")
print(out)
