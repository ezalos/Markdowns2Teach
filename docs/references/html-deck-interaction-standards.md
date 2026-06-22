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

## 5. Verify HEADFUL, not headless

Headless Chrome diverges from real browsers on compositor transitions and gave
false passes here. Test with `make test-decks` (`scripts/test-deck-nav.js`),
which runs **headful** when a display is present, drives the real controller to
every stepped slide via event listeners, and asserts **forward animates / zero
backward animation events**. See [[feedback-animation-testing]].
