# What Is an Agent? (Hermes, Claude Code, and friends)

*A foundations primer for a moderately technical audience. The goal here is to nail down the vocabulary and the core mental model, so that deeper topics land on solid ground.*

---

## The one-sentence version

An **LLM agent** is a system where a language model is given a goal, a set of **tools**, and the freedom to **decide its own next steps in a loop** — taking actions, observing the results, and adjusting — until the goal is met.

The key word is *loop*. A plain chatbot answers once. An agent keeps going: act, look at what happened, decide what to do next, repeat.

---

## 1. From chatbot to agent

It helps to see the progression, because "agent" is the last step of a fairly natural ladder.

| Level | What it is | Who's in control of the steps |
|-------|-----------|-------------------------------|
| **Single call** | One prompt in, one completion out | The human |
| **Chain / pipeline** | Several LLM calls wired together in a fixed order (e.g. summarize → classify → respond) | The developer (hardcoded) |
| **Workflow** | LLM calls and tools orchestrated through **predefined paths**, possibly with branching | The developer (the control flow is written in advance) |
| **Agent** | The LLM itself **decides** what to do next, which tool to call, and when it's done | The model (dynamic control flow) |

The line that actually matters is the last one. In a **workflow**, a human author has written the control flow — the model just fills in steps. In an **agent**, the model *directs its own control flow*: it chooses the sequence of actions at runtime. That shift — from "the model is a step in someone else's program" to "the model is running the program" — is the whole idea.

A useful litmus test: *if you can't predict in advance exactly which tools will be called, in what order, and how many times — it's an agent.*

---

## 2. The anatomy of an agent

Almost every agent, however fancy, is built from the same five parts:

1. **A model** — the LLM doing the reasoning and deciding. This is the "brain."
2. **Tools** — the things the model can *do* to affect the outside world: read a file, run a shell command, search the web, call an API, query a database. Without tools, a model can only talk. (More in §4.)
3. **A loop** — the control mechanism that feeds the results of actions back to the model so it can decide the next move. (More in §3.)
4. **Context / memory** — what the model can "see" right now (the conversation, retrieved documents, prior results) plus, in more advanced systems, what it remembers across sessions.
5. **An objective + a stopping condition** — the goal it's pursuing, and some way of knowing it's finished (task complete, user satisfied, budget exhausted, max steps reached).

If you remember nothing else: **model + tools + loop**. The rest is refinement.

---

## 3. The agent loop (the core mechanic)

This is the engine. Often called the **ReAct** pattern (Reason + Act). One turn of the loop looks like:

```
  ┌─────────────────────────────────────────────┐
  │                                               │
  │   1. OBSERVE   →   2. REASON   →   3. ACT      │
  │   (current state)  (think/plan)  (call a tool) │
  │        ▲                              │        │
  │        └──────────────────────────────┘        │
  │              result feeds back in              │
  └─────────────────────────────────────────────┘
        repeat until the goal is met or it stops
```

Concretely, each iteration is:

1. **Observe** — the model receives the goal plus the current state (including the result of the last action).
2. **Reason** — it thinks about what to do next ("the test failed because of an import error; I should open the file and fix the import").
3. **Act** — it emits a **tool call** (e.g. `edit_file(path, change)`).
4. The environment **executes** the tool and returns an **observation** (e.g. the new file contents, or an error).
5. That observation is **appended to the context**, and the loop repeats.

A worked example — *"fix the failing test in my project"*:

```
Goal: make the test suite pass

Step 1  Reason: "I should run the tests to see what's broken."
        Act:    run_command("pytest")
        Observe: "FAILED test_auth.py — ImportError: no module named 'jwt'"

Step 2  Reason: "A dependency is missing. Install it."
        Act:    run_command("pip install pyjwt")
        Observe: "Successfully installed pyjwt-2.8.0"

Step 3  Reason: "Re-run the tests to confirm."
        Act:    run_command("pytest")
        Observe: "5 passed"

Step 4  Reason: "All tests pass. Done."
        → stop
```

Nobody hardcoded "install pyjwt then re-run." The model figured out that sequence from the observations. That's the agent doing its own control flow.

---

## 4. Tools (how a model actually *does* things)

A model on its own only outputs text. **Tools** (a.k.a. **function calling**) are what let it act on the world. The mechanism is simpler than it sounds:

1. You give the model a list of available tools, each with a **name**, a **description**, and a **schema** for its arguments (typically JSON).
2. When the model wants to act, it doesn't *perform* the action — it **emits a structured request**: "call `search_web` with `{query: "..."}`".
3. Your surrounding code (the "harness" or "runtime") actually executes that function and hands the **result back** to the model as the next observation.

