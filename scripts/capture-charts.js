// ABOUTME: Puppeteer-based chart capture script for JS-heavy web pages (Epoch AI, Plotly, etc.).
// ABOUTME: Navigates to a URL, waits for charts to render, and saves high-res PNG screenshots.

const fs = require("fs");
const path = require("path");
const puppeteer = require("puppeteer");

// ---------------------------------------------------------------------------
// CLI argument parsing (manual — no external deps, matches project convention)
// ---------------------------------------------------------------------------

function printUsage() {
  console.log(`Usage: node capture-charts.js <url> [options]

Options:
  -o, --output <dir>     Output directory (default: .)
  -s, --selector <css>   CSS selector to capture (repeatable)
  -p, --prefix <name>    Filename prefix (default: derived from URL slug)
  --full-page            Full-page screenshot instead of individual elements
  --width <px>           Viewport width (default: 1400)
  --scale <factor>       Device pixel ratio (default: 2)
  --wait <ms>            Extra wait after network idle (default: 2000)
  --list                 List detected chart elements without capturing
  -h, --help             Show this help`);
}

function parseArgs(argv) {
  const opts = {
    url: null,
    output: ".",
    selectors: [],
    prefix: null,
    fullPage: false,
    width: 1400,
    scale: 2,
    wait: 2000,
    list: false,
  };

  let i = 0;
  while (i < argv.length) {
    const arg = argv[i];
    if (arg === "-h" || arg === "--help") {
      printUsage();
      process.exit(0);
    } else if (arg === "-o" || arg === "--output") {
      opts.output = argv[++i];
    } else if (arg === "-s" || arg === "--selector") {
      opts.selectors.push(argv[++i]);
    } else if (arg === "-p" || arg === "--prefix") {
      opts.prefix = argv[++i];
    } else if (arg === "--full-page") {
      opts.fullPage = true;
    } else if (arg === "--width") {
      opts.width = parseInt(argv[++i], 10);
    } else if (arg === "--scale") {
      opts.scale = parseFloat(argv[++i]);
    } else if (arg === "--wait") {
      opts.wait = parseInt(argv[++i], 10);
    } else if (arg === "--list") {
      opts.list = true;
    } else if (!arg.startsWith("-") && !opts.url) {
      opts.url = arg;
    } else {
      console.error(`Unknown option: ${arg}`);
      printUsage();
      process.exit(1);
    }
    i++;
  }

  if (!opts.url) {
    console.error("Error: URL is required.");
    printUsage();
    process.exit(1);
  }

  // Validate URL
  try {
    new URL(opts.url);
  } catch {
    console.error(`Error: invalid URL "${opts.url}"`);
    process.exit(1);
  }

  // Derive prefix from URL slug if not provided
  if (!opts.prefix) {
    const urlPath = new URL(opts.url).pathname.replace(/\/$/, "");
    const slug = urlPath.split("/").pop() || "chart";
    opts.prefix = slug.replace(/[^a-z0-9-]/gi, "-").substring(0, 40);
  }

  return opts;
}

// ---------------------------------------------------------------------------
// Chart auto-detection (priority cascade)
// ---------------------------------------------------------------------------

async function detectCharts(page) {
  return page.evaluate(() => {
    const seen = new Set();
    const results = [];

    function addElement(el, source) {
      // Skip elements inside nav, header, footer
      if (el.closest("nav, header, footer")) return;
      // Deduplicate: if we already captured a parent <figure>, skip child
      for (const s of seen) {
        if (s.contains(el) || el.contains(s)) return;
      }
      seen.add(el);

      const rect = el.getBoundingClientRect();
      results.push({
        tag: el.tagName.toLowerCase(),
        id: el.id || null,
        className: (el.className && typeof el.className === "string")
          ? el.className.split(/\s+/).slice(0, 3).join(" ")
          : "",
        width: Math.round(rect.width),
        height: Math.round(rect.height),
        source: source,
      });
    }

    // 1. Epoch AI convention: [id^="figure-"]
    for (const el of document.querySelectorAll('[id^="figure-"]')) {
      addElement(el, "figure-id");
    }

    // 2. <figure> elements containing <svg> or <canvas>
    for (const fig of document.querySelectorAll("figure")) {
      if (fig.querySelector("svg, canvas")) {
        addElement(fig, "figure-with-chart");
      }
    }

    // 3. Common chart library classes
    const chartSelectors = [
      ".chart", ".plot", ".plotly", ".js-plotly-plot",
      ".vega-embed", ".highcharts-container",
      ".recharts-wrapper", ".chart-container",
      ".observable", "[data-chart]",
    ];
    for (const sel of chartSelectors) {
      for (const el of document.querySelectorAll(sel)) {
        addElement(el, `class:${sel}`);
      }
    }

    // 4. Large standalone <svg> (>300px wide, not tiny icons)
    for (const svg of document.querySelectorAll("svg")) {
      const rect = svg.getBoundingClientRect();
      if (rect.width > 300 && rect.height > 100) {
        addElement(svg, "large-svg");
      }
    }

    // 5. Large standalone <canvas> (>300px wide)
    for (const canvas of document.querySelectorAll("canvas")) {
      const rect = canvas.getBoundingClientRect();
      if (rect.width > 300 && rect.height > 100) {
        addElement(canvas, "large-canvas");
      }
    }

    return results;
  });
}

