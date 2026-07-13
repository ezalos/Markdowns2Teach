<!-- ABOUTME: THE deck-building workflow for sessions in this repo: from intake drops to a
     shipped, citation-gated frontend-slides deck. Marp is plan B (workflow-new-slides.md). -->

# Workflow — new deck (frontend-slides, the default engine)

Scope: ANY new deck — standalone talk or Sorbonne course deck. The default engine is
**frontend-slides** (self-contained HTML, fixed 1920x1080 stage). **Marp is plan B**: use it
only with a stated reason (e.g. editable PPTX handouts for students, bulk Markdown edits
across many decks), record the reason in the deck README or a manifest comment, then follow
`workflow-new-slides.md` — and still ship a `sources.yml`.

## 0. Inputs

- **Cross-project decks**: intake drops at `docs/talks/<slug>/intake_<datetime>/`, produced
  by a source-side agent per `docs/references/deck-intake-spec.md`. The bundle is the union
  of drops (newest wins). The first drop carries `HANDOFF.md`: audience, story, verified
  numbers (with honesty caveats), asset map with sensitivity marks, external sources, open
  calls. Read ALL drops before building; `ANSWERS.md` files respond to earlier requests.
- **Repo-native decks** (course decks, self-sourced talks): write the same `HANDOFF.md`
  yourself at `docs/talks/<slug>/HANDOFF.md` (committed) before building. Same quality bar;
  no rsync involved.

## 1. Build

- Deck dir: `slides/<slug>/` — self-contained `.html` named `<slug>.html`, generated with
  the frontend-slides skill from portable Markdown content (keep it in
  `slides/<slug>/content/` if the deck will be regenerated).
- Every regeneration must satisfy `docs/references/html-deck-interaction-standards.md`
  (macOS-safe forward-only reveals, wheel nav, deep-link citations, no-overlap on the
  fixed stage).
- Data charts: NEVER hand-drawn SVG — `scripts/charts/deck_chart.py` per
  `docs/references/deck-charts.md`.
- Seed `slides/<slug>/sources.yml` from HANDOFF's External sources table (URL entries with
  verbatim quotes) and its asset map (file entries).

## 2. Provenance & citations (the gates)

- **External claims**: clickable exact deep links with `[n]` markers; registry entry with a
  verbatim quote. `python3 scripts/check-citation-links.py <deck> --check-live` and
  `python3 scripts/verify-sources.py <deck>` must pass — see CLAUDE.md's non-negotiable.
- **Internal artifacts** (experiment data, project files from the bundle): mark the claim's
  footer element with `data-file-source="<registry-id>"` and register a `file:` entry.
  Then EITHER promote the artifact — copy it out of the gitignored drop to a committed
  location (`docs/talks/<slug>/` or the deck assets) after a size + sensitivity check —
  OR register it `verify: local-only` + `sha256` + `reason` (heavy/personal artifacts).
- **PERSONAL-marked files**: never committed, never promoted or shown without Louis's
  explicit approval. Prefer redacted derivatives.
- Run `make check` (offline gates) and `make test-decks` (nav + overlap) after every build.

## 3. Critique loop

Iterate until the deck holds:
- Read the deck as the audience would; check every slide against HANDOFF's story and
  verified-numbers table (numbers not in the table do not go on slides; CAVEAT numbers
  carry their caveat).
- When material is missing, escalate in order:
  1. **Re-pull** — the source side may have pushed a new drop; list `intake_*/` dirs newer
     than the last one you read.
  2. **Request** — write `docs/talks/<slug>/requests/REQUESTS-<YYYY-MM-DD-HHMM>.md`:
     numbered items, each *what / why / preferred form*. Commit it and tell Louis
     "requests ready for <slug>" — he relays "pull new requests" to the source agent, which
     answers with a new `intake_<datetime>/` drop containing `ANSWERS.md`.
  3. **Derive** — produce what you need from drops already present (charts, crops,
     recomputation), with subagents where useful.

  If a re-pull fails, report it and stop — never guess at bundle state.

## 4. Ship

1. `slides/index.manifest.yml`: add the deck (`date`, `prebuilt_html`).
2. `make check && make test-decks` — clean.
3. `make export-pdf-<slug>` — the LIVE gate (fetches every URL, greps quotes, verifies file
   sources) then builds the link-annotated PDF with a References page.
4. `make deploy` — publish to slides.develle.fr.
