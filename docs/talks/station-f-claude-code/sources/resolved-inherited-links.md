<!-- ABOUTME: Resolution of the 12 text-only source mentions inherited from the heuritech deck (ledger section B). -->
<!-- ABOUTME: Every URL fetched live and every quote grepped character-by-character with verify-sources.py's norm() contract on 2026-08-31. -->

# Resolved inherited links — Station F talk

**Resolved**: 2026-08-31. **Method**: `curl` + a local re-implementation of
`scripts/verify-sources.py`'s `norm()` (entity-unescape → NFKC → quote/dash unification →
whitespace collapse), matched against both the raw body and the tag-stripped body — i.e. the
*exact* check `make export-pdf-*` will run. Nothing below is proposed on memory or on a search
snippet; every `quote:` was grepped and returned a hit.

**Score: 12 / 12 resolved to a live exact URL with a verified verbatim quote — but 4 of them
change what the deck is allowed to say.** See [Failures & claim changes](#failures--claim-changes-read-this-first)
first; it is the part that blocks the build.

---

## Failures & claim changes (READ THIS FIRST)

| # | What broke | Consequence |
|---|-----------|-------------|
| **3** | `llm-stats.com/frontiercode` is a **hard 404**. The real path is `/benchmarks/frontiercode`. | Dead link would have shipped. Fixed below. |
| **3** | The deck says *"today Claude Fable 5 leads FrontierCode Diamond"*. **False on both halves.** Live leaderboard 2026-08-31: **Grok 4.6 (xAI) 0.613** leads; Claude Opus 5 0.534; **Claude Fable 5 is 3rd at 0.463**. And Cognition **deprecated the Diamond subset** in FrontierCode 1.1 (2026-07-07). | **The S15 sentence must be rewritten.** Also: llm-stats flags this benchmark `0 verified / 4 self-reported` — the caveat must travel. |
| **8** | `anthropic.com/research/building-effective-agents` **301s** to `/engineering/…`. And **no contiguous sentence on that page names the five patterns** — they are five separate `Workflow:` H3 headings (text offsets 4846 → 9009). | Cite the canonical `/engineering/` URL. **A "names the five patterns" quote does not exist**; use the verified `building blocks` quote instead. Do not fabricate one. |
| **9** | **`mistral.ai` has no page supporting "open-weights track close behind."** Its homepage says only *"In-region inference, open models, and new European infrastructure for sovereign AI"* — a product line, not a capability-gap measurement. | **Replace the source**, not the wording: Epoch AI measures the gap at **4 months**. Entry below. |
| **12b** | **Boris Cherny has no primary, linkable, first-person source for "loops built into the harness."** His own on-record loop content is a Bloomberg video interview surfaced only through third-party quote-tweets. His `/loop`-adjacent tweet (2007179847949500714) is about `.claude/commands/` slash commands, **not** `/loop` — citing it for this claim is a misattribution. | Either drop the name and cite Anthropic's loops post (already in the parent registry), or keep the name behind a **labelled secondary**. Both options below. |
| **11** | The *viral* "Karpathy CLAUDE.md" (`multica-ai/andrej-karpathy-skills`) was **written by Forrest Chang from Karpathy's X observations — not by Karpathy.** Karpathy does publish a real one, in `karpathy/llm-council`. | Cite the real one (below). **Do not present the viral repo as his.** Note it is project-specific technical notes, so *"a great model to steal from"* oversells it. |

Also worth knowing (not a failure): `docs.claude.com` is in `check-citation-links.py`'s
`REDIRECT_HOSTS` — **every** `docs.claude.com` URL is rejected offline. Both #4 and #5 must be
cited at their canonical `code.claude.com` homes.

---

## Ready-to-paste `sources.yml` blocks

All verified `FOUND`. Paste under `sources:` in `slides/station-f-claude-code/sources.yml`,
adjusting `slides:` keys to the final slide numbering.

```yaml
  # ---- 1. Skills are markdown recipes (S21) ----
  - id: agentskills-overview
    url: https://agentskills.io/home
    authority: Agent Skills (open specification)
    title: "Agent Skills Overview"
    quote: "At its core, a skill is a folder containing a SKILL.md file"
    slides: [21]

  # ---- 2. Skill supply-chain security (S21) ----
  - id: snyk-skill-md-shell-access
    url: https://snyk.io/articles/skill-md-shell-access/
    authority: Snyk
    title: "From SKILL.md to Shell Access in Three Lines of Markdown: Threat Modeling Agent Skills"
    quote: "treat third-party skills as trusted code. Read them before enabling"
    slides: [21]

  # ---- 2b. OPTIONAL corroborating primary: the measured scale of the problem ----
  - id: snyk-toxicskills
    url: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
    authority: Snyk (Beurer-Kellner et al., 2026-02-05)
    title: "Snyk Finds Prompt Injection in 36%, 1467 Malicious Payloads in a ToxicSkills Study of Agent Skills Supply Chain Compromise"
    quote: "Audit installed skills immediately"
    slides: [21]

  # ---- 3. Build with the best model available — LIVE leaderboard (S15) ----
  # WAS llm-stats.com/frontiercode -> HTTP 404. Correct path is /benchmarks/frontiercode.
  - id: llmstats-frontiercode
    url: https://llm-stats.com/benchmarks/frontiercode
    authority: LLM Stats
    title: "FrontierCode Leaderboard"
    quote: "Grok 4.6 from xAI currently leads the FrontierCode leaderboard"
    slides: [15]

  # ---- 3b. The benchmark's own primary + the Diamond deprecation ----
  - id: cognition-frontiercode
    url: https://cognition.com/frontiercode
    authority: Cognition
    title: "FrontierCode Leaderboard (methodology)"
    quote: "deprecates the Diamond subset"
    slides: [15]

  # ---- 4. CLAUDE.md / standing instructions (S19) ----
  # WAS docs.claude.com -> in REDIRECT_HOSTS; canonical home is code.claude.com.
  - id: claude-code-memory
    url: https://code.claude.com/docs/en/memory
    authority: Anthropic (Claude Code docs)
    title: "How Claude remembers your project"
    quote: "You write these files in plain text; Claude reads them at the start of every session"
    slides: [19]

  # ---- 5. Permissions & auto mode (S18) — A DIFFERENT PAGE from #4 ----
  # Note: /iam is now "Authentication"; the permissions content lives at /permissions.
  - id: claude-code-permissions
    url: https://code.claude.com/docs/en/permissions
    authority: Anthropic (Claude Code docs)
    title: "Configure permissions"
    quote: "Claude Code uses a tiered permission system to balance power and safety"
    slides: [18]

  # ---- 6. Definition of an agent (S12) ----
  - id: anthropic-context-engineering
    url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    authority: Anthropic Engineering
    title: "Effective context engineering for AI agents"
    quote: "a simple definition for agents: LLMs autonomously using tools in a loop"
    slides: [12]

  # ---- 7. Model Context Protocol announcement (S22) ----
  - id: anthropic-mcp-announcement
    url: https://www.anthropic.com/news/model-context-protocol
    authority: Anthropic
    title: "Introducing the Model Context Protocol"
    quote: "replacing fragmented integrations with a single protocol"
    slides: [22]

  # ---- 8. The five orchestration patterns (S34) ----
  # WAS /research/... -> 301s to /engineering/... Cite the canonical.
  # NOTE: no sentence on this page names all five patterns; see the notes section.
  - id: anthropic-building-effective-agents
    url: https://www.anthropic.com/engineering/building-effective-agents
    authority: Anthropic Engineering
    title: "Building Effective AI Agents"
    quote: "These building blocks aren't prescriptive. They're common patterns that developers can shape and combine"
    slides: [34]

  # ---- 9. Open-weights track close behind (S09) ----
  # REPLACES the mistral.ai mention, which supports nothing of the kind.
  - id: epoch-open-closed-gap
    url: https://epoch.ai/data-insights/open-closed-eci-gap
    authority: Epoch AI (Edwards & Emberson, 2026-05-29)
    title: "Open models lag state-of-the-art closed models by 4 months"
    quote: "the most capable open-weight models have lagged frontier closed models by an average of four months"
    slides: [9]

  # ---- 10a. EU sovereign inference — Mistral (A01) ----
  - id: mistral-data-residency
    url: https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data
    authority: Mistral AI (Help Center)
    title: "Where do you store my data or my Organization's data?"
    quote: "By default, your data is hosted in the European Union"
    slides: [35]

  # ---- 10b. EU sovereign inference — Scaleway (A01) ----
  - id: scaleway-generative-apis
    url: https://www.scaleway.com/en/generative-apis/
    authority: Scaleway
    title: "Generative APIs - Serverless"
    quote: "Towards a sovereign AI where your data remains yours, and only in Europe"
    slides: [35]

  # ---- 11. Karpathy's published CLAUDE.md (S19) ----
  - id: karpathy-claude-md
    url: https://github.com/karpathy/llm-council/blob/master/CLAUDE.md
    authority: GitHub (Andrej Karpathy)
    title: "llm-council — CLAUDE.md"
    quote: "This file contains technical details, architectural decisions, and important implementation notes"
    slides: [19]

  # ---- 12a. Steinberger — design loops, don't prompt agents (S35) ----
  - id: steinberger-design-loops
    url: https://x.com/steipete/status/2063697162748260627
    authority: X (Peter Steinberger, 2026-06-07)
    title: "You should be designing loops that prompt your agents"
    quote: "You should be designing loops that prompt your agents"
    slides: [35]

  # ---- 12b. Loops are built into the harness — /loop (S35) ----
  # PRIMARY, replaces the un-sourceable "Boris Cherny" attribution.
  - id: claude-code-slash-commands
    url: https://code.claude.com/docs/en/slash-commands
    authority: Anthropic (Claude Code docs)
    title: "Slash commands"
    quote: "Claude Code includes a set of bundled skills"
    slides: [35]

  # ---- 12b-alt. ONLY if Louis insists on keeping Cherny's NAME on the slide. ----
  # This is a THIRD PARTY quoting a Bloomberg interview. Secondary. Label it as such
  # on the slide or drop it — do not present it as Cherny publishing.
  - id: cherny-agents-to-loops-secondary
    url: https://x.com/0xDepressionn/status/2070468357539635626
    authority: X (@0xDepressionn, quoting Boris Cherny, 2026-06-26)
    title: "Boris Cherny: going from agents to loops"
    quote: "Going from agents to loops is as big a jump as going from code to agents"
    slides: [35]
```

---

## Per-item detail

### 1. `agentskills.io` → skills are markdown recipes — **REGISTER**
- **Claim**: "A skill is just a markdown recipe — one folder, one markdown file."
- **URL**: `https://agentskills.io/home` (`https://agentskills.io` 302s here; the bare domain
  would be rejected by the linter anyway).
- **Verdict on "thin marketing page": NO — the opposite.** It is the official Agent Skills
  specification site (`agentskills/agentskills`), with Overview / Specification / Best practices /
  Client implementation sections. It is a **better** source for the *"one folder, one markdown
  file"* claim than the Anthropic post, because it states the file layout literally.
- **Quote**: `At its core, a skill is a folder containing a SKILL.md file` — **VERIFIED**
  (HTTP 200; 1 hit in tag-stripped body).
- **Recommendation**: **Register.** Keep `anthropic-agent-skills` alongside it — they carry
  different halves of S21 (format vs. why-it-works). Not a replacement.

### 2. `snyk.io` → read external skills before installing — **REGISTER**
- **Claim**: "External skills are instructions you didn't write. Read them before installing."
- **URL**: `https://snyk.io/articles/skill-md-shell-access/` — "From SKILL.md to Shell Access in
  Three Lines of Markdown: Threat Modeling Agent Skills".
- **Quote**: `treat third-party skills as trusted code. Read them before enabling` — **VERIFIED**.
  This is Snyk quoting the ecosystem's own official guidance, then documenting that it fails at
  scale — which is exactly the deck's reflex, from a security authority.
- **Optional corroboration**: `https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/`
  (ToxicSkills, 2026-02-05) — quote `Audit installed skills immediately` **VERIFIED**. Carries the
  measured scale (36% prompt injection, 1467 malicious payloads) if S21 wants a number.
- **Recommendation**: **Register** the first; add the second only if the slide states a figure.

### 3. `llm-stats.com/frontiercode` → build with the best model — **BROKEN, FIXED, CLAIM MUST CHANGE**
- **`https://llm-stats.com/frontiercode` → HTTP 404.** Correct: `https://llm-stats.com/benchmarks/frontiercode` (200).
- **Live snapshot, 2026-08-31** (the page's own "Last updated: August 31, 2026"):

  | # | Model | Score | Price in/out |
  |---|-------|-------|--------------|
  | 1 | **Grok 4.6** (xAI) | **0.613** | $2.00 / $6.00 |
  | 2 | Claude Opus 5 (Anthropic) | 0.534 | $5.00 / $25.00 |
  | 3 | **Claude Fable 5** (Anthropic) | **0.463** | $10.00 / $50.00 |
  | 4 | Claude Sonnet 5 (Anthropic) | 0.388 | $2.00 / $10.00 |

- **The deck's claim is wrong twice over.** (a) Claude Fable 5 does **not** lead — it is third,
  15 points behind Grok 4.6. (b) **"FrontierCode Diamond" no longer exists**: Cognition's
  FrontierCode 1.1 (2026-07-07) *"deprecates the Diamond subset"*.
- **Third caveat**: llm-stats marks this benchmark **`Verification: Unverified — 0 verified,
  4 self-reported`**. Every number above is vendor self-report.
- **Quotes** — `Grok 4.6 from xAI currently leads the FrontierCode leaderboard` **VERIFIED** on
  llm-stats; `deprecates the Diamond subset` **VERIFIED** on `https://cognition.com/frontiercode`.
- **Caution**: `cognition.com/frontiercode` renders its table client-side ("Loading leaderboard…"),
  so **only its methodology prose is text-verifiable** — never quote a number from it. Numbers come
  from llm-stats, which is server-rendered.
- **Recommendation**: **Register both.** **Rewrite the S15 sentence** — the pedagogical point
  ("build with the best model available, check the leaderboard on the day") survives intact and is
  arguably stronger now that the leader is not the house model. Re-snapshot on talk morning.

### 4. `docs.claude.com` → CLAUDE.md / standing instructions — **REGISTER (canonical host)**
- **URL**: `https://code.claude.com/docs/en/memory` — "How Claude remembers your project".
  (`docs.claude.com/en/docs/claude-code/memory` 301s here **and** is rejected offline by
  `check-citation-links.py`'s `REDIRECT_HOSTS`.)
- **Quote**: `You write these files in plain text; Claude reads them at the start of every session`
  — **VERIFIED**. Alternate, equally verified: `CLAUDE.md files are loaded into the context window
  at the start of every session`.

### 5. `docs.claude.com` (iam) → permissions & auto mode — **REGISTER (different page)**
- **URL**: `https://code.claude.com/docs/en/permissions` — "Configure permissions".
- **`/iam` is now "Authentication"** (plans, SSO, billing) — the permissions content moved to its
  own page. Citing `/iam` today would point at the wrong document.
- **Quote**: `Claude Code uses a tiered permission system to balance power and safety` — **VERIFIED**.
  Two more, both **VERIFIED**, if the slide wants the default-vs-auto contrast literally:
  - `Prompts for permission on first use of each tool` (the `default`/Manual mode row)
  - `Auto-approves tool calls with background safety checks that verify actions align with your request` (the `auto` mode row)
- **Confirmed distinct from #4** — different page, different content, both required.

### 6. `anthropic.com` → the definition of an agent — **REGISTER, with a caveat**
- **URL**: `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`.
- **Quote**: `a simple definition for agents: LLMs autonomously using tools in a loop` — **VERIFIED**.
  Full sentence on the page: *"Since we wrote that post, we've gravitated towards a simple definition
  for agents: LLMs autonomously using tools in a loop."* This is Anthropic explicitly labelling it
  **their definition** — the strongest thing available.
- **Caveat, stated plainly**: the deck's five-fragment wording ("a system / which uses tools / to
  interact repeatedly / with its environment / to accomplish its goal") is **not** an Anthropic
  quote and is nowhere on anthropic.com. It is Louis's paraphrase. That is fine on a slide as long
  as it isn't in quotation marks and isn't attributed as Anthropic's words.
- Second-choice quotes, both **VERIFIED** on `building-effective-agents`:
  `are systems where LLMs dynamically direct their own processes and tool usage, maintaining control
  over how they accomplish tasks` and `using tools based on environmental feedback in a loop`. Using
  the context-engineering page keeps #6 and #8 on separate URLs, which reads better on the deck.

### 7. `anthropic.com/news` → MCP announcement — **REGISTER**
- **URL**: `https://www.anthropic.com/news/model-context-protocol` (200, no redirect).
  Note `anthropic.com/news` bare is in `INDEX_DENYLIST`; the article path passes.
- **Quote**: `replacing fragmented integrations with a single protocol` — **VERIFIED**. This is the
  M×N → M+N argument in Anthropic's own words, which is exactly what the two S22 schemas teach.

### 8. `anthropic.com/research/building-effective-agents` — **REGISTER at the canonical URL; the "five patterns" quote does not exist**
- **The cited URL 301s**: `/research/building-effective-agents` → `/engineering/building-effective-agents`.
  It survives the offline linter (only the bare `/research` index is denylisted) and
  `verify-sources.py` follows redirects — but citing a stale URL in a deck whose whole contract is
  "the exact page" is indefensible. **Cite `/engineering/…`.**
- **The five patterns are five separate `Workflow:` H3 headings**, at text offsets 4846
  (Prompt chaining), 5646 (Routing), 6595 (Parallelization), 8116 (Orchestrator-workers), 9009
  (Evaluator-optimizer). There is **no sentence, list, or TOC anywhere in the fetched body that
  names all five contiguously** — I checked raw HTML and tag-stripped text, and the concluding
  "Combining and customizing these patterns" section names none of them.
- **So: a "names the five patterns" quote is not available, and I did not invent one.**
  The verified stand-in — `These building blocks aren't prescriptive. They're common patterns that
  developers can shape and combine` — supports what S34 actually asserts ("all five are doable
  with skills, no framework required"), which is the load-bearing part.
- If Louis wants the names in the registry, the only honest option is five entries with five
  per-pattern quotes (e.g. `Prompt chaining decomposes a task into a sequence of steps`, each
  contiguous and verifiable) — heavy for one slide. **Recommend the single entry above.**

### 9. `mistral.ai` → "open-weights track close behind" — **DOES NOT EXIST. REPLACE.**
- **Searched and fetched `mistral.ai`.** The only relevant string on the site is
  *"In-region inference, open models, and new European infrastructure for sovereign AI"* — a
  product announcement. **Nothing on mistral.ai measures, or even asserts, how far open weights
  trail the frontier.** It is a vendor whose interest in the claim disqualifies it anyway.
- **Replacement, which measures exactly this claim**:
  `https://epoch.ai/data-insights/open-closed-eci-gap` — "Open models lag state-of-the-art closed
  models by 4 months" (Epoch AI, Edwards & Emberson, 2026-05-29).
- **Quote**: `the most capable open-weight models have lagged frontier closed models by an average
  of four months` — **VERIFIED**.
- **Bonus**: this keeps S09 on Epoch AI for *both* citations ([1] inference price trends, [2] the
  open/closed gap), which is tidier and puts one authority behind the whole cost-collapse slide.
- If a *European* angle is wanted on that slide, say "open weights" and let Mistral be an **example
  named in the body text without a citation marker** — an unlinked illustration is not a source.

### 10. `help.mistral.ai` + `scaleway.com` → EU sovereign inference — **REGISTER BOTH**
- **Mistral**: `https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data`
  Quote `By default, your data is hosted in the European Union` — **VERIFIED**.
  (`help.mistral.ai` bare redirects to `/en/`, a collection index — not citable. This article is the
  exact page and carries the GDPR Article 46 language too.)
- **Scaleway**: `https://www.scaleway.com/en/generative-apis/`
  Quote `Towards a sovereign AI where your data remains yours, and only in Europe` — **VERIFIED**.
  For the OpenAI-compatibility half of the claim, also **VERIFIED** on the same page:
  `Easily integrate with existing tools like OpenAI libraries and LangChain SDKs`.
- Between them the three sub-claims (EU-hosted, GDPR, OpenAI-compatible) are all covered.

### 11. Karpathy's published CLAUDE.md — **REGISTER, but fix what the slide says**
- **URL**: `https://github.com/karpathy/llm-council/blob/master/CLAUDE.md` — the only CLAUDE.md in
  Karpathy's public repos (probed `nanochat`, `autoresearch`, `llm.c`, `nanoGPT`, `micrograd`,
  `minbpe`, `llama2.c`, `build-nanogpt`, `rustbpe`, `reader3`, `rendergit`, `jobs`,
  `hn-time-capsule`, both `main` and `master`, CLAUDE.md and AGENTS.md).
- **Quote**: `This file contains technical details, architectural decisions, and important
  implementation notes` — **VERIFIED** (GitHub blob pages are server-rendered; the file body is in
  the HTML).
- **The correction that matters**: the CLAUDE.md that went viral as "Karpathy's" — the
  `multica-ai/andrej-karpathy-skills` / `white-sand-grand/karpathy-claude-md` repos — was **written
  by Forrest Chang, distilling Karpathy's X observations.** Karpathy did not publish it. If S19
  shows the famous 4-rule file, **the attribution on the slide is wrong** and must be fixed.
- **Also honest**: `llm-council/CLAUDE.md` is project-specific architecture notes (ports, module
  responsibilities), not a transferable template. *"A great model to steal from"* oversells it.
  Suggest: *"Karpathy ships a CLAUDE.md in his own repos — worth reading for the shape, not the
  content."*

### 12. Steinberger's loops post · Cherny `/loop` — **12a REGISTER · 12b RE-SOURCE**
- **12a — Steinberger. Register.** `https://x.com/steipete/status/2063697162748260627`
  (2026-06-07). Full text, via `api.fxtwitter.com`: *"Here's your monthly reminder that you
  shouldn't be prompting coding agents anymore. You should be designing loops that prompt your
  agents."* Quote `You should be designing loops that prompt your agents` — **VERIFIED against
  x.com itself** (13 raw / 4 text hits — x.com does serve tweet text to this UA, same as the
  parent registry's existing `trq-make-me-understand` entry, which I re-verified live and which
  still passes). It is an X post, **not** a blog post — no long-form Steinberger piece with this
  thesis exists; the "loop engineering" essays circulating are other people writing about him.
- **12b — Cherny. This is the one that fails.**
  - His slash-commands tweet (`x.com/bcherny/status/2007179847949500714`, 2026-01-02) is about
    *"inner loop" workflows* checked into `.claude/commands/` — **English idiom, not the `/loop`
    feature**. Citing it for "loops built into the harness" would be a misattribution and I will
    not propose it.
  - His actual loops material ("Going from agents to loops is as big a jump as going from code to
    agents"; "hundreds, sometimes thousands of agents running in loops for 5, 10, 20 hours") comes
    from a **Bloomberg video interview**, reaching the web only via third-party quote-tweets. No
    first-person, linkable, text-verifiable Cherny page exists.
  - **Recommended fix — use the primary the claim actually needs**:
    `https://code.claude.com/docs/en/slash-commands`, quote `Claude Code includes a set of bundled
    skills` — **VERIFIED**; the same page lists `/loop` among them. And the parent registry
    **already holds** `claude-getting-started-with-loops`
    (`https://claude.com/blog/getting-started-with-loops`), which spells it out:
    *"you can trigger when Claude runs with `/loop` which re-runs a prompt on an interval"*.
    Between them, "loops are built into the harness" is fully sourced **without needing Cherny**.
  - **If the name stays on the slide**, register `cherny-agents-to-loops-secondary` above
    (quote **VERIFIED** on x.com) and **label it on-slide as a second-hand quote of an interview**.
    That is the honest floor. Dropping the name and keeping "the Claude Code team" is cleaner.

---

## Verification log

Every row below was executed on 2026-08-31 against the live page.

| # | URL | HTTP | Quote grep |
|---|-----|------|-----------|
| 1 | agentskills.io/home | 200 | **FOUND** |
| 2 | snyk.io/articles/skill-md-shell-access/ | 200 | **FOUND** |
| 2b | snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ | 200 | **FOUND** |
| 3 | llm-stats.com/**frontiercode** | **404** | — **DEAD** |
| 3 | llm-stats.com/benchmarks/frontiercode | 200 | **FOUND** |
| 3b | cognition.com/frontiercode | 200 | **FOUND** (prose only; table is JS) |
| 4 | code.claude.com/docs/en/memory | 200 | **FOUND** |
| 5 | code.claude.com/docs/en/permissions | 200 | **FOUND** (3 quotes) |
| 6 | anthropic.com/engineering/effective-context-engineering-for-ai-agents | 200 | **FOUND** |
| 7 | anthropic.com/news/model-context-protocol | 200 | **FOUND** |
| 8 | anthropic.com/research/building-effective-agents | 200 → **301 to /engineering/** | — |
| 8 | anthropic.com/engineering/building-effective-agents | 200 | **FOUND** (3 quotes); five-pattern sentence **absent** |
| 9 | mistral.ai | 200 | **no supporting text exists** |
| 9 | epoch.ai/data-insights/open-closed-eci-gap | 200 | **FOUND** |
| 10a | help.mistral.ai/en/articles/347629-… | 200 | **FOUND** |
| 10b | scaleway.com/en/generative-apis/ | 200 | **FOUND** (2 quotes) |
| 11 | github.com/karpathy/llm-council/blob/master/CLAUDE.md | 200 | **FOUND** |
| 12a | x.com/steipete/status/2063697162748260627 | 200 | **FOUND** |
| 12b | code.claude.com/docs/en/slash-commands | 200 | **FOUND** |
| 12b-alt | x.com/0xDepressionn/status/2070468357539635626 | 200 | **FOUND** (secondary) |

Matching used `verify-sources.py`'s `norm()` against both the raw body and the tag-stripped body,
so a `FOUND` here is a pass under `make export-pdf-*`. Quotes were kept free of smart quotes and
apostrophes wherever a safe fragment existed.

## Follow-ups this creates

1. **S15 must be rewritten** before build — the model claim is factually wrong and the Diamond
   subset is retired. Re-snapshot the leaderboard on talk morning; it moves.
2. **S19 attribution check** — if the slide shows the viral 4-rule CLAUDE.md, that is not Karpathy's.
3. **S35 decision for Louis** — drop "Boris Cherny" from the slide, or keep it with a visible
   "quoted from a Bloomberg interview" label. There is no third option that is honest.
4. **S12** — do not put Louis's five-fragment definition in quotation marks or attribute the wording
   to Anthropic.
5. **Update `source-ledger.md` section B** — mark these rows resolved, and add
   `epoch-open-closed-gap` (replacing the mistral.ai row) plus the two `/loop` primaries.
