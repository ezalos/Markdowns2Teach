#!/usr/bin/env python3
# ABOUTME: Cost-vs-capability scatter for the light-paper decks, with one line per model showing its reasoning-effort ladder.
# ABOUTME: Companion to deck_chart.py (which is a time-series tool); same palette and fonts, different chart shape.
#
# Why a second tool: deck_chart.py plots value-over-time. The question "what does more
# thinking effort buy, and what does it cost" is a scatter with a connected ladder per
# model — a different geometry, same house style.
#
# Run: uv run --with matplotlib --with seaborn scripts/charts/effort_scatter.py <data.csv> <out.png>

import csv
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns

# Light-paper theme, mirroring deck_chart.py / the deck :root variables
INK, DIM, BRAND = "#1a2238", "#6b6f78", "#b1502a"
GRID = "#d9d2c4"

# Families to draw, in legend order, with their colour. Everything else is context.
FEATURED = {
    "Claude Opus 5":  "#b1502a",
    "Claude Fable 5": "#8c3d1f",
    "GPT-5.6 Sol":    "#2f6f8f",
    "GPT-5.6 Luna":   "#5aa0bf",
    "Grok 4.6":       "#2f8f63",
}

def load(path):
    rows = []
    with open(path) as f:
        for r in csv.DictReader(f):
            try:
                r["x"] = float(r["cost_per_index_task_usd"])
                r["y"] = float(r["intelligence_index"])
            except (ValueError, KeyError):
                continue
            rows.append(r)
    return rows

def main(src, out):
    rows = load(src)
    sns.set_style("white")
    fig, ax = plt.subplots(figsize=(7.9, 4.5), dpi=200)
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # every non-featured model, as quiet context
    others = [r for r in rows if r["family"] not in FEATURED]
    if others:
        ax.scatter([r["x"] for r in others], [r["y"] for r in others],
                   s=42, c="#c9c2b4", edgecolors="none", zorder=2,
                   label="other frontier models")

    # featured families: connect the effort ladder low -> high
    by_family = defaultdict(list)
    for r in rows:
        if r["family"] in FEATURED:
            by_family[r["family"]].append(r)

    for fi, (fam, colour) in enumerate(FEATURED.items()):
        pts = sorted(by_family.get(fam, []), key=lambda r: r["x"])
        if not pts:
            continue
        if len(pts) > 1:
            ax.plot([p["x"] for p in pts], [p["y"] for p in pts],
                    color=colour, lw=1.6, alpha=0.55, zorder=3, solid_capstyle="round")
        ax.scatter([p["x"] for p in pts], [p["y"] for p in pts],
                   s=95, c=colour, edgecolors="white", linewidths=1.4, zorder=4, label=fam)
        # Label only the ends of each ladder. Labelling every rung collides on the
        # right-hand cluster, where four families overlap within a few cents.
        ends = [pts[0]] if len(pts) == 1 else [pts[0], pts[-1]]
        for k, p in enumerate(ends):
            eff = (p.get("reasoning_effort") or "").strip()
            if not eff or eff == "with fallback":
                continue
            below = (k == 0)
            # fan the labels sideways per family: four ladders converge within a
            # few cents on the right, so a pure vertical offset still collides.
            dx = (-26, 26, 0, -26, 26)[fi % 5]
            ha = "right" if dx < 0 else ("left" if dx > 0 else "center")
            ax.annotate(eff, (p["x"], p["y"]), textcoords="offset points",
                        xytext=(dx, -16 if below else 11), ha=ha,
                        fontsize=8.5, color=DIM)

    ax.set_xscale("log")
    ax.set_xlabel("cost per task  ($, log scale)", fontsize=11, color=DIM, labelpad=9)
    ax.set_ylabel("Artificial Analysis Intelligence Index", fontsize=11, color=DIM, labelpad=9)
    ax.tick_params(colors=DIM, labelsize=10)
    ax.grid(True, which="major", color=GRID, lw=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)

    leg = ax.legend(loc="lower right", frameon=False, fontsize=9.5, labelspacing=0.45)
    for t in leg.get_texts():
        t.set_color(INK)

    fig.tight_layout(pad=0.6)
    fig.savefig(out, transparent=True, bbox_inches="tight")
    print(f"wrote {out}  ({len(rows)} points, {len(by_family)} featured families)")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
