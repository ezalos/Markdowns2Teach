# Lessons — patterns from corrections

## 2026-07-09 — "Verified" must mean the artifact the reader receives
**What happened:** the heuritech PDF shipped with bare-domain citations even though
`check-citation-links.py --check-live` passed. Two blind spots compounded: (1) the linter
validated `href` attributes only, never the visible label ("metr.org" as display text over a
deep-link href); (2) the PDF was built from screenshots, which strip every hyperlink — so the
delivered artifact degraded to exactly the failure the linter "guaranteed" impossible.
**Rule:** a guarantee is only as strong as its coverage of the DELIVERED artifact. When
promising "X can never happen again", enumerate every artifact the user consumes (HTML, PDF,
PPTX, print) and every layer (href, display text, annotations), and put the check in the
default tool path (Makefile target), not in a skill or my memory. Skills don't fire
systematically; `make` does.
**Tooling:** `sources.yml` registry + `scripts/verify-sources.py` (verbatim quote grep, gates
`make export-pdf-%`), `scripts/export-deck-pdf.{js,py}` (paint-synced, link annotations,
references page, identical-page hard-fail).

## 2026-07-09 — Never trust page.pdf() on fixed-stage decks; never sleep as sync
**What happened:** per-slide `page.pdf()` after `deck.goTo()` + fixed 180ms sleep produced
runs of byte-identical pages — Chrome printed the last committed compositor frame, not the
mutated DOM. Non-deterministic: single-slide repros passed.
**Rule:** after a DOM mutation, synchronize on an actual paint (double requestAnimationFrame),
then capture via screenshot (forces fresh composite), and HARD-FAIL the pipeline if two
consecutive captures hash identical. A fixed sleep is a race, and "it worked when I tested one"
is exactly how races ship.
