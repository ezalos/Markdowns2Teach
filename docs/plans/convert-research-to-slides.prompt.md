# Convert Research Topic to Marp Slide Deck

<!-- ABOUTME: Standalone prompt for a new Claude Code session to convert a completed research topic into slides. -->
<!-- ABOUTME: Point to this file + the research directory, and the session can work autonomously. -->

## Your Task

Convert a completed research topic into a Marp slide deck for the M2 Entrepreneuriat course at Sorbonne.

**You will be given**: a path to a research directory (e.g. `docs/research/ai-market-intelligence/`) containing `report.md` and `results/*.json`.

## Step-by-Step Process

### Phase 1: Read the references

1. Read the conversion template: `plans/research-to-slides-template.md` — this is your playbook
2. Read the reference deck: `slides/ai-value-chain/01-ai-value-chain.md` — match this style exactly
3. Read the project conventions: `CLAUDE.md` — especially slide standards and language rules

### Phase 2: Analyze the source material

4. **Use a subagent** to read `report.md` and extract structured data:
   - Identify all categories/layers/sections
   - Count total items (companies, tools, frameworks, etc.)
   - Build tables per category: Name, Country, Key Metric, Role
   - Flag EU/French items to weave throughout
5. **Use a subagent** to read 4-6 spotlight JSONs from `results/*.json`:
   - Pick diverse, interesting items relevant to the audience (business school entrepreneurs)
   - Prioritize: at least 1 French/EU item, 1 market leader, 1 surprising underdog
   - Extract: financials, products, moats, startup lessons

> **CRITICAL**: Do NOT read large files (report.md, PDFs) directly in the main context. Always use subagents. Large files cause context window compaction failures.

### Phase 3: Plan the deck

6. Estimate slide count using the template formula (~25-30 slides)
7. Draft a slide-by-slide outline before writing:
   - Title slide + 1-2 intro slides
   - 1-2 slides per category (tables capped at 7 rows, split if needed)
   - 1 spotlight per ~8-10 items (use `_class: cols`)
   - 1 discussion question per major section
   - 2-3 synthesis slides + Key Takeaways

### Phase 4: Write the deck

8. Create directory: `slides/<research-slug>/assets/`
9. Write the slide deck following all conventions from the template:
   - Front matter with sorbonne theme
   - ABOUTME comments after front matter
   - `# 01 — Title` numbering (2-digit, em dash), title/section slides unnumbered
   - French body, English technical terms used directly (no translations)
   - `_class: title`, `_class: section`, `_class: cols` as appropriate
   - Footer: `"Recherche [Topic] 2024–2026 · Données publiques"`
   - **Citations**: every data claim needs `[1]` in-text + `<small>Sources : [1] [Authority](url)</small>` at slide bottom
   - Source URLs from research JSONs or official company/report pages
   - Discussion slides and section dividers may omit citations if no data claims

### Phase 5: Verify and fix

10. Fix CRLF line endings: `sed -i 's/\r$//' <file>` (the Write tool may produce CRLF)
11. Run `make check` — fix any overflow violations (15-line threshold, budget ~13 with sources)
12. Run `make check-citations` — fix any missing citation warnings for the new deck
    - **cols slides**: div tags count as content lines — budget only ~10 lines of actual content
    - **Tables**: cap at 7 rows, split across 2 slides if needed
    - Avoid `###` subheaders inside cols — they waste a line
13. Run `make html` — verify clean build, no errors
14. Report what was created: slide count, spotlight list, discussion questions, citation count

## Naming Convention

```
slides/<research-slug>/
├── 01-<topic-name>.md
└── assets/
```

Derive the slug from the research directory name. Examples:
- `docs/research/ai-market-intelligence/` → `slides/ai-market-intelligence/01-ai-market.md`
- `docs/research/prompt-engineering/` → `slides/prompt-engineering/01-prompt-techniques.md`

## Quality Checklist

Before reporting done:

- [ ] `make check` passes (0 overflow warnings)
- [ ] `make check-citations` passes for the new deck (all data slides have sources)
- [ ] `make html` builds without errors
- [ ] ABOUTME comments present
- [ ] Numbering correct (01-XX continuous, title/section unnumbered)
- [ ] French body + English tech terms (no parenthetical translations)
- [ ] EU companies woven throughout, not isolated
- [ ] Discussion questions are concrete entrepreneur scenarios
- [ ] All financial figures match report.md source data
- [ ] No slide has subheaders inside cols layout
