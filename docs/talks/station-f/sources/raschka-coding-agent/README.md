---
title: Components of A Coding Agent
subtitle: How coding agents use tools, memory, and repo context to make LLMs work better in practice
author: Sebastian Raschka
publication: Ahead of AI (magazine.sebastianraschka.com)
published_date: 2026-04-04
accessed_date: 2026-04-12
source_url: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
archive_reason: Primary source for "Components of a Coding Agent" section of Station F course (Week of April 15 2026)
archive_note: |
  This is a structural archive (metadata + section outline + short quoted excerpts +
  figure images) rather than a verbatim full-text copy. The article is under the
  author's / Substack's copyright. For quoting in the deck, pull short excerpts from
  the "Key quotable passages" blocks below and cite the source_url.
---

# Archive note

The article is a copyrighted post on Sebastian Raschka's Substack "Ahead of AI". This
file preserves what is needed to cite and discuss the piece accurately in a course deck:

- full author / publication / date metadata (YAML above)
- the complete table of contents (author's own section headings)
- a short neutral summary of what each section argues
- short verbatim excerpts that are likely to be quoted in the deck (each clearly marked)
- the author's own figure captions (verbatim, since they are the intended legend text)
- all 13 figures downloaded locally to `images/` for reference

For verbatim full-text access, follow the `source_url` in the frontmatter.

---

# Table of contents (author's own headings, in order)

1. Intro (untitled opening)
2. Claude Code, Codex CLI, and Other Coding Agents
3. On The Relationship Between LLMs, Reasoning Models, and Agents
4. The Coding Harness
5. 1. Live Repo Context
6. 2. Prompt Shape And Cache Reuse
7. 3. Tool Access and Use
8. 4. Minimizing Context Bloat
9. 5. Structured Session Memory
10. 6. Delegation With (Bounded) Subagents
11. Components Summary
12. How Does This Compare To OpenClaw?
13. (Book announcement — *Build A Reasoning Model (From Scratch)*)

---

# The six components (author's own list, verbatim)

From Raschka's Mini Coding Agent source, annotated in a comment block:

```
##############################
#### Six Agent Components ####
##############################
# 1) Live Repo Context -> WorkspaceContext
# 2) Prompt Shape And Cache Reuse -> build_prefix, memory_text, prompt
# 3) Structured Tools, Validation, And Permissions -> build_tools, run_tool, validate_tool, approve, parse, path, tool_*
# 4) Context Reduction And Output Management -> clip, history_text
# 5) Transcripts, Memory, And Resumption -> SessionStore, record, note_tool, ask, reset
# 6) Delegation And Bounded Subagents -> tool_delegate
```

Reference implementation: https://github.com/rasbt/mini-coding-agent

---

# Section-by-section outline

## Intro (untitled opening)

**Summary.** Raschka frames the piece as a reference on coding agents and "agent
harnesses": what they are, how they work, and how the pieces fit together. He argues
that recent progress in practical LLM systems comes less from better models than from
the surrounding system — tool use, context management, memory — which is why products
like Claude Code or Codex can feel more capable than the same model in a plain chat UI.

**Key quotable passages:**

> "In many real-world applications, the surrounding system, such as tool use, context
> management, and memory, plays as much of a role as the model itself."

> "This also helps explain why systems like Claude Code or Codex can feel significantly
> more capable than the same models used in a plain chat interface."

---

## Claude Code, Codex CLI, and Other Coding Agents

**Summary.** Defines a coding agent as an LLM wrapped in an application layer — an
"agentic harness" — tuned for convenience and performance on coding tasks. Stresses
that what matters is the surrounding system (repo context, tool design, prompt-cache
stability, memory, long-session continuity) rather than just the model choice, and
warns against collapsing "the model, the reasoning behavior, and the agent product
into one thing".

**Key quotable passage:**

> "Coding agents are engineered for software work where the notable parts are not only
> the model choice but the surrounding system, including repo context, tool design,
> prompt-cache stability, memory, and long-session continuity."

**Figure 1** — `images/01-claude-code-codex-mini.png`
Caption: *Claude Code CLI, Codex CLI, and my [Mini Coding Agent](https://github.com/rasbt/mini-coding-agent).*

---

## On The Relationship Between LLMs, Reasoning Models, and Agents

**Summary.** Walks through definitions: an LLM is the core next-token model; a
reasoning model is an LLM trained/prompted to spend more inference-time compute on
intermediate reasoning and verification; an agent is a control loop on top. The
car-engine analogy: LLM = engine, reasoning model = beefed-up engine (more powerful
but more expensive), agent harness = helps the model. Raschka also gives a short
glossary (LLM / reasoning model / agent / agent harness / coding harness) and notes
that coding work is only partly next-token generation — a lot of it is repo
navigation, search, function lookup, diff application, test execution, error
inspection, and keeping relevant information in context.

**Key quotable passages (the glossary — author's own bullet list):**

> - *LLM:* the raw model
> - *Reasoning model*: an LLM optimized to output intermediate reasoning traces and to verify itself more
> - *Agent:* a loop that uses a model plus tools, memory, and environment feedback
> - *Agent harness:* the software scaffold around an agent that manages context, tool use, prompts, state, and control flow
> - *Coding harness:* a special case of an agent harness; i.e., a task-specific harness for software engineering that manages code context, tools, execution, and iterative feedback

> "In other words, the agent is the system that repeatedly calls the model inside an environment."

**Figure 2** — `images/02-llm-reasoning-agent-relationship.png`
Caption: *The relationship between conventional LLM, reasoning LLM (or reasoning model), and an LLM wrapped in an agent harness.*

**Figure 3** — `images/03-coding-harness-three-layers.png`
Caption: *A coding harness combines three layers: the model family, an agent loop, and runtime supports. The model provides the "engine", the agent loop drives iterative problem solving, and the runtime supports provide the plumbing. Within the loop, "observe" collects information from the environment, "inspect" analyzes that information, "choose" selects the next step, and "act" executes it.*

---

## The Coding Harness

**Summary.** Zooms in on the harness as the software layer around the model that
assembles prompts, exposes tools, tracks file state, applies edits, runs commands,
manages permissions, caches stable prefixes, and stores memory. Raschka argues that
because vanilla frontier LLMs today have very similar capabilities, the harness is
often the distinguishing factor. He speculates that dropping a top open-weight model
(e.g. GLM-5) into a comparable harness could likely match GPT-5.4 in Codex or
Claude Opus 4.6 in Claude Code, though harness-specific post-training usually helps
(citing OpenAI historically maintaining separate GPT-5.3 and GPT-5.3-Codex variants).
Notes a terminology caveat: he uses "coding agent" and "coding harness"
interchangeably, but strictly the agent is the decision loop and the harness is the
scaffold.

**Key quotable passage:**

> "Since, in my view, the vanilla versions of LLMs nowadays have very similar
> capabilities […], the harness can often be the distinguishing factor that makes
> one LLM work better than another."

**Figure 4** — `images/04-six-harness-features.png`
Caption: *Main harness features of a coding agent / coding harness that will be discussed in the following sections.*

**Figure 5** — `images/05-mini-coding-agent-overview.png`
Caption: *Minimal but fully working, from-scratch [Mini Coding Agent](https://github.com/rasbt/mini-coding-agent/blob/main/mini_coding_agent.py) (implemented in pure Python)*

---

## 1. Live Repo Context

**Summary.** The harness collects "stable facts" about the workspace upfront — Git
repo status, branch, project documents like AGENTS.md or README, repo root and
layout — so the model is not starting from zero on every prompt. Raschka uses
"fix the tests" as an example of an instruction that is not self-contained: the
right action depends on project conventions that only exist in context.

**Key quotable passage:**

> "The takeaway is that the coding agent collects info ('stable facts' as a workspace
> summary) upfront before doing any work, so that it's is not starting from zero,
> without context, on every prompt." *(sic — original contains "it's is")*

**Figure 6** — `images/06-workspace-summary.png`
Caption: *The agent harness first builds a small workspace summary that gets combined with the user request for additional project context.*

---

## 2. Prompt Shape And Cache Reuse

**Summary.** Given the workspace context, the next question is how to feed it to the
model turn after turn. Rebuilding one giant prompt every turn is wasteful because
coding sessions are repetitive — instructions, tool descriptions, and the workspace
summary mostly stay the same. Smart runtimes separate a **stable prompt prefix**
(general instructions, tool descriptions, workspace summary) that can be reused via
prompt caching, from the **changing session state** (short-term memory, recent
transcript, newest user request) that gets rebuilt each turn. Raschka emphasizes this
section is about *packaging and caching* the facts gathered in §1 efficiently across
repeated model calls.

**Figure 7** — `images/07-stable-prompt-prefix.png`
Caption: *The agent harness builds a stable prompt prefix, adds the changing session state, and then feeds that combined prompt to the model.*

---

## 3. Tool Access and Use

**Summary.** Tool use is where the system stops feeling like chat and starts feeling
like an agent: the harness actually executes commands and feeds results back, rather
than asking the user to copy-paste. Instead of letting the model improvise arbitrary
syntax, the harness usually exposes a pre-defined list of named tools with typed
inputs and clear boundaries (though a broad tool like `subprocess.call` can still be
one of them). When the model emits a structured action, the runtime runs programmatic
checks — is this a known tool? are the arguments valid? does it need user approval?
is the requested path inside the workspace? — before anything runs. Raschka frames
this as giving the model less freedom in exchange for usability and reliability.

**Key quotable passages:**

> "A plain model can suggest commands in prose, but an LLM in a coding harness should
> do something narrower and more useful and be actually able to execute the command
> and retrieve the results."

> "In a sense, the harness is giving the model less freedom, but it also improves
> the usability at the same time."

**Figure 8** — `images/08-tool-use-flow.png`
Caption: *The model emits a structured action, the harness validates it, optionally asks for approval, executes it, and feeds the bounded result back into the loop.*

**Figure 9** — `images/09-tool-approval-prompt.png`
Caption: *Illustration of a tool call approval request in the Mini Coding Agent.*

---

## 4. Minimizing Context Bloat

**Summary.** Long contexts are expensive and noisy; coding agents are especially
prone to bloat because of repeated file reads, long tool outputs, and logs. A good
harness uses at least two compaction strategies. **Clipping** shortens any single
verbose piece of text (document snippets, tool outputs, memory notes, transcript
entries) so no one item monopolizes the prompt budget. **Transcript reduction /
summarization** compresses session history, keeping recent events richer (likely
relevant) and compressing older events more aggressively. The harness also
deduplicates older file reads so the same file content doesn't recur in the prompt.
Raschka links out to his earlier piece on attention variants and argues that "a lot
of apparent 'model quality' is really context quality".

**Key quotable passage:**

> "Overall, I think this is one of the underrated, boring parts of good coding-agent
> design. A lot of apparent 'model quality' is really context quality."

**Figure 10** — `images/10-context-compaction.png`
Caption: *Large outputs are clipped, older reads are deduplicated, and the transcript is compressed before it goes back into the prompt.*

---

## 5. Structured Session Memory

**Summary.** §4 was about *prompt-time* use of history (what goes back into the
model next turn — compression, clipping, deduplication, recency). This section is
about *storage-time* structure of history — what the agent keeps as a permanent
record. The agent separates state into at least two layers:

- **working memory**: a small, distilled state the agent keeps explicitly
- **full transcript**: all user requests, tool outputs, and LLM responses

Both are usually stored as JSON files on disk. The full transcript is durable and
resumable after closing the agent. The working memory is a distilled version of
currently-important info. Their jobs differ: the compact transcript serves
**prompt reconstruction** (a compressed view of recent history so the model can
continue without re-seeing everything); the working memory serves **task
continuity** (a small explicitly-maintained summary of what matters across turns —
current task, important files, recent notes).

**Figure 11** — `images/11-transcript-and-memory.png`
Caption: *New events get appended to a full transcript and summarized in a working memory. The session files on disk are usually stored as JSON files.*

---

## 6. Delegation With (Bounded) Subagents

**Summary.** Delegation lets the main agent parallelize subtasks — e.g. "which file
defines this symbol?", "what does this config say?", "why is this test failing?" —
into bounded subagents instead of carrying every thread in one loop. The hard design
problem is not spawning subagents but *binding* them: a subagent needs enough
inherited context to do real work, but without restriction you get multiple agents
duplicating work, touching the same files, or spawning further subagents. The fix is
tighter boundaries (e.g. read-only mode, restricted recursion depth). Raschka notes
that Claude Code has supported subagents for a long time while Codex added them more
recently; Codex doesn't generally force read-only and instead scopes via task,
context, and depth.

**Key quotable passage:**

> "So the tricky design problem is not just how to spawn a subagent but also how to
> bind one :)."

**Figure 12** — `images/12-bounded-subagent.png`
Caption: *The subagent inherits enough context to be useful, but it runs inside tighter boundaries than the main agent.*

---

## Components Summary

**Summary.** The six components are deeply intertwined in implementation but were
covered one-by-one to build the mental model of why a coding harness makes an LLM
more useful than plain multi-turn chat. Raschka points readers again to his
open-source Mini Coding Agent for a clean Python reference implementation.

**Figure 13** — `images/13-six-features-summary.png`
Caption: *Six main features of a coding harness discussed in previous sections.*

---

## How Does This Compare To OpenClaw?

**Summary.** OpenClaw is positioned as a local, general agent platform that can also
code, rather than a specialized terminal coding assistant. It overlaps with a coding
harness: prompt and instruction files in the workspace (AGENTS.md, SOUL.md,
TOOLS.md); JSONL session files with transcript compaction and session management;
ability to spawn helper sessions and subagents. The emphasis differs though —
coding agents are optimized for one person working in one repository, while OpenClaw
is optimized for many long-lived local agents across chats, channels, and workspaces,
with coding as one of several workloads.

---

## Book announcement

Raschka closes by announcing that *Build A Reasoning Model (From Scratch)* is
finished, with all chapters in early access; the publisher is finalizing layouts and
it should be available summer 2026. Main topics listed: evaluating reasoning models,
inference-time scaling, self-refinement, reinforcement learning, distillation.
Available on Manning (early access, 528 pages, pre-final layout) and Amazon
(pre-order).

---

# Image manifest

| Local file | Remote URL (original) | Size |
|---|---|---|
| `images/01-claude-code-codex-mini.png` | substackcdn.com/.../c90147bc-...png | 708 KB |
| `images/02-llm-reasoning-agent-relationship.png` | substackcdn.com/.../09a4d839-...png | 293 KB |
| `images/03-coding-harness-three-layers.png` | substackcdn.com/.../76f2c37e-...png | 137 KB |
| `images/04-six-harness-features.png` | substackcdn.com/.../82c0f343-...png | 254 KB |
| `images/05-mini-coding-agent-overview.png` | substackcdn.com/.../89ec8895-...png | 274 KB |
| `images/06-workspace-summary.png` | substackcdn.com/.../2e3a1e6a-...png | 233 KB |
| `images/07-stable-prompt-prefix.png` | substackcdn.com/.../92d9467c-...png | 234 KB |
| `images/08-tool-use-flow.png` | substackcdn.com/.../7aff251f-...png | 177 KB |
| `images/09-tool-approval-prompt.png` | substackcdn.com/.../6ff4770e-...png | 620 KB |
| `images/10-context-compaction.png` | substackcdn.com/.../1d61d701-...png | 271 KB |
| `images/11-transcript-and-memory.png` | substackcdn.com/.../e58efdfb-...png | 281 KB |
| `images/12-bounded-subagent.png` | substackcdn.com/.../81b2ae42-...png | 165 KB |
| `images/13-six-features-summary.png` | substackcdn.com/.../4fe9e9f0-...png | 254 KB |

All 13 figures downloaded successfully; no failures.