// ---------------------------------------------------------------------------
// Cookie banner dismissal
// ---------------------------------------------------------------------------

async function dismissCookieBanners(page) {
  // First try clicking accept buttons
  const buttonSelectors = [
    'button[id*="cookie" i][id*="accept" i]',
    'button[class*="cookie" i][class*="accept" i]',
    'button[aria-label*="accept" i]',
    'a[id*="cookie" i][id*="accept" i]',
    '[class*="cookie-banner" i] button',
    '[class*="cookie-consent" i] button',
    '[id*="cookie-banner" i] button',
    '[id*="consent" i] button:first-of-type',
  ];

  for (const sel of buttonSelectors) {
    try {
      const btn = await page.$(sel);
      if (btn) {
        await btn.click();
        await new Promise((r) => setTimeout(r, 500));
        break;
      }
    } catch {
      // Ignore — selector may not exist
    }
  }

  // Then forcibly remove any remaining cookie/consent overlays from the DOM
  const removed = await page.evaluate(() => {
    const selectors = [
      '[class*="cookie" i]', '[id*="cookie" i]',
      '[class*="consent" i]', '[id*="consent" i]',
      '[class*="CookieBanner" i]', '[id*="CookieBanner" i]',
    ];
    let count = 0;
    for (const sel of selectors) {
      for (const el of document.querySelectorAll(sel)) {
        // Only remove if it looks like a banner (fixed/sticky positioned, or covers viewport)
        const style = window.getComputedStyle(el);
        const isOverlay = style.position === "fixed" || style.position === "sticky"
          || el.getBoundingClientRect().width > window.innerWidth * 0.5;
        if (isOverlay) {
          el.remove();
          count++;
        }
      }
    }
    return count;
  });

  return removed > 0;
}

// ---------------------------------------------------------------------------
// Scroll to bottom (triggers lazy-loading)
// ---------------------------------------------------------------------------

async function scrollToBottom(page) {
  await page.evaluate(async () => {
    const delay = (ms) => new Promise((r) => setTimeout(r, ms));
    const step = Math.max(document.documentElement.clientHeight, 400);
    let y = 0;
    while (y < document.body.scrollHeight) {
      y += step;
      window.scrollTo(0, y);
      await delay(200);
    }
    // Scroll back to top
    window.scrollTo(0, 0);
  });
}

// ---------------------------------------------------------------------------
// Wait for chart elements to stabilize
// ---------------------------------------------------------------------------

