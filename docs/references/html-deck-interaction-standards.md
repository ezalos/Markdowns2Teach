# HTML deck interaction standards (frontend-slides)

<!-- ABOUTME: The interaction/animation contract every frontend-slides HTML deck must follow. -->
<!-- ABOUTME: Hard-won rules (esp. macOS-safe backward nav); reuse on every regeneration. -->

These rules apply to the self-contained HTML decks built outside Marp (the
`frontend-slides` skill), e.g. `slides/capgemini-ai-agents/`. **When you
regenerate or hand-edit such a deck, replicate every rule below** — they encode
bugs that were expensive to find (especially the macOS backward-animation one).

## 1. Stepped reveals — animate forward only, the macOS-safe way

The end state of a reveal/flip must be **identical in both directions**; only the
*transition* differs. Set the transition **inline on the element, in the same
synchronous update as the class/transform change** (do NOT rely on an ancestor
class + reflow — macOS Chromium/Brave's Core Animation compositor keeps tweening
the transform anyway, even though headless Linux Chrome doesn't):

```js
// in applySteps(), per animated element:
const back = this.dir === 'backward';
inner.style.transition = back ? 'none' : 'transform 0.65s var(--ease)'; // flip
el.style.transition    = back ? 'none' : 'opacity 0.5s var(--ease), transform 0.5s var(--ease)'; // reveal
el.classList.toggle('shown', ...);   // state change happens right after, same task
```

Track a `this.dir` flag: `'forward'` only on a forward single-step reveal;
`'backward'` for everything else (slide entry, jumps, Home/End, init).

## 2. Backward = previous slide at its final state

`LEFT` / wheel-up / `PageUp` calls `prev()`, which **jumps to the previous slide
at its final fully-revealed step** — it never reverse-steps a slide's reveals.
"Going backward = see the final state only." (Mirrors the original deck's
`retreat()`.) `RIGHT` / `Space` / wheel-down advances one reveal step (animated),
then moves to the next slide at step 0.

## 3. Scroll wheel drives slides like the arrows

Wheel-down → `next()`, wheel-up → `prev()`. **Normalize `deltaMode`** (some mice
report lines/pages, not pixels) and use a small threshold + short lock, or a
mouse that reports line deltas will silently do nothing:

```js
const dy = e.deltaMode===1 ? e.deltaY*16 : (e.deltaMode===2 ? e.deltaY*400 : e.deltaY);
if(Math.abs(dy) < 6) return;
lock=true; (dy>0 ? this.next() : this.prev()); setTimeout(()=>lock=false, 450);
```

## 4. Chrome & copy buttons & timers

- **One pagination, bottom-right.** No top-right page/step counter (it overlaps).
  Step progress as dots, bottom-center.
- **Copy buttons**: copy the full prompt via `navigator.clipboard.writeText`
  (textarea `execCommand` fallback) + a brief "Copied!"; store the payload in a
  hidden `data-copy` attribute — **never render the prompt text on the slide**.
- **Timers**: real countdowns; persist across navigation (deadline in a JS
  var/localStorage, recompute on slide entry); amber under 60s.
- **Self-contained**: inline CSS/JS; **base64-inline images**; fonts may use a CDN.
- Keep diagrams as vanilla HTML/CSS/SVG (no framework); preserve presenter notes
  as `<!-- NOTES: -->` comments; no client branding.

## 5. Citations deep-link to the EXACT source — never a bare domain

Every `Sources :` footnote link MUST point to the specific page that backs the
claim (the article, the data-insight, the docs page, the video with its `?v=`),
**never** the publisher's bare domain. `https://anthropic.com` is a failure;
`https://www.anthropic.com/engineering/building-effective-agents` is correct.

- The exact URLs live in the talk's source registry (e.g.
  `docs/talks/<talk>/sources-and-speakers.md`). **Wire that registry into the
  citation step** — pass each slide-builder the exact deep URL, not just the
  display text. An agent given only "Source: Anthropic" will default to the bare
  domain; that is the root cause this rule exists to kill.
- If the exact supporting page genuinely cannot be found, make the citation
  **text-only** (no `<a>`). A bare-domain or guessed link is worse than no link.
- Enforced by `scripts/check-citation-links.py` (wired into `make check`). The
  bar is strict: it FAILS the build on a non-asset `href` that is **(a)** a bare
  domain, **(b)** a known section index / listing page (`anthropic.com/news`,
  `/research`, `/engineering`, …), or **(c)** a stale-redirect host
  (`docs.claude.com` → cite the `code.claude.com` canonical). A deck does not
  ship until this passes with zero findings. Extend `INDEX_DENYLIST` /
  `REDIRECT_HOSTS` in the script as new index/redirect patterns surface.
- **Every source must be CLICKABLE.** The linter also FAILS on non-clickable
  sources — a text-only attribution ("Source: PostHog — …" with no `<a>`) or a
  domain named in a `Sources :` line that isn't wrapped in a link. A source you
  can't click is a source you can't verify. See CLAUDE.md's non-negotiable rule.
- **Before publishing**, also run it with `--check-live` (network): it FAILS on
  dead deep-links (4xx/5xx) — a link can have a path yet 404 (stale slug), which
  the offline check can't see. `make check` stays offline/fast; the live pass is
  the publish gate. A single-page tracker whose root IS the content goes in the
  linter's `ROOT_SOURCES` (still live-checked), not shipped as bare/text-only.
- Remediation reference: `scripts/fix-citation-links.py` rewrites bare-domain
  anchors to exact URLs in document order (the same domain is cited for different
  claims on different slides, so order matters), unlinking the unrecoverable ones.

## 6. No box overlap, no off-stage spill — the fixed stage is unforgiving

The 1920×1080 stage does not reflow: when a slide holds too much, boxes silently
overlap or content runs off the stage (a `flex:1;min-height:0` row shrinks below
a card's intrinsic height, so the card spills into the row below). `scrollHeight`
checks miss it — grid/flex panels cover each other without scrolling.

- Authoring discipline: keep one row's content within its height; if it doesn't
  fit, **split the slide or move content to a second column** — do not rely on
  `min-height:0` to magically shrink intrinsic-height cards. Respect the density
  limits (few boxes per slide, comfortable type).
- Enforced by `scripts/check-slide-overlap.js` (in `make test-decks`). It reveals
  every step (`goTo(i,true)`) to measure the fullest layout, and FAILS on:
  **OVERLAP** — two non-nested visible elements that intersect, where an element
  is a bg/border **box** OR a **leaf block of text** (a quote/paragraph whose
  accent is a `::before` has no real border but still collides — the box-only
  check missed exactly this on the SOTA-loop slide); **SPILL** — a content child
  leaving the slide-content area. Inline elements (`strong`/`span`/`a`…) are
  excluded (their line-wrap boxes overlap harmlessly), as are deck chrome, SVG
  internals, and 3D flip-card faces. Extend those exclusions, never loosen the
  thresholds, if a new intentional pattern trips it.

## 7. Verify HEADFUL, not headless

Headless Chrome diverges from real browsers on compositor transitions and gave
false passes here. Test with `make test-decks` (`scripts/test-deck-nav.js` +
`scripts/check-slide-overlap.js`), which run **headful** when a display is
present, drive the real controller to every stepped slide, and assert **forward
animates / zero backward animation events** and **zero overlap/spill**. (Overlap
geometry is identical headless; the headful requirement is only for the animation
test.) See [[feedback-animation-testing]].
