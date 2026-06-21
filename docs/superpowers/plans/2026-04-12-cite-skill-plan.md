# `/cite` Skill Family Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a four-skill family (`/cite`, `/cite-scan`, `/cite-research`, `/cite-apply`) that automates the citation audit workflow with a strict direct-quote verification contract and a human-in-the-loop review gate.

**Architecture:** Four Claude Code skills under `~/.claude/skills/`. Phase skills are chained by a meta-skill. State lives in per-file bundles at `docs/citation-audit/<slug>/` (gitignored) with one YAML per claim. Global references (`authority-map.md`, `cite-skill-backlog.md`) live under `docs/references/` and accumulate over time.

**Tech Stack:** Claude Code Skill framework (SKILL.md + frontmatter), Tavily Search + Extract (with WebSearch/WebFetch fallback), YAML for claim records, Markdown for human-facing artifacts. No runtime code — skills are declarative instructions to Claude.

**Spec:** See `docs/superpowers/specs/2026-04-12-cite-skill-design.md` for the approved design and rationale.

---

## File Structure

| Path | Purpose | Task |
|------|---------|------|
| `.gitignore` | Add `docs/citation-audit/` | 1 |
| `docs/references/test-fixtures/cite-fixture.md` | Minimal slide file with 3 known unsourced claims, used for integration tests | 2 |
| `docs/references/authority-map.md` | Global concrete roster of publishers mapped to §6.2 tiers | 3 |
| `docs/references/cite-skill-backlog.md` | Persistent improvement backlog fed by `caveats.md` | 4 |
| `~/.claude/skills/cite-scan/SKILL.md` | Phase 1: extract claims + build authority overlay | 5 |
| `~/.claude/skills/cite-research/SKILL.md` | Phase 2: parallel subagents fetch sources + quotes | 7 |
| `~/.claude/skills/cite-apply/SKILL.md` | Phase 3: patch source file + promotion gates | 9 |
| `~/.claude/skills/cite/SKILL.md` | Meta-skill: orchestrates phases with review gates | 11 |
| `docs/references/workflow-citation-audit.md` | Cross-reference the new skill | 13 |
| `CLAUDE.md` | Mention skill in project conventions | 14 |

Each SKILL.md is ~200–400 lines of instructions — they are the "code" here.

---

## Task 1: Add `docs/citation-audit/` to `.gitignore`

**Files:**
- Modify: `/home/ezalos/42/Markdowns2Teach/.gitignore`

- [ ] **Step 1: Read current .gitignore**

Run: `cat /home/ezalos/42/Markdowns2Teach/.gitignore`
Note: verify the end of the file to append cleanly.

- [ ] **Step 2: Append citation-audit entry**

Append this block at the end of `.gitignore`:

```
# Per-run citation audit bundles (kept local, not versioned)
docs/citation-audit/
```

- [ ] **Step 3: Verify**

Run: `cd /home/ezalos/42/Markdowns2Teach && git check-ignore -v docs/citation-audit/foo/outline.md`
Expected output: `.gitignore:<line>:docs/citation-audit/  docs/citation-audit/foo/outline.md`

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add .gitignore
git commit -m "chore: gitignore docs/citation-audit/ for per-run audit bundles"
```

---

## Task 2: Create test fixture with known unsourced claims

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/docs/references/test-fixtures/cite-fixture.md`

- [ ] **Step 1: Create fixture directory**

Run: `mkdir -p /home/ezalos/42/Markdowns2Teach/docs/references/test-fixtures`

- [ ] **Step 2: Write fixture file**

Write this exact content to `docs/references/test-fixtures/cite-fixture.md`:

```markdown
---
marp: true
theme: sorbonne
paginate: true
header: "Test Fixture"
footer: "Fixture for /cite skill testing"
---

<!-- ABOUTME: Minimal 3-slide test fixture for the /cite skill family. -->
<!-- ABOUTME: Contains exactly 3 unsourced claims with known public sources for integration testing. -->

<!-- _class: title -->
<!-- _paginate: skip -->

# Cite Skill Test Fixture

---

# 01 — Historical event

- Le Flash Crash du 6 mai 2010 a effacé environ $1T de valeur en 36 minutes.
- L'indice Dow Jones a chuté d'environ 9% en quelques minutes.

---

# 02 — Regulation

- L'EU AI Act a été formellement adopté en mars 2024.
- Les systèmes IA à risque inacceptable sont interdits sous peine de **35 M€** d'amende.

---

# 03 — Company fact

- Anthropic a été fondée en 2021 par d'anciens membres d'OpenAI.
```

Known sources for each claim (for test verification):
- claim 1 (Flash Crash $1T / 36 min): SEC/CFTC Joint Report 2010-09-30 (tier 1, historical)
- claim 2 (Dow -9%): same report or Bloomberg/Reuters archive (tier 1 or 4)
- claim 3 (AI Act adopted March 2024): EUR-Lex / European Parliament press release (tier 1)
- claim 4 (€35M fine): EU AI Act Article 99 official text (tier 1)
- claim 5 (Anthropic founded 2021): Anthropic "About" page or Wikipedia-linked IR announcements (tier 1 or lower)

- [ ] **Step 3: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/test-fixtures/cite-fixture.md
git commit -m "test: add minimal fixture for /cite skill integration tests"
```

---

## Task 3: Write global authority-map.md baseline

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/docs/references/authority-map.md`

- [ ] **Step 1: Write authority-map.md**

Write this exact content:

````markdown
# Authority Map — concrete publisher roster

<!-- ABOUTME: Global baseline roster of named publishers mapped to slide-creation-standards.md §6.2 tiers. -->
<!-- ABOUTME: Extended per-run by /cite-scan and promoted globally via /cite-apply promotion gates. -->

