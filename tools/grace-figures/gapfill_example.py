"""Gap-filling method figure: observed GWSa, the piecewise trend and the filled months (Northern Midwest Aquifer System).

data/northern_midwest_filled.csv holds the app's seasonal fill of a GWSa export for the region
(columns month, observed, trend, seasonal, filled, is_filled).
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import C, OUT

d = pd.read_csv(Path(__file__).parent / "data" / "northern_midwest_filled.csv")
d["date"] = pd.to_datetime(d.month)
filled = d.is_filled == 1

# breakpoints are where the piecewise trend changes slope
bend = np.flatnonzero(np.abs(np.diff(d.trend.values, 2)) > 1e-3) + 1
bps = [0, *bend.tolist(), len(d) - 1]

lo, hi = np.floor(d.filled.min()) - 4, np.ceil(d.filled.max()) + 4
plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})
fig, ax = plt.subplots(figsize=(11, 4.8), dpi=200)
ax.axvspan(pd.Timestamp("2017-06-01"), pd.Timestamp("2018-06-01"), color=C["lightgray"], alpha=0.7, lw=0)
ax.text(pd.Timestamp("2017-12-01"), hi - 0.3, "GRACE / GRACE-FO gap", ha="center", va="top", fontsize=9.5, color=C["gray"])

ax.plot(d.date, d.observed, color=C["navy"], lw=1.4, label="Observed", zorder=3)
# filled: a red line over each gap, joined to the observed month on each side
runs = (filled != filled.shift()).cumsum()[filled]
for k, (_, idx) in enumerate(runs.groupby(runs).groups.items()):
    seg = d.loc[idx.min() - 1:idx.max() + 1]
    ax.plot(seg.date, seg.filled, color=C["red"], lw=1.8, zorder=4, label="Filled months" if k == 0 else None)
ax.plot(d.date, d.trend, color=C["teal"], lw=2.2, alpha=0.9, label="Piecewise trend", zorder=2)

# slope of each trend segment, labelled along the bottom of the plot, clear of the data
for a, b in zip(bps[:-1], bps[1:]):
    slope = (d.trend[b] - d.trend[a]) / (b - a) * 12
    ax.text(d.date[(a + b) // 2], lo + 0.4, f"{slope:+.1f} cm/yr".replace("-", "−"), ha="center", va="bottom", fontsize=10,
            color=C["teal"], weight="bold")
for b in bps[1:-1]:
    ax.axvline(d.date[b], color=C["teal"], lw=0.8, ls=":", alpha=0.8)

ax.set_ylabel("GWSa (cm)")
ax.set_ylim(lo, hi)
ax.set_xlim(d.date.iloc[0] - pd.Timedelta(days=60), d.date.iloc[-1] + pd.Timedelta(days=60))
ax.grid(axis="y", color=C["lightgray"], lw=0.8)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper left", frameon=False, ncol=3)
fig.tight_layout()
out = OUT / "gap-filling-example.png"
fig.savefig(out, facecolor="white")
print(out, [d.month[b] for b in bps[1:-1]])
