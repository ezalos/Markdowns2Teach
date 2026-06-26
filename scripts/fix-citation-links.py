#!/usr/bin/env python3
# ABOUTME: One-shot remediation: rewrite bare-domain citation anchors to exact source URLs.
# ABOUTME: Order-stable — the i-th bare-domain <a> in a deck gets the i-th URL in its list.

"""
The same bare domain (e.g. anthropic.com) is cited for DIFFERENT claims on
different slides, so a blind find/replace would mislink them. This walks the
bare-domain anchors in document order and applies a per-deck ordered list:
  - a URL  -> set that anchor's href to the exact source (keep the link text)
  - "TEXT_ONLY" -> unwrap the anchor (drop <a>, keep the visible text); used when
    no exact supporting page exists, since a guessed/bare link is worse than none.

Run from repo root: python3 scripts/fix-citation-links.py
Idempotent: once hrefs have paths they are no longer "bare", so re-runs that
find fewer anchors than the list expects will refuse to touch the file.
"""

import re
import sys
from urllib.parse import urlparse

ALLOW_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com", "api.fontshare.com"}
ANCHOR_RE = re.compile(r'<a\b[^>]*\bhref="(https?://[^"]+)"[^>]*>(.*?)</a>', re.S)


def is_bare(url: str) -> bool:
    p = urlparse(url)
    if (p.hostname or "").lower() in ALLOW_HOSTS:
        return False
    return p.path.strip("/") == "" and not p.query


def fix(path: str, mapping: list[str]) -> int:
    html = open(path, encoding="utf-8").read()
    # collect bare-domain anchor spans in document order
    spans = [m for m in ANCHOR_RE.finditer(html) if is_bare(m.group(1))]
    if len(spans) != len(mapping):
        sys.exit(
            f"ABORT {path}: found {len(spans)} bare-domain anchors but mapping has "
            f"{len(mapping)}. Refusing to guess alignment."
        )
    # rewrite right-to-left so earlier spans' offsets stay valid
    for m, target in reversed(list(zip(spans, mapping))):
        whole, href, inner = m.group(0), m.group(1), m.group(2)
        if target == "TEXT_ONLY":
            new = inner  # unwrap: keep visible text, drop the misleading link
        else:
            new = whole.replace(f'href="{href}"', f'href="{target}"', 1)
        html = html[: m.start()] + new + html[m.end():]
    open(path, "w", encoding="utf-8").write(html)
    return len(spans)


# --- Exact source URLs (all HTTP-verified 2026-06-26) ---
SEMI   = "https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point"
VB     = "https://venturebeat.com/ai/the-great-ai-agent-acceleration-why-enterprise-adoption-is-happening-faster-than-anyone-predicted"
FIN    = "https://fin.ai/benchmarks"
METR   = "https://metr.org/blog/2026-1-29-time-horizon-1-1/"
ARXIV  = "https://arxiv.org/abs/2503.14499"
EPOCH  = "https://epoch.ai/data-insights/llm-inference-price-trends"
BEA    = "https://www.anthropic.com/engineering/building-effective-agents"      # agent loop def + 5 patterns
SKILLS = "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"
CONTAIN= "https://www.anthropic.com/engineering/how-we-contain-claude"          # read-only / attack surface
CTXENG = "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"  # finite window
RASCHKA= "https://magazine.sebastianraschka.com/p/components-of-a-coding-agent" # harness + orchestration/subagents
ASKILLS= "https://agentskills.io/specification"
SNYK   = "https://snyk.io/articles/skill-md-shell-access/"
HAMEL  = "https://hamel.dev/blog/posts/evals/"
BRAIN  = "https://www.youtube.com/watch?v=FB-MLPhL9Ms"                          # Phil Hetzel / Braintrust talk
SUPPORT= "https://support.claude.com/en/articles/13364135-use-claude-cowork-safely"
MKEY   = "https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key"
MPRICE = "https://mistral.ai/pricing/"
SCALE  = "https://www.scaleway.com/en/generative-apis/"
CC_MEM = "https://code.claude.com/docs/en/memory"
CC_IAM = "https://code.claude.com/docs/en/iam"                                  # permission modes (ask/plan/auto)
T      = "TEXT_ONLY"   # no exact page exists → unlink rather than mislead
# TEXT_ONLY cases: coremention (not a real authority), anthropic "$2.5B Claude Code ARR"
# (no clean Anthropic page carries that number), llm-stats.com/frontiercode (404).

# --- Per-deck ordered mappings (document order — see scripts/check-citation-links.py output) ---
MAPPINGS: dict[str, list[str]] = {
    "slides/heuritech-agents/heuritech-agents.html": [
        SEMI, T, VB, FIN, T, METR, ARXIV, EPOCH, BEA, RASCHKA,
        SKILLS, ASKILLS, SNYK, RASCHKA, HAMEL, BRAIN, BEA,
    ],
    "slides/capgemini-ai-agents/capgemini-ai-agents.html": [
        SEMI, T, VB, FIN, T, METR, ARXIV, EPOCH, RASCHKA, BEA,
        SKILLS, ASKILLS, SNYK, CONTAIN, SUPPORT, RASCHKA, CTXENG, MKEY, SCALE, BEA,
    ],
    "slides/capgemini-ai-agents/capgemini-ai-agents-original.html": [
        SEMI, T, VB, FIN, T, METR, EPOCH, MPRICE, RASCHKA, ASKILLS,
        SNYK, RASCHKA, CC_MEM, CC_IAM, T, MKEY, SCALE, HAMEL,
    ],
}


if __name__ == "__main__":
    if not MAPPINGS:
        sys.exit("MAPPINGS not yet populated — fill in the per-deck ordered URL lists first.")
    for path, mapping in MAPPINGS.items():
        n = fix(path, mapping)
        print(f"fixed {n} citation link(s) in {path}")
