Plan: Repo Restructuring, Convention Updates, and Conversion Pipeline
                                                             
 Context                             

 The Marp slide pipeline POC is working (theme, Makefile, 8 slides build to HTML+PPTX). Louis has reorganized the repo — source materials are now in references/ and docs/. Several convention changes are needed (language, numbering,
 images), and we need to set up the full conversion pipeline for both Andrew Ng and Kevin Vu materials.

 ---
 Step 1: Fix .gitignore for reference PDFs

 File: .gitignore

 The blanket *.pdf rule blocks reference PDFs from git. Change it to target only dist/ output:

 - Replace *.pdf with dist/**/*.pdf
 - Keep *.pptx as-is (or similarly scope to dist/**/*.pptx)

 ---
 Step 2: Update CLAUDE.md — paths and structure

 File: CLAUDE.md

 Update directory structure to reflect references/, docs/, plans/, scripts/, and assets/ subdirs. Update the Source Materials table:
 ┌──────────────────────────────┬─────────────────────────────────┐
 │           Old path           │            New path             │
 ├──────────────────────────────┼─────────────────────────────────┤
 │ sorbonne/AndrewNg/W1 (1).pdf │ references/AndrewNg/W1.pdf      │
 ├──────────────────────────────┼─────────────────────────────────┤
 │ 2026 M2 - ML & DeepTech.md   │ docs/2026 M2 - ML & DeepTech.md │
 ├──────────────────────────────┼─────────────────────────────────┤
 │ Kevin Vu M2 Sorbonne *.md    │ docs/Kevin Vu M2 Sorbonne *.md  │
 ├──────────────────────────────┼─────────────────────────────────┤
 │ NotebookLM.prompt.txt        │ docs/NotebookLM.prompt.txt      │
 ├──────────────────────────────┼─────────────────────────────────┤
 │ sorbonne/archivedwl-455/     │ references/KevinVu/             │
 └──────────────────────────────┴─────────────────────────────────┘
 Add entries for W2, W3 PDFs and Kevin Vu's HTML files.

 ---
 Step 3: Update CLAUDE.md — language convention

 File: CLAUDE.md (Content guidelines section)

 Replace bilingual translation rule with:
 - French body text, English technical terms used directly (no French translation)
 - Technical terms stay English: "Supervised Learning", "Deep Learning", "Prompt Engineering"
 - Do NOT write "Apprentissage supervisé (Supervised Learning)"
 - Instead: "Le Supervised Learning est la technique la plus déployée..."

 ---
 Step 4: Update CLAUDE.md — slide numbering convention

 File: CLAUDE.md (Marp Slide Standards section)

 Add flat per-file numbering:
 - Format: # 03 — Title Here (2-digit number)
 - Title slides and section dividers are NOT numbered
 - Numbering is per-file, restarts in each .md
 - Makes it easy to reference: "move slide 03 after 05"

 ---
 Step 5: Apply convention changes to existing POC slides

 File: slides/andrew-ng-genai/ch01-intro-genai/01-what-is-genai.md

 - Remove *(English Term)* translation patterns — keep technical terms in English directly
 - Add flat slide numbers to content slide H1 titles
 - Update ABOUTME comment to remove "Bilingual" phrasing

 Key changes:
 - L'essor de l'IA générative *(The Rise of GenAI)* → # 01 — L'essor de la Generative AI
 - Apprentissage supervisé *(Supervised Learning)* → Supervised Learning
 - Détection de fraude *(Fraud detection)* → Fraud Detection
 - etc.

 ---
 Step 6: Add overflow: hidden CSS safety + build overflow checker script

 Files: themes/sorbonne.css, scripts/check-overflow.sh, Makefile

 CSS

 Add overflow: hidden to section in the theme to clip overflowing content visually.

 Script (scripts/check-overflow.sh)

 Splits markdown on ---, counts non-empty/non-comment content lines per slide, warns if any exceed a threshold (default: 15 lines). Exits non-zero if warnings found.

 Makefile

 Add check target that runs the script on all slide files:
 make check    # Warn about likely overflow

 ---
 Step 7: Extract images from Andrew Ng W1 PDF

 Files: scripts/extract-images.sh, slides/andrew-ng-genai/ch01-intro-genai/assets/

 Create a reusable scripts/extract-images.sh that:
 1. Uses pdfimages -png to extract embedded images
 2. Filters out small images (<200px wide) — logos, masks, decorative elements
 3. Renames remaining images sequentially (img-001.png, img-002.png, ...)

 Run it on references/AndrewNg/W1.pdf for ch01. Verify ![bg left:50%](assets/img-001.png) renders correctly with the sorbonne theme (Marp's bg left/right directives are built-in, no extra CSS needed).

 ---
 Step 8: Create Andrew Ng conversion roadmap

 File: plans/andrew-ng-conversion-roadmap.md

 A chapter-by-chapter plan for converting W1.pdf (88p), W2.pdf (57p), W3.pdf (49p) into numbered Marp slide decks. Structure:

 - Overview table (week, PDF, pages, estimated Marp slides, target chapter)
 - Conversion principles (progressive-reveal compression, English terms, stats updates for 2026, engagement questions)
 - Per-week section breakdown mapping PDF page ranges to output .md files
 - Image strategy (what to extract, what to render as full-page screenshots)

 ---
 Step 9: Test conversion of Kevin Vu cours_1.html

 Files: slides/kevin-vu-ml/ch01-introduction/01-intro-ml.md, slides/kevin-vu-ml/ch01-introduction/assets/

 Download images

 Attempt to fetch images from kvu.pythonanywhere.com/static/images/ (referenced in the HTML). If the server is offline, fall back to [IMAGE MISSING] placeholders.

 Convert first ~8-10 sections of cours_1.html

 WebSlides → Marp mapping:
 - <section> boundary → ---
 - <div class="cta"> → <!-- _class: title -->
 - <div class="card-50"> → <!-- _class: cols --> or ![bg left:50%]
 - <ul class="flexblock steps"> → numbered list
 - <div class="grid vertical-align"><div class="column"> → columns or bg image

 Apply the new conventions: flat numbering, English technical terms, sorbonne theme.

 Validate

 Build HTML + PPTX, run make check for overflow warnings.

 ---
 Step 10: Update memory file

 File: /home/ezalos/.claude/projects/-home-ezalos-42-Markdowns2Teach/memory/MEMORY.md

 Update with new conventions (language, numbering, image workflow, Kevin Vu format notes).

 ---
 Execution Order

 Batch 1 (independent):  Steps 1, 2, 3, 4, 6
 Batch 2 (depends on 3): Step 5
 Batch 3 (independent):  Steps 7, 9 (image work)
 Batch 4 (depends on 7): Step 8
 Batch 5 (all done):     Step 10

 No git commit in this plan — will do separately when Louis is ready.

 ---
 Verification

 1. make build succeeds with no errors
 2. make check reports no overflow warnings on updated POC slides
 3. PPTX renders correctly with images (test ![bg left:50%] layout)
 4. Kevin Vu test conversion builds and renders
 5. plans/andrew-ng-conversion-roadmap.md exists with per-chapter breakdown
 6. CLAUDE.md accurately reflects repo structure, language rules, and numbering
