<!-- ABOUTME: Human-readable mirror of authority-map.yaml — this repo's OVERLAY over the
     global /cite base map. Kept in sync by make lint-authority-map. -->

# Authority map — Markdowns2Teach overlay

The global base roster lives at `~/.claude/skills/cite/memory/authority-map.md` (source:
`~/Setup/skills/cite/memory/`). This file holds ONLY repo-specific additions and overrides;
/cite layers it over the base via repeatable `--map` (later wins). The byte-identical
duplication of the base was removed 2026-07-13 (deck-capability design).

*(No overlay entries yet. To add one, create a `## Tier N — <label>` section with
`- `domain.tld` — rationale` bullets, mirror it in authority-map.yaml, and run
`make lint-authority-map`.)*
