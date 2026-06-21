# `/cite` skill family — design spec

## Context

Louis needs a systematic way to audit slide decks (and eventually any markdown doc) for unsourced claims, research them, and apply verified citations back to the source file.

The existing `workflow-citation-audit.md` + `scripts/check-citations.sh` give a binary lint (does a slide with `$`/`%` have a `<small>Sources` line?) and a manual workflow. That's not enough. Louis has been burned multiple times by:
- URLs that point to broad pages not containing the claim
- Sources that look authoritative on the surface but don't actually support the specific number
- "Estimations sectorielles" / "Estimations développeurs" — placeholder strings masquerading as citations
- Stale stats that are still technically sourceable but no longer represent current reality

This skill family enforces a **strict verification contract**: for every claim, a structured record with the exact quote from the source, the surrounding paragraph, the section heading it lives under, the publisher, the dates, and the alignment justification. That's the core innovation.

Today scope is slides; design should not couple too hard to slide format so the skill can extend to plain markdown later.

---

## 1. Architecture

Three phase-skills chained by a meta-skill:

```
┌─────────┐     ┌─────────────┐     ┌────────────────┐     ┌──────────────┐
│  /cite  │────▶│ /cite-scan  │────▶│ /cite-research │────▶│ /cite-apply  │
│  (orch) │     │  (phase 1)  │     │   (phase 2)    │     │  (phase 3)   │
└─────────┘     └─────────────┘     └────────────────┘     └──────────────┘
                      │                      │                     │
               extract claims         parallel subagents     patch .md file
               build authority        fetch sources +        + promote
               map (pre-research)     extract quotes         authorities
```

Each phase-skill is independently invocable. `/cite` runs them in sequence with review gates.

The design mirrors Louis's existing `research → research-deep → research-report` pipeline so the mental model transfers.

---

## 2. Artifact layout

```
docs/citation-audit/<slug>/          # gitignored by default
├── outline.md                       # human review gate — summary + flagged items
├── authority-map.md                 # per-run overlay (inherits global baseline)
├── caveats.md                       # issues / tool failures / improvement notes
├── claims/
│   ├── claim-01.yaml                # one file per claim, parallel-write safe
│   └── ...
└── apply-preview.diff               # /cite-apply writes this before touching source

docs/references/authority-map.md     # NEW — global baseline, tracked in git
docs/references/cite-skill-backlog.md # NEW — accumulated caveats / improvement ideas
```

`<slug>` = file path dashified (e.g., `session-05-A-regulation-ethique`).

The `docs/references/authority-map.md` file is the **concrete roster** of named publishers mapped to §6.2 tiers. Slide-creation-standards §6.2 stays as the tier *definitions*; this new file is the populated roster. Extends over time via the promotion gate in `/cite-apply`.

The `docs/references/cite-skill-backlog.md` file accumulates persistent issues Louis wants to address in future versions of the skill (tool gaps, detection misses, etc.). Fed by `caveats.md` from each run via the end-of-run report.

---

## 3. Claim schema (`claims/claim-NN.yaml`)

```yaml
id: claim-03
location:
  file: slides/session-05/A-regulation-ethique.md
  slide: "07 — Flash Crash 2010"
  line: 142
claim:
  text: "Le Flash Crash du 6 mai 2010 a effacé $1T en 36 minutes"
  type: historical-event         # per §6.1: number | named-stat | company-fact | benchmark | pricing | forecast | historical-event
  has_existing_source: false
proposed_source:
  url: https://www.sec.gov/news/studies/2010/marketevents-report.pdf
  url_domain: sec.gov
  publisher_org: "SEC/CFTC"
  author: "Staff of CFTC and SEC"
  publication_date: 2010-09-30
  accessed_date: 2026-04-12
  authority_tier: 1              # §6.2 tier
  authority_name: "SEC/CFTC Joint Report"
  recency_verdict: historical-event    # fresh | recent | stale | historical-event
  quote: "The markets lost approximately $1 trillion..."
  surrounding_paragraph: "On May 6, 2010, the prices of many..."
  section_heading: "Executive Summary"
  alignment_justification: "Quote directly states $1T loss; 36-min window in Section II"
  confidence: high               # high | medium | low
status: auto-approved            # auto-approved | flagged-low-reputation | flagged-unsourceable
                                 # | flagged-stale-stat | approved | rejected | needs-rework | pending
flag_reason: null                # set when status starts with "flagged-"
proposed_action: add-citation    # add-citation | update-claim-value | soften-language | none
proposed_claim_update: null      # new text if proposed_action == update-claim-value
```

