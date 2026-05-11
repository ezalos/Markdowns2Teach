# Social Skills — Design Spec

**Date:** 2026-04-16
**Author:** Louis Develle (with Claude)
**Status:** Approved (brainstorming → ready for plan)

## Problem

Louis posts on LinkedIn (existing voice, ~20 posts) and wants to start posting on X/Twitter (fresh, sharper-articulation goal). Each post currently takes ~30 minutes of blank-screen time. Manual publication is non-negotiable (Louis presses publish himself), but every step before that — voice consistency, hook generation, drafting, iteration, and post-mortem metric capture — is automatable.

Long-term, the system should learn from real engagement metrics and evolve its rules. v1 ships the writer + the data scaffolding; the pattern engine is deferred until enough data accumulates.

## Goals

- Write LinkedIn and X posts in Louis's voice, in minutes not 30+
- Capture every published post's metrics in a structured, grep-able format
- Make voice rules a versioned, evolvable artifact (not buried in a prompt)
- Manual publication preserved — skills never call platform APIs to publish
- Free / no-cost data collection (manual entry; ~60s per post)

## Non-goals (v1)

- Automated publishing
- Automated metric scraping (API/scraping rabbit hole)
- A "pattern engine" that auto-mutates voice rules from metrics — deferred to v2 once corpus is ≥10 posts/platform
- Cross-platform repurposing (write once → adapt across platforms) — deferred
- Instagram, Mastodon, Bluesky, etc. — architecture supports adding them, but not built v1

## Voice baseline (observed from 3 pasted LinkedIn posts)

**Hook patterns:**
1. Concrete event + specific claim ("I just taught AI agents to founders at STATION F. The slide that sparked the most debate? …")
2. Achievement + scale number ("I just designed three AI projects that will teach 25,000+ students worldwide…")
3. Bold Unicode title block (𝗦𝗲𝗲𝗸𝗶𝗻𝗴 𝗻𝗲𝘄 𝗼𝗽𝗽𝗼𝗿𝘁𝘂𝗻𝗶𝘁𝗶𝗲𝘀…)

**Signature moves:** Unicode bold for mid-post section headers; 🔹/→ bullet hierarchy; numbers early and often, bolded; explicit named gratitude (full names, role); EN for tech, FR with EN tech terms preserved for local/teaching content.

**Structure:** opener → context → bullets → reflection → gratitude → CTA → hashtag cluster.

**Tone:** confident, evidence-first ("from the data, not intuition"); no false modesty, no bragging; gratitude is explicit and names people.

