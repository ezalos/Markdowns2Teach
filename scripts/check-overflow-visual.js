// ABOUTME: Pixel-accurate slide overflow detector using Puppeteer and headless Chrome.
// ABOUTME: Checks both vertical (scrollHeight) and horizontal (scrollWidth + descendant right edges).

const { execFileSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");
const puppeteer = require("puppeteer");

const LINE_HEIGHT_PX = 37.5; // 25px font * 1.5 line-height
const RIGHT_EDGE_TOLERANCE_PX = 1; // sub-pixel rounding tolerance

function findMarp() {
  // Try common locations for the marp binary
  const candidates = [
    "marp", // in PATH
    path.join(os.homedir(), ".nvm/versions/node", "v24.11.0", "bin", "marp"),
  ];
  // Also check nvm versions dir for any installed version
  const nvmDir = path.join(os.homedir(), ".nvm/versions/node");
  if (fs.existsSync(nvmDir)) {
    const versions = fs.readdirSync(nvmDir).sort().reverse();
    for (const v of versions) {
      candidates.push(path.join(nvmDir, v, "bin", "marp"));
    }
  }
  for (const candidate of candidates) {
    try {
      execFileSync(candidate, ["--version"], {
        encoding: "utf-8",
        stdio: ["pipe", "pipe", "pipe"],
      });
      return candidate;
    } catch {
      // not found, try next
    }
  }
  console.error("Error: marp CLI not found. Install with: npm i -g @marp-team/marp-cli");
  process.exit(2);
}

function findSlideFiles(targets) {
  const files = [];
  for (const target of targets) {
    const stat = fs.statSync(target);
    if (stat.isDirectory()) {
      const found = execFileSync("find", [target, "-name", "*.md", "-type", "f"], {
        encoding: "utf-8",
      })
        .trim()
        .split("\n")
        .filter(Boolean)
        .sort();
      files.push(...found);
    } else if (target.endsWith(".md")) {
      files.push(target);
    }
  }
  return files;
}

function renderToHtml(marpBin, mdFile, tmpDir) {
  const outFile = path.join(tmpDir, "slides.html");
  try {
    execFileSync(
      marpBin,
      ["--no-stdin", "--html", "--theme-set", "./themes", "-o", outFile, mdFile],
      { encoding: "utf-8", stdio: ["pipe", "pipe", "pipe"] }
    );
    return outFile;
  } catch (err) {
    console.error(`  [WARN] Marp render failed for ${mdFile}: ${err.stderr || err.message}`);
    return null;
  }
}

async function measureOverflow(page, tolerance) {
  return page.evaluate((tol) => {
    // Only measure sections with an id (actual content slides).
    // Sections without id are Marp background pseudo-elements.
    const sections = document.querySelectorAll("section[id]");
    const results = [];
    for (let i = 0; i < sections.length; i++) {
      const s = sections[i];

      // Vertical (bottom) overflow — content taller than the slide.
      const scrollH = s.scrollHeight;
      const clientH = s.clientHeight;
      const overflowY = scrollH - clientH;

      // Horizontal (right) overflow — content wider than the slide.
      // Two complementary signals:
      //   1. scrollWidth vs clientWidth (catches any content past the right edge)
      //   2. specific descendants (img/pre/table/code) whose bounding box
      //      extends past the section's right edge — gives us the
      //      culprit element for the report
      const scrollW = s.scrollWidth;
      const clientW = s.clientWidth;
      const overflowX = scrollW - clientW;

      const sRect = s.getBoundingClientRect();
      const sectionRight = sRect.right;
      let worstRight = 0;
      let worstRightTag = null;
      let worstRightHint = null;
      // Descendants likely to push width: images, code blocks, tables, embeds.
      const candidates = s.querySelectorAll("img, pre, code, table, video, iframe, figure");
      for (const el of candidates) {
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) continue; // skip non-rendered
        const overshoot = r.right - sectionRight;
        if (overshoot > worstRight) {
          worstRight = overshoot;
          worstRightTag = el.tagName.toLowerCase();
          const src = el.getAttribute("src");
          if (src) {
            worstRightHint = src.split("/").pop();
          } else {
            const txt = (el.textContent || "").trim().replace(/\s+/g, " ");
            worstRightHint = txt ? txt.slice(0, 40) + (txt.length > 40 ? "…" : "") : null;
          }
        }
      }
      worstRight = Math.max(0, Math.round(worstRight));
      // Apply tolerance — only flag if the overshoot is meaningful.
      const flaggedRight = worstRight > tol ? worstRight : 0;
      const flaggedScrollX = overflowX > tol ? overflowX : 0;

      const heading = s.querySelector("h1, h2");
      let title = null;
      if (heading) {
        title = heading.textContent.trim().replace(/^\d+\s*[—–-]\s*/, "");
      }
      results.push({
        index: i,
        scrollH,
        clientH,
        overflowY,
        scrollW,
        clientW,
        overflowX: flaggedScrollX,
        worstRight: flaggedRight,
        worstRightTag,
        worstRightHint,
        title,
      });
    }
    return results;
  }, tolerance);
}