This file lists **which publishers count at which tier** for citation purposes.
Tier *definitions* live in `slide-creation-standards.md` §6.2; this file is the
populated *roster*. The `/cite` skill family reads this to assign
`authority_tier` to discovered sources and flag low-reputation ones.

Grow this file by promoting per-run overlays (see `/cite-apply` promotion gate).

---

## Tier 1 — Primary sources (company IR, SEC filings, government)

- **SEC.gov** — US Securities and Exchange Commission (filings, enforcement actions, joint reports with CFTC)
- **CFTC.gov** — US Commodity Futures Trading Commission
- **EUR-Lex** (`eur-lex.europa.eu`) — EU legal texts, including the AI Act
- **European Parliament** (`europarl.europa.eu`) — press releases, committee reports
- **European Commission** (`ec.europa.eu`, `digital-strategy.ec.europa.eu`) — official communications
- **Company investor relations** — any URL matching `investor.*`, `ir.*`, or `<domain>/investors`
- **Company official news pages** — `anthropic.com/news`, `openai.com/index/*`, `mistral.ai/news`, etc.
- **Company pricing pages** — `openai.com/pricing`, `anthropic.com/pricing`, `aws.amazon.com/*/pricing`
- **Government statistics offices** — INSEE (FR), Eurostat (EU), BLS (US), ONS (UK)

## Tier 2 — Peer-reviewed academic

- **arXiv** (`arxiv.org`) — preprints (note acceptance venue in quote when available)
- **NeurIPS / ICML / ICLR / EMNLP / ACL** — ML conference proceedings
- **Nature**, **Science** — journals
- **IEEE Xplore**, **ACM Digital Library** — engineering/CS journals
- **The Lancet**, **NEJM** — medical journals (if ever relevant)

## Tier 3 — Tier-1 research firms and trackers

- **Gartner** (`gartner.com`) — market forecasts, Magic Quadrants
- **McKinsey** (`mckinsey.com`, McKinsey Global Institute)
- **Deloitte Insights** (`deloitte.com/insights`)
- **IDC** (`idc.com`)
- **Forrester** (`forrester.com`)
- **Stanford HAI AI Index** (`hai.stanford.edu`)
- **OECD.AI** (`oecd.ai`)
- **Epoch AI** (`epochai.org`) — compute / training / model trends
- **Our World in Data** (`ourworldindata.org`)
- **CB Insights** (`cbinsights.com`)
- **Statista** (`statista.com`)
- Domain-specific:
  - **SemiAnalysis** (`semianalysis.com`) — AI hardware / datacenter
  - **CEPS** (`ceps.eu`) — EU policy
  - **Chinchilla / DeepMind research blog** — LLM scaling laws

## Tier 4 — Tier-1 press

- **Bloomberg** (`bloomberg.com`)
- **Reuters** (`reuters.com`)
- **Financial Times** (`ft.com`)
- **CNBC** (`cnbc.com`)
- **The New York Times** (`nytimes.com`)
- **The Wall Street Journal** (`wsj.com`)
- **The Economist** (`economist.com`)
- **The Information** (`theinformation.com`)
- **Les Échos** (`lesechos.fr`) — FR business press
- **Le Monde** (`lemonde.fr`) — FR general press (business sections)

## Tier 5 — Tier-2 press (flagged, needs human review)

- **TechCrunch** (`techcrunch.com`)
- **The Verge** (`theverge.com`)
- **Ars Technica** (`arstechnica.com`)
- **Wired** (`wired.com`)
- **VentureBeat** (`venturebeat.com`)
- **MIT Technology Review** (`technologyreview.com`)

## Tier 6 — Startup databases and aggregators (flagged, needs human review)

- **Crunchbase** (`crunchbase.com`)
- **Sacra** (`sacra.com`)
- **PitchBook** (`pitchbook.com`)
- **Dealroom** (`dealroom.co`)
- **Wikipedia** (`en.wikipedia.org`, `fr.wikipedia.org`) — acceptable only as a pointer to primary sources

---

## How `/cite` uses this file

- `/cite-scan` reads this file and proposes a per-run overlay with domain-specific sources it surfaced during pre-research.
- `/cite-research` resolves `publisher_org` → `authority_tier` by matching against entries here (and the per-run overlay). A publisher not matched to any tier defaults to `tier: unknown` and flags `flagged-low-reputation`.
- `/cite-apply` offers a promotion gate: per-run overlay entries that Louis approves get appended here.

When promoting a new entry, include the domain-specific context as a comment (e.g., `- **Jane Street Tech Blog** (trading-tech domain only)`).
````

- [ ] **Step 2: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/authority-map.md
git commit -m "docs: add authority-map.md baseline roster for /cite skill"
```

---

## Task 4: Initialize `cite-skill-backlog.md`

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/docs/references/cite-skill-backlog.md`

- [ ] **Step 1: Write the backlog file**

```markdown
# /cite skill — improvement backlog

<!-- ABOUTME: Persistent backlog of improvements for the /cite skill family. -->
<!-- ABOUTME: Fed by caveats.md from each run via the /cite-apply end-of-run prompt. -->

This file accumulates caveats surfaced during `/cite` runs that Louis flagged
for future skill revisions. Each entry is a specific thing the skill failed at
or handled imperfectly, so the next revision has a concrete target list.

Entries are appended by `/cite-apply` after Louis confirms per-item at the
end-of-run prompt. Format:

```
## YYYY-MM-DD — <file slug>

- **<category>**: <short description>
  - Context: <what happened>
  - Suggestion: <what the skill should do instead, if known>
```

Categories:
- **tool** — Tavily rate limit, extract failure, Wayback unavailable
- **research** — multi-source disagreement, date not extractable, alignment ambiguity
- **detection** — claim classifier missed something or was unsure

---

## Open

_(No entries yet — `/cite-apply` appends here.)_

---

## Resolved

_(Move entries here when addressed in a skill revision.)_
```

