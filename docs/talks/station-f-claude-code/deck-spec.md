<!-- ABOUTME: Voice + visual spec for the Station F deck — ports Louis's X-thread identity and speaking rules onto an HTML deck. -->
<!-- ABOUTME: Derived from ~/42/social (voice/x.md, voice/feynman-explanations.md, voice/templates/tech-talk.md, visuals/). -->

# Deck spec — voice and visuals

Sources of truth, all in `~/42/social`: `voice/x.md` (voice + clarity + citations),
`voice/feynman-explanations.md` (the understandability bar), `voice/templates/tech-talk.md`
(talk-shaped beats), `visuals/templates/theme.css` (the terminal design system — already
HTML), `visuals/identity/IDENTITY.md` (the hard rules). **The deck stays HTML**
(frontend-slides, fixed 1920×1080 stage) — only the look and the language are ported.

## 1. Language — binding rules

From `voice/x.md`'s ASD-STE100 subset. These are gates, not preferences.

- **One word, one meaning, deck-wide.** Pick the term and keep it. If S13 says "check"
  and S45 says "validate" for the same action, one is wrong. Candidate deck dictionary to
  fix before writing: **agent · harness · loop · context · memory · skill · tool ·
  coordinator · eval**. Never introduce a synonym for one of these mid-deck.
- **Name the mechanism, not a word that gestures at it.** No "leverage", "utilize",
  "robust", "powerful", "significant", "stuff", "things". If a word stands in for a
  number, give the number.
- **25 words per sentence, maximum.** A slide line describes; it is not a paragraph.
- **No hedges** — "may be", "could be", "arguably", "seems to". State the claim flat. If a
  claim is genuinely uncertain, say what is uncertain in a declarative sentence
  ("Anthropic self-reports this number; nobody has audited it").
- **Active voice** unless the actor is genuinely irrelevant.

## 2. Explanation — the Feynman bar

From `voice/feynman-explanations.md`. Applied per slide, and checked at the movement level.

