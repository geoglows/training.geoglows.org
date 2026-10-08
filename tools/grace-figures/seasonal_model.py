"""Seasonal model figures for the Northern Midwest Aquifer System.

Refits the app's gap-fill model (src/gapFill.js in webapp-grace-groundwater) to the observed GWSa in
data/northern_midwest_filled.csv, with the same constraints, grid search and BIC rule, and draws:

  seasonal-decomposition.png  observed series, trend, seasonal cycle and residual, stacked
  seasonal-levels.png         the twelve monthly levels of the seasonal cycle
  seasonal-breakpoints.png    the best trend with 0, 1, 2 and 3 breakpoints, and the BIC of each
  seasonal-gap-correction.png the residual correction across the gap between the missions
"""
import itertools
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import C, OUT

END_BUFFER, MIN_SEGMENT, GRID_STEP, MIN_BIC_DROP = 48, 36, 3, 10

d = pd.read_csv(Path(__file__).parent / "data" / "northern_midwest_filled.csv")
d["date"] = pd.to_datetime(d.month)
obs = d.observed.notna().values
t_all = np.arange(len(d))  # the export has one row per month
cal = d.date.dt.month.values - 1
t, mon, y = t_all[obs], cal[obs], d.observed.values[obs]
n = len(y)


def design(bps, tt, mm):
    return np.column_stack([tt, *[np.maximum(tt - b, 0) for b in bps], *[(mm == k).astype(float) for k in range(12)]])


def fit(bps):
    beta, *_ = np.linalg.lstsq(design(bps, t, mon), y, rcond=None)
    r = y - design(bps, t, mon) @ beta
    rss = r @ r
    return dict(bps=list(bps), beta=beta, rss=rss, bic=n * np.log(rss / n) + (1 + 2 * len(bps) + 12) * np.log(n))


def valid(b):
    return b[0] - t[0] >= END_BUFFER and t[-1] - b[-1] >= END_BUFFER and all(
        b[i] - b[i - 1] >= MIN_SEGMENT for i in range(1, len(b)))


def best(k):
    if k == 0:
        return fit([])
    cands = range(t[0] + END_BUFFER, t[-1] - END_BUFFER + 1, GRID_STEP)
    b = min((fit(c) for c in itertools.combinations(cands, k) if valid(c)), key=lambda f: f["rss"])
    improved = True
    while improved:
        improved = False
        for i in range(k):
            for s in (-1, 1):
                trial = list(b["bps"])
                trial[i] += s
                if valid(trial) and (f := fit(trial))["rss"] < b["rss"] - 1e-9:
                    b, improved = f, True
    return b


def parts(f):
    """Trend and seasonal cycle over every month, shifted so the cycle averages zero."""
    k = len(f["bps"])
    trend = design(f["bps"], t_all, cal)[:, :1 + k] @ f["beta"][:1 + k]
    levels = f["beta"][1 + k:]
    off = levels.mean()
    return trend + off, levels - off


fits = [best(k) for k in range(4)]
chosen = 0
for k in range(1, 4):
    if fits[k]["bic"] <= fits[chosen]["bic"] - MIN_BIC_DROP:
        chosen = k
model = fits[chosen]
trend, levels = parts(model)
seasonal = levels[cal]
resid = np.where(obs, d.observed.values - trend - seasonal, np.nan)
assert np.allclose(trend + seasonal, d.trend + d.seasonal, atol=1e-3), "refit differs from the app's fill"
bp_dates = [d.date[b] for b in model["bps"]]

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})
GAP = (pd.Timestamp("2017-06-15"), pd.Timestamp("2018-05-15"))
xlim = (d.date.iloc[0] - pd.Timedelta(days=60), d.date.iloc[-1] + pd.Timedelta(days=60))


def tidy(ax, grid=True):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if grid:
        ax.grid(axis="y", color=C["lightgray"], lw=0.8)


