#!/usr/bin/env python3
# ABOUTME: Assembles the Station F deck from its body parts + the shared light-paper design system.
# ABOUTME: Reproducible: concat parts, add step reveals, patch display-font glyph gaps, inline images.
#
# Why a build script: the deck is a single self-contained HTML file, but it is edited as
# parts. Re-applying the reveal classes, the glyph workarounds and the base64 inlining by
# hand after every content edit is how you get an inconsistent deck. Run this instead:
#
#   python3 slides/station-f-claude-code/build.py
#
# Inputs live in parts/ (body-a/b/c) plus head.html and tail.html, which carry the design
# system and the controller lifted from the Tech Lab deck (same visual language on purpose).

import base64
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
OUT = os.path.join(HERE, "station-f-claude-code.html")

# The fixed stage does not reflow: .figframe is height:100% in the base system, so on a
# slide that also carries a sources footer it grows straight through it. Cap it explicitly.
OVERRIDES = """
/* === DECK-SCOPED OVERRIDES === */
.s-body .figframe{max-height:600px;}
.s-body .ctxpanel{max-height:660px;overflow:hidden;}
.s-body .ctxaxis{max-height:660px;}
"""

# Bodoni Moda has no '+', '~', en-dash or multiplication-sign glyph at display weight — they
# silently vanish. Set the symbol in the body face, keep the numerals in the display face.
def body_face(sym, weight=700):
    return f'<span style="font-family:var(--font-body);font-weight:{weight};">{sym}</span>'

GLYPH_FIXES = [
    ('>+14%<', f'>{body_face("+")}14%<'),
    ('>6&ndash;18%<', f'>6{body_face("&ndash;", 600)}18%<'),
    ('>+80.8%<', f'>{body_face("+")}80.8%<'),
    ('>&minus;70.0%<', f'>{body_face("&minus;")}70.0%<'),
    ('>9&times; &ndash; 900&times;<', f'>9{body_face("&times;",600)} {body_face("to",600)} 900{body_face("&times;",600)}<'),
    ('>8&ndash;9%<', f'>8{body_face("&ndash;",600)}9%<'),
    ('>~1,200<', f'>{body_face("~",600)}1,200<'),
    ('>70,000+<', f'>70,000{body_face("+")}<'),
]


# Bodoni Moda renders an em-dash as a near-invisible hairline at display sizes, so any
# "a &mdash; b" inside a display-font element reads as an unexplained gap on the projector.
# Swap it for a comma in exactly those places (h1 titles and display-font inline styles).
def de_dash_display(html):
    def fix(m):
        return m.group(0).replace(" &mdash; ", ", ")
    html = re.sub(r"<h1[^>]*>.*?</h1>", fix, html, flags=re.S)
    html = re.sub(r'<p style="[^"]*font-display[^"]*">.*?</p>', fix, html, flags=re.S)
    # .figtitle is display-face too, so a figure caption's em-dash disappears the same way.
    html = re.sub(r'<div class="figtitle">.*?</div>', fix, html, flags=re.S)
    return html

def sniff(raw, path):
    """Trust the bytes, not the extension — a .png that is really WebP breaks silently."""
    if raw[:4] == b"\x89PNG":
        return "image/png"
    if raw[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
        return "image/webp"
    if b"<svg" in raw[:400]:
        return "image/svg+xml"
    sys.exit(f"unknown image type: {path}")

def main():
    head = open(os.path.join(PARTS, "head.html")).read()
    tail = open(os.path.join(PARTS, "tail.html")).read()
    body = open(os.path.join(PARTS, "body.html")).read()

    # progressive disclosure on the teaching elements
    body = body.replace('<div class="stat" style=', '<div class="stat step-group" style=')
    body = body.replace('<div class="card">', '<div class="card step-group">')
    body = re.sub(r"<li>(?!\s*<)", '<li class="step-group">', body)

    for old, new in GLYPH_FIXES:
        body = body.replace(old, new)
    body = de_dash_display(body)
    # Section labels: the numbered "Part N" mastheads outlived the dividers they belonged to.
    for old, new in (("Part 4 &middot; One or many", "How to work"),
                     ("Part 5 &middot; Loops", "Loops"),
                     ("Part 6 &middot; The method", "Loops"),
                     ("Part 7 &middot; Leverage", "Close"),
                     ("Part 3 &middot; Your codebase", "How to work"),
                     ("Part 2 &middot; What", "What an agent is"),
                     ("Part 1 &middot; Why", "Why now")):
        body = body.replace(f"<span>{old}</span>", f"<span>{new}</span>")

    html = head.replace("\n</style>", OVERRIDES + "\n</style>", 1) + body + tail + "\n</body>\n</html>\n"

    # self-contained: inline every local image
    missing = []
    for ref in sorted(set(re.findall(r'src="(assets/[^"]+)"', html))):
        path = os.path.join(HERE, ref)
        if not os.path.exists(path):
            missing.append(ref)
            continue
        raw = open(path, "rb").read()
        html = html.replace(f'src="{ref}"',
                            f'src="data:{sniff(raw, path)};base64,{base64.b64encode(raw).decode()}"')
    if missing:
        sys.exit("MISSING IMAGES (deck would ship broken):\n  " + "\n  ".join(missing))

    open(OUT, "w").write(html)
    print(f"built {OUT}  ({html.count('<section class=\"slide')} slides, {len(html)//1024} KB)")

if __name__ == "__main__":
    main()
