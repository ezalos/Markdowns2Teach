<!-- ABOUTME: Design spec for the cross-project deck-building capability: intake bundles, the
critique loop, engine policy, global discoverability, and citation-tooling consolidation. -->

# Deck capability — design

Status: approved design, 2026-07-13. Origin: `docs/2026-07-09-deck-capability-handoff.md`
(handoff from the ~/Setup capability-surface session). Decisions below were validated with
Louis in the brainstorming session; the rlaif-vlm deck (2026-07-09) is the workflow's
empirical prototype.

## Problem

Deck building is cross-functional: the source material lives in whichever project the deck
is about (possibly on another machine), while the standards, citation gates, index, and
publish pipeline live here. Nothing outside this repo knows the capability exists. The
build has two engines with no declared default. The citation validators exist in two
drifting implementations. And the one real cross-project deck (rlaif-vlm) worked via an
ad-hoc handoff doc, left its provenance untracked, and cited internal artifacts a contract
that only knows URLs.

## Decisions (validated with Louis)

1. **Source flow**: a formalized intake bundle, produced by a source-side agent from a
   portable spec, delivered by one-way rsync into this repo. No M2T session needs to exist
   before the data is ready.
2. **Provenance**: intake drops are gitignored by default (sources can be heavy or contain
   personal info); what a deck cites or embeds is promoted deliberately, or registered as
   `local-only` with a checksum. Blanket commit/no-commit rules were explicitly rejected.
3. **Engine**: frontend-slides is the default for ALL new decks, talks and future course
   editions alike. Marp is plan B — kept working, chosen only with a stated reason.
4. **Discoverability**: one global `deck` skill (intake + pointer) plus a capability-index
   line in global CLAUDE.md. The deck loop itself stays sequestered in this repo.
5. **Citation SSOT**: the global `~/Setup/skills/cite` bundle is canonical for the shared
   validators; this repo's frozen `scripts/cite/` mirror is deleted. The deck-artifact
   linters (`check-citation-links.py`, `verify-sources.py`) stay repo-canonical.

## The flow, end to end

Actors: the **source-side agent** (any repo, any machine), **Louis** (courier and
approver), the **deck agent** (a session in this repo).

1. A deck need arises in project X. The source-side agent gets the intake spec — via the
   global `deck` skill on Louis's machines, or pasted / `share-file`'d to a remote agent —
   and produces a `deck-intake/` bundle inside project X, on its own schedule.
2. The bundle is pushed by rsync to `docs/talks/<slug>/intake_<datetime>/` here. At first
   push the source side records the endpoints (host alias, talk dir path) in its own
   `deck-intake/SYNC.md`, so every later round-trip is deterministic.
3. The deck session here builds `slides/<slug>/` with frontend-slides under this repo's
   gates (interaction standards, citation linters, sources.yml registry), iterating.
4. "More data" has three escalation levels:
   - **(a) re-pull** — the deck agent re-runs the pull itself when the source side adds
     material;
   - **(b) request round-trip** — the deck agent writes
     `docs/talks/<slug>/requests/REQUESTS-<datetime>.md` (committed). Louis tells the
     source-side agent to "pull new requests"; that agent rsyncs the talk dir down, does
     the work (gather missing data, answer questions, produce artifacts), and pushes back a
     NEW drop `intake_<datetime>/` containing an `ANSWERS.md`. Previous drops are never
     modified;
   - **(c) derive** — the deck agent spawns its own agents to derive material from drops
     already present (charts via `scripts/charts/deck_chart.py`, crops, recomputations).
5. Ship: `make check` → `make export-pdf-<slug>` → `slides/index.manifest.yml` entry →
   `make deploy`.

Transport assumptions: rsync source→here always available (same machine = local rsync);
here→source NOT assumed — every transfer is initiated from the source side or is a
deck-side pull. Louis carries nothing by hand except the sentence "pull new requests".

## Component: the intake spec — `docs/references/deck-intake-spec.md`

