// ABOUTME: Headless regression test that a frontend-slides deck never animates on BACKWARD nav.
// ABOUTME: Event-listener based (not screenshot timing): drives window.deck to each stepped slide.
//
// Why this exists: an earlier screenshot/getAnimations test gave FALSE PASSES — it sampled
// animation state too late and didn't drive to the stepped slides, so it "passed" on a deck
// that visibly replayed animations when stepping backward. This test instead:
//   - forces prefers-reduced-motion: no-preference (match a real browser, not headless defaults)
//   - listens for transitionstart/animationstart events (fire deterministically when anything moves)
//   - drives the real controller (window.deck) to EVERY stepped slide
//   - asserts forward DOES animate (proves detection works) and backward fires ZERO events,
//     including the mid-animation interrupt case (ArrowLeft pressed during a forward reveal)
//
// Usage: node scripts/test-deck-nav.js <deck.html> [<deck2.html> ...]
// Exit 0 = all decks pass; non-zero = a backward animation was detected (prints the culprit).

const puppeteer = require("puppeteer");
const path = require("path");

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const CHROME = process.env.CHROME_PATH || "/usr/bin/google-chrome";

async function launch() {
  // First Chrome launch in a fresh shell occasionally exits 126; retry once.
  try {
    return await puppeteer.launch({
      headless: "new",
      executablePath: CHROME,
      args: ["--no-sandbox", "--disable-dev-shm-usage"],
      protocolTimeout: 180000,
    });
  } catch (e) {
    await sleep(500);
    return await puppeteer.launch({
      headless: "new",
      executablePath: CHROME,
      args: ["--no-sandbox", "--disable-dev-shm-usage"],
      protocolTimeout: 180000,
    });
  }
}

async function installListeners(page) {
  await page.evaluate(() => {
    window.__ev = [];
    const rec = (e) => {
      const t = e.target;
      const cls = ((t.className && t.className.baseVal !== undefined ? t.className.baseVal : t.className) || "").toString();
      window.__ev.push(`${e.type}:${e.propertyName || e.animationName || ""} on ${t.tagName || "?"}.${cls.split(" ").slice(0, 2).join(".")}`);
    };
    ["transitionstart", "animationstart"].forEach((ev) => document.addEventListener(ev, rec, true));
    window.__reset = () => { window.__ev = []; };
    window.__events = () => window.__ev.slice();
  });
}

const state = (page) =>
  page.evaluate(() => ({
    cur: window.deck.cur,
    step: window.deck.step,
    steps: window.deck.stepCount(window.deck.cur),
    count: window.deck.slides.length,
  }));

async function testDeck(file) {
  const browser = await launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.emulateMediaFeatures([{ name: "prefers-reduced-motion", value: "no-preference" }]);
  await page.goto("file://" + file, { waitUntil: "load", timeout: 60000 });
  await sleep(400);
  await installListeners(page);

  const fails = [];
  let fwdEventsTotal = 0;
  const total = (await state(page)).count;

  // Walk the whole deck forward; at every stepped slide, verify forward animates
  // and backward (within the slide) fires nothing.
  await page.evaluate(() => window.deck.goTo(0, false));
  for (let i = 0; i < total; i++) {
    await page.evaluate((n) => window.deck.goTo(n, false), i);
    await sleep(120);
    const s = await state(page);
    if (!s.steps) continue;

    // forward through the steps — must animate
    await page.evaluate(() => window.__reset());
    for (let k = 0; k < s.steps; k++) { await page.keyboard.press("ArrowRight"); await sleep(320); }
    const fwd = (await page.evaluate(() => window.__events())).length;
    fwdEventsTotal += fwd;
    if (fwd === 0) fails.push(`slide ${i + 1}: forward fired NO animation (detection or anim broken)`);

    // backward through the steps — must fire nothing
    for (let k = 0; k < s.steps + 1; k++) {
      await page.evaluate(() => window.__reset());
      await page.keyboard.press("ArrowLeft");
      await sleep(420);
      const evs = await page.evaluate(() => window.__events());
      if (evs.length) fails.push(`slide ${i + 1} back-step ${k}: ${evs.slice(0, 3).join(" | ")}`);
    }

    // mid-animation interrupt: start a forward reveal, press ArrowLeft 80ms in
    await page.evaluate((n) => window.deck.goTo(n, false), i);
    await sleep(120);
    for (let k = 0; k < Math.min(s.steps, 4); k++) {
      await page.keyboard.press("ArrowRight"); await sleep(80);
      await page.evaluate(() => window.__reset());
      await page.keyboard.press("ArrowLeft"); await sleep(450);
      const evs = await page.evaluate(() => window.__events());
      if (evs.length) fails.push(`slide ${i + 1} interrupt ${k}: ${evs.slice(0, 3).join(" | ")}`);
    }
  }

  await browser.close();
  return { file: path.basename(file), forwardEvents: fwdEventsTotal, backwardViolations: fails.length, fails: fails.slice(0, 12) };
}

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) { console.error("usage: node scripts/test-deck-nav.js <deck.html> [...]"); process.exit(2); }
  let bad = 0;
  for (const f of files) {
    const r = await testDeck(path.resolve(f));
    const ok = r.backwardViolations === 0 && r.forwardEvents > 0;
    console.log(`${ok ? "PASS" : "FAIL"}  ${r.file}  (forward animated: ${r.forwardEvents} events, backward violations: ${r.backwardViolations})`);
    if (!ok) { bad++; r.fails.forEach((x) => console.log("    - " + x)); if (r.forwardEvents === 0) console.log("    - forward never animated — test may not be driving the deck"); }
  }
  process.exit(bad ? 1 : 0);
})();