def breaks(ax):
    for b in bp_dates:
        ax.axvline(b, color=C["teal"], lw=0.8, ls=":", alpha=0.8)


def label(ax, s):
    ax.text(0.005, 0.97, s, transform=ax.transAxes, ha="left", va="top", fontsize=11.5, weight="bold", color=C["darkgray"])


def observed_line(ax, **kw):
    # NaN breaks the line at each missing month
    ax.plot(d.date, d.observed, color=C["navy"], lw=1.3, **kw)
    # a month with gaps on both sides has no segment to draw, so mark it
    lone = obs & ~np.r_[False, obs[:-1]] & ~np.r_[obs[1:], False]
    ax.plot(d.date[lone], d.observed[lone], "o", color=C["navy"], ms=2.5, **kw)


# --- 1. decomposition ---------------------------------------------------------------------------------------------
fig, axs = plt.subplots(4, 1, figsize=(11, 9), dpi=200, sharex=True,
                        gridspec_kw=dict(height_ratios=[1.3, 1.3, 1, 1], hspace=0.18))
ax = axs[0]
observed_line(ax)
label(ax, "Observed GWSa,  y")
lo = min(np.nanmin(d.observed), trend.min()) - 2
hi = max(np.nanmax(d.observed), trend.max()) + 4
ax = axs[1]
ax.plot(d.date, trend, color=C["teal"], lw=2.2)
breaks(ax)
label(ax, "Trend,  T")
for b in bp_dates:
    ax.text(b + pd.Timedelta(days=45), hi - 1, f"{b:%b %Y}", va="top", ha="left", fontsize=9, color=C["teal"])
ax = axs[2]
ax.plot(d.date, seasonal, color=C["orange"], lw=1.4)
label(ax, "Seasonal cycle,  S")
ax = axs[3]
ax.axhline(0, color=C["gray"], lw=0.8)
ax.plot(d.date, resid, color=C["gray"], lw=1.1)
lone = obs & ~np.r_[False, obs[:-1]] & ~np.r_[obs[1:], False]
ax.plot(d.date[lone], resid[lone], "o", color=C["gray"], ms=2.5)
label(ax, "Residual,  r = y − T − S")
for ax in axs[:2]:
    ax.set_ylim(lo, hi)
s_lim = max(np.abs(seasonal).max(), np.nanmax(np.abs(resid))) + 1.5
for ax in axs[2:]:
    ax.set_ylim(-s_lim, s_lim)
for ax in axs:
    ax.axvspan(*GAP, color=C["lightgray"], alpha=0.7, lw=0)
    ax.set_ylabel("cm")
    tidy(ax)
