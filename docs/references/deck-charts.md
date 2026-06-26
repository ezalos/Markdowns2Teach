<!-- ABOUTME: Reusable methodology for real, sourced data charts in the light-paper HTML decks. -->
<!-- ABOUTME: Never hand-draw a data chart in SVG — generate it from a spec with deck_chart.py. -->

# Deck charts — the reusable methodology

A data chart in a slide is evidence. Hand-drawing one in `<svg>` (guessing coordinates,
eyeballing a time axis) produces wrong, un-auditable graphics — e.g. a time axis where
"6 weeks" and "1 year" sit equally spaced. **Don't.** Generate every data chart from a real
tool against real, dated, sourced points.

## Tooling

- **`scripts/charts/deck_chart.py`** — themed time-series generator (matplotlib + seaborn).
  Takes a JSON spec, emits a transparent PNG matched to the light-paper palette and the
  deck fonts (JetBrains Mono ticks / Work Sans / Bodoni). Run via uv:
  ```bash
  uv run --with matplotlib --with seaborn \
    scripts/charts/deck_chart.py scripts/charts/specs/<name>.json /tmp/<name>.png
  ```
- **`scripts/charts/specs/<name>.json`** — the committed, editable data spec (one per chart).
  Points carry `date`, `value`, `src` (the `[n]` key), `label`, and optional `dx/dy/ha` to
  dodge neighbours. Sections: `points_measured`, `points_disputed` (hollow outliers),
  `projection` (dashed). See `specs/heuritech-commit-share.json`.
- Fonts are fetched once to `scripts/charts/.fontcache/` (gitignored); falls back to DejaVu
  if offline. The chart still renders, just with substitute fonts.

## Workflow (every data chart)

1. **Research the points first.** Get *dated* values, each with its own source. Dispatch a
   web-search agent; demand a `date | value | source URL | confidence | vendor/independent`
   table. **No fabricated in-between points** — plot only what a source supports. If only 3–4
   real points exist, plot 4 honest points, not 10 invented ones.
2. **Be honest in the spec.** Measured points solid; **projections dashed** (label them so);
   conflicting single-vendor figures as **hollow "disputed" markers**, not peers of measured
   data. Keep one metric per series (don't mix daily- and weekly-denominator shares silently).
3. **Sources: `[n]` on the plot, clickable text in the slide.** The PNG shows only the `[n]`
   marker per point. The source *names/links* live in the slide's HTML `<div class="sources">`
   footer, keyed to the same `[n]`, so they're clickable. Never bake source text into the image.
4. **Embed** the PNG base64 into the deck's chart card (`base64.b64encode` in a small script —
   don't paste base64 into the editor). Keep the card title + a one-line legend caption in HTML.
5. **Re-verify**: the image changes layout, so re-run `make test-decks`
   (`scripts/check-slide-overlap.js`) and `scripts/check-citation-links.py --check-live`. A
   flaky/dead source link (e.g. a 522) → make that `[n]` **text-only** but keep the attribution.

## Why this is the standard

Reproducible (spec in git), honest (only sourced points, projections marked), correct
(proportional real-date axis from a real plotting lib), on-brand (deck palette + fonts), and
auditable (every point keyed to a clickable source). The first use is the s05 commit-share
chart in `slides/heuritech-agents/`. See also [[overlap-detector]] and the citation rules in
`html-deck-interaction-standards.md` §5.
