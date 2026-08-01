# Deck capability: handoff from the Setup capability-surface session

Status: resolved (noted 2026-08-01). The design session ran and the capability
shipped: a global `deck` skill routes any project to an intake bundle, and this
repo's CLAUDE.md section "Deck capability — cross-project intake" plus
`docs/references/deck-intake-spec.md` are now the authoritative answer to the
open questions below. Kept as the record of what seeded that design.

Original status: handoff, 2026-07-09. Written from a `~/Setup` session that was
designing cross-session capability discovery (secrets, domains, ports, deck).
The deck was deliberately scoped out of that spec: Louis's call, because the
design question is a product question and the context to answer it lives here,
not in Setup. This file carries over what that session verified and what it
could not know, so a session in this repo can design the deck capability
without re-deriving the cross-repo facts.

**Warning to the reading session: the Setup-side view of this repo was stale.**
Its explorer summarized Markdowns2Teach as "a legacy Marp pipeline, declining."
The repo's own CLAUDE.md shows much more: citation gates
(`check-citation-links.py`, `verify-sources.py`, per-deck `sources.yml`
registries), a hardened `make export-pdf-<deck>` pipeline, fixed-stage HTML
decks, and the repo as home for all teaching and writing. Design from the repo,
not from any summary of it, including this one.

## The question, in Louis's framing

- Deck building is cross-functional, but **the source documents live in
  whichever project the deck is about**, not here. Unsure how sources should
  flow in.
- The process is **iterative**: read the deck, critique, ask for more data to
  be added, rebuild, loop. It is not a one-shot build command.
- Two build engines exist: **frontend-slides** (the plugin skill, extended
  with a lot of added machinery, ascendant) and the **legacy Marp pipeline**
  here (used less and less).
- A lot of the real work is adjacent: **citation source verification and
  extension** (the `/cite` family) and **visuals** (`/visual`).
- Louis explicitly did not want this designed from Setup: "handoff as a doc I
  can rework in ~/42/Markdowns2Teach so it's done seriously from where the
  context is."

## Cross-repo facts verified in the Setup session (reuse, don't re-derive)

- **Only two surfaces are global in every Claude session:** the user-level
  `~/.claude/CLAUDE.md`, and the name+description frontmatter of skills
  deployed in `~/.claude/skills/`. Auto-memory is per-project and cannot cross
  repo boundaries. This repo has no deployed skill, so nothing outside this
  directory knows deck-building exists or where it happens.
- **direnv does not run in agent Bash shells.** Verified directly: an agent
  shell that `cd`s into a repo keeps the launch directory's direnv state, so
  `cd <repo> && make ...` invocations run without the repo's `.envrc` and fail
  half-configured. Any cross-project entry point must not depend on `cd` +
  direnv. The Setup design's answer is one cwd-agnostic front door per
  capability, on PATH, that `cd`s internally; `send-email` and `pull-uploads`
  already prove the pattern.
- **Related Setup docs:** `~/Setup/docs/plans/
  2026-07-09-cross-functional-capabilities-design.md` (partially superseded)
  and `2026-07-09-secrets-methodology-handoff.md` (the live one). Whatever
  front-door and secrets pattern lands there is what a deck entry point should
  ride, not a parallel invention.
- **This repo's `.envrc` holds 7 plaintext secret-shaped exports** (census
  2026-07-09): `CLOUDFLARE_API_TOKEN`, `FC_API_KEY`, `GEMINI_API_KEY`,
  `HF_TOKEN`, `OPENROUTER_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TV_API_KEY`. In
  scope for the secrets migration being designed in Setup, not for the deck
  design; noted so nobody is surprised.

## Open design questions for the session here

1. **Where does a deck live, and how do sources flow in?** Sources belong to
   the originating project; this repo owns standards, index, and publish.
   Options sketched from Setup, WITHOUT this repo's context; treat them as
   strawmen to react against, not a menu:
   a distributable build front door (`autodeck build --src <docs> --out ...`)
   so decks build in the source project; copying/symlinking sources into
   `slides/<name>/` here (drift risk); extracting the pipeline as a library;
   or keeping decks here and treating source flow as part of the iterative
   loop instead of a file-layout problem.
2. **What is the iterative loop, concretely?** Read, critique, request more
   data, rebuild. It needs the source project's knowledge AND this repo's
   citation gates at the same time. Is it a skill? Where does it run from?
   What does "ask for more data" resolve to when the data lives in another
   repo's session context?
3. **Engine consolidation.** What still depends on Marp, what is already on
   fixed-stage HTML/frontend-slides, and what is the retirement story for the
   declining path? A capability with two engines and no stated default is a
   footgun for every future session.
4. **Minimal global discoverability.** What one-line skill description should
   exist globally so a session in any project knows deck-building exists and
   is done HERE, under THIS repo's citation rules, without dragging the whole
   loop cross-repo? (Counterpart of the Setup design's discovery-scope-
   matches-blast-radius rule.)
5. **Single source of truth for citation tooling.** `verify-sources.py` here
   shares the `/cite` contract (`validate_claim.py`). Two implementations of
   one contract will drift. Decide which one is canonical and how the other
   consumes it.

## How to run the follow-up

Start a session in this repo. Read this repo's CLAUDE.md first, then this
file. Brainstorm before plan mode. The Setup session's strawmen in question 1
were formed without local context; discard freely.