All `proposed_source` fields except `quote` are derived from the extracted page content — `authority_tier` from `publisher_org` via the authority map, `recency_verdict` from `publication_date`.

---

## 4. `outline.md` — the review gate

Human-readable index of all claims. Louis edits `claims/*.yaml` to mark decisions; `outline.md` is the entry point that surfaces what needs attention.

```markdown
# Citation audit — slides/session-05/A-regulation-ethique.md

**Status**: research complete · 2026-04-12
**Summary**: 27 claims · 21 auto-approved · 4 flagged · 2 unsourceable

## Flagged — review required

### claim-07 · flagged-low-reputation · slide 12
- **Claim**: "Amazon a supprimé son outil de recrutement IA en 2018"
- **Source**: Reuters — tier 4 (actually auto-approved; flagging is for tier 5+)
- _edit `claims/claim-07.yaml` → `status: approved|rejected|needs-rework`_

### claim-14 · flagged-stale-stat · slide 08
- **Claim**: "Le marché atteint $2 527 Mds en 2026"
- **Source**: Gartner, March 2024 — tier 3
- **Proposed update**: $2 527 Mds → $2 890 Mds (Gartner, Feb 2026)
- _`approved` = accept update · `rejected` = keep original · `needs-rework` = find different source_

## Auto-approved (audit trail)
- claim-01 · slide 02 · Stanford HAI AI Index (tier 3)
- claim-02 · slide 02 · EUR-Lex (tier 1)
- ... (collapsed)

## Unsourceable — manual decision required
- claim-22 · slide 18: "90% of AI projects fail" — no primary source found after 3 search passes
  _options: soften ("la plupart des projets IA") · remove · provide your own URL_
```

`/cite-apply` only processes rows where `status ∈ {approved, auto-approved}`.

---

## 5. Authority map

### Global baseline — `docs/references/authority-map.md`

Extends §6.2 with a concrete roster. Initial seed (derived from existing research pipeline outputs):

```markdown
## Tier 1 — Primary (company IR, SEC filings, gov)
- SEC.gov (filings, enforcement actions)
- Company IR pages (investor.*, */news, */pricing)
- EUR-Lex (EU legislation)
- European Parliament

## Tier 2 — Peer-reviewed
- arXiv (with acceptance venue noted when available)
- NeurIPS, ICML, ICLR proceedings
- Nature, Science

## Tier 3 — Tier-1 research
- Gartner, McKinsey, IDC, Stanford HAI, OECD
- Epoch AI (compute/training trends)
- Our World in Data
- Domain-specific: SemiAnalysis (AI hardware), CEPS (EU regulation)

## Tier 4 — Tier-1 press
- Bloomberg, Reuters, CNBC, Financial Times, NYT, WSJ, The Information

## Tier 5 — Tier-2 press (flagged, needs review)
- TechCrunch, The Verge, Ars Technica, Wired

## Tier 6 — Startup databases (flagged, needs review)
- Crunchbase, Sacra, PitchBook
```

### Per-run overlay — `docs/citation-audit/<slug>/authority-map.md`

Inherits from global, adds domain-specific entries `/cite-scan` surfaced for THIS file's topics. Promotion gate at `/cite-apply` asks per-entry: "Promote to global?"

---

## 6. Caveats and self-improvement loop

`docs/citation-audit/<slug>/caveats.md` accumulates issues during the run. Three categories:

### Tool-level
- Tavily rate limit hit at claim-N → fell back to WebSearch; fallback may reduce quality
- Tavily Extract returned empty/timeout on URL → retry via WebFetch
- Wayback Machine unavailable for 404 recovery

### Research-level
- Claim-N: multiple authoritative sources disagree — picked most recent, worth a second look
- Claim-N: new publisher "X" surfaced repeatedly but not in authority map — promotion candidate
- Claim-N: publication_date not determinable from page — recency verdict is best-guess
- Claim-N: quote alignment confidence medium — human should verify

### Detection-level
- Lines L1–L2 possibly contain claims but classifier was unsure (logged, not extracted)
- Slide N has no extractable claims but reads like a data slide — possible false negative