async function waitForCharts(page, timeoutMs) {
  const start = Date.now();
  let lastCount = 0;

  while (Date.now() - start < timeoutMs) {
    const count = await page.evaluate(() => {
      return document.querySelectorAll("svg, canvas, [id^='figure-']").length;
    });
    if (count > 0 && count === lastCount) {
      return count;
    }
    lastCount = count;
    await new Promise((r) => setTimeout(r, 300));
  }
  return lastCount;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const opts = parseArgs(process.argv.slice(2));

  // Ensure output directory exists
  if (!opts.list) {
    fs.mkdirSync(opts.output, { recursive: true });
  }

  console.log(`Navigating to: ${opts.url}`);
  console.log(`Viewport: ${opts.width}x900 @ ${opts.scale}x`);

  const browser = await puppeteer.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });

  const page = await browser.newPage();
  await page.setViewport({
    width: opts.width,
    height: 900,
    deviceScaleFactor: opts.scale,
  });

  // Navigate and wait for network to settle
  await page.goto(opts.url, {
    waitUntil: "networkidle0",
    timeout: 30000,
  });

  // Scroll to trigger lazy-loading
  await scrollToBottom(page);

  // Wait for chart elements to appear and stabilize
  const chartElCount = await waitForCharts(page, opts.wait);
  console.log(`Found ${chartElCount} SVG/canvas/figure elements after waiting.`);

  // Dismiss cookie banners
  const dismissed = await dismissCookieBanners(page);
  if (dismissed) {
    console.log("Dismissed cookie banner.");
  }

  // -- Full-page mode --
  if (opts.fullPage && !opts.list) {
    const outPath = path.join(opts.output, `${opts.prefix}-full.png`);
    await page.screenshot({ path: outPath, fullPage: true });
    console.log(`Saved full-page screenshot: ${outPath}`);
    await browser.close();
    return;
  }

  // -- Detect or use explicit selectors --
  let elements;

  if (opts.selectors.length > 0) {
    // Use explicit selectors
    elements = [];
    for (const sel of opts.selectors) {
      const found = await page.evaluate((s) => {
        const els = document.querySelectorAll(s);
        return Array.from(els).map((el) => {
          const rect = el.getBoundingClientRect();
          return {
            tag: el.tagName.toLowerCase(),
            id: el.id || null,
            className: (el.className && typeof el.className === "string")
              ? el.className.split(/\s+/).slice(0, 3).join(" ")
              : "",
            width: Math.round(rect.width),
            height: Math.round(rect.height),
            source: `selector:${s}`,
          };
        });
      }, sel);
      elements.push(...found);
    }
  } else {
    // Auto-detect
    elements = await detectCharts(page);
  }

  if (elements.length === 0) {
    console.log("No chart elements detected.");
    await browser.close();
    return;
  }

  // -- List mode --
  if (opts.list) {
    console.log(`\nDetected ${elements.length} chart element(s):\n`);
    for (let i = 0; i < elements.length; i++) {
      const el = elements[i];
      const idStr = el.id ? `#${el.id}` : "(no id)";
      const classStr = el.className ? `.${el.className.replace(/ /g, ".")}` : "";
      const hidden = (el.width === 0 && el.height === 0) ? "  [HIDDEN]" : "";
      console.log(
        `  ${String(i + 1).padStart(2)}. <${el.tag}> ${idStr} ${classStr}  ${el.width}×${el.height}px  [${el.source}]${hidden}`
      );
    }
    await browser.close();
    return;
  }

  // Filter out hidden (0×0) elements before capture
  elements = elements.filter((el) => el.width > 0 && el.height > 0);

  // -- Capture mode --
  console.log(`\nCapturing ${elements.length} element(s)...\n`);
  const captured = [];

  for (let i = 0; i < elements.length; i++) {
    const el = elements[i];

    // Build selector to re-find this specific element
    let selector;
    if (opts.selectors.length > 0) {
      // For explicit selectors, re-use them (nth match)
      selector = opts.selectors[Math.min(i, opts.selectors.length - 1)];
    } else if (el.id) {
      selector = `#${el.id}`;
    } else {
      // Fall back to nth-of-type for the detection source
      selector = null;
    }

    // Build filename
    let filename;
    if (el.id) {
      filename = `${opts.prefix}-${el.id}.png`;
    } else {
      filename = `${opts.prefix}-${String(i + 1).padStart(2, "0")}.png`;
    }
    const outPath = path.join(opts.output, filename);

    try {
      let handle;
      if (selector) {
        const handles = await page.$$(selector);
        // For auto-detected elements with an id, there's exactly one match
        // For explicit selectors, take the i-th match
        handle = el.id ? handles[0] : handles[i] || handles[0];
      } else {
        // Fallback: use the auto-detection ordering — re-run detection and index
        const allHandles = await detectAndGetHandles(page, i);
        handle = allHandles;
      }

      if (handle) {
        await handle.screenshot({ path: outPath });
        captured.push(outPath);
        console.log(`  [${String(i + 1).padStart(2)}] ${filename}  (${el.width}×${el.height}px)`);
      } else {
        console.log(`  [${String(i + 1).padStart(2)}] SKIP — could not locate element`);
      }
    } catch (err) {
      console.log(`  [${String(i + 1).padStart(2)}] ERROR — ${err.message}`);
    }
  }

  await browser.close();

  console.log(`\nDone: ${captured.length}/${elements.length} chart(s) captured.`);
  if (captured.length > 0) {
    console.log(`Output directory: ${path.resolve(opts.output)}`);
  }
}

// ---------------------------------------------------------------------------
// Fallback handle finder for elements without an id or explicit selector.
// Re-runs the same detection cascade and returns the handle at the given index.
// ---------------------------------------------------------------------------

async function detectAndGetHandles(page, targetIndex) {
  return page.evaluateHandle((idx) => {
    const seen = new Set();
    const results = [];

    function maybeAdd(el) {
      if (el.closest("nav, header, footer")) return;
      for (const s of seen) {
        if (s.contains(el) || el.contains(s)) return;
      }
      seen.add(el);
      results.push(el);
    }

    for (const el of document.querySelectorAll('[id^="figure-"]')) maybeAdd(el);
    for (const fig of document.querySelectorAll("figure")) {
      if (fig.querySelector("svg, canvas")) maybeAdd(fig);
    }
    const cls = [
      ".chart", ".plot", ".plotly", ".js-plotly-plot",
      ".vega-embed", ".highcharts-container",
      ".recharts-wrapper", ".chart-container",
      ".observable", "[data-chart]",
    ];
    for (const sel of cls) {
      for (const el of document.querySelectorAll(sel)) maybeAdd(el);
    }
    for (const svg of document.querySelectorAll("svg")) {
      const r = svg.getBoundingClientRect();
      if (r.width > 300 && r.height > 100) maybeAdd(svg);
    }
    for (const canvas of document.querySelectorAll("canvas")) {
      const r = canvas.getBoundingClientRect();
      if (r.width > 300 && r.height > 100) maybeAdd(canvas);
    }

    return results[idx] || null;
  }, targetIndex);
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