- **Picture first, then zoom.** Open a movement on something the room can already see
  (a folder, a new hire's first week, a spreadsheet), then move to the mechanism.
- **Stakes before the answer.** A question or tension precedes the fact.
- **One load-bearing plain word per concept**, reused until it owns the idea. This deck's
  candidates: *loop*, *harness*, *coordinator*, *treadmill*.
- **Every analogy is marked as one, and its breaking point is stated.** The harness/new-hire
  metaphor must say where it stops (an agent does not accumulate judgment between jobs
  unless you write the memory file).
- **No false comfort.** Where the honest answer is "nobody knows" or "this part is just
  hard", say it. The admitted limits are what make the confident claims credible.
- **Name last.** Phenomenon before label: show the behaviour, then christen it
  ("…that is what people call graph engineering").
- **Rephrasing test.** Could the slide be restated without its jargon and survive? If a
  term cannot be unpacked in a clause, it is a name, not an explanation.
- **Backbone check** (the deck-level test): reading only each slide's title, in order, the
  whole argument still stands. Run this on the finished deck before ship.

## 3. Slide-level beats

From `voice/templates/tech-talk.md`, applied per movement rather than per slide:
**hook → claim → mechanism → evidence → caveat → steal → sources.** Every movement must
end with a *steal* — the thing a founder can apply on Monday. A movement with no steal is
a movement that gets cut.

Per slide, from `voice/x.md`'s structure rules: **lead with the claim or the number**;
**one idea per slide** (a second idea is a second slide or it is cut); **close on the
takeaway, not a question**.

## 4. Citations — the deck already has a harder rule

`voice/x.md` says every factual claim ships with `[n]` and the sources travel inside the
thread; figures get a `[📷N]` credit. The repo's non-negotiable is stricter and wins:
**every source is a clickable, live, exact link**, registered in `sources.yml` with a
verbatim quote, gated by `check-citation-links.py --check-live` and `verify-sources.py`.

What carries over from the X rules and is NOT already in the repo rule:
- **Figure credits are systematic.** Every figure carries its origin, not just the claims.
  A source's original published figure keeps **its title and legend intact** — never crop
  them away.
- **Never hand-build a chart with invented values to illustrate a fact.** The figure IS
  the fact. Real data through `scripts/charts/deck_chart.py`, or the source's own figure.
- **Marker findability** (from `IDENTITY.md`): a `[n]` that sources the whole slide sits by
  the title; a `[n]` that sources one element sits by that element. A footer entry with no
  marker anywhere on the slide is a bug.

## 5. Visual identity — porting the terminal design system

`visuals/templates/theme.css` is the system behind Louis's post visuals, and it is already
HTML/CSS, so the deck inherits it directly rather than imitating it.

**Tokens** (copy verbatim into the deck CSS; do not re-pick colours):

| Token | Value | Use |
|-------|-------|-----|
| `--bg` / `--bg2` | `#05070d` / `#0a0e17` | stage |
| `--ink` / `--dim` / `--faint` | `#e6edf3` / `#9fb0bd` / `#5a6a76` | text, secondary, footer |
| `--accent` | `#8ab4ff` | the number, the emphasis word |
| `--cyan` | `#5eead4` | eyebrow, prompt, chips |
| `--mono` | JetBrains Mono | eyebrows, sources, data, code |
| `--sans` | Inter | headlines and body |

**Structure** carried from the templates: the layered background (fine dot grain + two soft
glows + lifted base gradient) and the faint 54px engineering grid masked at top and bottom;
the **terminal prompt line** as the eyebrow idiom; **chips** for tags; the heavy headline
(900 weight, −.03em tracking) with a single accent word; the `.stat` treatment for a
headline number; the hairline-topped `.note` for a slide's takeaway line.

**Scaling**: the templates are built for a 1080×1350 card. The deck stage is 1920×1080, so
type steps down (a 104px card headline is ~72px here) — keep the *ratios*, not the pixel
values, and keep the mono/sans register split exactly.

**Hard rules inherited from `IDENTITY.md`** (they apply to slides as much as cards):
1. Credit on the visual: the X mark + the handle, per `IDENTITY.md` §7 — quiet, bottom left. On a deck, once
   on the cover and once on the close is enough; a per-slide credit would be noise.
2. **Never a graph with undefined axes.**
3. **Colour never carries meaning alone** — always pair with pattern, glyph, shape or position.
4. **Labels are never smaller than the caption.**
5. Source-figure crops keep the full caption and legend.
6. Constant arrowhead size in diagrams.
7. Where the field has a convention, follow it exactly; where it has several, ship one and
   say which is in use; never invent one more.

**What does NOT port**: the manim identity in `visuals/identity/` (Newsreader / Space
Grotesk / blue-purple ramps, dither-means-imagined) is the ML-explainer system for figures
and video. Mixing both in one deck would break rule 3 of `IDENTITY.md` (one colour axis per
figure). **Decision: the deck runs on the terminal system.** If a diagram is genuinely an
ML-architecture figure, it may be rendered in the manim identity and placed as an image —
but then it keeps its own legend and does not borrow deck accent colours.

## 6. Interaction

Unchanged from the repo standard: `docs/references/html-deck-interaction-standards.md`
(macOS-safe forward-only reveals, wheel nav, deep-link citations, no overlap on the fixed
stage). Motion guidance worth importing from `IDENTITY.md` §8, since stepped slides are
motion: **reveal in reading order, one element per beat**; **morph what persists** between
related slides; **a beat before the impact line**; **never show a concept before it is
introduced** (recaps come after what they summarise).

## 7. Pre-ship checklist

- [ ] Deck dictionary honoured — no synonym drift on the nine fixed terms.
- [ ] No hedges, no gesture words, no sentence over 25 words.
- [ ] Backbone check passes: titles alone carry the argument.
- [ ] Every movement ends on a steal.
- [ ] Every analogy states where it breaks.
- [ ] Every claim has `[n]`, every marker resolves, every figure is credited.
- [ ] No hand-built chart with invented values.
- [ ] `check-citation-links.py --check-live` and `verify-sources.py` clean.
- [ ] `make check` and `make test-decks` clean (overflow + overlap + nav).
