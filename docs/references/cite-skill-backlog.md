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

_(No open items. `/cite-apply` appends here when new caveats are surfaced.)_

---

## Resolved

### v2 (2026-04-13) — see `docs/superpowers/specs/2026-04-13-cite-skill-v2-design.md`

All 5 items below addressed by the v2 implementation. Quote-in-page substring check + page.txt preservation fix fabrication; tier lookup moved to `~/Setup/skills/cite/scripts/tier_lookup.py` (not subagent judgment); enum validation via `~/Setup/skills/cite/scripts/validate_claim.py`; verification command routing via `~/Setup/skills/cite/scripts/target_scope.py`; PDF fallback chain (tavily advanced → WebFetch → pdftotext) documented in the cite-research subagent prompt.

## 2026-04-13 — docs-references-test-fixtures-cite-fixture (initial integration test)

- **research**: Subagent assigned `authority_tier: 1` to a URL whose domain (`encyclopedia.pub`) is not in the authority-map baseline, because the page cites a tier-1 primary source.
  - Context: claim-01 (Flash Crash). Subagent picked encyclopedia.pub as "high-quality secondary source" and promoted to tier 1 based on what it cites, not what it is.
  - Suggestion: tighten cite-research subagent prompt so `authority_tier` is derived ONLY from the URL domain match against the authority map. No promotion from "source cites tier-1 primary". Unmapped domain → `tier: null` + `flagged-low-reputation` with a clear message to re-research with the primary URL.

- **research**: Subagent fabricated `surrounding_paragraph` by combining partial Tavily Extract content with content from a different source.
  - Context: claim-02 (Dow -9%). SEC PDF extract was partial; subagent reconstructed the paragraph using claim-01's encyclopedia.pub text. This crosses a hard line — the field's purpose is verbatim verifiable content.
  - Suggestion: add explicit "DO NOT fabricate or combine content from multiple sources in surrounding_paragraph" rule. If extract is partial, note the limitation in an `extraction_note` field and set `confidence: medium` with only the actually-extracted text.

- **research**: Subagent used out-of-enum `status` value and wrong `proposed_action`.
  - Context: claim-03 (EU AI Act adoption). Returned `status: sourced` instead of one of `auto-approved | flagged-low-reputation | flagged-unsourceable | flagged-stale-stat`. Set `proposed_action: null` instead of `add-citation`.
  - Suggestion: cite-research subagent prompt should explicitly enumerate valid status values and action values, and reject any other strings. Consider a validation step in the orchestrator.

- **tool**: `/cite-apply` Step 6 runs `make check`/`check-citations`/`html` which scan `slides/` only, missing targets under `docs/references/` or `docs/research/`.
  - Context: integration test fixture lived under `docs/references/test-fixtures/` — `make check` ran against the whole `slides/` project (2+ minutes, killed) and did not validate the fixture. Targeted `bash scripts/check-citations.sh docs/references/test-fixtures/` worked.
  - Suggestion: `/cite-apply` should (a) run `check-citations.sh` against the target file's directory, (b) render just the target via marp CLI for Marp-syntax validation, or (c) explicitly restrict v1 scope to targets under `slides/` and document this precondition.

- **tool**: Tavily Extract returned partial content for a large government PDF (~100 pages).
  - Context: SEC/CFTC Joint Report PDF for claim-02. Subagent got a fragment that didn't contain the specific sentence needed, though a corroborating figure was in the extract.
  - Suggestion: for PDFs over N pages, skill could chain multiple Extract calls with different `query` parameters to pull targeted chunks, OR fall back to downloading the PDF and using a local PDF-to-text subagent.

## Follow-ups (2026-07-13 deck-capability final review)

- **tool**: `check-citation-links.py`'s `data-file-source` exemption is element-wide, not
  per-source — a footer that mixes a clickable `<a>` citation with a `.file-src` span
  in the SAME sources element escapes the no-clickable-link check entirely instead of
  being checked source-by-source. Tighten the check to per-source granularity so a
  file-backed source can't accidentally shield an adjacent bare/non-clickable URL
  citation in the same element.
- **tool**: `slides/rlaif-vlm/rlaif-vlm.html` lacks the `window.deck` API other decks
  expose, so `make test-decks` cannot drive it (no programmatic slide navigation to
  screenshot/inspect). Either retrofit the deck with the standard `window.deck` API or
  explicitly exempt it in `test-decks` with a documented reason.
- **tool**: `lint_authority_map.py`'s `only_in_md` branch (entries present in the `.md`
  roster but missing from the `.yaml`) has no test coverage in the global skill's suite —
  add one so a regression there isn't silent.
- **process**: keep a reproducible layout-check script (à la `check-slide-overlap.js` /
  `check-overflow-visual.js`) usable on decks `test-decks` can't drive, so overflow/overlap
  regressions on those decks are still caught mechanically instead of only by eyeballing.
