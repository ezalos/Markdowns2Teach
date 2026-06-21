# Agents Talk — June 1st 2026 (External University)

**Goal:** Ship an English-language standalone deck on AI Agents for a ~45–60 min talk at another university on 2026-06-01, derived from `slides/session-03/C-agents.md` but with (a) a better "what is an agent" intro using the new primer, (b) a new Evaluation section (80/20 from deep research), (c) Hermes Agent slides replacing OpenClaw, and (d) a full claims-update pass.

**Source deck:** `slides/session-03/C-agents.md` (44 slides, French, M2 IMT&E context).

**New deck path:** `slides/agents-talk-2026-06-01/agents.md`.

**Inputs (from `~/Inbox/`):**
- `compass_artifact_wf-267f2541-…_text_markdown.md` — Evaluation deep research (Husain/Shankar, Anthropic Jan 2026, Inspect-AI, Princeton reliability).
- `what-are-agents.md` — primer (chatbot→agent ladder, anatomy, ReAct loop, Claude Code vs Hermes).
- `compass_artifact_wf-b93a25a6-…_text_markdown.md` — Hermes vs Claude Code deep research (the two copies are identical).

**Standards:** all body content follows `docs/references/slide-creation-standards.md` (overflow budget, citation format, layout classes). English body, English technical terms.

---

## Phases

### Phase 1 — Scaffold (mechanical)

- [x] `mkdir -p slides/agents-talk-2026-06-01/assets`
- [ ] Duplicate `slides/session-03/C-agents.md` → `slides/agents-talk-2026-06-01/agents.md` (raw copy, no edits)
- [ ] Update front matter: `header: "Building With AI: Agents — 2026-06-01 · <Host University>"`, footer multi-sources
- [ ] Translate two ABOUTME lines to English
- [ ] Decide assets strategy: copy used images into new `assets/` subtree, OR reference `../session-03/assets/…` (decide before Phase 3 so paths are consistent)

### Phase 2 — Intro rewrite ("What is an agent")

Replace current slides 01–05 (Alfred analogy + agency spectrum + Think/Act/Observe + augmented LLM + discussion) with the primer-derived arc:

- [ ] **01 — From chatbot to agent: the control ladder** (table: single call / chain / workflow / agent) + litmus test ("if you can't predict tool order, it's an agent")
- [ ] **02 — Anatomy: model + tools + loop** (the 5 parts, but headline is the 3 that matter)
- [ ] **03 — The ReAct loop with a worked example** (use the "fix failing test" walkthrough from primer §3 — concrete + debuggable)
- [ ] **04 — Tools: how a model acts** (function calling mechanism: model proposes, runtime disposes; MCP one-line teaser)
- [ ] **05 — Discussion** (keep the 200 CVs scenario, translated)

Drop or relocate the 5-level agency spectrum infographic — it duplicates the ladder; if kept, move to Synthesis as a recap.

### Phase 3 — Body translation (French → English)

For every retained slide (06–44, minus the ones rewritten in other phases):

- [ ] Translate body text to English
- [ ] Keep English technical terms unchanged
- [ ] Translate table headers, blockquote callouts, discussion prompts
- [ ] Update tables that reference Mistral AI / French context if needed for international audience (keep or swap with global examples — Louis to flag)
- [ ] Re-check overflow per `make check` after translation (English is sometimes shorter, sometimes longer)

### Phase 4 — Hermes replaces OpenClaw

Replace current slide 38 with 3 Hermes slides; adapt slide 39 discussion:

- [ ] **37 — Claude Code** (kept; light edits to set up the contrast)
- [ ] **38 — Hermes: the agent that learns** — open-source MIT, model-agnostic, server-resident, multi-surface (20 messaging platforms). Launched 2026-02-25. README quote: "the only agent with a built-in learning loop"
- [ ] **38b — Hermes's learning loop: memory + auto-skills** — `MEMORY.md` (~800 tokens) + `USER.md` (~500 tokens) frozen at session start (cache-stable); FTS5 session search; auto skill-creation triggered by `creation_nudge_interval: 15` (tool-calling iterations — **explicitly debunk** the "every 15 tasks" misstatement); background Curator (active → stale 30d → archived 90d, agent-created skills only)
- [ ] **38c — Claude Code vs Hermes (`cols`)** — side-by-side table from primer §5 ("depth of learning vs controllable simplicity")
- [ ] **39 — Discussion** (adapt OpenClaw discussion: which agent shape for your startup — coding-CLI vs persistent personal agent?)

Caveats to bake in (footer + speaker note): "self-improving" is partly aspirational; the 40% efficiency claim is Nous Research–reported (vendor figure).

### Phase 5 — New Evaluation section (80/20 of deep research)

Insert between current Production block (slide 33) and Context Engineering (slide 34). ~7 slides.

