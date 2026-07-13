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

## 2026-07-13 — Acceptance must run EVERY documented gate, including export
**What happened:** the deck-capability plan shipped file-backed citation sources and its
acceptance task ran check/verify gates but never `make export-pdf-<deck>`. The final review
found the exporter's References page crashed (KeyError) on `file:` entries — the documented
ship gate was broken for the exact feature being accepted. Same root pattern as the
2026-07-09 lesson: the guarantee didn't cover the delivered artifact, this time at plan level.
**Rule:** an acceptance/verification step must enumerate and run every gate the docs promise
for the artifact's full lifecycle (check → test → EXPORT → deploy), not just the fast ones.
If a doc says "make export-pdf verifies X", the plan must run it.

## 2026-07-13 — Never `git add -A` in plans/subagent steps; pathspec commits bypass the index
**What happened:** (1) a task's `git add -A <paths>` step was executed as bare `-A` by a
subagent and swept 25.8MB of untracked experiment data (docs/talks/rlaif-vlm/examples/) into
history — discovered two tasks later. (2) In ~/Setup, `git commit <pathspec>` committed
working-tree content, bypassing a carefully partial-staged index and sweeping a concurrent
session's edits (caught and undone immediately).
**Rules:** plans and fix dispatches always use explicit `git add <file...>` (never `-A`);
after partial staging (`git apply --cached`), commit with NO pathspec; when two sessions
share a repo, treat the index as contested — stage and commit in one breath, verify
`git diff --cached` first.