**X target voice (Louis's brief, no corpus yet):** sharp insights, focused over broad, clarity + articulation, "deliver the value I would have liked to find myself."

## Architecture

### File layout

```
~/social/                           # new git repo, $SOCIAL_HOME
├── README.md
├── voice/
│   ├── linkedin.md                 # voice rules (audited from corpus)
│   └── x.md                        # voice rules (from brief + future corpus)
├── sources/
│   ├── linkedin-posts.md           # pasted seed posts
│   └── linkedin-export/            # gitignored — full LinkedIn archive when it arrives
├── drafts/
│   └── YYYY-MM-DD-slug-<platform>.md
├── posted/
│   └── YYYY-MM-DD-slug-<platform>.md  # metrics in frontmatter after /log
├── data-store.yaml                 # flat log, one entry per posted item
└── evolution-log.md                # manual rule-change notes

~/.claude/skills/
├── post/SKILL.md                   # /post linkedin|x
├── log/SKILL.md                    # /log linkedin|x
└── audit/SKILL.md                  # /audit linkedin|x
```

`SOCIAL_HOME=~/social` exported in `.zshrc`. Skills read `$SOCIAL_HOME` with `~/social` fallback.

### Why this layout

- **Content separated from code.** Voice rules evolve; `~/.claude/skills/` is for behavior. Couplings are explicit (env var) instead of hidden (paths-inside-skill).
- **Git-tracked content repo.** `git diff` on voice rules captures evolution. `evolution-log.md` is the human-readable record of *why* a rule changed (Woodrider92's "evolution log" concept).
- **Flat YAML data store.** One file, one row per post, grep-able. The future pattern engine reads this unchanged. No DB, no schema migration.
- **Drafts vs posted.** Posted items get metrics in frontmatter and move to `posted/`. The drafts dir stays clean.
- **Three skills, one job each.** Following the `/cite` family pattern Louis already uses. Avoids "what mode am I in?" branching inside a monolithic skill.

## Skills

### `/post linkedin|x`

**Steps:**
1. Read `$SOCIAL_HOME/voice/<platform>.md`. If missing → prompt to run `/audit <platform>` first.
2. Interview (one `AskUserQuestion` per field):
   - **Goal** — Build authority / Inspire / Convert / Entertain / Document
   - **Media** — Text-only / Image(s) / Carousel / Video (if video → ask for transcript or key points)
   - **Message** — raw idea, lesson, opinion, result. Messy is fine.
   - **Emotion** — what reaction? curiosity, urgency, agreement, awe
   - **Audience** — specifically who? (not "everyone")
3. Generate 5 hooks using hook patterns from voice rules. Numbered list, each with a one-line rationale tying to a specific pattern.
4. User picks one (or asks to regenerate, or edits inline).
5. Draft full post around the chosen hook, applying voice rules end-to-end (signature moves, structure, tone, vocabulary, what-to-avoid).
6. Iterate freely until "ship it".
7. Write to `$SOCIAL_HOME/drafts/YYYY-MM-DD-slug-<platform>.md` with frontmatter (goal, media, audience, hook-pattern).
8. Output the final post text ready to paste.

**Does not:** publish to any platform. Manual paste only.

### `/log linkedin|x`

**Steps:**
1. List drafts in `$SOCIAL_HOME/drafts/<platform>` not yet logged.
2. User picks one, or pastes a URL for a published post not in drafts.
3. Prompt for: post URL, impressions, reactions, comments, reposts, optional notes.
4. Append row to `$SOCIAL_HOME/data-store.yaml` (schema below).
5. Move the draft from `drafts/` to `posted/`, write metrics into its frontmatter.

**Data-store row schema:**
```yaml
- id: 2026-04-16-station-f-claude-memory-linkedin
  platform: linkedin
  url: https://www.linkedin.com/posts/...
  posted_at: 2026-04-16T17:00:00Z
  hook_pattern: "concrete-event-plus-claim"
  goal: "build-authority"
  media: "carousel-3-slides"
  audience: "ML practitioners / founders"
  word_count: 312
  metrics:
    impressions: 563
    reactions: 27
    comments: 6
    reposts: 0
  engagement_rate: 0.058   # (reactions + comments + reposts) / impressions
  notes: "Carousel of leaked Claude Code source — debate driver"
```

**Why flat YAML:** future pattern engine (v2) iterates this file with `grep`/`yq` or a 30-line Python script. No DB, no ORM, no schema migration.

### `/audit linkedin|x`

**Steps:**
1. Read corpus: `$SOCIAL_HOME/sources/<platform>-posts.md` + every `posted/*-<platform>.md`.
2. Read existing `voice/<platform>.md` if present.
3. Analyse: hooks, tone, structure, formatting, vocabulary, what's avoided.
4. Propose rule changes as a diff against current `voice/<platform>.md`.
5. User accepts / edits / rejects per-section.
6. Write updated `voice/<platform>.md`.
7. Append a one-line entry to `evolution-log.md`: date + rule changed + reason.

**First-run** (no `voice/<platform>.md` exists): generate from scratch using corpus + Louis's brief.

## Voice rules file structure

`voice/<platform>.md` sections:
- **Format** — length range, structural patterns, bullet style
- **Tone** — confidence level, formality, language conventions
- **Hook patterns** — 3-5 named patterns with real examples from corpus
- **Structure** — typical opener → … → close template
- **Vocabulary** — terms used freely; recurring expressions
- **What to avoid** — generic openers, AI tells, banned words
- **Endings** — CTA styles, closing patterns

Rules are **prescriptive** ("Always use Unicode bold for mid-post section headers") not descriptive ("tends to use Unicode bold"). Claude follows direct instructions better than observations.

## Workflow end-to-end

**Setup (one-time):**
1. `mkdir ~/social && cd ~/social && git init`
2. Paste 5–10 best LinkedIn posts into `sources/linkedin-posts.md`
3. Write X voice brief into `sources/x-brief.md` (bullets are fine)
4. Run `/audit linkedin` → generates `voice/linkedin.md`
5. Run `/audit x` → generates `voice/x.md` from brief
6. Export `SOCIAL_HOME=~/social` in `.zshrc`

**Per-post (recurring):**
1. `/post linkedin` → interview → hooks → draft → iterate → save to `drafts/`
2. Paste draft into LinkedIn, publish
3. ~24h later: `/log linkedin` → enter metrics → row in `data-store.yaml`

**Periodic (~monthly, after ~10 new posts/platform):**
1. `/audit linkedin` → suggested rule diff based on what's working
2. Accept/edit/reject → `voice/linkedin.md` updated, `evolution-log.md` appended

## Skill file shape

Each skill at `~/.claude/skills/<name>/SKILL.md` with frontmatter:

```yaml
---
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
description: <one-line trigger guidance>
---
```

Skill body documents: trigger, steps, error modes, references to `$SOCIAL_HOME`.

## Open questions deferred to v2

- **Pattern engine** — read `data-store.yaml`, propose voice-rule mutations. Needs ≥10 posts/platform corpus first.
- **Inspiration hooks bank** — `voice/inspiration.md` of proven angles. Manually curated initially.
- **Cross-platform adaptation** — `/post x --from drafts/...-linkedin.md` to remix.
- **LinkedIn full-archive importer** — once the real "Archive of your data" export arrives (24h after re-request), one-shot script extracts `Shares.csv` → `sources/linkedin-posts.md` and `Reactions.csv`/`Comments.csv` → historical entries in `data-store.yaml` (no impressions; those are analytics-only).

## Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| Voice rules drift from actual writing | Re-audit periodically; `evolution-log.md` keeps human reasoning |
| Manual metric entry feels tedious → skipped | `/log` is fast (≤60s); list of unlogged drafts is shown each time |
| LinkedIn analytics not exportable | Accept the manual-entry tradeoff; document it in README |
| Voice file too long / over-specified | Cap each section; prefer prescriptive bullets to prose |
| Skills duplicate voice rules in their bodies | Skills MUST read `voice/<platform>.md` at runtime, not embed |

## Success criteria

- Posting a LinkedIn post end-to-end (interview → draft → publish-ready) takes ≤10 minutes
- Voice rules in `voice/linkedin.md` are something Louis would actually share as "this is how I write"
- After 10 posts logged, `data-store.yaml` is structured enough that a future pattern engine can read it without preprocessing
- Manual entry per post is ≤60 seconds
