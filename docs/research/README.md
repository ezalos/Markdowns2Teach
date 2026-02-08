# ABOUTME: Status and guide for the 13-topic research pipeline supporting course content.
# ABOUTME: Describes what's done, what's in progress, output formats, and how to use results.

# Research Pipeline — Status & Guide

## Purpose

This research pipeline produces structured, verified data to feed into Marp slide decks for the **Deep Tech & ML** M2 course at Sorbonne (5 sessions x 3h, ~15-20 business school students).

Each research topic goes through three phases:
1. **`/research`** — generates `outline.yaml` (items list) + `fields.yaml` (field definitions)
2. **`/research-deep`** — launches parallel web-search agents, produces one JSON per item in `results/`
3. **`/research-report`** — synthesizes all JSONs into a single `report.md`

---

## Completion Status (as of 2026-02-08)

| # | Topic | Session | Type | Status | Report |
|---|-------|---------|------|--------|--------|
| 2 | **AI Value Chain Companies** | 1 | Gap-filling | **DONE** | `ai-value-chain-companies/report.md` |
| 1 | **AI Market Intelligence 2024-2026** | 1 | Gap-filling | **DONE** | `ai-market-intelligence/report.md` |
| 3 | **Reasoning Models & SLMs 2025-2026** | 1 | Gap-filling | **DONE** | `reasoning-models-slms/report.md` |
| 8 | AI Tech Watch & Learning Resources | 1 | Gap-filling | Pending | — |
| 4 | No-Code & Low-Code AI Tools | 2 | Gap-filling | Pending | — |
| 12 | Advanced Prompt Engineering | 2 | Complement | Pending | — |
| 5 | AI Project Frameworks & Methodologies | 3 | Gap-filling | Pending | — |
| 9 | RAG Ecosystem & Implementation Tools | 3 | Complement | Pending | — |
| 10 | Fine-tuning & Model Customization | 3 | Complement | Pending | — |
| 6 | AI Business Model Patterns 2024-2026 | 4 | Gap-filling | Pending | — |
| 11 | Agentic AI & MCP Ecosystem 2025-2026 | 4 | Complement | Pending | — |
| 13 | AI Regulation, Ethics & Governance | 5 | Complement | Pending | — |
| 7 | AI Case Studies for Entrepreneurs | Cross | Gap-filling | Pending | — |

**"Gap-filling"** = content Andrew Ng doesn't cover at all.
**"Complement"** = deepens/updates what Andrew Ng covers in the existing 3 slide decks.

---

## Completed: AI Value Chain Companies

### What's in it
- **52 JSON files** covering 50 companies across 9 value chain layers (xAI has 2 entries: infrastructure + model)
- **Layers**: Energy Infrastructure → Hardware → Cloud → Data Infrastructure → Model Creators → Model Hubs → API/Orchestration/VectorDB → Evaluation/Safety/MLOps → Applications
- **Per company**: identity, value chain position, products, business metrics (revenue, ARR, funding, burn rate), openness spectrum, startup relevance, ecosystem/moats, regulatory exposure

### Key files
```
docs/research/ai-value-chain-companies/
├── outline.yaml              # 50 items, 9 layers, execution config
├── fields.yaml               # 22 fields across 8 categories
├── generate_report.py        # Script to regenerate report.md from JSONs
├── report.md                 # 4,396-line synthesized report (THE MAIN OUTPUT)
└── results/                  # 52 individual JSON files
    ├── NVIDIA.json
    ├── Mistral_AI.json
    ├── OpenAI.json
    └── ... (49 more)
```

### How to use `report.md` for slides
The report is organized by layer with:
- **Table of Contents** with summary columns (region, role, revenue, openness) — good for comparison table slides
- **Detailed company profiles** with sections: Identity, Value Chain, Products, Business, Openness, Startup Relevance, Ecosystem, Regulatory

