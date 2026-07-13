<!-- ABOUTME: Portable spec for deck-intake bundles: what a source-side agent produces so a
     deck can be built in Markdowns2Teach under its citation gates. Self-contained. -->

# Deck-intake spec (v1 — 2026-07-13)

**You are the source-side agent**: you work in the project a deck/talk will be made ABOUT.
Your deliverable is an **intake bundle**, not slides. Deck building, citation verification,
and publishing happen in another repo (`~/42/Markdowns2Teach` on Louis's machine — "the deck
repo") by another agent ("the deck agent"). This document is the complete contract between
you and them: you need nothing else from the deck repo to comply.

**Why quality matters:** the deck agent can only claim what you can back. Every number on a
slide must trace to an artifact or URL you provide; anything unbacked gets cut or comes back
to you as a request. A tight bundle means a deck built in one pass.

## 1. Bundle layout

Create `deck-intake/` at your project root:

```
deck-intake/
├── HANDOFF.md      # the core deliverable (first drop) — see §2
├── SYNC.md         # delivery endpoints, written at first push — see §5
├── figures/        # plots/screenshots/diagrams; each needs an asset-map row
├── data/           # small machine-readable files backing claims (JSON/CSV/JSONL)
└── assets/         # photos, logos, misc visuals
```

Omit empty subdirs. Filenames: kebab-case or snake_case, NO spaces.

## 2. HANDOFF.md — required sections

### Audience & occasion
Who is in the room, when, expected talk length, stakes.

### The story
The ARGUMENT the deck should make — 5–15 sentences of narrative arc (hook → tension →
resolution → takeaway). Not a slide list; the deck agent owns slide design.

### Verified numbers
A table of every number a slide might state. **No number outside this table may appear on a
slide.** Columns:

| # | claim | value | provenance | status | caveat |
|---|-------|-------|------------|--------|--------|
| N1 | final win-rate vs baseline | 0.7227 | data/eval_clean.json | clean | measured on the decontaminated split |
| N2 | first-run win-rate | 0.887 | data/eval_run1.json | CAVEAT | eval split later found contaminated — never show without this caveat |

- `provenance` = a bundle file (relative path) or an exact external URL.
- `status` is `clean` or `CAVEAT`. A CAVEAT row MUST carry its honesty caveat verbatim; the
  deck agent will print the caveat next to the number, or drop the number.

### Asset map
One row per file in the bundle. **A file with no row does not exist for the deck agent.**

| file | what it shows | how it was generated | claims it can back | sensitivity |
|------|---------------|----------------------|--------------------|-------------|
| figures/win_rate.png | win-rate by training step | scripts/plot_eval.py on data/eval_clean.json | N1 | PUBLIC |

### External sources
For every claim backed by the open web: the exact deep URL (never a bare domain, never a
section/index page) plus a VERBATIM quote from that page proving the claim. These pre-seed
the deck's citation registry, which is machine-verified character-by-character — a
paraphrase will fail the gate.

### Open calls
Decisions you explicitly leave to the deck agent (tone, what to cut first, which figure
variant), one bullet each.

## 3. Sensitivity marks

Mark every file with the STRICTEST applicable:

- **PUBLIC** — may be committed to the deck repo and shown on a slide.
- **PERSONAL** — contains personal/confidential information. Never committed deck-side,
  never shown without Louis's explicit approval. Prefer providing a redacted derivative.
- **HEAVY** — too big for git (rule of thumb: >2 MB single file or >1000 files). Stays in
  gitignored drops; the deck side cites it by checksum.

## 4. Drop protocol

- Every delivery is ONE new directory on the deck side:
  `docs/talks/<slug>/intake_<YYYY-MM-DD-HHMM>/` (your rsync target, their tree).
- A drop is **immutable** once pushed. Corrections and additions are a NEW drop — never
  edit or re-push into an existing one.
- The first drop carries `HANDOFF.md`. Every later drop carries `ANSWERS.md` instead (§6),
  with the same subdir layout for any new material.
- The deck agent reads the union of all drops; on same-path conflicts the newest drop wins.

## 5. SYNC.md + delivery commands

`<slug>` = short kebab-case deck name agreed with Louis (e.g. `rlaif-vlm`).
At FIRST push, write `deck-intake/SYNC.md`:

```
# SYNC — deck delivery endpoints
slug: <slug>
deck_host: <ssh host alias, or "local" if same machine>
talk_dir: ~/42/Markdowns2Teach/docs/talks/<slug>
pushed:
  - intake_<YYYY-MM-DD-HHMM>    # append one line per drop
```

Push a drop (remote; same machine = drop the `<deck_host>:` prefix):

```bash
rsync -av deck-intake/ <deck_host>:~/42/Markdowns2Teach/docs/talks/<slug>/intake_$(date +%Y-%m-%d-%H%M)/
```

Pull the talk dir (to read requests / see deck state — you can always pull, the deck side
never pushes to you):

```bash
rsync -av <deck_host>:~/42/Markdowns2Teach/docs/talks/<slug>/ ./deck-talk-mirror/
```

## 6. Requests round-trip

When the deck agent needs more, it writes numbered requests to
`docs/talks/<slug>/requests/REQUESTS-<datetime>.md` on the deck side. When Louis tells you
**"pull new requests"**:

1. Pull the talk dir (§5); read every `requests/REQUESTS-*.md` newer than your last drop.
2. Do the work — gather the data, produce the figure, answer the question, rerun the
   experiment. New material follows §2 quality: numbers-table rows, asset-map rows,
   sensitivity marks.
3. Write `ANSWERS.md`: name the REQUESTS file(s) answered at the top, then one section per
   request number stating what you provide, where it is in this drop, or why it cannot be
   provided.
4. Push as a NEW drop (§4/§5) and append it to `SYNC.md`'s `pushed:` list.

## 7. Quality checklist (self-verify before EVERY push)

- [ ] Every number a slide could state is in Verified numbers, with provenance
- [ ] Every CAVEAT number carries its honesty caveat verbatim
- [ ] Every file has an asset-map row: generation provenance + sensitivity mark
- [ ] Every external claim has an exact deep URL + verbatim quote (no bare domains)
- [ ] No spaces in filenames; no secrets or credentials anywhere in the bundle
- [ ] The story section argues something — a stranger could pitch the talk from it alone
- [ ] SYNC.md created (first push) or its `pushed:` list appended (later pushes)