function formatRightIssue(slide) {
  // Prefer the descendant report (it tells you *which* element overflows);
  // fall back to scrollWidth for cases like long unbreakable text runs.
  if (slide.worstRight > 0) {
    const tag = slide.worstRightTag || "el";
    const hint = slide.worstRightHint ? ` "${slide.worstRightHint}"` : "";
    return `overflows RIGHT by ${slide.worstRight}px (<${tag}>${hint})`;
  }
  if (slide.overflowX > 0) {
    return `overflows RIGHT by ${slide.overflowX}px (content)`;
  }
  return null;
}

async function main() {
  const args = process.argv.slice(2);
  const targets = args.length > 0 ? args : ["slides"];

  const mdFiles = findSlideFiles(targets);
  if (mdFiles.length === 0) {
    console.error("No .md files found.");
    process.exit(1);
  }

  const marpBin = findMarp();

  const browser = await puppeteer.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });

  let totalOverflows = 0;
  let filesWithOverflow = 0;

  for (const mdFile of mdFiles) {
    const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), "marp-overflow-"));
    const htmlFile = renderToHtml(marpBin, mdFile, tmpDir);
    if (!htmlFile) {
      fs.rmSync(tmpDir, { recursive: true, force: true });
      continue;
    }

    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 720 });
    await page.goto(`file://${htmlFile}`, { waitUntil: "networkidle0" });

    const slides = await measureOverflow(page, RIGHT_EDGE_TOLERANCE_PX);
    await page.close();

    let fileHasOverflow = false;
    const lines = [];
    for (const slide of slides) {
      const num = String(slide.index + 1).padStart(2, "0");
      const label = slide.title ? `"${slide.title}"` : "(no title)";
      const issues = [];
      if (slide.overflowY > 0) {
        const approxLines = Math.ceil(slide.overflowY / LINE_HEIGHT_PX);
        issues.push(
          `overflows BOTTOM by ${slide.overflowY}px (~${approxLines} line${approxLines > 1 ? "s" : ""})`
        );
      }
      const rightIssue = formatRightIssue(slide);
      if (rightIssue) {
        issues.push(rightIssue);
      }
      if (issues.length > 0) {
        lines.push(`  [!] Slide ${num} ${label} -- ${issues.join("; ")}`);
        totalOverflows++;
        fileHasOverflow = true;
      } else {
        lines.push(`  [ok] Slide ${num} ${label}`);
      }
    }

    if (fileHasOverflow) {
      filesWithOverflow++;
      console.log(mdFile);
      for (const line of lines) console.log(line);
      console.log();
    }

    fs.rmSync(tmpDir, { recursive: true, force: true });
  }

  await browser.close();

  if (totalOverflows > 0) {
    console.log(
      `Result: ${totalOverflows} slide(s) overflow in ${filesWithOverflow} file(s)`
    );
    process.exit(1);
  } else {
    console.log(`OK: No overflow detected across ${mdFiles.length} file(s).`);
    process.exit(0);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