axs[-1].set_xlim(*xlim)
fig.align_ylabels(axs)
fig.savefig(OUT / "seasonal-decomposition.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 2. monthly levels --------------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 3.4), dpi=200)
names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
cols = [C["orange"] if v >= 0 else C["blue"] for v in levels]
ax.bar(names, levels, color=cols, width=0.7)
ax.axhline(0, color=C["darkgray"], lw=0.9)
for i, v in enumerate(levels):
    ax.text(i, v + (0.25 if v >= 0 else -0.25), f"{v:+.1f}".replace("-", "−"), ha="center", va="bottom" if v >= 0 else "top", fontsize=9,
            color=C["darkgray"])
ax.set_ylabel("S (cm)")
ax.set_ylim(levels.min() - 1.4, levels.max() + 1.4)
tidy(ax)
ax.tick_params(axis="x", length=0)
fig.tight_layout()
fig.savefig(OUT / "seasonal-levels.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 3. breakpoint counts -----------------------------------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(11, 6.4), dpi=200, sharex=True, sharey=True)
for k, (ax, f) in enumerate(zip(axs.flat, fits)):
    tr, _ = parts(f)
    observed_line(ax, alpha=0.45)
    ax.plot(d.date, tr, color=C["teal"] if k == chosen else C["red"], lw=2.2)
    for b in f["bps"]:
        ax.axvline(d.date[b], color=C["gray"], lw=0.8, ls=":")
    word = "breakpoint" if k == 1 else "breakpoints"
    head = f"{k} {word}:  BIC {f['bic']:.0f}"
    if k:
        drop = fits[k - 1]["bic"] - f["bic"]
        head += f"  (−{drop:.0f})" if drop > 0 else f"  (+{-drop:.0f})"
    ax.set_title(head, loc="left", fontsize=11.5, weight="bold" if k == chosen else "normal",
                 color=C["teal"] if k == chosen else C["darkgray"])
    tidy(ax)
for ax in axs[:, 0]:
    ax.set_ylabel("GWSa (cm)")
axs[0, 0].set_xlim(*xlim)
fig.tight_layout()
fig.savefig(OUT / "seasonal-breakpoints.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 4. gap correction --------------------------------------------------------------------------------------------
win = (d.date >= "2016-09-01") & (d.date <= "2019-03-01")
w = d[win]
gap = (d.date > "2017-06-01") & (d.date < "2018-06-01")
a, c = d.index[d.date == "2017-06-01"][0], d.index[d.date == "2018-06-01"][0]
model_only = trend + seasonal
r_line = np.interp(t_all[a:c + 1], [a, c], [resid[a], resid[c]])

fig, (ax, axr) = plt.subplots(2, 1, figsize=(11, 6.2), dpi=200, sharex=True,
                              gridspec_kw=dict(height_ratios=[2.2, 1], hspace=0.12))
for x in (ax, axr):
    x.axvspan(*GAP, color=C["lightgray"], alpha=0.7, lw=0)
ax.plot(w.date, w.observed, color=C["navy"], lw=1.5, marker="o", ms=3.5, label="Observed, y")
ax.plot(w.date, model_only[win], color=C["orange"], lw=1.4, ls=(0, (4, 3)), label="Model alone, T + S")
ax.plot(d.date[a:c + 1], d.filled[a:c + 1], color=C["red"], lw=2, marker="o", ms=4, mfc="white",
        label="Filled, T + S + correction")
ax.set_ylabel("GWSa (cm)")
ax.legend(loc="lower left", frameon=False, ncol=3, fontsize=10)
for i, nm in ((a, "a"), (c, "c")):
    ax.annotate(nm, (d.date[i], d.observed[i]), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=11,
                style="italic", color=C["navy"])
tidy(ax)
ax.set_ylim(min(np.nanmin(w.observed), model_only[win].min()) - 5, max(np.nanmax(w.observed), model_only[win].max()) + 3)
axr.axhline(0, color=C["gray"], lw=0.8)
axr.plot(w.date, resid[win], color=C["gray"], lw=1.1, marker="o", ms=3)
axr.plot(d.date[a:c + 1], r_line, color=C["red"], lw=2, ls=(0, (4, 3)))
axr.annotate("r$_a$", (d.date[a], resid[a]), xytext=(-6, 6), textcoords="offset points", ha="right", fontsize=11,
             color=C["red"])
axr.annotate("r$_c$", (d.date[c], resid[c]), xytext=(6, 6), textcoords="offset points", ha="left", fontsize=11,
             color=C["red"])
axr.text(d.date[(a + c) // 2], max(resid[a], resid[c]) + 1.2, "correction, interpolated from r$_a$ to r$_c$", ha="center",
         fontsize=10, color=C["red"])
axr.set_ylabel("Residual (cm)")
axr.set_ylim(np.nanmin(resid[win]) - 1.5, np.nanmax(resid[win]) + 2.5)
tidy(axr)
fig.align_ylabels((ax, axr))
fig.savefig(OUT / "seasonal-gap-correction.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

print("breakpoints", [f"{b:%Y-%m}" for b in bp_dates], "BIC", [round(f["bic"], 1) for f in fits], "chosen", chosen)
