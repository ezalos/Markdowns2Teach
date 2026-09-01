<!-- ABOUTME: Tested runbook for the two live demos in the Station F talk — timings measured on TheBeast, 2026-09-01. -->
<!-- ABOUTME: The Grill Me demo cannot be run cold on stage; the memory demo is instant. Both verified, not assumed. -->

# Demo runbook — tested 2026-09-01

Every timing below was measured on this machine, not estimated.

---

## Demo A — Memory files: `cat` versus a database (SAFE, INSTANT)

**Measured: 0.002s (Claude Code), 0.016s (Codex).** Zero risk. This is the demo to lean on.

### The point

Claude Code keeps what it learns as **plain markdown you can read, grep, diff and review**.
Codex keeps it in **SQLite**. Same idea, opposite ergonomics — and it is the concrete proof
behind chapter 5's claim that plain files are not the beginner option.

### The commands, in order

```bash
# 1. The index — one line per fact, loaded every session
head -12 ~/.claude/projects/-home-ezalos-42-Markdowns2Teach/memory/MEMORY.md

# 2. One fact, in full — this is the payoff
cat ~/.claude/projects/-home-ezalos-42-Markdowns2Teach/memory/make-build-quirks.md

# 3. The same idea, in the other tool
sqlite3 ~/.codex/memories_1.sqlite ".schema" | head -20
```

### Why `make-build-quirks.md` is the file to show

It carries frontmatter (`name`, `description`, `type: project`), then **Why** and **How to
apply** for each pitfall — a lesson the agent hit, wrote down, and now re-reads. It is about
**this repo**, so the line lands: *"the deck you are looking at was built by an agent whose
memory is these files."*

### What the Codex schema shows

`stage1_outputs` with `raw_memory`, `rollout_summary`, `usage_count`, `selected_for_phase2`
— a **two-stage curation pipeline with usage tracking**, not a folder. Worth naming out loud:
the vendors are diverging, files versus pipeline.

### Two honesty notes — say them, do not hide them

1. **The Codex table is empty (0 rows).** Say so: *"mine is empty, I do not use Codex daily —
   look at the shape, not the contents."* Pretending otherwise is the one thing that would
   cost credibility here.
2. **Instructions are files in both tools** (CLAUDE.md / AGENTS.md). The divergence is in
   *learned memory*, not instructions. Do not overclaim the contrast.

### One safety check before you project

`MEMORY.md` line 4 names credential variables (`N8N_EMAIL`, `N8N_PASSWORD`, `GEMINI_API_KEY`)
— **names only, no values**. It is safe, but if you would rather not have the word PASSWORD on
a 4-metre screen, start at line 5 (`sed -n '5,14p'`).

---

## Demo B — Grill Me: DO NOT RUN COLD (tested, and it fails as designed)

### What I measured

| Condition | Model | Time to first question |
|---|---|---|
| Inside this repo, rich context | Opus | **3 min 51 s** |
| Empty standalone dir | Sonnet | **>5 min (timed out)** |
| Baseline CLI latency, same dir | Sonnet | 5.7 s |

The CLI is not slow. **The skill is slow by design**: it says *"Finding facts is your job,
never the user's"* and dispatches sub-agents to explore before it asks anything. In an empty
directory it has to work harder, not less, so a "clean" demo dir is the *worst* case.

**A four-minute silence on stage is a dead demo.** Running this cold is the single riskiest
thing in the talk.

### The staging that works: start it, then talk

1. **On slide 14** (chapter opener, "Bad code is the most expensive it has ever been"), type
   the command and press enter. Say: *"I am starting this now, it does its homework before it
   asks me anything — I will come back to it."*
2. Present slides 14 and 15 normally — about **2.5 to 3 minutes** of prepared content.
3. **Switch to the terminal.** The questions are waiting. Read two of them aloud, answer one
   live, and move on.

This turns the latency into the point being made: *the agent refuses to ask you anything it
could find out itself.* That is the actual lesson of the pattern.

### The command

```bash
cd ~/42/Markdowns2Teach/slides/station-f-claude-code/demo
claude --model opus --permission-mode plan
# then: "Use the grilling skill. I want to build the agent described in README.md."
```

Run it from the **demo directory inside this repo** (not a standalone copy): the in-repo run
was the fast one, and the questions it produced were sharper because it had real context.

### Known behaviour: it will find the talk

Running inside this repo, it reads `docs/talks/station-f-claude-code/` and asks whether the
brief is a stage prop or a real tool — by name, citing slide 15. On stage this is either the
best moment of the demo or a confusing one. **Decide which**, and if you keep it, lean in:
*"it just worked out that this README is a prop for this talk — that is the level of homework
I am talking about."*

### Fallback if the room's network is bad

A real transcript from the tested run is saved at
`docs/talks/station-f-claude-code/demo/grill-transcript.md`. Four numbered questions, each
with a recommended answer. Show it as a slide and narrate. No apology needed — say it is a
recording and move on.

### The demo brief

`slides/station-f-claude-code/demo/README.md` — Support Signal, a 6-person B2B SaaS drowning
in 400 support conversations a week. Chosen because every founder in the room has this
problem, it needs no domain explanation, and its constraints (PII, no data engineer, under an
hour a month) are exactly the ones that make the interview interesting.
