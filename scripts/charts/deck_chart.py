#!/usr/bin/env python3
# ABOUTME: Reusable themed time-series chart generator for the light-paper HTML decks.
# ABOUTME: Spec (JSON) in -> transparent PNG out, matching the deck palette/fonts; [n] source markers on points.
#
# Why: hand-drawn SVG charts in slides look amateur and mis-scale time axes. This renders a
# REAL chart (matplotlib + seaborn) from a small JSON spec, so every deck chart is reproducible,
# proportional in time, and consistently styled. Source TEXT is NOT baked in — only the [n]
# markers — because the clickable source list lives in the slide's HTML footer.
#
# Run:  uv run --with matplotlib --with seaborn scripts/charts/deck_chart.py <spec.json> <out.png>
# Spec: see scripts/charts/specs/*.json and docs/references/deck-charts.md.

import json
import sys
import os
import urllib.request
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager
import seaborn as sns

# --- Light-paper theme (mirrors the deck :root variables) ---
INK   = "#1a2238"   # --text-primary
DIM   = "#6b6f78"   # ~ --text-dim on cream
BRAND = "#b1502a"   # --brand (sienna)
DARK  = "#9c441f"   # --brand-3
GREY  = "#9a8f7d"   # muted, for disputed/outlier points
AREA  = (0.694, 0.314, 0.165, 0.10)  # sienna @ 10%

# Deck fonts (JetBrains Mono / Work Sans / Bodoni Moda). Cached locally; fetched on first run;
# falls back to matplotlib defaults if offline. Keeps the chart visually identical to the deck.
FONT_CACHE = os.path.join(os.path.dirname(__file__), ".fontcache")
FONTS = {
    "WorkSans.ttf":     "https://github.com/google/fonts/raw/main/ofl/worksans/WorkSans%5Bwght%5D.ttf",
    "JetBrainsMono.ttf":"https://github.com/google/fonts/raw/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
    "BodoniModa.ttf":   "https://github.com/google/fonts/raw/main/ofl/bodonimoda/BodoniModa%5Bopsz,wght%5D.ttf",
}


def load_fonts():
    os.makedirs(FONT_CACHE, exist_ok=True)
    fams = {}
    # allow a pre-seeded /tmp/deckfonts (CI / current session) to avoid a network round-trip
    for fn, url in FONTS.items():
        path = os.path.join(FONT_CACHE, fn)
        if not os.path.exists(path):
            for src in (os.path.join("/tmp/deckfonts", fn), None):
                try:
                    if src and os.path.exists(src):
                        import shutil; shutil.copy(src, path); break
                    urllib.request.urlretrieve(url, path); break
                except Exception:
                    continue
        if os.path.exists(path):
            try:
                font_manager.fontManager.addfont(path)
                fams[fn] = font_manager.FontProperties(fname=path).get_name()
            except Exception:
                pass
    return (fams.get("WorkSans.ttf", "DejaVu Sans"),
            fams.get("JetBrainsMono.ttf", "DejaVu Sans Mono"),
            fams.get("BodoniModa.ttf", "DejaVu Serif"))


def d(s):
    return datetime.strptime(s, "%Y-%m-%d")


def render(spec, out):
    body, mono, _serif = load_fonts()
    sns.set_style("white")
    plt.rcParams.update({"font.family": body, "text.color": INK,
                         "axes.edgecolor": "#c8bfac", "svg.fonttype": "none"})

    fig, ax = plt.subplots(figsize=tuple(spec.get("figsize", [7.8, 3.05])), dpi=spec.get("dpi", 200))
    fig.patch.set_alpha(0); ax.patch.set_alpha(0)

    measured = spec["points_measured"]
    mx = [d(p["date"]) for p in measured]
    my = [p["value"] for p in measured]

    # filled area + solid measured line
    ax.fill_between(mx, my, color=AREA, zorder=1)
    ax.plot(mx, my, color=BRAND, lw=2.6, zorder=3, solid_capstyle="round")
    ax.scatter(mx, my, s=46, color=DARK, zorder=4, edgecolor="#fffdf7", linewidth=1.4)

    # projection (dashed) from the last measured point
    proj = spec.get("projection")
    if proj:
        last = measured[-1]
        px = [d(last["date"]), d(proj["to"])]; py = [last["value"], proj["value"]]
        ax.plot(px, py, color=BRAND, lw=2.0, ls=(0, (5, 4)), alpha=0.6, zorder=2)
        ax.scatter([px[1]], [py[1]], s=46, facecolor="#fffdf7", edgecolor=BRAND, linewidth=2, zorder=4)

    # disputed / outlier points (hollow grey)
    for p in spec.get("points_disputed", []):
        ax.scatter([d(p["date"])], [p["value"]], s=40, facecolor="none", edgecolor=GREY,
                   linewidth=1.6, zorder=4)

    # per-point label "value [n]" (mono, like the deck chart labels). The [n] keys to the
    # CLICKABLE source list in the slide HTML footer — source text is never baked into the PNG.
    # Each point may carry dx/dy/ha overrides to dodge its neighbours.
    def annotate(p, dy=12, dx=0, ha="center", color=DARK):
        txt = p.get("label", "")
        if p.get("src"):
            txt = (txt + " " if txt else "") + f"[{p['src']}]"
        if txt:
            ax.annotate(txt, (d(p["date"]), p["value"]), textcoords="offset points",
                        xytext=(p.get("dx", dx), p.get("dy", dy)), ha=p.get("ha", ha),
                        fontsize=p.get("fs", 12), fontfamily=mono, color=color)
    for p in measured:
        annotate(p)
    for p in spec.get("points_disputed", []):
        annotate(p, dy=-18, color=GREY)
    if proj:
        annotate({**proj, "date": proj["to"]}, dx=-12, dy=-6, ha="right", color=BRAND)

    # axes
    ax.set_ylim(0, spec.get("y_max", 22))
    ax.set_yticks(spec.get("y_ticks", [0, 5, 10, 15, 20]))
    ax.yaxis.set_major_formatter(lambda v, _: f"{int(v)}%")
    ax.set_xlim(d(spec["x_from"]), d(spec["x_to"]))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=spec.get("month_interval", 2)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n'%y"))   # two-line: narrower, no run-together
    ax.tick_params(colors=DIM, labelsize=11.5)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_fontfamily(mono)
    ax.grid(axis="y", color="#1a2238", alpha=0.08, lw=1)
    sns.despine(ax=ax, top=True, right=True)
    ax.spines["left"].set_alpha(0.35); ax.spines["bottom"].set_alpha(0.35)
    if spec.get("note"):
        ax.annotate(spec["note"], (0.5, -0.22), xycoords="axes fraction", ha="center",
                    fontsize=10.5, fontfamily=mono, color=DIM)

    fig.tight_layout(pad=0.6)
    fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.06)
    print(f"wrote {out}  ({len(measured)} measured pts"
          f"{', +projection' if proj else ''}"
          f"{', +%d disputed' % len(spec.get('points_disputed', [])) if spec.get('points_disputed') else ''})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: deck_chart.py <spec.json> <out.png>")
    render(json.load(open(sys.argv[1])), sys.argv[2])
