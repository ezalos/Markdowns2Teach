#!/usr/bin/env python3
# ABOUTME: Orders the Station F deck's slides, splicing verbatim slides from the Heuritech reference deck.
# ABOUTME: Emits parts/body.html, which build.py then turns into the self-contained deck.
#
# Why: the deck is a mix of three sources — slides written here, slides taken verbatim from
# the reference deck (Louis: "take rsX exactly as it is"), and new figure slides built around
# official published charts. Keeping the ORDER in code, separate from the content, means the
# running order can be changed without touching a single slide's markup.

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
REF = os.path.join(HERE, "..", "heuritech-agents", "heuritech-agents.html")

# Reference-deck slides, by their number in that deck (rsNN in Louis's review).
REF_PART = {2: "Why now", 4: "Why now", 10: "What an agent is", 13: "Loops",
            14: "Loops", 15: "Loops", 16: "Loops", 17: "How to work",
            19: "Evals", 22: "Close"}

def ref_slides():
    h = open(REF).read()
    body = h[h.find("<body"):h.rfind("<script")]
    return re.findall(r'<section class="slide.*?</section>', body, re.S)

def rs(n, secs):
    """Reference slide n, verbatim apart from the masthead branding."""
    s = secs[n - 1]
    return s.replace(
        '<span class="logo">AI</span><span class="sep"></span><span>Tech Lab</span>',
        f'<span class="logo">SF</span><span class="sep"></span><span>{REF_PART.get(n, "Station F")}</span>')

def local(name, marker):
    """One slide from a local part file, identified by its MARK: comment."""
    src = open(os.path.join(PARTS, name)).read()
    m = re.search(rf"<!-- MARK:{marker}\b.*?(<section class=\"slide.*?</section>)", src, re.S)
    if not m:
        sys.exit(f"marker {marker} not found in {name}")
    return m.group(1)

def nth(name, idx):
    """The idx-th slide (1-based) of a local part file."""
    secs = re.findall(r'<section class="slide.*?</section>', open(os.path.join(PARTS, name)).read(), re.S)
    if idx > len(secs):
        sys.exit(f"{name} has {len(secs)} slides, wanted {idx}")
    return secs[idx - 1]

def main():
    secs = ref_slides()
    order = [
        # --- Why now -------------------------------------------------------
        nth("body-a.html", 1),              # cover
        rs(2, secs),                        # instructor, verbatim + portrait
        rs(4, secs),                        # intelligence is now a commodity
        nth("body-a.html", 5),              # METR — outgrown, not gamed
        local("new-figures.html", "BENCHMARKS"),   # ECI + RLI (absorbs the old wrap)
        nth("body-a.html", 6),              # cost collapse
        local("new-figures.html", "COMMITS"),      # the two botcommits views
        local("new-figures.html", "ECONOMY"),      # Exponential View, two charts
        # --- What an agent is ----------------------------------------------
        rs(10, secs),                       # one goal, many small steps
        nth("body-b.html", 3),              # agent = LLM + harness
        nth("body-b.html", 4),              # the context window
        nth("body-c.html", 15),             # memory demo — moved up, right after context
        local("new-figures.html", "MODELCHOICE"),  # AA cost/intelligence + effort ladder
        # --- How to work ----------------------------------------------------
        nth("body-b.html", 7),              # bad code is the most expensive
        rs(17, secs),                       # two patterns to build with
        nth("body-c.html", 3),              # parallelise reads, serialise writes
        nth("body-c.html", 6),              # four orchestration patterns
        local("new-figures.html", "PATTERN5"),     # evaluator-optimizer, teased
        # --- Loops -----------------------------------------------------------
        rs(13, secs),                       # why now — real capability gains
        rs(14, secs),                       # don't prompt, build loops
        rs(15, secs),                       # loops in the wild
        local("new-figures.html", "NANOGPT"),      # what loops actually achieved
        rs(16, secs),                       # planner / generator / evaluator
        # --- Evals ------------------------------------------------------------
        local("evals.html", "EVALS1"),
        local("evals.html", "EVALS2"),
        # --- Method and leverage ----------------------------------------------
        nth("body-c.html", 12),             # the method spine
        local("new-figures.html", "LEVERAGE"),     # what the leverage looks like, measured
        rs(22, secs),                       # close
    ]
    # The slides are bare <section>s, so the stage wrappers and the presentation
    # chrome have to be emitted here — extracting sections drops whatever markup
    # used to surround them.
    head = ('<body>\n<div class="deck-viewport">\n'
            '<div class="deck-stage" id="deckStage">\n<main>\n')
    foot = ('\n</main>\n</div>\n</div>\n\n'
            '<div class="stepdots" id="stepDots"></div>\n'
            f'<div class="pagination"><b id="curNum">01</b> / <span id="totNum">{len(order)}</span></div>\n'
            '<div class="hint">\u2190 \u2192 \u00b7 Space \u00b7 Home/End</div>\n')
    open(os.path.join(PARTS, "body.html"), "w").write(head + "\n".join(order) + foot)
    print(f"assembled {len(order)} slides -> parts/body.html")

if __name__ == "__main__":
    main()
