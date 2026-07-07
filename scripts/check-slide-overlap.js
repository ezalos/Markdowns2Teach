// ABOUTME: Headful detector that fails when a frontend-slides deck has overlapping boxes or content spilling off the 1920x1080 stage.
// ABOUTME: Drives window.deck to each slide's FINAL step state, then measures bounding boxes — the systemic guard against the recurring overlap bug.
//
// Why: the fixed-stage HTML format silently overlaps boxes / overflows the stage when a
// slide holds too much. scrollHeight checks alone miss it (grid/flex panels visually cover
// each other without scrolling). This measures real rects at the final revealed state:
//   - OVERLAP: two visible boxes (bg/border) that are not nested yet intersect.
//   - SPILL:   a content child whose box extends past the slide-content area (off-stage).
// Headful (DISPLAY) because layout/scale must match a real browser. HEADLESS=1 to force.
//
// Usage: node scripts/check-slide-overlap.js <deck.html> [<deck2.html> ...]
// Exit 0 = clean; 1 = overlap/spill found (printed per slide); 2 = bad args.

const puppeteer = require("puppeteer");
const path = require("path");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const CHROME = process.env.CHROME_PATH || "/usr/bin/google-chrome";
const HEADFUL = !!process.env.DISPLAY && process.env.HEADLESS !== "1";

// Tolerances (design px @ 1920x1080). A few px of intersection is anti-aliasing, not a bug.
const TOL = 6;          // min overlap on BOTH axes to count
const MIN_AREA = 800;   // min overlapping area (px^2) to count (real collisions are large)
const SPILL = 3;        // px a child may exceed the content box before it's "off stage"

async function launch() {
  const opts = {
    headless: HEADFUL ? false : "new",
    executablePath: CHROME,
    args: ["--no-sandbox", "--disable-dev-shm-usage"].concat(HEADFUL ? ["--new-window", "--window-size=1930,1090"] : []),
    defaultViewport: { width: 1920, height: 1080, deviceScaleFactor: 1 },
    protocolTimeout: 180000,
  };
  try { return await puppeteer.launch(opts); }
  catch (e) { await sleep(500); return await puppeteer.launch(opts); }
}

