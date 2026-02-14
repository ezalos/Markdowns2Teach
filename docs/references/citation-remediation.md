# Citation Remediation Plan

<!-- ABOUTME: Systematic plan to audit and fix all unsourced data claims across 9 slide decks. -->
<!-- ABOUTME: Covers tooling, claim classification, search protocol, and per-file remediation. -->

## 1. Tooling

| Tool | Purpose | Free Tier |
|------|---------|-----------|
| **Brave Search MCP** | Web search for finding authoritative sources | 2,000 queries/month |
| **Tavily MCP** | Extract clean content from URLs to verify numbers | 1,000 credits/month |
| **WebSearch** (built-in) | Baseline web search | Unlimited |
| **WebFetch** (built-in) | Baseline page fetching | Unlimited |
| **Perplexity MCP** (fallback) | Synthesized answers with citations | ~$5/1000 queries |

## 2. Claim Classification

### Needs a source (`[1]` + `<small>Sources</small>`):

- Any **number**: dollar amounts, percentages, growth rates, market sizes, headcounts
- Any **named statistic**: "X% of companies do Y"
- Any **company-specific fact**: revenue, valuation, funding round, user count
- Any **benchmark result**: accuracy scores, error rates, performance comparisons
- Any **pricing data**: API costs, subscription prices, cost ranges
- Any **prediction/forecast**: "market will reach $X by 2030"

### Does NOT need a source:

- **Logical deductions**: reasoning, not data claims
- **Definitions**: textbook-level explanations of concepts
- **Pedagogical framing**: metaphors, teaching analogies
- **Tool descriptions** (without stats): what a tool does, not how many users it has
- **Discussion questions**: no factual claim

### Grey zone — resolve toward sourcing:

- "Andrew Ng says X" → Find where Ng got it from. Cite the upstream source, not Ng.
- "It's well known that..." → If it has a number, source it.
- "Estimations sectorielles" or "Estimations développeurs" → **Not real sources**. Replace with actual survey/report or soften the language.

## 3. Source Search Protocol

### Step 1 — Where to look by claim type:

| Claim Type | Primary Sources | Search Strategy |
|------------|----------------|-----------------|
| Market size / forecast | Gartner, IDC, Statista, McKinsey, CB Insights | `"[topic] market size 2025" site:gartner.com OR site:statista.com` |
| Company financials | Company IR pages, SEC filings, Bloomberg | `"[company] revenue 2024" site:investor.[company].com` |
| Adoption / survey stats | McKinsey, Deloitte, Stanford HAI AI Index | `"[stat]" survey 2024 2025` |
| Benchmark results | Original papers (arXiv), HuggingFace, WizWand | `"[model] [benchmark]" site:arxiv.org` or huggingface.co or wizwand.com |
| API pricing | Provider pricing pages directly | Go to openai.com/pricing, anthropic.com/pricing, etc. |
| Historical events | Reuters, Bloomberg, NYT, court records | `"[event]" [year] site:reuters.com OR site:nytimes.com` |
| EU regulation | EUR-Lex, European Parliament, CEPS | `"EU AI Act" [specific provision]` |

### Step 2 — Authority hierarchy:

1. **Company IR / SEC filings** — audited numbers
2. **Peer-reviewed papers** (arXiv, NeurIPS, ICML) — benchmarks and technical claims
3. **Tier-1 research** (Gartner, McKinsey, Stanford HAI, OECD) — market/adoption data
4. **Tier-1 press** (Bloomberg, Reuters, CNBC, Financial Times) — news/funding/events
5. **Tier-2 press** (TechCrunch, The Verge, Ars Technica) — when above unavailable
6. **Crunchbase / Sacra / PitchBook** — startup valuations/funding when no press coverage

### Step 3 — Recency filter:

- **Hard reject**: source > 2 years old for any AI market/adoption claim
- **Exception**: historical facts (AlexNet 2012, Flash Crash 2010) and legal precedents
- **Prefer**: source < 6 months old when available
- **Conflict resolution**: most recent wins, unless older source is significantly more authoritative

### Step 4 — Verification:

Use Tavily extract to read the actual page and confirm the number matches. Don't trust search snippets.

### Step 5 — Citation format:

```markdown
- Le marché atteint **$7 Mds** en 2025 [1]

<small>Sources : [1] [Precedence Research](https://full-url) · [2] [Gartner](https://full-url)</small>
```

- Authority shorthand as display text
- Full URL as href
- ` · ` separator between sources
- `[N]` markers correspond between in-text and footer
- One `<small>Sources</small>` line per slide, at bottom

## 4. Remediation Backlog

### Audit Summary: 30 uncited claims + 1 informal citation + 2 fake sources

| Priority | File | Issues | Key Claims |
|----------|------|:------:|------------|
| P1 | `session-02/A-prompt-au-produit.md` | 5 | API pricing table, "90% projects", "~7 mois", "~10x price drop" |
| P2 | `session-05/A-regulation-ethique.md` | 6 | Flash Crash $1T, Amazon recruiting, Meta RAI, Thomson Reuters v. Ross |
| P3 | `session-01/B-au-dela-des-llms.md` | 5+1 | ImageNet, AlexNet, CNN benchmarks, "(Gartner)" informal, SLM pricing |
| P4 | `session-03/B-methodologie-projet.md` | 4 | Fake "Estimations sectorielles", CRISP-DM "400+ citations", "50-70%" |
| P5 | `session-04/A-ecosysteme-ia.md` | 3 | Fake "Estimations développeurs" (CUDA 98%), cloud market share, ASML |
| P6 | `session-04/B-business-models.md` | 3 | API pricing table, OpenAI $57B funding, L'Oréal experts/patents |
| P7 | `session-03/A-evaluer-solution-ia.md` | 2 | Cost table ranges, "65% surcoûts" stat |
| P8 | `session-02/B-ingenierie-ia.md` | 1 | Embedding model pricing |
| P9 | `session-01/A-genai-fondamentaux.md` | 1 | "Supervised Learning most deployed" claim |

### Per-file process:

1. Subagent reads the file, extracts all uncited claims with line numbers
2. Search agent runs protocol: Brave Search → authority hierarchy → recency filter
3. Tavily extracts source page to verify exact numbers
4. If claim can't be sourced: soften language or flag for Louis
5. Agent edits file: adds `[N]` markers and `<small>Sources</small>` footers
6. Run `make check` + `make check-citations`

### Parallelization:

- Files are independent — process 2-3 concurrently
- Budget: ~65 Brave queries per file (2,000 total / 30 claims with margin)
- Tavily: ~1 credit per URL verification

## 5. Verification Gate

After all edits:

```bash
make check           # overflow linter (15-line threshold)
make check-citations # all data slides have sources
make html            # clean build
```

## 6. Unsourceable Claims Protocol

If a claim cannot be sourced after reasonable search effort:

1. **Soften**: Replace exact number with "environ", "de l'ordre de", "plusieurs"
2. **Remove**: Delete the specific stat if the slide works without it
3. **Flag**: Mark with `<!-- TODO: source needed for [claim] -->` for Louis to decide
4. **Never**: Invent a source or cite a secondary source that doesn't contain the actual data