- [ ] **Step 2: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/cite-skill-backlog.md
git commit -m "docs: initialize cite-skill-backlog.md for self-improvement loop"
```

---

## Task 5: Write `/cite-scan` skill

**Files:**
- Create: `~/.claude/skills/cite-scan/SKILL.md`

- [ ] **Step 1: Create skill directory**

Run: `mkdir -p ~/.claude/skills/cite-scan`

- [ ] **Step 2: Write SKILL.md**

Write this exact content to `~/.claude/skills/cite-scan/SKILL.md`:

````markdown
---
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, mcp__tavily__tavily_search, WebSearch, AskUserQuestion
description: Phase 1 of the /cite pipeline — extract claims needing sources from a markdown file, build a per-run authority map, and write YAML stubs for each claim. Does no source-hunting (that's /cite-research). Stops at a human review gate.
---

# /cite-scan — Claim Extraction

## Trigger
`/cite-scan <path-to-md-file>`

## Preconditions

- Target file exists and is a `.md` file
- `docs/references/slide-creation-standards.md` §6.1 (claim classification rubric) and §6.2 (tier definitions) are readable
- `docs/references/authority-map.md` exists (run is OK if missing — just skip baseline-read)

## Outputs

Per-file bundle at `docs/citation-audit/<slug>/`:
- `outline.md` — skeleton with claim count and review instructions
- `authority-map.md` — global baseline + per-run domain overlay
- `caveats.md` — classifier uncertainties logged during extraction
- `claims/claim-NN.yaml` — one stub per extracted claim (status: pending)
- `.scan-hash` — SHA-256 of target file content (for drift detection at /cite-apply time)

## Workflow

### Step 1: Resolve input and compute slug

- If no argument, use AskUserQuestion to ask which file to audit
- Verify the file exists: `ls <path>`
- Compute slug: replace `/` with `-`, strip `.md` suffix. No other prefix stripping — keep the full path so slugs are unambiguous across `slides/`, `docs/`, etc.
  - `slides/session-05/A-regulation-ethique.md` → `slides-session-05-A-regulation-ethique`
  - `docs/references/test-fixtures/cite-fixture.md` → `docs-references-test-fixtures-cite-fixture`
- Compute file hash: `sha256sum <path> | cut -d' ' -f1` → save for Step 7
- Create output directory: `mkdir -p docs/citation-audit/<slug>/claims`

### Step 2: Read classification rubric

Read `docs/references/slide-creation-standards.md` §6.1 into context. It defines:

**Needs a source:**
- Any number (dollars, percentages, growth rates, market sizes, headcounts)
- Any named statistic ("X% of companies do Y")
- Any company-specific fact (revenue, valuation, funding, users)
- Any benchmark result (accuracy, error rates)
- Any pricing data
- Any prediction/forecast

**Does NOT need a source:**
- Logical deductions / reasoning
- Definitions / textbook explanations
- Pedagogical framing (metaphors, analogies)
- Tool descriptions (without stats)
- Discussion questions

### Step 3: Extract claims from target file

Read the target file. For each line, classify per the rubric above.

For each claim found, produce an entry:
```yaml
id: claim-NN               # zero-padded counter starting at 01
location:
  file: <path>
  slide: "<slide number and title, if the claim is inside a numbered slide>"
  line: <line number of the claim in the file>
claim:
  text: "<verbatim claim text>"
  type: <number|named-stat|company-fact|benchmark|pricing|forecast|historical-event>
  has_existing_source: <true if the claim has a [N] marker on the same line or existing slide-level Sources line, else false>
proposed_source: {}        # empty — filled by /cite-research
status: pending
flag_reason: null
proposed_action: null
proposed_claim_update: null
```

**Important**: For v1, skip claims where `has_existing_source: true`. Do not extract them as pending. Log a count of skipped claims.

**Edge cases**:
- If a line ambiguously could be a claim (e.g., a general reference to a company without a specific number), log it to `caveats.md` under "Detection-level" and do NOT extract it as a claim.
- If a discussion slide (Discussion / Key Takeaways) contains numbers, skip it — per §6.4, discussion slides may omit citations.

### Step 4: Identify topic domains

Based on the file's headings, subheadings, and frequent named entities, identify 2–4 topic domains the file covers. Examples: "AI market forecasting", "EU AI regulation", "AI hardware", "AI company financials".

Use model knowledge only here — no web search yet.

### Step 5: Pre-research authority map

For each domain from Step 4, run at most **one** Tavily search with the query template:
```
"authoritative research organizations on {domain} 2025 2026"
```

(If Tavily is unavailable, use WebSearch with the same query.)

Collect the organizations mentioned in top results. Cross-reference with the baseline `docs/references/authority-map.md`:
- Publishers already in the baseline → skip (no overlay needed)
- Publishers not in the baseline → add to per-run overlay with a *proposed* tier (use tier definitions from §6.2 to guess)

Write `docs/citation-audit/<slug>/authority-map.md`:

```markdown
# Authority map — <slug> run

Inherits from `docs/references/authority-map.md` (baseline). Additions below
are per-run proposals surfaced by /cite-scan. `/cite-apply` will offer a
promotion gate per entry.

## Proposed additions (this run)

### Tier N — <tier name>
- **<Publisher>** (`<domain>`) — <context>
  - Why proposed: <domain relevance + recency of findings>
```

If no new publishers surfaced, write only the header paragraph.

### Step 6: Write stubs and outline

For each claim from Step 3, write the YAML to `docs/citation-audit/<slug>/claims/claim-NN.yaml`.

Write `docs/citation-audit/<slug>/outline.md`:

```markdown
# Citation audit — <path>