Canonical in this repo (it encodes this repo's citation contract and must evolve with it).
Written fully self-contained: an agent that has never seen this repo can follow it
verbatim. Contents:

**Bundle layout** (inside the source project):

```
deck-intake/
├── HANDOFF.md      # first drop; later drops carry ANSWERS.md instead
├── SYNC.md         # M2T endpoints, recorded at first push
├── figures/        # images/plots, generation provenance noted
├── data/           # small data files backing claims (JSON/CSV/JSONL)
└── assets/         # photos, logos, misc
```

**HANDOFF.md required sections** (distilled from rlaif-vlm's `HANDOFF-deck-agent.md`):
- *Audience & occasion* — who, when, time budget.
- *The story* — the argument the deck should make, not a slide list.
- *Verified numbers table* — every claim-worthy number: value, provenance (bundle file or
  external URL), clean/caveat status, honesty caveat verbatim (the
  contaminated-0.887-vs-clean-0.7227 pattern).
- *Asset map* — each file: what it shows, how generated, which claims it can back.
- *External sources* — URL + verbatim quote for anything citeable outside the bundle
  (pre-seeds `sources.yml`).
- *Sensitivity marks* — per-file `PUBLIC` / `PERSONAL` / `HEAVY` flags; these drive the
  promotion decision on the M2T side.
- *Open calls* — decisions explicitly left to the deck side.

**Drop protocol**: every delivery, including the first, is one immutable
`intake_<YYYY-MM-DD-HHMM>/` directory (filesystem-safe, sortable). The bundle is the union
of drops; newest wins on conflicts. First drop carries `HANDOFF.md`; every subsequent drop
carries `ANSWERS.md` naming the `REQUESTS-*` file it responds to, with the same subdir
layout for new material. "What's new" = drop dirs newer than last seen.

**REQUESTS protocol**: numbered requests, each with *what / why / preferred form*. Written
by the deck agent to `docs/talks/<slug>/requests/REQUESTS-<datetime>.md` and committed
(cheap text, loop provenance). The spec gives the source agent the exact pull and push
rsync command templates (remote and same-machine forms) using the `SYNC.md` endpoints.

**Quality bar**: a checklist the source agent self-verifies before pushing (numbers
adjudicated, caveats stated, every asset mapped, sensitivity marked, no orphan claims).

## Component: landing zone & provenance

- `docs/talks/*/intake_*/` is gitignored (precedent: `docs/courses/sorbonne-m2/sources/`).
- **Promotion rule**: anything a slide claim cites or the deck embeds must either
  - (a) be **promoted** — copied outside the intake drops to a committed location
    (`docs/talks/<slug>/` or the deck's assets) after a size + sensitivity check; PERSONAL-
    flagged files are never promoted without Louis's explicit approval; or
  - (b) get a `sources.yml` entry with `verify: local-only` + `sha256` + `reason:` (heavy
    or personal artifacts). The gate verifies the checksum when the file is present locally
    and warns loudly — never silently passes — when it is absent. A checksum mismatch is a
    hard fail: the artifact changed since the claim was verified.
- `sources.yml` grows a **`file:` source type**: repo-relative path, either committed
  (promoted) or `local-only` + checksum. `scripts/verify-sources.py` is extended
  accordingly, with unit tests. This closes the rlaif-vlm gap (1 external source for 14
  slides; provenance untracked).
- `.private/` remains the home for fully confidential decks.

## Component: engine policy

- **frontend-slides is the default engine for all new decks** — standalone talks and future
  Sorbonne course editions alike.
- **Marp is plan B**: existing decks, themes, and toolchain keep building; choosing Marp
  for a new deck requires a stated reason recorded with the deck (README or manifest
  comment) — e.g. editable PPTX handouts, bulk Markdown editing across many decks.
- Any new Marp deck also carries a `sources.yml`. (Today's warn-only Marp linting is the
  loophole that made CLAUDE.md's "every deck" guarantee an overstatement; new decks close
  it, existing frozen decks are not retrofitted.)
- New `docs/references/workflow-new-deck.md` becomes THE deck-loop doc for sessions here:
  intake → frontend-slides build under `html-deck-interaction-standards.md` → critique loop
  → citation gates → REQUESTS round-trips → ship. `workflow-new-slides.md` is demoted to
  the Marp plan-B annexe. CLAUDE.md's build-systems and new-deck sections are rewritten to
  state default + plan B and point at the new workflow doc.

## Component: global surface

- New skill `~/Setup/skills/deck/SKILL.md` — the existing `skills` fanout dotfile deploys
  it to `~/.claude/skills/deck` on every machine; no `dotfiles.json` edit needed.
- Description (drafted to out-compete the `frontend-slides` plugin skill in source repos):

  > Use when Louis wants a slide deck / talk / presentation made ABOUT the current project
  > or from its results — "make a deck from this", "prepare slides for the demo", "turn
  > this into a talk". Outside ~/42/Markdowns2Teach: produce a deck-intake bundle per the
  > portable spec and rsync it there — do NOT build deck HTML here. Inside: follow the deck
  > workflow doc. Deck building and its citation gates live in ~/42/Markdowns2Teach.

- Body = a short router: read the spec at its absolute path (paste/`share-file` it for
  remote agents), rsync templates, the explicit prohibition on building deck HTML
  source-side, and the pointer to `workflow-new-deck.md` when already in this repo.
- One line in the global `~/.claude/CLAUDE.md` capability index.
- The loop itself is sequestered here: no global skill carries it, so it always runs under
  this repo's CLAUDE.md gates (Setup design's discovery-scope-matches-blast-radius rule).

## Component: citation tooling consolidation

- Delete (via `rip`) the April-frozen `scripts/cite/` mirror in its entirety —
  `validate_claim.py`, `tier_lookup.py`, `target_scope.py`, `lint_authority_map.py`,
  `__init__.py`, and `tests/`. Test coverage migrates to
  `~/Setup/skills/cite/scripts/tests/`, merged with what already exists there (follow-up
  task in ~/Setup).
- `make lint-authority-map` calls the deployed
  `~/.claude/skills/cite/scripts/lint_authority_map.py`, passing this repo's map paths as
  arguments (add CLI args in ~/Setup if the defaults are not yet parameterized). `make
  check` thereby requires dotfiles deployed — consistent with everything else it assumes
  (node, Chrome, uv).
- `docs/references/authority-map.{md,yaml}` is trimmed from a byte-identical duplicate of
  the global base to a **true overlay** (repo-specific entries only). `cite-correct`
  promotions default to the global base.
- `verify-sources.py` and `check-citation-links.py` stay **repo-canonical**: they enforce
  the deck-artifact contract (registry, verbatim quotes on the delivered artifact,
  link-shape) that has no global counterpart. Cross-reference comments in both codebases
  acknowledge the shared verbatim-quote contract so future sessions don't re-unify or
  re-fork them blindly.

## Error handling

- rsync pull failure → the deck agent reports and stops; it never guesses at bundle state.
- Stale-bundle detection is structural: drops are append-only datetime dirs.
- `verify: local-only` absence → loud warning listing slide + artifact; checksum mismatch →
  hard fail.
- Skill collision: the `deck` skill description claims "deck about a project" intent
  source-side; its body prohibits building HTML there. Inside this repo, frontend-slides
  remains the rendering engine invoked by the loop.
- PERSONAL-flagged artifacts: never committed, never promoted without explicit approval.

## Verification

- Unit tests for the `verify-sources.py` extensions (`file:` type, `local-only` + sha256)
  at `scripts/tests/`.
- `make check` stays the umbrella gate; `make export-pdf-<deck>` keeps the live gate.
- Acceptance exercise: retrofit rlaif-vlm's provenance to the new contract — move
  `docs/talks/rlaif-vlm/examples/` into an `intake_*` drop, register cited artifacts as
  `file:` sources (promoted or local-only), and re-run the gates. If the machinery can't
  express the deck that inspired it, the design is wrong.

## Explicitly not doing (YAGNI)

- No `autodeck` CLI front door — the Setup session ruled the deck "a product question, not
  a missing front door", and nothing here needs a binary.
- No pipeline-library extraction, no two-way sync, no automated deck→source channel (Louis
  is the courier by design, and the courier's job is one sentence).
- No migration of existing Marp decks; no retrofit of frozen decks' citation gaps.

## Implementation surface (input to the plan)

In this repo:
1. `docs/references/deck-intake-spec.md` — new, portable, self-contained.
2. `docs/references/workflow-new-deck.md` — new; demote `workflow-new-slides.md` to Marp
   annexe.
3. CLAUDE.md — engine policy, new-deck pointer, intake/landing-zone conventions.
4. `.gitignore` — `docs/talks/*/intake_*/`.
5. `scripts/verify-sources.py` — `file:` sources, `local-only` + sha256; tests.
6. Makefile — `lint-authority-map` → deployed skill path.
7. `rip` `scripts/cite/`; trim `docs/references/authority-map.{md,yaml}` to a true overlay.
8. Acceptance: rlaif-vlm provenance retrofit.

In ~/Setup (follow-up session there):
9. `skills/deck/SKILL.md` + fanout redeploy.
10. Global CLAUDE.md capability-index line.
11. `lint_authority_map.py` CLI args (if needed); merge migrated tests; `cite-correct`
    promotion default documented as the global base.
