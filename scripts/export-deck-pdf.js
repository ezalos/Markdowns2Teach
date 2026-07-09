#!/usr/bin/env node
// ABOUTME: Stage 1 of deck→PDF export: race-free per-slide screenshots + hyperlink rectangles.
// ABOUTME: Never use page.pdf() on fixed-stage decks — it snapshots stale frames (2026-07-09 incident).

/*
 * Why this exists: a shipped PDF had runs of identical pages because page.pdf() captures
 * the last COMMITTED compositor frame — after deck.goTo() mutates the DOM, a fixed sleep
 * is a race (aggravated by deviceScaleFactor=2 rasterization cost). This exporter:
 *   1. waits for a real paint (double requestAnimationFrame) after each goTo,
 *   2. screenshots (captureScreenshot forces a fresh composite),
 *   3. HARD-FAILS if two consecutive slides hash identical (stale frame = abort, not ship),
 *   4. records every <a> rectangle of the active slide so stage 2 (export-deck-pdf.py)
 *      can re-attach clickable link annotations — a PDF must never lose the citations.
 *
 * Usage: node scripts/export-deck-pdf.js <deck.html> <outdir>
 * Writes <outdir>/sNN.png + <outdir>/rects.json. Stage 2 assembles the final PDF.
 */

const path = require("path");
const fs = require("fs");
const crypto = require("crypto");
const puppeteer = require("puppeteer");

const delay = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  const [deck, outdir] = process.argv.slice(2);
  if (!deck || !outdir) {
    console.error("usage: export-deck-pdf.js <deck.html> <outdir>");
    process.exit(2);
  }
  fs.mkdirSync(outdir, { recursive: true });

  const browser = await puppeteer.launch({
    headless: "new",
    executablePath: process.env.CHROME_PATH || "/usr/bin/google-chrome",
    args: ["--no-sandbox", "--disable-dev-shm-usage"],
  });
  const pg = await browser.newPage();
  await pg.emulateMediaFeatures([{ name: "prefers-reduced-motion", value: "reduce" }]);
  await pg.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });
  await pg.goto("file://" + path.resolve(deck), { waitUntil: "load" });
  await delay(700);

  const n = await pg.evaluate(() => document.querySelectorAll("section.slide").length);
  const rects = [];
  let prevHash = null;

  for (let i = 0; i < n; i++) {
    let buf = null;
    // paint-synced capture with stale-frame retry
    for (let attempt = 0; attempt < 4; attempt++) {
      await pg.evaluate((x) => window.deck.goTo(x, true), i);
      // double rAF: layout AND paint of the new state are committed before we shoot
      await pg.evaluate(() => new Promise((res) => requestAnimationFrame(() => requestAnimationFrame(res))));
      await delay(120);
      buf = await pg.screenshot({ type: "png" });
      const h = crypto.createHash("sha1").update(buf).digest("hex");
      if (h !== prevHash) { prevHash = h; break; }
      if (attempt === 3) {
        console.error(`FAIL stale frame: slide ${i + 1} rendered identical to slide ${i} after 4 attempts`);
        await browser.close();
        process.exit(1);
      }
      await delay(400); // stale frame detected — give the compositor time and retry
    }
    fs.writeFileSync(path.join(outdir, `s${String(i).padStart(2, "0")}.png`), buf);

    // hyperlink rectangles of the ACTIVE slide, in CSS px (viewport = 1920x1080 stage)
    const links = await pg.evaluate(() => {
      const slide = document.querySelectorAll("section.slide")[window.deck.cur];
      return Array.from(slide.querySelectorAll("a[href^='http']")).map((a) => {
        const r = a.getBoundingClientRect();
        return { href: a.href, x: r.x, y: r.y, w: r.width, h: r.height };
      }).filter((l) => l.w > 0 && l.h > 0);
    });
    rects.push({ slide: i + 1, links });
  }

  fs.writeFileSync(path.join(outdir, "rects.json"), JSON.stringify({ slides: n, pages: rects }, null, 1));
  console.log(`OK ${n} slides captured (paint-synced, stale-frame-checked) -> ${outdir}`);
  await browser.close();
})().catch((e) => { console.error("ERR", e.message); process.exit(1); });
