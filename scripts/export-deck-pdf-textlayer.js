#!/usr/bin/env node
// ABOUTME: Alternative deck→PDF export that keeps a real TEXT LAYER (selectable, searchable).
// ABOUTME: Chrome print-to-PDF against the deck's @media print rules; screenshot export stays the default.
//
// Why this exists alongside export-deck-pdf.js:
//   The screenshot exporter is the SAFE default — it guarantees correct frames after the
//   2026-07-09 stale-frame incident, at the cost of rasterising every slide (no selectable
//   text). This path renders vector text and native link annotations instead.
//
//   The stale-frame race it was written to avoid does not apply here: print mode reveals
//   every slide at once via the deck's own `@media print` rules, so nothing drives the
//   slide controller and there is no frame to go stale. That claim is not taken on trust —
//   the companion verifier refuses the output if any two consecutive pages are identical,
//   the same bar the screenshot path is held to.
//
// Usage: node scripts/export-deck-pdf-textlayer.js <deck.html> <out.pdf>

const puppeteer = require("puppeteer-core");
const path = require("path");

const CHROME = process.env.CHROME_PATH || "/usr/bin/google-chrome";

(async () => {
  const [deck, out] = process.argv.slice(2);
  if (!deck || !out) {
    console.error("usage: export-deck-pdf-textlayer.js <deck.html> <out.pdf>");
    process.exit(2);
  }

  const browser = await puppeteer.launch({
    headless: "new",
    executablePath: CHROME,
    args: ["--no-sandbox", "--font-render-hinting=none"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto("file://" + path.resolve(deck), { waitUntil: "networkidle0", timeout: 120000 });

  // Fonts must be in before layout is frozen for print, or headings reflow mid-export.
  await page.evaluate(() => document.fonts.ready);
  await new Promise((r) => setTimeout(r, 600));

  await page.emulateMediaType("print");
  await page.addStyleTag({
    content: `
      /* Presentation chrome is position:fixed, so without this it stamps itself
         onto every printed page. */
      .pagination, .stepdots, .hint, .deck-controls { display: none !important; }
      /* Reveal every step: a printed page has no clicks. */
      .step-group, .reveal { opacity: 1 !important; transform: none !important; }
      /* Kill the page margin so the 1920x1080 stage is the whole page. */
      @page { margin: 0; size: 1920px 1080px; }
    `,
  });
  await new Promise((r) => setTimeout(r, 400));

  await page.pdf({
    path: out,
    width: "1920px",
    height: "1080px",
    printBackground: true,
    preferCSSPageSize: false,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });

  await browser.close();
  console.log(`wrote ${out}`);
})();
