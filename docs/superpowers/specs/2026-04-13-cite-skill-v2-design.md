# `/cite` skill family — v2 design spec

## Context

v1 shipped yesterday (2026-04-12). The initial integration test on `cite-fixture.md` surfaced 5 real defects, logged to `docs/references/cite-skill-backlog.md`:

1. Subagent assigned `authority_tier: 1` to `encyclopedia.pub` because the page cites the SEC primary report — tier judged from what the source *cites*, not the URL domain
2. Subagent fabricated `surrounding_paragraph` by splicing content from two different sources when the primary PDF extract was partial
3. Subagent used out-of-enum `status: sourced` and wrong `proposed_action` value
4. `/cite-apply` Step 6 hardcodes `make check` which scans `slides/` only — doesn't handle targets under `docs/references/` or `docs/research/`
5. Tavily Extract returned partial content for large government PDFs (SEC/CFTC Joint Report)

**Root cause cluster**: the 5 defects reduce to 3 patterns:
- **Too-wide LLM latitude** (issues 1, 2): we ask the subagent to judge things a deterministic check could decide
- **No output validation** (issue 3): orchestrator trusts whatever YAML comes back
- **Happy-path tool assumptions** (issues 4, 5): no fallback chains when tools behave imperfectly

**v2 principle**: *Rule of Least Privilege for LLMs* — narrow the subagent's judgment surface. Subagents return DATA (URL, page text, candidate quote). Scripts make DECISIONS (tier assignment, enum validation, quote-in-page check). The skill orchestrator shells out to scripts between subagent steps.

No backwards compat with v1 bundles needed — the only existing bundle is the throwaway fixture, resettable on v2.

---

## 1. Architecture shift

```
[research subagent] → writes claim-NN.yaml + claim-NN.page.txt
         │
         ▼
[orchestrator: scripts/cite/validate_claim.py]
         │
    ┌────┴─────┐
   pass       fail → re-dispatch subagent once with --error-feedback
    │          │
    │       (retry) → still fail → status: flagged-validation-failed
    ▼
[orchestrator: scripts/cite/tier_lookup.py]
    │
[orchestrator computes recency_verdict + status deterministically]
    │
    ▼
claim-NN.yaml finalized
```

---

## 2. New artifacts

### In-repo (tracked)
- `docs/references/authority-map.yaml` — machine-readable tier lookup, sibling to existing `authority-map.md`
- `scripts/cite/validate_claim.py` — schema + enum + quote-in-page validator
- `scripts/cite/tier_lookup.py` — url_domain → tier via `authority-map.yaml`
- `scripts/cite/lint_authority_map.py` — catches drift between `.md` and `.yaml`
- `scripts/cite/target_scope.py` — given target `.md`, returns the verification shell command
- `scripts/cite/tests/` — pytest unit tests with tiny fixtures

### In bundle (gitignored)
- `docs/citation-audit/<slug>/claims/claim-NN.page.txt` — verbatim extracted page content, preserved per claim for audit trail + quote verification

### Scripts location rationale
- In-repo (`scripts/cite/`) matches existing `scripts/check-citations.sh`, `scripts/check-overflow-visual.js` pattern
- Skill references scripts via path relative to target project root
- Scripts are testable via pytest as part of the project; skills live outside the repo and stay small

---

## 3. Validator contracts

### `scripts/cite/validate_claim.py <claim.yaml> <page.txt>`

```
Exit 0 = valid. Exit 1 = invalid, stderr = human-readable failure list.

Checks:
  - YAML parses
  - Required fields present: id, location.{file,slide,line}, claim.{text,type,has_existing_source},
    proposed_source.{url,url_domain,publisher_org,publication_date,accessed_date,
    quote,surrounding_paragraph,section_heading,alignment_justification,confidence}
  - status ∈ {pending, auto-approved, approved, rejected, needs-rework,
    flagged-low-reputation, flagged-unsourceable, flagged-stale-stat,
    flagged-validation-failed}
  - proposed_action ∈ {null, add-citation, update-claim-value, soften-language, none}
  - confidence ∈ {high, medium, low}
  - recency_verdict ∈ {fresh, recent, stale, historical-event, unknown}
  - quote appears verbatim in page.txt (collapse runs of whitespace before compare)
  - surrounding_paragraph appears verbatim in page.txt
  - publication_date parses as YYYY-MM-DD
  - url_domain matches the parsed domain of url

Writes nothing. Pure check.
```

### `scripts/cite/tier_lookup.py <url_domain>`

