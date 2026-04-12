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
