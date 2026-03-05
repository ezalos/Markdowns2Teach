// ABOUTME: Pixel-accurate slide overflow detector using Puppeteer and headless Chrome.
// ABOUTME: Renders Marp slides to HTML and compares scrollHeight vs clientHeight per section.

const { execFileSync } = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");
const puppeteer = require("puppeteer");

const LINE_HEIGHT_PX = 37.5; // 25px font * 1.5 line-height

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

async function measureOverflow(page) {
  return page.evaluate(() => {
    // Only measure sections with an id (actual content slides).
    // Sections without id are Marp background pseudo-elements.
    const sections = document.querySelectorAll("section[id]");
    const results = [];
    for (let i = 0; i < sections.length; i++) {
      const s = sections[i];
      const scrollH = s.scrollHeight;
      const clientH = s.clientHeight;
      const overflow = scrollH - clientH;
      const heading = s.querySelector("h1, h2");
      let title = null;
      if (heading) {
        title = heading.textContent.trim().replace(/^\d+\s*[—–-]\s*/, "");
      }
      results.push({ index: i, scrollH, clientH, overflow, title });
    }
    return results;
  });
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

    const slides = await measureOverflow(page);
    await page.close();

    let fileHasOverflow = false;
    const lines = [];
    for (const slide of slides) {
      const num = String(slide.index + 1).padStart(2, "0");
      const label = slide.title ? `"${slide.title}"` : "(no title)";
      if (slide.overflow > 0) {
        const approxLines = Math.ceil(slide.overflow / LINE_HEIGHT_PX);
        lines.push(
          `  [!] Slide ${num} ${label} -- overflows by ${slide.overflow}px (~${approxLines} line${approxLines > 1 ? "s" : ""})`
        );
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
