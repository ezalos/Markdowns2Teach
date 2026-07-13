#!/usr/bin/env python3
# ABOUTME: Stage 2 of deck→PDF export: assembles slide PNGs into a PDF with CLICKABLE link
# ABOUTME: annotations + a References page listing every source's FULL URL, or repo path for file-backed sources, in selectable text.

"""
Why this exists: a shipped screenshot-PDF silently stripped every hyperlink — citations
degraded to bare-domain labels, unverifiable (2026-07-09 incident). This assembler
guarantees a PDF can never lose its sources:
  1. every <a> rectangle captured by export-deck-pdf.js becomes a real PDF link annotation
     (clickable in any reader), and
  2. a final References page lists every registry source as selectable text — URL entries
     get the FULL exact URL + a clickable link annotation; `file:` entries (internal
     artifacts, no live URL to click) get the repo-relative path instead, suffixed
     `(committed)` or `(local-only, sha256 <prefix>…)` — so even a print or flat copy
     carries every source in full.
It refuses to build if pages are missing or any two consecutive pages are identical.

Usage: python3 scripts/export-deck-pdf.py <shots_dir> <sources.yml> <out.pdf>
Run after: node scripts/export-deck-pdf.js <deck.html> <shots_dir>
Deps: pillow, reportlab, pyyaml (uv run --with pillow --with reportlab --with pyyaml).
"""

import hashlib
import io
import json
import sys
from pathlib import Path

import yaml
from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

PAGE_W, PAGE_H = 960, 540  # pt, 16:9
INK, BRAND, DIM = HexColor("#1a2238"), HexColor("#b1502a"), HexColor("#9a8f7d")
PAPER = HexColor("#f4efe4")


def main():
    if len(sys.argv) != 4:
        sys.exit("usage: export-deck-pdf.py <shots_dir> <sources.yml> <out.pdf>")
    shots_dir, reg_path, out_pdf = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]

    meta = json.loads((shots_dir / "rects.json").read_text())
    shots = sorted(shots_dir.glob("s*.png"))
    if len(shots) != meta["slides"]:
        sys.exit(f"FAIL page mismatch: {len(shots)} shots vs {meta['slides']} slides declared")
    hashes = [hashlib.sha1(p.read_bytes()).hexdigest() for p in shots]
    for i in range(1, len(hashes)):
        if hashes[i] == hashes[i - 1]:
            sys.exit(f"FAIL identical consecutive pages: {shots[i-1].name} == {shots[i].name} (stale frame)")

    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8"))
    c = canvas.Canvas(out_pdf, pagesize=(PAGE_W, PAGE_H))
    sx, sy = PAGE_W / 1920.0, PAGE_H / 1080.0

    for i, shot in enumerate(shots):
        img = Image.open(shot).convert("RGB")
        if img.width > 2560:  # dsf=2 shots are 3840px; 2560 is plenty for a 960pt page
            img = img.resize((2560, int(img.height * 2560 / img.width)), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=88)
        buf.seek(0)
        from reportlab.lib.utils import ImageReader
        c.drawImage(ImageReader(buf), 0, 0, PAGE_W, PAGE_H)
        for link in meta["pages"][i]["links"]:
            x1, y1 = link["x"] * sx, PAGE_H - (link["y"] + link["h"]) * sy  # css y-down -> pdf y-up
            c.linkURL(link["href"], (x1, y1, x1 + link["w"] * sx, y1 + link["h"] * sy), relative=0)
        c.showPage()

    # ---- References page(s): every source, full URL, selectable + clickable ----
    entries = reg.get("sources", [])
    per_page, idx = 11, 0
    while idx < len(entries):
        c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 20)
        title = "References — every source, full link"
        if idx: title += " (cont.)"
        c.drawString(48, PAGE_H - 52, title)
        y = PAGE_H - 90
        for e in entries[idx:idx + per_page]:
            slides = ",".join(str(s) for s in e.get("slides", []))
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 10.5)
            c.drawString(48, y, f"[s{slides}]  {e['authority']} — {e['title']}")
            c.setFillColor(BRAND); c.setFont("Helvetica", 9.5)
            if e.get("file"):
                # file-backed source: repo-relative path is the citation, not a URL —
                # nothing to click, so no linkURL annotation.
                if e.get("verify") == "local-only":
                    suffix = f" (local-only, sha256 {e.get('sha256', '')[:12]}…)"
                else:
                    suffix = " (committed)"
                c.drawString(66, y - 13, f"{e['file']}{suffix}")
            else:
                c.drawString(66, y - 13, e["url"])
                c.linkURL(e["url"], (66, y - 17, 66 + c.stringWidth(e["url"], "Helvetica", 9.5), y - 4), relative=0)
            if e.get("verify") == "link-only":
                c.setFillColor(DIM); c.setFont("Helvetica-Oblique", 8)
                c.drawString(66, y - 24, f"link-only: {e.get('reason','')[:110]}")
                y -= 11
            y -= 38
        c.showPage()
        idx += per_page

    c.save()
    print(f"OK {out_pdf}: {len(shots)} slide pages + references ({len(entries)} sources), "
          f"link annotations on every citation, no identical consecutive pages")


if __name__ == "__main__":
    main()