async function analyze(page) {
  return page.evaluate((cfg) => {
    const { TOL, MIN_AREA, SPILL } = cfg;
    const cur = window.deck.cur;
    const slide = window.deck.slides[cur];
    const content = slide.querySelector(".slide-content") || slide;
    const crect = content.getBoundingClientRect();
    const cls = (el) => ((el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className) || "").toString();
    const sel = (el) => el.tagName.toLowerCase() + (cls(el).trim() ? "." + cls(el).trim().split(/\s+/).slice(0, 2).join(".") : "");
    const SKIP = /\b(sep|logo|hl|kw|w|ix|eyb|eyebrow|sub|mascot)\b/;  // decorative inline bits
    // Deck chrome pinned outside the content flow (header bar, pager, dots, timers,
    // copy buttons) — intentionally positioned, not content boxes. Never flag them.
    const CHROME = /\b(masthead|pagination|pager|dots|progress|timer|tm-btn|copy-btn|page-num|minimap|stepbar|nav-rail)\b/;

    const visible = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 1 && r.height > 1 && s.visibility !== "hidden" && s.display !== "none" && parseFloat(s.opacity) > 0.05;
    };
    // Inline elements' bounding boxes overlap harmlessly when text wraps (e.g. two
    // <strong> words on one line) — never candidates. Only block-level content counts.
    const INLINE = /^(SPAN|STRONG|EM|B|I|A|CODE|SMALL|SUP|SUB|MARK|U|LABEL|BR|ABBR|CITE|Q)$/;
    const hasBox = (el) => {
      const s = getComputedStyle(el);
      const bg = s.backgroundColor;
      const hasBg = bg && bg !== "rgba(0, 0, 0, 0)" && bg !== "transparent";
      const hasBorder = ["Top", "Right", "Bottom", "Left"].some((d) => parseFloat(s["border" + d + "Width"]) > 0 && s["border" + d + "Style"] !== "none");
      return hasBg || hasBorder;
    };
    // A leaf block of text — the case a bg/border check misses (e.g. a quote whose
    // accent is a ::before, colliding with a neighbouring panel). "Leaf" = no
    // non-inline child that itself carries text, so we don't flag a parent vs its child.
    const blockText = (el) => {
      if (getComputedStyle(el).display.startsWith("inline")) return false;
      if (!(el.textContent || "").trim()) return false;
      return !Array.from(el.children).some((c) =>
        !INLINE.test(c.tagName) && !getComputedStyle(c).display.startsWith("inline") && (c.textContent || "").trim());
    };

    const boxes = Array.from(content.querySelectorAll("*")).filter((el) => {
      if (el.closest("svg")) return false;                 // SVG internals are not "boxes"
      if (INLINE.test(el.tagName)) return false;           // inline: harmless line-wrap overlap
      if (SKIP.test(cls(el)) || CHROME.test(cls(el)) || el.closest(".masthead")) return false;
      // Flip-card faces are intentionally stacked (one rotated 180°) — a 3D flip, not a bug.
      if (getComputedStyle(el).backfaceVisibility === "hidden" || el.closest('[style*="rotateY"], .flip, .flip-card, .face')) return false;
      if (!visible(el)) return false;
      if (!hasBox(el) && !blockText(el)) return false;     // a real box OR a leaf block of text
      const r = el.getBoundingClientRect();
      if (r.width > crect.width * 0.96 && r.height > crect.height * 0.96) return false; // full-bleed bg
      return true;
    });

    const rect = (el) => el.getBoundingClientRect();
    const overlaps = [];
    for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
      const A = boxes[i], B = boxes[j];
      if (A.contains(B) || B.contains(A)) continue;
      const a = rect(A), b = rect(B);
      const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
      const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
      if (ox > TOL && oy > TOL && ox * oy > MIN_AREA) overlaps.push(`${sel(A)} ∩ ${sel(B)} (${Math.round(ox)}×${Math.round(oy)}px)`);
    }

    // SPILL: any visible content child whose box leaves the slide-content area.
    const spill = [];
    Array.from(content.children).forEach((ch) => {
      if (!visible(ch) || CHROME.test(cls(ch))) return;     // skip pinned deck chrome
      const r = rect(ch);
      const over = Math.round(Math.max(r.bottom - crect.bottom, r.right - crect.right, crect.top - r.top, crect.left - r.left));
      if (over > SPILL) spill.push(`${sel(ch)} off by ${over}px`);
    });

    return { cur, count: window.deck.slides.length, overlaps: [...new Set(overlaps)], spill: [...new Set(spill)] };
  }, { TOL, MIN_AREA, SPILL });
}

async function testDeck(file) {
  const browser = await launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.emulateMediaFeatures([{ name: "prefers-reduced-motion", value: "reduce" }]); // snap to final state, no waiting on transitions
  await page.goto("file://" + file, { waitUntil: "load", timeout: 60000 });
  await sleep(400);
  const total = (await page.evaluate(() => window.deck.slides.length));
  const problems = [];
  for (let i = 0; i < total; i++) {
    // Reveal EVERY step instantly (final state) — measures the fullest layout, and
    // avoids animation-in-flight coordinates from stepping. reduced-motion is on too.
    await page.evaluate((n) => window.deck.goTo(n, true), i);
    await sleep(120);
    const r = await analyze(page);
    if (r.overlaps.length || r.spill.length) problems.push({ slide: i + 1, ...r });
  }
  await browser.close();
  return { file: path.basename(file), total, problems };
}

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) { console.error("usage: node scripts/check-slide-overlap.js <deck.html> [...]"); process.exit(2); }
  let bad = 0;
  for (const f of files) {
    const r = await testDeck(path.resolve(f));
    if (!r.problems.length) { console.log(`PASS  ${r.file}  (${r.total} slides, no overlap/spill)`); continue; }
    bad++;
    console.log(`FAIL  ${r.file}  (${r.problems.length}/${r.total} slides with overlap or spill):`);
    for (const p of r.problems) {
      p.overlaps.forEach((o) => console.log(`    s${String(p.slide).padStart(2, "0")} OVERLAP  ${o}`));
      p.spill.forEach((s) => console.log(`    s${String(p.slide).padStart(2, "0")} SPILL    ${s}`));
    }
  }
  process.exit(bad ? 1 : 0);
})();
