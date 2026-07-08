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

import csv
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


def load_points(spec):
    """Return (measured, disputed, projection) from a CSV (data_csv) or inline spec arrays.
    CSV columns: date,value,source,kind,label[,dx,dy,ha]. kind in {baseline,measured,disputed,projection}."""
    if not spec.get("data_csv"):
        return spec["points_measured"], spec.get("points_disputed", []), spec.get("projection")
    path = spec["data_csv"]
    if not os.path.isabs(path):
        path = os.path.join(os.path.dirname(__file__), path)
    def mk(r):
        o = {"date": r["date"], "value": float(r["value"]), "source": (r.get("source") or "").strip(),
             "label": (r.get("label") or "").strip(), "ha": (r.get("ha") or "center").strip()}
        for k in ("dx", "dy"):
            if r.get(k):
                o[k] = float(r[k])
        return o
    rows = list(csv.DictReader(open(path)))
    measured = [mk(r) for r in rows if r["kind"] in ("measured", "baseline")]
    disputed = [mk(r) for r in rows if r["kind"] == "disputed"]
    pj = [mk(r) for r in rows if r["kind"] == "projection"]
    proj = ({"to": pj[0]["date"], "value": pj[0]["value"], "label": pj[0]["label"],
             "source": pj[0]["source"], **{k: pj[0][k] for k in ("dx", "dy", "ha") if k in pj[0]}}
            if pj else None)
    return measured, disputed, proj


def render(spec, out):
    body, mono, _serif = load_fonts()
    sns.set_style("white")
    plt.rcParams.update({"font.family": body, "text.color": INK,
                         "axes.edgecolor": "#c8bfac", "svg.fonttype": "none"})

    fig, ax = plt.subplots(figsize=tuple(spec.get("figsize", [7.8, 3.05])), dpi=spec.get("dpi", 200))
    fig.patch.set_alpha(0); ax.patch.set_alpha(0)

    # ---- points: from CSV (one row per dot, with a `source` column) or inline spec arrays ----
    src_colors = {**{"SemiAnalysis": BRAND, "Kinlan": INK, "CoreMention": GREY, "botcommits": GREY, "GA": GREY},
                  **spec.get("source_colors", {})}
    src_legend = {**{"Kinlan": "Kinlan · aifoc.us — commits", "SemiAnalysis": "SemiAnalysis — commits", "botcommits": "botcommits — all coding agents (pushes)"},
                  **spec.get("source_legend", {})}
    measured, disputed, proj = load_points(spec)

    mx = [d(p["date"]) for p in measured]
    my = [p["value"] for p in measured]

    # filled area + solid measured line (the trend)
    ax.fill_between(mx, my, color=AREA, zorder=1)
    ax.plot(mx, my, color=BRAND, lw=2.6, zorder=3, solid_capstyle="round")
    # measured dots COLOURED BY SOURCE
    for p in measured:
        ax.scatter([d(p["date"])], [p["value"]], s=54, zorder=4, edgecolor="#fffdf7",
                   linewidth=1.4, color=src_colors.get(p.get("source", ""), DARK))

    # projection (dashed) from the last measured point; endpoint hollow in its source colour
    if proj:
        last = measured[-1]
        px = [d(last["date"]), d(proj["to"])]; py = [last["value"], proj["value"]]
        ax.plot(px, py, color=BRAND, lw=2.0, ls=(0, (5, 4)), alpha=0.6, zorder=2)
        ax.scatter([px[1]], [py[1]], s=54, facecolor="#fffdf7", linewidth=2, zorder=4,
                   edgecolor=src_colors.get(proj.get("source", ""), BRAND))

    # disputed / outlier points (hollow, in the source colour)
    for p in disputed:
        ax.scatter([d(p["date"])], [p["value"]], s=48, facecolor="none", linewidth=1.8, zorder=4,
                   edgecolor=src_colors.get(p.get("source", ""), GREY))

    # per-point value label (mono). Source identity now comes from the LEGEND, not a [n].
    def annotate(p, dy=12, dx=0, ha="center", color=DARK):
        if p.get("label"):
            ax.annotate(p["label"], (d(p["date"]), p["value"]), textcoords="offset points",
                        xytext=(p.get("dx", dx), p.get("dy", dy)), ha=p.get("ha", ha),
                        fontsize=p.get("fs", 12), fontfamily=mono, color=color)
    for p in measured:
        annotate(p, color=src_colors.get(p.get("source", ""), DARK))
    for p in disputed:
        annotate(p, dy=-18, color=GREY)
    if proj:
        annotate({**proj, "date": proj["to"]}, dx=-12, dy=-6, ha="right", color=BRAND)

    # ---- legend: one entry per data source (each dot's origin) ----
    from matplotlib.lines import Line2D
    seen, handles = set(), []
    for p in measured + disputed + ([proj] if proj else []):
        s = p.get("source", "")
        if not s or s == "GA" or s in seen:
            continue
        seen.add(s)
        hollow = s in {q.get("source", "") for q in disputed}
        handles.append(Line2D([0], [0], marker="o", linestyle="none", markersize=9, markeredgewidth=1.6,
                              markerfacecolor="none" if hollow else src_colors.get(s, DARK),
                              markeredgecolor=src_colors.get(s, DARK), label=src_legend.get(s, s)))
    if handles:
        leg = ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=10.5,
                        handletextpad=0.4, labelspacing=0.35, borderaxespad=0.3)
        for t in leg.get_texts():
            t.set_fontfamily(mono); t.set_color(DIM)

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

    fig.tight_layout(pad=0.6)
    fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.06)
    print(f"wrote {out}  ({len(measured)} measured pts"
          f"{', +projection' if proj else ''}"
          f"{', +%d disputed' % len(disputed) if disputed else ''})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: deck_chart.py <spec.json> <out.png>")
    render(json.load(open(sys.argv[1])), sys.argv[2])