```
Reads: docs/references/authority-map.yaml
Output on stdout: tier integer (1-6) or "null"
Exit 0 always. "null" = domain not in map.

No LLM judgment. Simple YAML lookup with domain match.
```

### `scripts/cite/lint_authority_map.py`

```
Reads: docs/references/authority-map.md AND docs/references/authority-map.yaml
Checks: every .yaml entry has a corresponding bullet in .md at same tier, and vice versa.
Exit 0 = in sync. Exit 1 = drift, stderr = diff.

Wired into `make check` as a new gate.
```

### `scripts/cite/target_scope.py <target-md>`

```
Output on stdout: shell command to run for verification.
  target under slides/ → "make check && make check-citations && make html"
  otherwise           → "bash scripts/check-citations.sh <dirname> && marp --no-stdin <target>"
Exit 0.
```

---

## 4. `authority-map.yaml` format

```yaml
# docs/references/authority-map.yaml
tiers:
  1:
    name: "Primary sources (company IR, SEC filings, government)"
    publishers:
      - name: "SEC.gov"
        domains: ["sec.gov"]
        note: "US Securities and Exchange Commission"
      - name: "EUR-Lex"
        domains: ["eur-lex.europa.eu"]
      - name: "European Parliament"
        domains: ["europarl.europa.eu"]
      # ...
  2:
    name: "Peer-reviewed academic"
    publishers:
      - name: "arXiv"
        domains: ["arxiv.org"]
      # ...
  # ... tiers 3-6 similarly
```

Multiple domains per publisher (e.g., Anthropic has `anthropic.com` and `investor.anthropic.com`).

---

## 5. Behavior changes per skill

### `/cite-scan` (minimal)

Add `validation: null` stub and `page_text_file: null` stub to each claim YAML — lets the schema validator recognize them.

### `/cite-research` (biggest rewrite)

**Subagent prompt narrowed**:
- Returns ONLY raw extracted fields: `url`, `url_domain`, `publisher_org`, `author`, `publication_date`, `quote`, `surrounding_paragraph`, `section_heading`, `alignment_justification`, `confidence`
- **Does NOT** assign `authority_tier`, `recency_verdict`, or `status` — those are orchestrator-computed
- **Does NOT** write status values at all in v2 (except `pending` from scan)
- **MUST** save Tavily/WebFetch output to `claims/claim-NN.page.txt` before returning
- Explicit anti-fabrication clause: *"Every character of `quote` and `surrounding_paragraph` must appear verbatim in the page.txt you just saved. Do not combine content from other sources. If the extract was partial and you cannot find the exact sentence, return `confidence: low` with what you actually extracted — do not splice."*

**PDF fallback chain** (in subagent prompt):
1. `mcp__tavily__tavily_extract` with `extract_depth: "advanced"` and `format: "markdown"`
2. If result truncated or empty: `WebFetch` with same URL
3. If URL ends in `.pdf` and previous layers failed: `curl -sL <URL> -o /tmp/cite-<claim-id>.pdf && pdftotext /tmp/cite-<claim-id>.pdf -` via Bash
4. Every fallback invocation gets logged to `caveats.md`

**Orchestrator validation loop** (cite-research skill main thread):
```
For each claim in pending:
  1. dispatch research subagent
  2. run: python scripts/cite/validate_claim.py claims/claim-NN.yaml claims/claim-NN.page.txt
  3. if exit 1:
       re-dispatch subagent with error feedback (`--error-feedback "<stderr>"`)
       run validator again
       if exit 1: set status: flagged-validation-failed; continue
  4. run: python scripts/cite/tier_lookup.py <url_domain>
     assign authority_tier from result (or null)
  5. compute recency_verdict from publication_date:
       fresh (< 6 mo), recent (6-12 mo), stale (> 12 mo), historical-event (< 2020)
  6. compute status from tier + recency:
       tier ∈ {1,2,3,4} AND recency ∈ {fresh, recent, historical-event} → auto-approved
       tier ∈ {5,6} OR tier == null → flagged-low-reputation
       tier unknown → flagged-low-reputation
  7. write finalized claim-NN.yaml
```

### `/cite-apply` (targeted fix)

Step 6 changes:
```
target_scope_cmd=$(python scripts/cite/target_scope.py <target-file>)
eval "$target_scope_cmd"
```

No longer hardcodes `make check`. Backwards compat for `slides/` targets preserved.

### `/cite` orchestrator — unchanged.

---

## 6. Schema additions (additive, no breaking changes within v2 lifetime)

