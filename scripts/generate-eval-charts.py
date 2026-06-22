# ABOUTME: Generates scatter plot charts for the LLM Evaluation deck (D-eval-llm.md).
# ABOUTME: Produces price vs quality score and price vs Arena Elo plots using real 2026 data.

"""
Generate two scatter plots for the LLM Evaluation deck:
  1. Price (output/1M tokens) vs Quality Score
  2. Price (output/1M tokens) vs Chatbot Arena Elo

Usage:
    python scripts/generate-eval-charts.py

Output:
    slides/sorbonne-m2-2026/evaluation/assets/infographics/price_vs_score_scatter.png
    slides/sorbonne-m2-2026/evaluation/assets/infographics/price_vs_elo_scatter.png
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# --- Data (February/March 2026 pricing + benchmark scores) ---

models = [
    # (name, output_price_per_1M, quality_score_0_100, arena_elo, tier)
    ("DeepSeek V3.2",    0.42,   79,  1361, "Budget"),
    ("GPT-5 Mini",       2.00,   72,  None, "Budget"),
    ("Gemini 2.5 Flash", 0.60,   75,  1335, "Budget"),
    ("Claude Sonnet 4",  15.00,  88,  None, "Mid"),
    ("GPT-5.2",          14.00,  92,  1481, "Mid-Premium"),
    ("Gemini 3.1 Pro",   12.00,  94,  1500, "Premium"),
    ("Claude Opus 4.6",  25.00, 100,  1503, "Premium"),
    ("GPT-5.2 Pro",     168.00,  97,  None, "Ultra-Premium"),
]

tier_colors = {
    "Budget": "#2E7D32",
    "Mid": "#1565C0",
    "Mid-Premium": "#6A1B9A",
    "Premium": "#C62828",
    "Ultra-Premium": "#E65100",
}

OUTPUT_DIR = "slides/sorbonne-m2-2026/evaluation/assets/infographics"


def setup_style():
    """Configure matplotlib for NeurIPS-style academic plots."""
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 11,
        "axes.linewidth": 1.2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
        "axes.facecolor": "#FAFAFA",
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.8,
    })


def plot_price_vs_score():
    """Scatter plot: output price (log scale) vs quality score (0-100)."""
    fig, ax = plt.subplots(figsize=(10, 7))

    for name, price, score, _, tier in models:
        color = tier_colors[tier]
        ax.scatter(price, score, c=color, s=180, zorder=5, edgecolors="white",
                   linewidth=1.5, alpha=0.9)
        # Label placement: offset to avoid overlap
        offset_x = 1.15  # multiplicative for log scale
        offset_y = 1.2
        ha = "left"
        if name == "GPT-5.2":
            offset_y = -2.5
        elif name == "Claude Sonnet 4":
            offset_y = -2.5
        elif name == "GPT-5.2 Pro":
            ha = "right"
            offset_x = 0.85
        ax.annotate(name, (price * offset_x, score + offset_y),
                    fontsize=9, ha=ha, va="bottom", color=color, fontweight="bold")

    ax.set_xscale("log")
    ax.set_xlabel("Output Price ($/1M tokens) — log scale", fontsize=12, fontweight="bold")
    ax.set_ylabel("Quality Score (0–100)", fontsize=12, fontweight="bold")
    ax.set_title("LLM Price vs Quality Score (March 2026)", fontsize=14, fontweight="bold",
                 pad=15)

    # Format x-axis with dollar signs
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"${x:g}"))
    ax.set_xlim(0.1, 300)
    ax.set_ylim(65, 105)

    # Sweet spot annotation
    ax.axhspan(85, 100, xmin=0, xmax=0.35, alpha=0.08, color="#2E7D32")
    ax.annotate("Sweet spot\n($0.50–$2/M)", xy=(1.0, 86), fontsize=9,
                color="#2E7D32", fontstyle="italic", ha="center")

    # Legend
    for tier, color in tier_colors.items():
        ax.scatter([], [], c=color, s=80, label=tier, edgecolors="white", linewidth=1)
    ax.legend(loc="lower right", fontsize=9, framealpha=0.9, title="Tier", title_fontsize=10)

    # Source
    fig.text(0.99, 0.01, "Sources: CostGoat, TLDL, SiliconData (Feb 2026)",
             fontsize=7, ha="right", va="bottom", color="gray", fontstyle="italic")

    plt.tight_layout()
    fig.savefig(f"{OUTPUT_DIR}/price_vs_score_scatter.png", dpi=200, bbox_inches="tight")
    print(f"Saved: {OUTPUT_DIR}/price_vs_score_scatter.png")
    plt.close()


def plot_price_vs_elo():
    """Scatter plot: output price (log scale) vs Chatbot Arena Elo."""
    # Filter to models with Elo scores
    elo_models = [(n, p, s, e, t) for n, p, s, e, t in models if e is not None]

    fig, ax = plt.subplots(figsize=(10, 7))

    # Manual label positions: (dx_mult, dy, ha)
    label_pos = {
        "DeepSeek V3.2":    (1.15, 8, "left"),
        "Gemini 2.5 Flash": (1.15, 8, "left"),
        "GPT-5.2":          (1.15, -18, "left"),
        "Gemini 3.1 Pro":   (0.35, 5, "right"),
        "Claude Opus 4.6":  (1.15, -18, "left"),
    }

    for name, price, _, elo, tier in elo_models:
        color = tier_colors[tier]
        ax.scatter(price, elo, c=color, s=220, zorder=5, edgecolors="white",
                   linewidth=1.5, alpha=0.9)
        dx, dy, ha = label_pos.get(name, (1.15, 5, "left"))
        ax.annotate(name, (price * dx, elo + dy),
                    fontsize=9, ha=ha, va="bottom", color=color, fontweight="bold")

    ax.set_xscale("log")
    ax.set_xlabel("Output Price ($/1M tokens) — log scale", fontsize=12, fontweight="bold")
    ax.set_ylabel("Chatbot Arena Elo", fontsize=12, fontweight="bold")
    ax.set_title("LLM Price vs Arena Elo (March 2026)", fontsize=14, fontweight="bold", pad=15)

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"${x:g}"))
    ax.set_xlim(0.1, 50)
    ax.set_ylim(1300, 1540)

    # Highlight the value gap
    ax.annotate("", xy=(0.42, 1361), xytext=(25, 1503),
                arrowprops=dict(arrowstyle="<->", color="#666", lw=1.5, ls="--"))
    ax.annotate("60x cheaper\n-142 Elo pts", xy=(3, 1430), fontsize=9,
                color="#666", ha="center", fontstyle="italic")

    # Legend
    for tier, color in tier_colors.items():
        if any(t == tier for _, _, _, _, t in elo_models):
            ax.scatter([], [], c=color, s=80, label=tier, edgecolors="white", linewidth=1)
    ax.legend(loc="lower right", fontsize=9, framealpha=0.9, title="Tier", title_fontsize=10)

    # Source
    fig.text(0.99, 0.01, "Sources: LM Arena, Vertu, CostGoat (Feb 2026)",
             fontsize=7, ha="right", va="bottom", color="gray", fontstyle="italic")

    plt.tight_layout()
    fig.savefig(f"{OUTPUT_DIR}/price_vs_elo_scatter.png", dpi=200, bbox_inches="tight")
    print(f"Saved: {OUTPUT_DIR}/price_vs_elo_scatter.png")
    plt.close()


if __name__ == "__main__":
    setup_style()
    plot_price_vs_score()
    plot_price_vs_elo()
    print("Done — 2 charts generated.")