At `/cite-apply` end, caveats are summarized to Louis with a prompt: "Roll any of these into the persistent backlog at `docs/references/cite-skill-backlog.md`?" — per-item yes/no. Selected items get appended with date + context so future skill revisions have a target list.

This is how the system gets better with time — each run's surprises become tomorrow's improvement targets.

---

## 7. Behavior per phase

### `/cite-scan <file>`

1. Read file. LLM classifies every line per §6.1 rubric: needs-a-source? If yes, extract it as a claim (id, location, text, type, `has_existing_source`).
2. Identify topic domains from file content (e.g., "AI regulation", "AI markets", "AI hardware").
3. Pre-research authority map: 2–3 Tavily searches ("authoritative publishers for X") → write `authority-map.md` (global seed + domain overlay).
4. Write empty `claims/claim-NN.yaml` stubs (location + claim text filled, source fields empty, `status: pending`) and skeleton `outline.md`.
5. Log any classification uncertainties to `caveats.md`.
6. Stop. Louis reviews extracted-claims list before the expensive research phase runs.

### `/cite-research`

1. Read `outline.md` + all pending `claims/*.yaml`.
2. Spawn up to 5 concurrent subagents, one claim per agent. Each agent:
   - Searches per §6.5 protocol, honoring authority map
   - Tavily Extract the best candidate page
   - Fills schema fields (quote, surrounding paragraph, section heading, publisher, dates, alignment justification, confidence)
   - Derives `authority_tier` from `publisher_org` via authority map
   - Derives `recency_verdict` from `publication_date` (fresh < 6mo, recent 6–12mo, stale > 12mo, historical-event for events before 2020)
   - Assigns `status`:
     - `auto-approved` if tier ∈ {1,2,3,4} and recency_verdict ∈ {fresh, recent, historical-event}
     - `flagged-low-reputation` if tier ≥ 5
     - `flagged-stale-stat` if an authoritative source contains a newer datapoint (by publication date) differing by >10%
     - `flagged-unsourceable` if no qualifying source found after 3 different search queries (varying site: filters, date windows, synonyms)
   - When multiple sources disagree on a number, pick by (higher tier, then more recent `publication_date`); log the runner-up to `caveats.md`
   - Logs tool failures, missing dates, disagreeing sources to `caveats.md`
3. Main skill: post-research authority refinement — newly-surfaced strong publishers get added to per-run overlay with a proposed tier.
4. Update `outline.md` with categorized sections.
5. Budget: ~2 Tavily credits/claim × 30 claims ≈ 60 credits per deck. Tavily monthly budget 1000 ⇒ ~16 files/month.

### `/cite-apply`

1. Read all `claims/*.yaml`. Process only `status ∈ {approved, auto-approved}`.
2. Build patch:
   - Insert `[N]` markers at each claim location per §6.4
   - `[N]` numbering restarts per slide (matches §6.4 convention); claims on the same slide sharing a URL share the same `[N]`
   - Rewrite claim text where `proposed_action == update-claim-value` AND `status == approved`
   - Append one `<small>Sources : [1] [Authority](url) · ... </small>` line per slide with citations
3. Detect hash drift: if source file was edited since `/cite-scan` ran, abort with "re-run `/cite-scan` — source changed".
4. Write `apply-preview.diff`. Show diff to Louis. Confirm y/n.
5. Apply edits → run `make check` + `make check-citations` + `make html`. Report results.
6. Authority promotion gate: for each new entry in per-run overlay, ask "promote to `docs/references/authority-map.md`?" — per-entry yes/no.
7. Caveats report: summarize `caveats.md` to Louis, ask "roll any into `docs/references/cite-skill-backlog.md`?" — per-item yes/no.

### `/cite <file>`

Orchestrator. Sequences the three phases with explicit review gates:

```
Phase 1 (scan) complete → shows extracted-claims summary → "Proceed to research? [y/n]"
Phase 2 (research) complete → shows outline.md summary → "Review flagged items in <path>, then reply 'go' to apply"
Phase 3 (apply) → shows diff → "Apply? [y/n]"
```

If Louis invoked a phase-skill manually first, `/cite <file>` detects existing state and resumes from the appropriate phase.

---

## 8. Error handling

