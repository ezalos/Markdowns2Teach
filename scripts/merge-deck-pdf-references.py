#!/usr/bin/env python3
# ABOUTME: Appends the References pages from the screenshot-export PDF onto the text-layer PDF, then verifies both.
# ABOUTME: Refuses to write if any slide page lacks text, or if two consecutive pages are identical.
#
# Why: the text-layer exporter renders only the deck's own slides. The References pages —
# every source's full URL in selectable text — are built by export-deck-pdf.py and already
# live at the tail of the screenshot PDF, so they are carried over rather than rebuilt.
#
# The identical-consecutive-page check is the same bar the screenshot exporter enforces
# (2026-07-09 stale-frame incident); it is applied here too so the alternative path cannot
# ship a defect the default path would have caught.
#
# Usage: merge-deck-pdf-references.py <text-slides.pdf> <screenshot.pdf> <n_slides> <out.pdf>

import hashlib
import sys

from pypdf import PdfReader, PdfWriter


def page_fingerprint(page):
    """Hash the page's drawing instructions — catches a duplicated frame."""
    try:
        data = page.get_contents().get_data()
    except Exception:
        data = b""
    return hashlib.sha256(data).hexdigest()


def main():
    text_pdf, shot_pdf, n_slides, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    text = PdfReader(text_pdf)
    shot = PdfReader(shot_pdf)

    if len(text.pages) != n_slides:
        sys.exit(f"FAIL text layer has {len(text.pages)} pages, expected {n_slides} slides")

    # every slide page must carry real text — that is the whole point of this path
    empty = [i + 1 for i, p in enumerate(text.pages) if len((p.extract_text() or "").strip()) < 40]
    if empty:
        sys.exit(f"FAIL slide pages with no extractable text: {empty}")

    # no two consecutive slide pages may be identical (stale-frame guard)
    prints = [page_fingerprint(p) for p in text.pages]
    dupes = [i + 1 for i in range(len(prints) - 1) if prints[i] == prints[i + 1]]
    if dupes:
        sys.exit(f"FAIL identical consecutive pages after: {dupes}")

    writer = PdfWriter()
    for p in text.pages:
        writer.add_page(p)
    refs = shot.pages[n_slides:]
    if not refs:
        sys.exit("FAIL no References pages found in the screenshot PDF")
    for p in refs:
        writer.add_page(p)

    with open(out, "wb") as fh:
        writer.write(fh)

    links = sum(len(p.get("/Annots") or []) for p in PdfReader(out).pages)
    print(f"OK {out}: {n_slides} text-layer slide pages + {len(refs)} references pages, "
          f"{links} link annotations, no identical consecutive pages")


if __name__ == "__main__":
    main()