So the model proposes; the runtime disposes. This separation is important: the model never directly touches your filesystem or network — it asks, and a layer you control decides whether and how to fulfill the request. (That's also where most of the **safety and permissioning** lives.)

Tools are the single biggest lever on what an agent can accomplish. A great model with no tools is just a conversationalist; a modest model with well-designed tools can get real work done.

> **MCP (Model Context Protocol)** is worth knowing as a term: it's an emerging open standard for exposing tools and data sources to agents in a uniform way, so the same tool can plug into many different agents. Both Claude Code and Hermes support it.

---

## 5. Two concrete examples

These two sit at different points on the spectrum, which is exactly why they're a useful pair.

### Claude Code — a *task / coding* agent

A coding agent that runs in your terminal (and in IDEs). You point it at a project and give it a goal; it then reads and edits files, runs commands, inspects the output, and iterates — the §3 loop, applied to software. Characteristics:

- **Scoped to a session and a task.** You start it, it works toward a goal, you close it.
- **Lives where your code lives** — the terminal / repo / IDE.
- **Interactive** — you're typically in the loop, reviewing and steering.

Think of it as a very capable pair-programmer that can actually touch the keyboard.

### Hermes Agent — a *persistent autonomous* agent

An open-source agent from Nous Research (released early 2026) that takes a different stance. Rather than living in your IDE for one task, it's designed to **run continuously on a server** and act as an always-on personal agent. Characteristics:

- **Persistent memory** — it remembers your projects, preferences, and past work *across sessions*, instead of starting fresh each time.
- **Model-agnostic** — it can be pointed at many different underlying LLMs rather than being tied to one.
- **Multi-platform reach** — you can talk to it from messaging apps (Telegram, Discord, Slack…) while it works on a remote machine.
- **Self-improving** — it can write reusable "skills" from experience so it doesn't re-solve the same problem twice.

Think of it less as a tool you open and more as a process that lives somewhere and keeps working.

### The contrast in one line

| | Claude Code | Hermes |
|---|---|---|
| **Lifespan** | Per-session, per-task | Always-on, persistent |
| **Lives in** | Your terminal / IDE | A server you control |
| **Memory** | Mostly within the session | Long-term, across sessions |
| **Model** | Anthropic's | Pluggable / many |
| **Human role** | In the loop, steering | More hands-off, message it |

Same fundamental machinery (model + tools + loop) — very different product shape. That's the point worth driving home: **"agent" is an architecture, not a single product.** The interesting variation is in *autonomy, persistence, and where the human sits.*

---

## 6. What agents are good at — and where they struggle

**Good fit:**
- Multi-step tasks where the steps can't be fully scripted in advance
- Tasks with a clear feedback signal to act on (tests pass/fail, a query returns/errors)
- Work that benefits from tool use (code, research, data wrangling, ops)

**Still hard / risky:**
- **Error compounding** — a wrong turn early can cascade; small mistakes accumulate over a long loop.
- **Cost and latency** — every loop iteration is one or more model calls.
- **Knowing when to stop** — agents can loop, over-engineer, or declare victory too early.
- **Trust and safety** — an agent with real tools can do real damage; permissioning and human oversight matter.

A practical principle from the field: *use the simplest thing that works.* A fixed workflow is more predictable and cheaper than an agent — reach for full agentic autonomy only when the task genuinely needs dynamic, unpredictable control flow.

---

## 7. Quick glossary

- **LLM** — large language model; the underlying text-prediction model.
- **Agent** — an LLM given tools and a loop, directing its own steps toward a goal.
- **Tool / function calling** — structured requests the model emits to perform actions; executed by surrounding code.
- **ReAct** — the Reason-then-Act loop pattern most agents use.
- **Harness / runtime / scaffold** — the code around the model that runs the loop, executes tools, and manages context.
- **Workflow** — orchestration with *predefined* control flow (vs. an agent's dynamic control flow).
- **Context window** — what the model can "see" in a given call; finite, and a key constraint.
- **Memory** — persistence of information across turns or sessions, beyond the context window.
- **MCP (Model Context Protocol)** — an open standard for connecting tools and data to agents.
- **Stopping condition** — how the loop knows it's done (task complete, max steps, budget).

---

*Next up: the in-depth topics build on this — planning strategies, memory architectures, multi-agent systems, evaluation, and safety/permissioning all sit on top of the model + tools + loop foundation above.*
