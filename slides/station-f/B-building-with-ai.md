---
marp: true
theme: station-f
paginate: true
header: "Building With AI · Station F · 2026-04-15"
footer: "Sources multiples · See docs/station-f/spec.md"
---

<!-- ABOUTME: Deck B of the Station F talk — methodology, MVP, business reality, EU regs. -->
<!-- ABOUTME: English-language scoped exception. Source of truth: docs/station-f/spec.md. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# From understanding to shipping.

## Building With AI — Part B

Station F · April 15, 2026

---

<!-- _class: compact -->

# 01 — The Bitter Lesson, for founders

Richard Sutton (2019) summarises **70 years of AI research** in one line:

> *"General methods that leverage computation are ultimately the most effective, and by a large margin."*

**The recurring pattern**:
- Researchers encode human knowledge → it works **short-term**, then plateaus
- General methods (Search + Learning) **always** win in the end
- Why? **Moore's Law** — compute doubles every ~2 years

**Examples**: Chess (Deep Blue — 1997), Go (AlphaGo — 2015), Speech (HMMs → Deep Learning), Vision (SIFT → CNNs → VLMs)

> **Founder takeaway**: general platforms (GPT, Claude, Gemini) beat bespoke solutions. Bet on compute, not on manual engineering.

<small>Sources : [1] [Richard Sutton — The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)</small>

---

<!-- _class: img-right -->

# 02 — Prompt-based development changes the cost structure

**Before (2015)** — gender detection on a photo:
- Collect **thousands** of labelled images
- Train a **first model** (face detection)
- Train a **second model** (gender classification)
- Complex pipeline, **months** of work

**Now (2025)** — same task:
- Image → VLM → structured output
- **0 training**, **0 data**, **days** to prototype
- Competitive performance

> The Bitter Lesson in action: general compute replaced specialised engineering.

![bg right:55% contain](assets/infographics/cv-before-vs-now_run_20260322_155403_87a8f5.png)