- [ ] **E1 — Section divider:** "Evaluating an agent"
- [ ] **E2 — Why this matters (Monte Carlo survey, Apr 28 2026)** — **64% of enterprise leaders & engineers deployed AI agents before they were ready**; 63% found agents accessing unintended systems; 36% can't disable/rollback within minutes; 70% expect significant rebuilds post-deployment; only 47% have end-to-end traceability. *Source: Monte Carlo "Agents in Production: The Builder's Perspective," n=260 practitioners at 1,000+-employee orgs, early 2026; reported by Yahoo Finance Apr 28 2026.*
- [ ] **E3 — The real target is reliability, not accuracy** — Princeton arXiv:2602.16666 (4 dims: consistency, robustness, predictability, safety); pass@1 varies 2.2–6.0 pp single-run (KTH "On Randomness in Agentic Evals," arXiv:2602.07150). Update slide 29's outro line to point forward here.
- [ ] **E4 — Look at your data first (error analysis)** — Husain/Shankar Jan 2026 FAQ: "60–80% of dev time on error analysis"; review ≥100 traces; open coding → axial coding → counted failure taxonomy; one "benevolent dictator" owns quality
- [ ] **E5 — Scoring rules of thumb (Anthropic Jan 2026)** — 20–50 unambiguous tasks; binary > Likert; outcomes > paths (don't grade exact tool sequences); allow partial credit; balance positive/negative cases
- [ ] **E6 — LLM-as-judge: useful but must be validated** — scoped binary judges, TPR/TNR ≥ 80% on a labeled hold-out, known biases (position/verbosity), authority hierarchy EXPERT > HUMAN > LLM > UNKNOWN
- [ ] **E7 — Offline + online (the Swiss-cheese model)** — Inspect-AI (UK AISI + Meridian Labs, MIT) for the offline sandbox harness + Langfuse / Phoenix for production observability; close the loop: every production failure → new offline regression case
- [ ] **E8 — Discussion** — scenario: your recruiting agent rejects a candidate's CV. Design the eval: what's the failure taxonomy, what's the judge, what would you sample online?

Explicitly **not** including (the 80% that delivers diminishing returns for this audience):
- Multi-agent failure attribution (research-frontier)
- Vendor matrix detail beyond one mention
- Inspect-AI abstractions deep dive (Task/Solver/Scorer)
- Benchmark zoo (Cybench / MLE-bench / FIRE-Bench)

### Phase 6 — Claims update pass

Run a single `/cite` cycle on the new file once Phases 1–5 are done. Rule per Louis's instruction:
- **Auto-update** when the new source is newer AND at the same tier or higher per `docs/references/authority-map.yaml`.
- **Flag for review** when newer but lower tier — report a checklist in the chat.

Priority claims to chase (highest-impact / oldest):

| Slide | Claim | Action |
|---|---|---|
| (new — Eval E2) | Monte Carlo "Agents in Production" — 64% rushed agents before ready; 63% / 36% / 70% / 47% supporting stats | Cite Monte Carlo report directly + Yahoo Finance Apr 28 2026 secondary URL |
| (new) | EpochAI open vs closed gap — updated 4-month rolling average | Pull fresh figure; add to LLM-numbers opener or to a synthesis slide |
| 10 | MCP "~90M+ downloads/mo, 10K+ servers" | Verify May 2026 numbers |
| 10/13 | AAIF Linux Foundation member count (was 146) | Verify |
| 29 | Gartner "40% of agent projects cancelled by 2027" | Verify date + percentage |
| 38 (was OpenClaw) | If kept anywhere: 315K stars, Cisco 26% of 31K skills vulnerable | Verify or drop with the slide |
| 40 | Karpathy AutoResearch run numbers | Verify Discussion #43 + latest commit |
| 41 | Tobi Lutke 19% / 0.8B beats 1.6B | Verify tweet ID |
| all | Every `<small>Sources …</small>` URL | Spot-check resolves to the cited number |

### Phase 7 — LLM-numbers opener (decision pending)

Louis said the intro could be improved "after the LLM numbers showed off" — implies an LLM state-of-the-field opener before the agent intro. Sketch (1–3 slides) to discuss with Louis before writing:

- [ ] LLM 2026 snapshot — frontier model capability curve, open-vs-closed gap (EpochAI 4-month avg), inference cost trajectory
- [ ] Transition: "the models got good — now the interesting question is what you wrap around them"
- [ ] Lead into Phase 2 intro

### Phase 8 — Verification

- [ ] `make check` — overflow pixel-accurate (Puppeteer + headless Chrome)
- [ ] `make check-citations` — every data slide has sources
- [ ] `make html` — clean build, no errors
- [ ] Spot-check the HTML output visually (title slide, section dividers, cols, infographics)
- [ ] Verify all assets resolve (no broken images)

---

## Open questions before execution

1. **LLM-numbers opener** — do we add an opening LLM-context section (Phase 7), and if so, what's the angle? Without it, we jump straight into the agent intro.
2. **Host university name** — for the deck header and footer attribution.
3. **Assets strategy** — copy or reference `../session-03/assets/`? Copy is more portable; reference saves disk.
4. **Examples localization** — keep Mistral AI / L'Oréal / Klarna, or swap some for more globally-recognizable cases?
5. **Optional `spec.md`** — Station F has `docs/station-f/spec.md` as a source of truth. Do we want `docs/agents-talk-2026-06-01/spec.md` too, or is this plan enough?

---

## Execution order recommendation

Phase 1 → Phase 4 → Phase 5 → Phase 2 → Phase 3 (translate everything left) → Phase 7 (if needed) → Phase 6 → Phase 8.

Rationale: structural changes (Hermes swap + Eval section) reshape the deck most; rewrite the intro after structure is settled; translate last so we don't translate text we end up cutting; claims pass at the end on the final English copy.