**Status**: scan complete · <YYYY-MM-DD>
**Summary**: <N> claims extracted · <M> skipped (already sourced)
**Next step**: run `/cite-research` from the repo root (expects `docs/citation-audit/<slug>/` to exist)

## Extracted claims

| id | slide | line | claim (truncated 80 chars) | type |
|----|-------|------|----------------------------|------|
| claim-01 | 07 — Flash Crash 2010 | 142 | "Le Flash Crash du 6 mai 2010..." | historical-event |
| ... |

## Domains identified
- <domain 1>
- <domain 2>

## Authority overlay
See `authority-map.md` in this directory. <N> new publishers proposed.

## Caveats
See `caveats.md` in this directory. <N> entries logged.
```

### Step 7: Write hash + caveats

- Save the file hash from Step 1 to `docs/citation-audit/<slug>/.scan-hash` (single line, hex digest, no newline).
- Initialize `caveats.md` with sections `## Tool-level`, `## Research-level`, `## Detection-level`. Any classifier uncertainties from Step 3 go under Detection-level.

### Step 8: Report to user

Show a summary:
```
/cite-scan complete for <path>
- <N> claims extracted → docs/citation-audit/<slug>/claims/
- <M> claims skipped (already sourced)
- <K> authority overlay proposals
- <L> caveats logged

Next: review the extracted claims in docs/citation-audit/<slug>/outline.md.
When ready, run /cite-research.
```

## Common failure modes

- **Target file not found**: abort with clear message, no output written
- **Output directory already exists**: warn, ask via AskUserQuestion whether to overwrite or abort
- **File has zero extractable claims**: still write outline.md (noting zero), don't run Step 5 (no domain → no overlay)
- **Tavily unavailable in Step 5**: fall back to WebSearch. Log to caveats.md.

## Non-goals (v1)

- Do NOT re-verify existing sources (claims with `has_existing_source: true` are skipped)
- Do NOT search for sources to fill claims — that's `/cite-research`'s job
- Do NOT edit the target file — only `/cite-apply` does that
````

- [ ] **Step 3: Commit (skill files are outside the repo)**

Skills live outside the repo. No commit needed for the skill itself — document the path in the next task's integration test.

---

## Task 6: Integration test `/cite-scan` against fixture

**Files:**
- Uses: `docs/references/test-fixtures/cite-fixture.md`
- Produces: `docs/citation-audit/docs-references-test-fixtures-cite-fixture/`

- [ ] **Step 1: Run the skill**

In a fresh Claude Code session (or via the current one), invoke:
```
/cite-scan docs/references/test-fixtures/cite-fixture.md
```

- [ ] **Step 2: Verify outputs**

Run these checks:

```bash
cd /home/ezalos/42/Markdowns2Teach
test -d docs/citation-audit/docs-references-test-fixtures-cite-fixture/ && echo "OK: bundle dir exists"
test -f docs/citation-audit/docs-references-test-fixtures-cite-fixture/outline.md && echo "OK: outline.md"
test -f docs/citation-audit/docs-references-test-fixtures-cite-fixture/authority-map.md && echo "OK: authority-map.md"
test -f docs/citation-audit/docs-references-test-fixtures-cite-fixture/caveats.md && echo "OK: caveats.md"
test -f docs/citation-audit/docs-references-test-fixtures-cite-fixture/.scan-hash && echo "OK: scan hash"
ls docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.yaml | wc -l
```

Expected: 5 claim yaml files (matching the 5 claims in the fixture).

- [ ] **Step 3: Inspect one claim yaml**

Run: `cat docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/claim-01.yaml`

Expected fields present: `id`, `location.file`, `location.line`, `claim.text`, `claim.type`, `claim.has_existing_source: false`, `status: pending`, and an empty `proposed_source: {}`.

If any field is missing → update the skill's Step 3 instructions and re-run.

- [ ] **Step 4: If test passes, proceed to Task 7. If not, debug**

Common issues:
- Wrong claim count → claim detection is too strict or too loose → revise Step 3 rubric
- Missing `has_existing_source` → skill instruction needs tightening
- `.scan-hash` missing → Step 7 not executing

---

## Task 7: Write `/cite-research` skill

**Files:**
- Create: `~/.claude/skills/cite-research/SKILL.md`

- [ ] **Step 1: Create directory**

Run: `mkdir -p ~/.claude/skills/cite-research`

- [ ] **Step 2: Write SKILL.md**

Write this to `~/.claude/skills/cite-research/SKILL.md`:

````markdown
---
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, mcp__tavily__tavily_search, mcp__tavily__tavily_extract, WebSearch, WebFetch, AskUserQuestion
description: Phase 2 of the /cite pipeline — for each pending claim, spawn a subagent to find a source, Tavily-extract the page, and fill the claim schema with the exact supporting quote. Updates outline.md with categorized sections. No source-file edits.
---

# /cite-research — Source Hunting with Strict Quote Extraction

## Trigger
`/cite-research [<slug>]`

If no slug provided, use AskUserQuestion to list `docs/citation-audit/*/` directories and pick one.

## Preconditions

- A bundle exists at `docs/citation-audit/<slug>/` with `outline.md`, `authority-map.md`, `claims/*.yaml`, `.scan-hash`
- At least one `claims/*.yaml` has `status: pending`

## Outputs (modifications to existing bundle)

- Every `claims/*.yaml` with `status: pending` is updated with filled `proposed_source` and a new `status` (auto-approved / flagged-low-reputation / flagged-unsourceable / flagged-stale-stat)
- `outline.md` is rewritten with categorized sections
- `authority-map.md` may gain new entries (post-research refinement)
- `caveats.md` gains entries for tool/research-level issues

## Workflow

### Step 1: Load state

Read `outline.md`, `authority-map.md` (per-run overlay), and the global `docs/references/authority-map.md`. Collect all `claims/*.yaml` with `status: pending`.