<small>Sources : [1] [Andrew Ng — Generative AI for Everyone](https://www.coursera.org/learn/generative-ai-for-everyone)</small>

---

<!-- _class: img-right -->

# 03 — The GenAI lifecycle: Scope → Build → Evaluate → Deploy

Every GenAI project follows an iterative 4-phase loop:

1. **Scope** — define project and success metrics
2. **Build** — assemble prompts, pipeline, tools
3. **Evaluate** — test internally, hunt edge cases
4. **Deploy** — staged rollout, monitor in production

> It is **not linear**. Feedback loops between stages are the norm — monitoring can send you back to Build or Evaluate.

![bg right:55% contain](assets/infographics/genai-lifecycle_run_20260216_171314_f23e16.png)

<small>Sources : [1] [Andrew Ng — Generative AI for Everyone](https://www.coursera.org/learn/generative-ai-for-everyone)</small>

---

# 04 — Baseline first, then iterate

The first iteration is different — the goal is a **reference point**, not a good model.

**The "AI toy model"**:
- **Classification** → predict the majority class (if most emails are non-spam, always predict non-spam)
- **Regression** → predict the mean value

**Then iterate**:
- Modify the system (prompt, model, pipeline)
- Keep a change **only if it improves the score**
- Every production miss → add it to the test dataset

> A baseline in 1 day beats a perfect model in 3 months. If your baseline already beats expectations, maybe you don't need ML at all.

---

# 05 — Building an MVP: 3 ingredients + the anti-pattern

An MVP is **not** a degraded version of the final product — it is the **simplest test** of your hypothesis.

**The 3 ingredients**:
- **Clear hypothesis** — "recruiters save 2h/day if AI pre-filters CVs"
- **Success metric** — filtering accuracy, time saved, NPS
- **Time-box** — 1–2 weeks max. If longer, your scope is too wide

**The "fake MVP" anti-pattern**:
- Building "the product" and calling it an MVP
- Adding features "just in case"
- Forgetting to measure

> **Gmail v0** = 1 feature (email search), 1 day, reused code. Everything else came after validation.

---

# 06 — MVP patterns: 5 ways to validate before you build

Before building a model, **5 patterns** to test for value [1]:

| Pattern | Principle | Cost | Example |
|---------|-----------|------|---------|
| **Wizard of Oz** | Human behind the curtain | EUR EUR | An expert answers as the AI would |
| **Concierge** | Manual service, automated promise | EUR EUR | Contract analysis done "by hand" |
| **Rule-Based First** | Simple rules before ML | EUR | Keyword filter before NLP |
| **Prompt Eng. MVP** | LLM via API, zero-code | EUR | GPT-4o prototype in 1 day |
| **API Wrapper** | Stitch existing APIs | EUR EUR | OCR + LLM + CRM combined |

> **Google "Rule of ML #1"**: if you can solve the problem without ML, do that first [2].

<small>Sources : [1] [MIT Sloan](https://sloanreview.mit.edu/article/what-is-a-minimum-viable-ai-product/) · [2] [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) · [3] [YC — Startup Ideas](https://www.youtube.com/watch?v=Th8JoIan4dg) · [4] [YC — Plan an MVP](https://www.youtube.com/watch?v=1hHMwLxN6EM)</small>

---

<!-- _class: compact -->

# 07 — The 6 pitfalls of AI Engineering (Chip Huyen)

Chip Huyen flags **6 recurring mistakes** in GenAI projects [1]:

1. **Using GenAI when you don't need to** — a classical algorithm often beats it
2. **Confusing "bad product" with "bad AI"** — Intuit fixed its tax chatbot by adding suggested questions, without touching the model [1]
3. **Starting too complex** — vector DB, agents, fine-tuning… before checking a plain prompt is not enough
4. **Overestimating early success** — LinkedIn reached *"80% of the experience they wanted"* in **1 month**, then needed **4 more months** to surpass 95% (Huyen doesn't name the specific metric — just "the experience" quality) [1]
5. **Neglecting compliance and safety** — copyright, privacy, abuse by bad actors
6. **Crowdsourcing use cases** — with no strategy you end up with "a million Slack bots" and zero ROI [1]

> *"It's easy to build a demo, but hard to build a product."* — Chip Huyen

<small>Sources : [1] [Chip Huyen — AI Engineering Pitfalls](https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html)</small>

---

# 08 — Rapid agent prototyping (Claude Code as harness)

Most teams **waste months** building agent infrastructure before validating the idea [1].

**Jason Liu's approach** — use Claude Code as the harness:
- `CLAUDE.md` = natural-language spec (mission, tools, success criteria)
- `tools/` = CLI scripts wrapping the real APIs
- `tests/` = scenarios with `request.txt` (input) + `check.py` (pass/fail)

**The decisive test**: if Claude Code cannot complete the task with perfect tool access, your production agent will not either.

> This is the **Prompt Engineering MVP** applied to agents. A passing test = concept validated [1].

<small>Sources : [1] [Jason Liu — Rapid Agent Prototyping](https://jxnl.co/writing/2025/09/04/context-engineering-rapid-agent-prototyping/)</small>

---

# 09 — Pricing is being reinvented

| Model | Share 2024 → 2025 [1] | Example | Price |
|-------|------------------------|---------|-------|
| Seat-based | 21% → **15%** | GitHub Copilot | $19–39/user/month |
| Hybrid | 27% → **41%** | Cursor | $20/month + credits |
| Outcome-based | Emerging | Intercom Fin | $0.99/resolution |
| Per-action | Emerging | Salesforce | $0.10/action |

- By 2030, **40%+** of SaaS spend usage/outcome-based [1]

> Same output costs less every quarter — **anticipate deflation**.

<small>Sources : [1] [Revenue Wizards — AI is Challenging Seat-Based Pricing](https://revenuewizards.com/blog/ai-is-challenging-seat-based-pricing)</small>

---

<!-- _class: img-right -->

# 10 — Klarna: replace → backlash → rehire

- **2022**: $1B losses → CEO hunts for cost cuts
- **2024**: AI chatbot handles **2/3 of chats**, replaces 700 agents, 11→2 min [1]
- **Late 2024**: **$40M** saved, return to profit ($244M loss → $21M profit)
- **Early 2025**: customer backlash, CEO admits *"we went too far"*
- **Mid 2025**: rehiring humans (400 SEK/h), H1 = **$152M loss** [2]

> **Augmentation > full replacement** — 2025's most expensive lesson.

![bg right:55% contain](assets/infographics/klarna-timeline_run_20260323_143048_2c1e7c.png)

<small>Sources : [1] [Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · [2] [Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)</small>

---

# 11 — L'Oréal + Doctolib: augmentation that works

- **L'Oréal** — acquired **ModiFace** (AR virtual try-on, 2018); **100M+ virtual try-on sessions in 2023** (+150% YoY) [1]; **8,000+** tech & data experts [2]
- **Doctolib** — **1.6M** AI consultations, **80M** users, **€5.8B** valuation — the doctor stays in the loop [3]

> **Pattern**: AI augments a domain expert, it does not replace them. The companies keeping the human in the loop are winning.

<small>Sources : [1] [PYMNTS — L'Oréal virtual try-on growth](https://www.pymnts.com/news/retail/2024/loreal-sees-150percent-increase-in-virtual-try-ons-as-consumers-seek-ar-immersion/) · [2] [L'Oréal Annual Report 2024](https://www.loreal-finance.com/en/annual-report-2024/beauty-tech-champion/) · [3] [Sifted — Doctolib 2024](https://sifted.eu/articles/doctolib-results-2024)</small>

---

<!-- _class: img-right -->

# 12 — EU AI Act — the 4 risk categories

![bg right:55% contain](assets/infographics/eu-ai-act-risk-pyramid.png)

- **Prohibited** — banned outright (social scoring, real-time biometrics) [1]
- **High-risk** — conformity assessment + human oversight (HR, credit, health, critical infra) [1]
- **Limited risk** — transparency only (chatbots, deepfakes) [1]
- **Minimal risk** — no obligations (most startup products) [1]

> If your product touches **HR, credit, health, or critical infra**, you're high-risk. Next slide is your deadline.

<small>Sources : [1] [Artificial Intelligence Act — high-level summary](https://artificialintelligenceact.eu/high-level-summary/)</small>

---

<!-- _class: compact -->

# 13 — EU AI Act: the one date

| Date | Who | What changes |
|------|-----|--------------|
| Feb 2025 | Everyone | Prohibited practices (social scoring, biometrics) |
| Aug 2025 | **GPAI** providers (GPT, Gemini, Mistral) | Tech docs, training-data summary |
| **Aug 2026** | **High-risk** providers (employment, credit, health) | **Full conformity + penalties** |
| Aug 2027 | High-risk embedded in already-regulated products | Same, dual-certification delay |

- Penalties: up to **€35M or 7%** of global revenue; compliance cost **€193K–330K** per system [1][2]
- EU AI Act applies to any AI sold in the EU, regardless of where the company is based

<small>Sources : [1] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/) · [2] [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

# 14 — 5 structural trends — and what to do this week

1. **Cost deflation** — inference cost drops **10×/year**; $1 today = $0.01 in 2 years [1]

2. **Moat shift** — value migrates from models to **data + workflows + harness**; the model alone is no longer your product [2]

3. **Pricing revolution** — seat-based shrinks (21% → 15%), hybrid dominates (**41%**), outcome-based emerges [3]

4. **AI augments, does not replace** — Klarna rehires, Doctolib keeps the doctor, Duolingo loses quality [4]

5. **Regulation creates markets** — EU AI Act opens a **billions-over-5-years** compliance market (CDI and CEPS differ on the exact range) [5][6]

> **Ship something this week.** Claude Code + a thoughtful `CLAUDE.md` + 3 tools = a working agent prototype.

<small>Sources : [1] [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends) · [2] [a16z](https://a16z.com/big-ideas-in-tech-2025/) · [3] [Industry pricing surveys](https://www.gartner.com/en/articles/ai-pricing-tips-control-costs-effectively) · [4] [Bloomberg](https://www.bloomberg.com/news/articles/2025-03-06/the-hottest-ai-companies-right-now-are-apps) · [5] [CDI](https://www2.datainnovation.org/2021-aia-costs.pdf) · [6] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/)</small>

---

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Questions.

![bg right:40% contain](assets/linkedin-qr-louis-develle.png)

## Louis Develle

[linkedin.com/in/louis-develle](https://www.linkedin.com/in/louis-develle/)