```yaml
# claim-NN.yaml gains:
validation:
  validated_at: 2026-04-13T14:23:00Z
  quote_found_in_page: true
  surrounding_paragraph_found_in_page: true
  enum_valid: true
  attempts: 1              # 1 or 2 — 2 means retry was needed
page_text_file: claim-NN.page.txt   # relative to the YAML

# New status value:
# flagged-validation-failed
```

---

## 7. What v2 prevents (traceability to backlog items)

| Backlog issue | v2 fix |
|---------------|--------|
| 1. tier-from-citation bug | `tier_lookup.py` reads url_domain only; subagent does not assign tier |
| 2. fabricated surrounding_paragraph | `validate_claim.py` greps page.txt for verbatim match; rejects on mismatch |
| 3. status enum drift | `validate_claim.py` rejects invalid enums; orchestrator computes final status deterministically |
| 4. make check scoping | `target_scope.py` routes verification command per target path |
| 5. Tavily partial PDF | 3-layer fallback chain documented in subagent prompt (tavily advanced → WebFetch → pdftotext) |

---

## 8. Critical files to create/modify

### Create
- `docs/references/authority-map.yaml`
- `scripts/cite/__init__.py`
- `scripts/cite/validate_claim.py`
- `scripts/cite/tier_lookup.py`
- `scripts/cite/lint_authority_map.py`
- `scripts/cite/target_scope.py`
- `scripts/cite/tests/__init__.py`
- `scripts/cite/tests/fixtures/*` (tiny YAMLs + page.txt samples)
- `scripts/cite/tests/test_validate_claim.py`
- `scripts/cite/tests/test_tier_lookup.py`
- `scripts/cite/tests/test_lint_authority_map.py`
- `scripts/cite/tests/test_target_scope.py`

### Modify (outside repo, skill files)
- `~/.claude/skills/cite-scan/SKILL.md` — add validation/page_text_file stubs
- `~/.claude/skills/cite-research/SKILL.md` — major rewrite per §5
- `~/.claude/skills/cite-apply/SKILL.md` — Step 6 target_scope integration

### Modify (in repo)
- `Makefile` — wire `lint_authority_map.py` into `make check`
- `docs/references/cite-skill-backlog.md` — move the 5 v1 items to `## Resolved` with date + v2 reference

---

## 9. Testing

**Unit tests** (pytest, per-script):
- `test_validate_claim.py`:
  - accepts a well-formed claim
  - rejects out-of-enum status
  - rejects quote not in page.txt
  - rejects fabricated surrounding_paragraph
  - rejects malformed publication_date
  - whitespace normalization (extra spaces should still match)
- `test_tier_lookup.py`:
  - known domain → correct tier
  - unknown domain → `null`
  - subdomain handling (e.g., `investor.anthropic.com` → matches anthropic.com tier)
- `test_lint_authority_map.py`:
  - in-sync files → pass
  - domain in .yaml missing from .md → fail
  - tier mismatch → fail
- `test_target_scope.py`:
  - `slides/*.md` → slides command
  - `docs/references/*.md` → fixture command
  - `docs/research/*.md` → fixture command

**Integration test** (re-run cite-fixture):
- Reset bundle: `rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/`
- Restore fixture: `git checkout docs/references/test-fixtures/cite-fixture.md`
- Run `/cite-scan` → `/cite-research` → `/cite-apply`
- Expected outcomes distinct from v1:
  - claim-01 (Flash Crash): subagent finds encyclopedia.pub → orchestrator tier lookup returns `null` → auto-assigned `flagged-low-reputation` IMMEDIATELY (not the old tier-1 mis-promotion)
  - claim-02 (Dow -9%): partial SEC PDF triggers fallback chain → pdftotext succeeds → full page.txt preserved → `quote` validates verbatim → no fabrication
  - claim-03 (AI Act adopted): status computed deterministically as `auto-approved`; no enum drift possible
  - `/cite-apply`: target_scope.py routes to fixture command; runs in seconds, not 2+ minutes
  - `claim-NN.page.txt` files exist in bundle for all 5 claims

**Regression**: re-run `make check` on the real session decks to confirm v2 scripts don't break `slides/` workflow.

---

## 10. Out of scope for v2

- **Cross-checking by a second subagent** — adds cost for marginal benefit once validators exist; revisit if validator-passing claims still turn out wrong in practice
- **Wayback Machine fallback for dead URLs** — v1 already notes this as a v2+ idea; v2 keeps the PDF fallback but not the dead-link recovery
- **Multi-file parallel `/cite`** — still one file at a time in v2
- **Verify-existing mode** — still deferred (was v1 deferral, stays deferred)
- **Move skills into the repo** — stays at `~/.claude/skills/` for v2; portability is a v3+ concern