**Suggested slide extraction patterns:**
- Layer overview slides: use TOC tables directly (one slide per layer)
- Company spotlight slides: pick 2-3 fields per company (e.g., revenue + moat + startup relevance)
- Comparison slides: cross-company tables by field (e.g., all model creators' openness spectrum)
- European focus slides: filter by `headquarters_region: EU` (Mistral AI, OVHcloud, Scaleway, Weaviate, Giskard, ElevenLabs, Hugging Face founders)
- Discussion slides: use `relevance_for_startups` field as prompts

### JSON structure (for programmatic access)
Each JSON follows this nested structure:
```json
{
  "identity": { "company_name": "...", "headquarters": "...", "headquarters_region": "US/EU/China/Other", "founded_year": 2023 },
  "value_chain": { "role_in_value_chain": "...", "value_chain_position": "...", "vertical_integration_level": "..." },
  "products": { "key_products": ["...", "..."] },
  "business": { "revenue_or_valuation": "...", "annual_recurring_revenue_arr": "...", "funding_total_and_last_round": "...", "business_model": "...", "burn_rate_and_runway": "..." },
  "openness": { "open_vs_closed_spectrum": "..." },
  "startup_relevance": { "relevance_for_startups": "...", "accessibility": "...", "primary_model_dependency": "..." },
  "ecosystem": { "key_partnerships": "...", "competitive_moat": "...", "data_moat_type": "..." },
  "regulatory": { "regulatory_exposure": "..." },
  "uncertain": ["field_name_1", "field_name_2"]
}
```
Fields listed in `uncertain` array or containing `[uncertain]` in their value have low confidence and should be treated carefully.

---

## Completed: AI Market Intelligence 2024-2026

### What's in it
- **41 JSON files** covering verified statistics across 10 categories
- **Categories**: Major Reports & Indices, Global Market Metrics, Cost & Efficiency, Adoption & Growth, Infrastructure & Strategic, Regional & European Focus, Labor & Talent, Risk & Governance, Competition & Ecosystem, Sector-Specific
- **Per metric**: identity (name, source, URL, date), value (figure, unit, scope, period), trend (direction, YoY change, CAGR, forecast), entrepreneurial relevance (why it matters, actionable insight, session mapping, risk profile), confidence (quality, cross-reference, caveats, reliability)

### Key files
```
docs/research/ai-market-intelligence/
├── outline.yaml              # 41 items, 10 categories, execution config
├── fields.yaml               # 25 fields across 5 categories
├── generate_report.py        # Script to regenerate report.md from JSONs
├── report.md                 # 3,267-line synthesized report (THE MAIN OUTPUT)
└── results/                  # 41 individual JSON files
    ├── Stanford_HAI_AI_Index_Report_2025.json
    ├── Stargate_Project.json
    ├── Mistral_AI_as_European_AI_Champion.json
    └── ... (38 more)
```

### How to use `report.md` for slides
The report is organized by category with:
- **Table of Contents** with summary columns (value, scope, trend, quality) — good for comparison slides
- **Detailed metric profiles** with 5 field sections per metric

**Suggested slide extraction patterns:**
- Market overview slides: use TOC tables directly (one slide per category)
- Stat spotlight slides: pick value + trend + entrepreneurial relevance from key metrics
- French/European focus slides: filter regional category (European AI Investment, French AI Ecosystem, Mistral AI)
- Risk/debate slides: use AI Bubble Risk Indicators, AI Safety Spending Gap, EU AI Act Economic Impact as discussion prompts
- Cost curve slides: Training Cost Reduction (280x), LLM API Pricing, SLM Economics

### JSON structure (for programmatic access)
Each JSON follows this nested structure:
```json
{
  "metric_identity": { "metric_name": "...", "source_report": "...", "source_url": "...", "publication_date": "...", "methodology_notes": "..." },
  "metric_value": { "value": "...", "unit": "...", "geographic_scope": "...", "time_period": "...", "comparison_baseline": "...", "market_layer": "..." },
  "trend": { "trend_direction": "...", "year_over_year_change": "...", "compound_annual_growth_rate": "...", "forecast_value": "...", "forecast_year": "...", "velocity_indicator": "..." },
  "entrepreneurial_relevance": { "relevance_for_entrepreneurs": "...", "actionable_insight": "...", "session_mapping": "...", "risk_profile": "..." },
  "confidence": { "data_quality": "...", "cross_reference": "...", "caveats": "...", "measurement_reliability": "..." },
  "uncertain": ["field_name_1", "field_name_2"]
}
```

---

## Completed: Reasoning Models & SLMs 2025-2026

### What's in it
- **33 JSON files** covering models across 4 categories
- **Categories**: Reasoning Models (12), Frontier General-Purpose (8), Small Language Models (10), Specialized Coding (3)
- **Per model**: identity (name, creator, release date, family), architecture (params, active params, type, context, output), capabilities (open/closed, license, reasoning, multimodal, multilingual, agentic), benchmarks (key benchmarks, reasoning composite), pricing (per 1M tokens, cost efficiency), deployment (hardware, quantization, on-device), business (use cases, entrepreneur relevance, competitive position, ecosystem, regulation)

### Key files
```
docs/research/reasoning-models-slms/
├── outline.yaml              # 33 items, 4 categories, execution config
├── fields.yaml               # 27 fields across 7 categories
├── generate_report.py        # Script to regenerate report.md from JSONs
├── report.md                 # 2,955-line synthesized report (THE MAIN OUTPUT)
└── results/                  # 33 individual JSON files
    ├── OpenAI_o3.json
    ├── DeepSeek-R1.json
    ├── Claude_Opus_4.6.json
    └── ... (30 more)
```

### How to use `report.md` for slides
The report is organized by model category with:
- **Table of Contents** with summary columns (params, open/closed, pricing, context) — good for comparison table slides
- **Detailed model profiles** with 7 field sections per model

**Suggested slide extraction patterns:**
- Category overview slides: use TOC tables directly (one slide per category)
- Model comparison slides: cross-model tables by field (e.g., all reasoning models' AIME scores)
- Cost comparison slides: pricing_per_1M_tokens across tiers (frontier vs SLM vs coding)
- European focus slides: Mistral models (Small 3, Medium 3.1, Large 3, Magistral Medium, Devstral 2, Codestral 2501, Ministral 3) + Falcon 3 (UAE)
- Open-weight slides: filter open_or_closed for self-hostable models (DeepSeek, Llama, Qwen, Mistral, Gemma, Phi, Falcon)
- Discussion slides: use relevance_for_entrepreneurs + geographic_origin_and_regulation fields
- EU regulatory slides: Llama 4 EU exclusion, DeepSeek GDPR concerns, Mistral GDPR-native advantage

### JSON structure (for programmatic access)
Each JSON follows this nested structure:
```json
{
  "identity": { "model_name": "...", "creator": "...", "release_date": "...", "model_family": "..." },
  "architecture": { "parameter_count": "...", "active_parameters": "...", "architecture_type": "...", "context_window": "...", "max_output_tokens": "..." },
  "capabilities": { "open_or_closed": "...", "license_type": "...", "reasoning_capability": "...", "multimodal_support": "...", "multilingual_support": "...", "agentic_capability": "..." },
  "benchmarks": { "key_benchmarks": "...", "reasoning_benchmarks_composite": "..." },
  "pricing": { "pricing_per_1M_tokens": "...", "cost_efficiency_notes": "..." },
  "deployment": { "minimum_hardware_requirement": "...", "quantization_availability": "...", "on_device_capable": "..." },
  "business": { "best_use_cases": "...", "relevance_for_entrepreneurs": "...", "competitive_position": "...", "ecosystem_and_tooling": "...", "geographic_origin_and_regulation": "..." },
  "uncertain": ["field_name_1", "field_name_2"]
}
```

---

## Pipeline for Remaining Topics

Execution order follows session priority:

**Session 1 block** (next):
- Research 3: Reasoning Models & SLMs — model comparison tables
- Research 8: Tech Watch & Learning Resources — curated reading list for students

**Session 2 block**:
- Research 4: No-Code & Low-Code AI Tools — tool comparison for hands-on exercises
- Research 12: Advanced Prompt Engineering — techniques beyond basics

**Session 3 block**:
- Research 5: AI Project Frameworks — CRISP-DM, AI Canvas, Build vs Buy
- Research 9: RAG Ecosystem — practical RAG stack guide
- Research 10: Fine-tuning Platforms — how to actually fine-tune

**Session 4 block**:
- Research 6: AI Business Models — pattern library with examples
- Research 11: Agentic AI & MCP — what's working in production

**Session 5 block**:
- Research 13: AI Regulation & Ethics — practical compliance + debate material

**Cross-session**:
- Research 7: AI Case Studies — 1-slide company stories, French/EU priority

---

## Content Conventions (for slide conversion)

- **Language**: French body, English technical terms used directly (no translation)
- **Framing**: Business-first for entrepreneurs, not researchers
- **Slide numbering**: `# 01 — Title` (2-digit, em dash), title/section slides unnumbered
- **Theme classes**: `title` (dark blue), `section` (light blue), `cols` (two-column)
- **Attribution**: footer on adapted slides citing sources
- **Engagement**: 1-2 discussion questions per major section

See `/CLAUDE.md` and `/docs/2026 M2 - ML & DeepTech.md` for full course plan and conventions.

---

## Existing Andrew Ng Slide Decks (already converted)

These 3 decks cover foundational GenAI concepts. The research topics above either fill gaps or extend/update what Andrew Ng covers:

| Deck | File | Slides | Content |
|------|------|--------|---------|
| 1 | `slides/andrew-ng-genai/deck-01-comprendre-genai/01-comprendre-genai.md` | ~40 | What is GenAI, LLMs, Supervised Learning, AI categories |
| 2 | `slides/andrew-ng-genai/deck-02-construire-genai/01-construire-genai.md` | ~40 | Lifecycle, RAG, Fine-tuning, Agents, Tool Use |
| 3 | `slides/andrew-ng-genai/deck-03-ia-business-societe/01-ia-business-societe.md` | ~38 | Business analysis, jobs, ethics, EU AI Act, bias |