If no pending claims, report "nothing to do" and exit.

### Step 2: Dispatch parallel research subagents

Use the `Agent` tool to spawn up to **5 concurrent** subagents. Each subagent is given **exactly one** claim. Use `subagent_type: general-purpose`.

**Subagent prompt template** (substitute placeholders):

```
You are a source researcher for a specific factual claim. Your task is to
find ONE authoritative source that supports the claim, then extract a direct
quote and metadata into a YAML file.

## Claim to source
- Text: "{claim.text}"
- Type: {claim.type}
- Located in: {location.file}, slide "{location.slide}", line {location.line}

## Authority map (global + per-run overlay)
{contents of global authority-map.md + per-run overlay}

## Process

1. Run up to 3 different search queries using Tavily Search (fall back to
   WebSearch if Tavily rate-limits). Vary queries: different site: filters,
   date windows, synonyms. Prefer queries that restrict to Tier 1-3 publishers
   per the authority map.

2. From the top results, pick the single best source by (highest tier,
   then most recent publication_date). If multiple sources disagree on a
   number, note the disagreement in the caveats field below.

3. Use Tavily Extract (fall back to WebFetch) on the chosen URL to get the
   actual page text. DO NOT trust the search snippet — you must read the
   page.

4. Find the exact sentence(s) in the page that support the claim. Extract:
   - `quote`: the single sentence containing the number/fact, verbatim
   - `surrounding_paragraph`: the full paragraph the quote is in
   - `section_heading`: the heading of the section the paragraph lives under
   - `url`, `url_domain`, `publisher_org`, `author`, `publication_date`
     (all from the page metadata or header)
   - `alignment_justification`: one sentence explaining WHY the quote
     supports the claim as written

5. If the page does NOT actually contain the claim (common failure mode —
   search result was misleading), try another source. Give up after 3
   queries and mark the claim flagged-unsourceable.

## Classification

Compute:
- `authority_tier`: integer 1-6, by matching `publisher_org` or `url_domain`
  against the authority map. If no match, set to `null` and flag.
- `recency_verdict`:
  - `fresh` if publication_date within 6 months of today
  - `recent` if 6-12 months
  - `stale` if > 12 months
  - `historical-event` if the claim is about an event before 2020 (e.g., AlexNet 2012, Flash Crash 2010)
- `confidence`: high (exact quote, obvious match) / medium (quote close but paraphrased) / low (no perfect quote, but strong contextual support)

## Status assignment

- `auto-approved` if tier ∈ {1,2,3,4} AND recency_verdict ∈ {fresh, recent, historical-event} AND confidence ∈ {high, medium}
- `flagged-low-reputation` if tier ∈ {5,6} or tier == null
- `flagged-stale-stat` if any source with publication_date > this one has a number differing by >10% (this means you found a better source but chose this one because of tier — document the alternative)
- `flagged-unsourceable` if no source found after 3 queries, or no page contains the claim

## Output

Write the completed claim YAML to:
  docs/citation-audit/{slug}/claims/{claim.id}.yaml

Preserve all fields from the input stub. Fill `proposed_source` with all the
extracted metadata. Set `status`, `flag_reason` (if flagged), `proposed_action`
(`add-citation` default, `update-claim-value` if flagged-stale-stat,
`soften-language` if flagged-unsourceable).

If you encountered issues (Tavily rate-limit, page 404, ambiguous quote),
append a line to docs/citation-audit/{slug}/caveats.md under the appropriate
category.
```

Launch the subagents in parallel (single message, multiple Agent tool calls) in batches of 5. Wait for each batch before launching the next.

### Step 3: Post-research authority refinement

After all subagents complete, collect publishers that showed up across multiple claims but weren't in the baseline authority-map.md. Add them to the per-run overlay in `authority-map.md` under a new section:

```markdown
## Post-research additions (surfaced during /cite-research)

### Tier N — <tier name>
- **<Publisher>** (`<domain>`) — appeared in claims {list}, proposed tier based on <rationale>
```

### Step 4: Update outline.md

Rewrite `outline.md` with these sections:

```markdown
# Citation audit — <path>

**Status**: research complete · <YYYY-MM-DD>
**Summary**: <total> claims · <auto-approved count> auto-approved · <flagged count> flagged · <unsourceable count> unsourceable
**Next step**: edit flagged claim YAMLs to set `status: approved`/`rejected`/`needs-rework`, then run `/cite-apply`.

## Flagged — review required

### claim-NN · <flag-reason> · slide <num>
- **Claim**: "..."
- **Source found**: <authority name> — tier <N> (<date>)
- **Quote**: "..."
- **Note**: <flag-specific note>
- _edit `claims/claim-NN.yaml` → `status: approved|rejected|needs-rework`_

<repeat for each flagged claim>

## Auto-approved (audit trail)

| id | slide | authority | tier | recency | confidence |
|----|-------|-----------|------|---------|------------|
| claim-01 | ... | ... | ... | ... | ... |

## Unsourceable

### claim-NN · slide <num>
- **Claim**: "..."
- **Searches attempted**: <list of queries>
- _options: soften language (`proposed_action: soften-language`) · remove · provide your own URL_
```

### Step 5: Report to user

```
/cite-research complete for <slug>
- <auto> auto-approved
- <flagged> flagged (review in outline.md flagged section)
- <unsourceable> unsourceable (need manual decision)
- <caveats> caveats logged
- <new-authorities> publishers added to per-run authority overlay

Next: open docs/citation-audit/<slug>/outline.md, review flagged items,
edit the corresponding claims/*.yaml to set status, then run /cite-apply.
```

## Common failure modes

