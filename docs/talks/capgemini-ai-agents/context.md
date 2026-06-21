<!-- ABOUTME: Provenance + context for the AI Agents & Claude Code Tech Lab portable content. -->
<!-- ABOUTME: Records source versions, what was extracted, and the IP boundary respected. -->

# AI Agents & Claude Code — Tech Lab · provenance

Portable, build-system-agnostic teaching content for Louis Develle's **AI Agents
& Claude Code "Tech Lab"** — a ~3h hands-on executive workshop (understand agents →
build one with Claude Code → leave with a slide-generation system + routine).

The deck content lives at `slides/capgemini-ai-agents/content/` as Markdown.
The original was authored in a proprietary React/TSX framework (not ours); only
the **teaching content** (slide copy + presenter notes + copy-paste prompts) was
reproduced here. Branding was removed so the deck is reusable for any audience.

## Versions extracted

| File | Source (read-only) | Commit | Slides |
|------|--------------------|--------|--------|
| `content/latest.md` | `~/Pro/wt-iqdeck` branch `feat/scroll-nav` | `5c55c7c` (deck def `tech-lab.ts`) | 38 active |
| `content/2026-06-10-original.md` | `~/Pro/IQxCapG-LabAgent` branch `origin/slides` | `f3d7812` (2026-06-14) | 37 |

Both are the **same course** (the agent lab) at two points in time. The latest is
the refined June 17–18 2026 rework; the original is the first ~June 10–14 build,
kept as an archival reference (slightly different ordering and a 6-step method
spine vs the latest's merged steps).

## What was removed (genericization)

The talk was originally delivered as a co-branded client engagement. Per the
content owner, **all client/company branding was stripped** while keeping every
bit of teaching content and every copy-paste prompt:

- Client/company names and co-branding (cover masthead, footers, follow-up URLs)
  → neutral placeholders ("your company", "an executive team", "[Company]").
- Co-instructor bios removed; instructor reduced to Louis Develle.
- Example person/company names in slides → generic roles.

If re-delivering for a specific client, re-skin the cover and swap the example
company back in — the structure is intentionally audience-agnostic.

## Deliberately NOT extracted (not ours)

- The sister **"AI Augmented Thinking" (Lab 1)** executive deck.
- The React framework / design-system / deck engine and any other clients' decks.
- Engagement-specific material (call transcripts, client briefs).

## Regenerating a beautiful HTML deck

The HTML deliverable is produced **outside Marp** by the `frontend-slides`
skill from `content/latest.md`. See `slides/capgemini-ai-agents/README.md`.