| Failure | Response |
|---------|----------|
| Tavily rate limit | Fall back to WebSearch + WebFetch (unlimited), log to `caveats.md` |
| Tavily Extract empty/timeout | Retry once with WebFetch; if still fails, flag-unsourceable + log |
| URL returns 404 during extract | Retry via Wayback Machine (oldest capture matching pub date); if still fails, flag |
| Source .md edited between scan and apply | Content-hash check aborts `/cite-apply` with "re-run `/cite-scan`" |
| Quote extraction ambiguous | Set `confidence: medium` or `low`, log to caveats.md |
| Publication date not determinable | Set `publication_date: unknown`, `recency_verdict: unknown`, flag-low-reputation |
| `make check` fails after apply | Report, do not auto-retry. Louis fixes overflow manually. |

---

## 9. Parameters (defaults)

| Parameter | Default | Rationale |
|-----------|---------|-----------|
| Concurrency cap | 5 | Matches `research-deep` pattern |
| Stale-stat threshold | 10% | Flags meaningful drift, tolerates rounding |
| Flag tier | 5+ | Per Louis's pick; Tier 4 press (Bloomberg etc.) auto-approved |
| Tavily budget per file | ~60 credits | Works within 1000/month for ~16 files |
| Max search variations | 3 | Per claim before giving up and flagging unsourceable |

---

## 10. Out of scope for v1 (YAGNI)

- **Verify-existing mode**: Louis's default pick was unsourced-only. Claims with `has_existing_source: true` are skipped in v1. Easy to add later as `--verify-existing` flag that re-verifies each existing citation's URL still contains the claim.
- **Non-markdown inputs**: `.md` only. PDF/HTML sources are future work.
- **BibTeX / separate bibliography file**: slide format uses inline `[N]` + `<small>Sources</small>`. One format suffices.
- **Auto-retry on `make check` failure**: too surgical; human fixes overflow.
- **Batch `/cite` across multiple files**: run one file at a time in v1. Parallel cross-file orchestration is future work.

---

## 11. Critical files / directories

New skill directories (one per phase-skill + meta):
- `~/.claude/skills/cite/SKILL.md`
- `~/.claude/skills/cite-scan/SKILL.md`
- `~/.claude/skills/cite-research/SKILL.md`
- `~/.claude/skills/cite-apply/SKILL.md`

New global reference files (tracked in git):
- `docs/references/authority-map.md` — baseline roster
- `docs/references/cite-skill-backlog.md` — improvement ideas

Reads from:
- `docs/references/slide-creation-standards.md` §6 — citation rules (tier definitions, classification rubric, §6.4 format, §6.5 research protocol)
- Target .md file — claims extraction

Writes to:
- `docs/citation-audit/<slug>/` — gitignored per-run bundle
- Target .md file — only at `/cite-apply` time, only after diff approval
- Global authority-map.md and backlog.md — only via promotion gates

`.gitignore` addition: `docs/citation-audit/`.

---

## 12. Verification

End-to-end test plan:

1. Pick one file with known unsourced claims from the existing P1–P9 backlog (e.g., `session-02/A-prompt-au-produit.md` or `session-04/A-ecosysteme-ia.md`).
2. Run `/cite-scan <file>`. Verify:
   - `claims/*.yaml` stubs created with correct locations
   - `outline.md` skeleton present with expected claim count
   - `authority-map.md` per-run overlay lists domain-relevant sources
3. Run `/cite-research`. Verify:
   - Every claim has `quote`, `surrounding_paragraph`, `section_heading`, `publisher_org`, dates
   - `status` correctly distinguishes auto-approved vs. flagged vs. unsourceable
   - `caveats.md` populated with any tool/research issues
4. Manually edit one flagged yaml to `status: approved`, one to `status: rejected`.
5. Run `/cite-apply`. Verify:
   - `apply-preview.diff` matches expectations (rejected claim untouched; approved claims get `[N]` + sources footer)
   - After apply: `make check` passes, `make check-citations` passes, `make html` builds
   - Authority promotion gate asks per-entry
   - Caveats report surfaces at end
6. Re-run `/cite-scan` on the same file — verify the now-sourced claims are not re-extracted (they should set `has_existing_source: true` and be skipped in v1).
7. Hash-drift test: run `/cite-scan`, manually edit the .md file, try `/cite-apply` — verify it aborts.