- **No `.scan-hash`**: abort with "run `/cite-scan` first"
- **All claims already processed**: report "nothing to do"
- **Tavily rate limit partway through**: finish remaining claims with WebSearch fallback, log each fallback to caveats.md
- **Subagent timeout or error**: retry once; if fails again, mark claim `flagged-unsourceable` with error note in caveats

## Non-goals (v1)

- Do NOT edit the target source file
- Do NOT process claims with `status` other than `pending`
- Do NOT re-research `status: needs-rework` claims in the same run (user must explicitly re-invoke)
````

- [ ] **Step 3: Skill is self-contained (no commit needed for the skill file)**

---

## Task 8: Integration test `/cite-research` against fixture output

- [ ] **Step 1: Ensure Task 6 output exists**

```bash
ls docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.yaml
```
Expected: 5 yaml files with `status: pending`.

- [ ] **Step 2: Run the skill**

```
/cite-research docs-references-test-fixtures-cite-fixture
```

Expected: 2–5 minutes runtime (5 parallel subagents, each doing 1-3 Tavily calls).

- [ ] **Step 3: Verify outputs**

```bash
cd /home/ezalos/42/Markdowns2Teach
# Every claim should have a filled proposed_source now
grep -L "proposed_source: {}" docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.yaml | wc -l
# Should equal 5

# Check one claim has all required fields
cat docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/claim-01.yaml | grep -E "(url:|publisher_org:|publication_date:|authority_tier:|quote:|surrounding_paragraph:|section_heading:|alignment_justification:|confidence:|status:)"
# Should list all 10 fields
```

- [ ] **Step 4: Verify outline.md was rewritten**

```bash
grep "Status.*research complete" docs/citation-audit/docs-references-test-fixtures-cite-fixture/outline.md && echo "OK"
grep "auto-approved\|flagged\|unsourceable" docs/citation-audit/docs-references-test-fixtures-cite-fixture/outline.md
```

- [ ] **Step 5: Verify at least the Flash Crash + AI Act claims landed auto-approved at tier 1**

The fixture has historical/regulatory claims with strong primary sources. If any of the 5 claims came back `flagged-unsourceable`, the skill's subagent prompt needs tightening.

If test passes, proceed. If not, debug the subagent prompt in SKILL.md Step 2.

---

## Task 9: Write `/cite-apply` skill

**Files:**
- Create: `~/.claude/skills/cite-apply/SKILL.md`

- [ ] **Step 1: Create directory**

Run: `mkdir -p ~/.claude/skills/cite-apply`

- [ ] **Step 2: Write SKILL.md**

Write this to `~/.claude/skills/cite-apply/SKILL.md`:

````markdown
---
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
description: Phase 3 of the /cite pipeline — patch the source markdown file with [N] citation markers and per-slide <small>Sources</small> footers based on approved claim YAMLs. Offers authority-map promotion gate and caveats-to-backlog gate at the end.
---

# /cite-apply — Apply Approved Citations

## Trigger
`/cite-apply [<slug>]`

## Preconditions

- Bundle at `docs/citation-audit/<slug>/` with `claims/*.yaml` all filled
- `.scan-hash` matches current SHA-256 of target file (drift check)
- At least one claim has `status ∈ {approved, auto-approved}`

## Workflow

### Step 1: Load and drift-check

- If no slug argument, AskUserQuestion to pick from `docs/citation-audit/*/` dirs
- Read every `claims/*.yaml`. Parse target file path from any claim's `location.file`
- Re-hash target file: `sha256sum <file> | cut -d' ' -f1`
- Compare with `.scan-hash`. If differ, abort with:
  ```
  ABORT: source file has changed since /cite-scan ran.
  Re-run /cite-scan to regenerate the audit bundle.
  ```

### Step 2: Partition claims

Split claims by status:
- **to_apply**: `status ∈ {approved, auto-approved}`
- **to_skip**: `status ∈ {rejected, needs-rework, flagged-*}` (all flagged statuses that weren't manually moved to `approved`)
- **unsourceable_decisions**: `status == flagged-unsourceable` with `proposed_action == soften-language`

If `to_apply` is empty AND `unsourceable_decisions` is empty:
```
Nothing to apply. All claims are either rejected, flagged, or unsourceable
without a soften-language action. Edit the YAMLs and re-run.
```

### Step 3: Group by slide and number

Group `to_apply` claims by slide (via `location.slide`). Within each slide:
- Assign `[N]` where N starts at 1 per slide
- Claims sharing the same `proposed_source.url` share the same `[N]`
- Order by line number within the slide

### Step 4: Build the patch

For each claim in `to_apply`:
- Find the claim's line in the target file
- Append ` [N]` to the end of the claim sentence (before any trailing period or bullet nesting)
- If `proposed_action == update-claim-value`, replace the claim text with `proposed_claim_update`

For each slide with citations:
- Find the slide's last non-empty content line (before the next `---` or EOF)
- Insert a new line: `<small>Sources : [1] [<authority_name>](<url>) · [2] [<authority_name>](<url>) · …</small>`

For each claim in `unsourceable_decisions`:
- Replace the claim sentence with `proposed_claim_update` (the softened version)
- Log an apply-note to caveats.md

### Step 5: Write preview diff

Write `docs/citation-audit/<slug>/apply-preview.diff` using `diff -u <original> <patched>` output.

Show the diff to Louis:
```
--- Patch preview ---
<paste apply-preview.diff content, or `head -50` if huge>

To apply these edits: reply `apply`
To review a specific claim before applying: reply `detail <claim-id>`
To abort: reply `abort`
```

Use AskUserQuestion to capture the decision (Apply / Abort / Show detail).

### Step 6: Apply edits

If user chose apply:
- Apply the patched content to the target file (use Edit with the original → patched substrings, not a full file rewrite — keeps diff surgical)
- Run in order:
  ```bash
  make check
  make check-citations
  make html
  ```
- Capture each exit code. Report pass/fail per step.
- If any fail: report the failure, do NOT revert. Louis fixes manually (per spec §8).

### Step 7: Authority promotion gate

Read the per-run `authority-map.md` (overlay section). For each proposed publisher addition, show it and use AskUserQuestion:
- "Promote **<Publisher>** (<domain>) to global authority-map.md at tier <N>? yes/no/skip"

For each `yes`, append the entry under the correct tier in `docs/references/authority-map.md`. Single commit at the end:
```bash
cd <repo>
git add docs/references/authority-map.md
git commit -m "chore: promote <N> publishers from <slug> to global authority map"
```

(Skip commit if nothing was promoted.)

### Step 8: Caveats → backlog gate

Read `caveats.md` from the bundle. For each entry, show it and use AskUserQuestion:
- "Roll this into cite-skill-backlog.md? yes/no"

For each `yes`, append under `## Open` in `docs/references/cite-skill-backlog.md` with today's date and the `<slug>` as context. Commit:
```bash
git add docs/references/cite-skill-backlog.md
git commit -m "chore: append <N> backlog items from <slug> caveats"
```

### Step 9: Final report

```
/cite-apply complete for <slug>

Applied:
- <N> claims cited across <M> slides
- <K> claims soften-languaged (unsourceable)

Verification:
- make check: <PASS|FAIL>
- make check-citations: <PASS|FAIL>
- make html: <PASS|FAIL>

Promotions: <N> publishers → global authority-map.md
Backlog: <M> caveats → cite-skill-backlog.md

Target file: <path>
Audit bundle (gitignored): docs/citation-audit/<slug>/
```

## Common failure modes

- **Hash drift**: abort cleanly, don't touch anything
- **Line number stale** (claim location no longer matches file content — rare if hash matched, but possible with whitespace-only edits): abort the specific claim, report others
- **`make check` overflow after citation added**: report, leave file as-is for Louis to fix manually (per spec §8)
- **Per-slide `[N]` collision with existing numbering**: shouldn't happen because v1 skips already-sourced claims, but if detected, abort with clear message

## Non-goals (v1)

- Do NOT retry `make check` failures automatically
- Do NOT revert on `make check` failure — leave the file for Louis
- Do NOT delete the audit bundle (it stays for reference and re-runs)
````

---

## Task 10: Integration test `/cite-apply` against fixture

- [ ] **Step 1: Manually edit one claim to `approved`**

Pick one of the flagged claims from Task 8 and edit its YAML:
```yaml
# Change status from flagged-<reason> to approved
status: approved
```

- [ ] **Step 2: Run `/cite-apply`**

```
/cite-apply docs-references-test-fixtures-cite-fixture
```

- [ ] **Step 3: At the diff preview, reply `apply`**

- [ ] **Step 4: Verify target file was patched**

```bash
cd /home/ezalos/42/Markdowns2Teach
grep -c "\[1\]" docs/references/test-fixtures/cite-fixture.md
grep -c "<small>Sources" docs/references/test-fixtures/cite-fixture.md
```

Expected: ≥1 `[1]` and ≥1 `<small>Sources` line added.

- [ ] **Step 5: Verify `make check`, `make check-citations`, `make html`**

The skill reports these itself — verify all three pass.

- [ ] **Step 6: Verify authority promotion gate ran**

The skill should have asked about promotions. If the per-run overlay was empty, it skips (that's OK for the fixture).

- [ ] **Step 7: Verify caveats gate ran**

Similar — if no caveats, skipped.

- [ ] **Step 8: Clean up the fixture edit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git checkout docs/references/test-fixtures/cite-fixture.md
rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/
```

(Re-runnable state for future runs.)

---

## Task 11: Write `/cite` meta-skill

**Files:**
- Create: `~/.claude/skills/cite/SKILL.md`

- [ ] **Step 1: Create directory**

Run: `mkdir -p ~/.claude/skills/cite`

- [ ] **Step 2: Write SKILL.md**

```markdown
---
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Skill, AskUserQuestion
description: Meta-skill — orchestrates /cite-scan, /cite-research, and /cite-apply on a markdown file with explicit review gates between each phase. Detects existing state and resumes.
---

# /cite — Citation Audit Orchestrator

## Trigger
`/cite <path-to-md-file>`

## Workflow

### Step 1: Resolve state

Compute slug from the input path. Check whether `docs/citation-audit/<slug>/` exists:

| State | Inferred phase | Action |
|-------|----------------|--------|
| Dir does not exist | Not started | Start at Scan |
| Dir exists, `claims/*.yaml` all `status: pending` | Scan complete | Start at Research |
| Dir exists, at least one claim has `status != pending` and some flagged | Research complete | Prompt for Apply |
| Dir exists, `apply-preview.diff` already present and patch already applied (check via hash) | Apply complete | Report nothing to do |

Use AskUserQuestion to confirm the inferred phase.

### Step 2: Phase 1 — Scan (if needed)

Invoke `/cite-scan <path>` via the Skill tool.

After it completes, show the summary from `outline.md` and ask:
```
Scan complete. N claims extracted.
Review docs/citation-audit/<slug>/outline.md for the extracted list.
Proceed to research? [yes/no/abort]
```

### Step 3: Phase 2 — Research (if needed)

Invoke `/cite-research <slug>` via the Skill tool.

After it completes, show the summary from the rewritten `outline.md` and stop:
```
Research complete.
- <N> auto-approved
- <M> flagged (review in docs/citation-audit/<slug>/outline.md)
- <K> unsourceable

Review the flagged items and edit the corresponding YAMLs:
  docs/citation-audit/<slug>/claims/claim-NN.yaml
Set status to: approved | rejected | needs-rework

When ready, reply 'go' to apply.
```

Wait for Louis to reply. If he says `go`, proceed to Step 4. If he says `abort`, stop.

### Step 4: Phase 3 — Apply

Invoke `/cite-apply <slug>` via the Skill tool.

Its diff-preview gate is Louis's final checkpoint. After `/cite-apply` completes, relay its final report.

## Common failure modes

- **Hash drift between phases**: `/cite-apply` will abort; `/cite` should surface the abort cleanly and suggest re-running `/cite-scan`.
- **User declines to proceed after scan**: leave the bundle in place; exit cleanly.

## Non-goals (v1)

- Does NOT batch across files. Run one file at a time.
- Does NOT parallelize scan with research or research with apply.
```

---

## Task 12: Integration test `/cite` end-to-end

- [ ] **Step 1: Ensure bundle is cleaned**

```bash
rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/
```

- [ ] **Step 2: Run `/cite` on fixture**

```
/cite docs/references/test-fixtures/cite-fixture.md
```

- [ ] **Step 3: Accept "proceed to research"**

When asked, reply `yes`.

- [ ] **Step 4: After research, manually edit one flagged YAML to approved (if any)**

If all 5 fixture claims auto-approved, skip this step.

- [ ] **Step 5: Reply `go`**

- [ ] **Step 6: At the apply diff preview, reply `apply`**

- [ ] **Step 7: Verify target file was patched and builds cleanly**

```bash
cd /home/ezalos/42/Markdowns2Teach
make check-citations 2>&1 | grep cite-fixture
# Expected: no WARNING for any fixture slide
make html 2>&1 | tail -5
# Expected: success
```

- [ ] **Step 8: Clean up**

```bash
git checkout docs/references/test-fixtures/cite-fixture.md
rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/
```

---

## Task 13: Cross-reference in `workflow-citation-audit.md`

**Files:**
- Modify: `/home/ezalos/42/Markdowns2Teach/docs/references/workflow-citation-audit.md`

- [ ] **Step 1: Read the existing file**

Run: `cat /home/ezalos/42/Markdowns2Teach/docs/references/workflow-citation-audit.md`

- [ ] **Step 2: Add a new section at the top (after the ABOUTME lines)**

Insert after line 4 (after the two ABOUTME comments):

```markdown
## Automation: the `/cite` skill family

For new audits, use the `/cite` skill family instead of the manual process
below. It automates claim extraction, source research with strict quote
verification, and citation application — with human-in-the-loop review gates.

- `/cite <file>` — run all three phases with review gates
- `/cite-scan <file>` — phase 1, extract claims (outputs to `docs/citation-audit/<slug>/`)
- `/cite-research` — phase 2, parallel source-hunting
- `/cite-apply` — phase 3, patch the file after you review flagged claims

The manual workflow below remains as the fallback and reference for when
claims need hand-sourcing.

---

```

- [ ] **Step 3: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/workflow-citation-audit.md
git commit -m "docs: cross-reference /cite skill family from workflow-citation-audit.md"
```

---

## Task 14: Mention skill in project `CLAUDE.md`

**Files:**
- Modify: `/home/ezalos/42/Markdowns2Teach/CLAUDE.md`

- [ ] **Step 1: Find the build commands section**

Run: `grep -n "## Build Commands" /home/ezalos/42/Markdowns2Teach/CLAUDE.md`

- [ ] **Step 2: Add a new section before "## Attribution"**

Insert after the Build Commands section (before `## Attribution`):

```markdown
## Citation Audit Skill

Use the `/cite <file>` skill family to audit and source slide decks. Three
phase-skills (`/cite-scan`, `/cite-research`, `/cite-apply`) plus the `/cite`
orchestrator. Per-run state lives at `docs/citation-audit/<slug>/` (gitignored).
Global references:

- `docs/references/authority-map.md` — publisher roster by §6.2 tier
- `docs/references/cite-skill-backlog.md` — self-improvement tracker

Design: `docs/superpowers/specs/2026-04-12-cite-skill-design.md`.

```

- [ ] **Step 3: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add CLAUDE.md
git commit -m "docs: add /cite skill family reference to CLAUDE.md"
```

---

## Self-Review Checklist

Run this mentally before declaring complete:

- [ ] **Spec coverage**: §1 architecture (Tasks 5,7,9,11) · §2 artifacts (Tasks 1,3,4) · §3 claim schema (Task 5 Step 3) · §4 outline.md (Tasks 5,7) · §5 authority map (Tasks 3,5,7,9) · §6 caveats (Tasks 4,5,7,9) · §7 behavior (Tasks 5,7,9,11) · §8 error handling (each skill's Common failure modes) · §9 parameters (in skill files) · §10 out-of-scope (documented in each skill) · §11 files (Task 1-4, 5, 7, 9, 11) · §12 verification (Tasks 6, 8, 10, 12)
- [ ] **Placeholder scan**: No "TBD", "implement later", "similar to Task N". Every code/content block is literal.
- [ ] **Type consistency**: YAML field names match across skills — `claim.text`, `location.file`, `location.slide`, `location.line`, `proposed_source.*`, `status`, `flag_reason`, `proposed_action`, `proposed_claim_update`. Checked.
- [ ] **Fixture claims count**: Task 2 fixture has 5 claims (Flash Crash, Dow 9%, AI Act March 2024, €35M fine, Anthropic 2021). Task 6 verification expects 5 yaml files. Aligned.

---

## Execution notes

- Skills live outside the repo (`~/.claude/skills/`) and are not version-controlled here. Only the repo-side artifacts (authority-map.md, backlog.md, fixture, doc updates, gitignore) get committed.
- Tavily usage per integration test pass: ~10 credits (5 claims × 2 avg calls). Budget: comfortable.
- Failed integration tests mean the skill instructions need tightening — iterate on the SKILL.md, not on auxiliary code.
