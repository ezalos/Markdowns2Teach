# ABOUTME: Build automation for Marp slide decks.
# ABOUTME: Pattern-rule build with per-file timestamps + asset deps (incremental).

SLIDES_DIR := slides
DIST_DIR := dist
HTML_DIR := $(DIST_DIR)/html
PPTX_DIR := $(DIST_DIR)/pptx
PDF_FULL_DIR := $(DIST_DIR)/pdf-full
MARP := marp
GDRIVE_REMOTE := gdrive:Travail/Formations/Sorbonne/AutoDecks

# All Marp source files. Auto-exclude any prebuilt frontend-slides deck dir
# (one that holds its own .html): their .md are portable content + README
# (regeneration sources), not Marp decks.
SLIDE_FILES := $(shell find $(SLIDES_DIR) -name '*.md' -type f $(shell find $(SLIDES_DIR) -maxdepth 2 -name '*.html' -type f -printf '-not -path %h/* '))

# Output paths mirror source layout under dist/ (no path-flattening)
HTML_OUT := $(patsubst $(SLIDES_DIR)/%.md,$(HTML_DIR)/%.html,$(SLIDE_FILES))
PPTX_OUT := $(patsubst $(SLIDES_DIR)/%.md,$(PPTX_DIR)/%.pptx,$(SLIDE_FILES))
PDF_OUT  := $(patsubst $(SLIDES_DIR)/%.md,$(PDF_FULL_DIR)/%.pdf,$(SLIDE_FILES))

# Pre-built HTML decks (rendered by frontend-slides, not Marp)
PREBUILT_SRC := $(shell find $(SLIDES_DIR) -maxdepth 2 -name '*.html' -type f)
PREBUILT_OUT := $(patsubst $(SLIDES_DIR)/%.html,$(HTML_DIR)/%.html,$(PREBUILT_SRC))

# Asset symlinks: for each deck dir that has assets/, expose dist/html/<deck>/assets → source
ASSET_SRC_DIRS := $(shell find $(SLIDES_DIR) -type d -name assets)
ASSET_LINK_OUT := $(patsubst $(SLIDES_DIR)/%,$(HTML_DIR)/%,$(ASSET_SRC_DIRS))

# Global build inputs (any change → rebuild all)
THEMES := $(wildcard themes/*.css)
GLOBAL_DEPS := .marprc.yml $(THEMES) Makefile

# Pre-bucket outputs by top-level deck dir so per-subdir targets can use simple variable
# lookups (filter+stem in prereqs runs into Make's % escape rules — variables sidestep it).
TOP_DIRS := $(notdir $(patsubst %/,%,$(wildcard $(SLIDES_DIR)/*/)))
define topdir_rules
HTML_OUT_$(1)     := $$(filter $(HTML_DIR)/$(1)/%,$$(HTML_OUT))
PREBUILT_OUT_$(1) := $$(filter $(HTML_DIR)/$(1)/%,$$(PREBUILT_OUT))
ASSET_OUT_$(1)    := $$(filter $(HTML_DIR)/$(1)/%,$$(ASSET_LINK_OUT))
PPTX_OUT_$(1)     := $$(filter $(PPTX_DIR)/$(1)/%,$$(PPTX_OUT))
PDF_OUT_$(1)      := $$(filter $(PDF_FULL_DIR)/$(1)/%,$$(PDF_OUT))
endef
$(foreach d,$(TOP_DIRS),$(eval $(call topdir_rules,$(d))))

GUIDE_DIR := $(DIST_DIR)/guide
PANDOC := $(shell command -v pandoc 2>/dev/null || echo "$(HOME)/.local/bin/pandoc")

.PHONY: all preview build pptx html html-inline index check check-citations lint-authority-map dedup clean sync serve deploy test-decks guide pdf-full help html-% pptx-% pdf-full-% build-% assets

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@printf "\n  Per-subdir pattern targets (scope to slides/<NAME>/):\n"
	@printf "    \033[36m%-15s\033[0m %s\n" "html-<NAME>"     "e.g. make html-station-f"
	@printf "    \033[36m%-15s\033[0m %s\n" "pptx-<NAME>"     "e.g. make pptx-session-04"
	@printf "    \033[36m%-15s\033[0m %s\n" "pdf-full-<NAME>" "e.g. make pdf-full-station-f"
	@printf "    \033[36m%-15s\033[0m %s\n" "build-<NAME>"    "HTML + PDF + PPTX for one subdir"

all: build ## Build all outputs (HTML + PDF + PPTX)

preview: ## Launch Marp preview server
	$(MARP) --preview $(SLIDES_DIR)

# Order: HTML first (fastest), PDF next (most important), PPTX last.
build: html pdf-full pptx ## Build HTML + PDF + PPTX (incremental)

# --- HTML ---

html: $(HTML_OUT) $(PREBUILT_OUT) assets index ## Build HTML slides → dist/html/<deck>/
	@if [ -x .private/build-hook.sh ]; then .private/build-hook.sh "$(HTML_DIR)"; fi

# Pattern rule: dist/html/<rel>.html depends on slides/<rel>.md + global deps + that deck's assets.
# Asset deps are resolved at expansion time via $(shell find ...).
.SECONDEXPANSION:
$(HTML_DIR)/%.html: $(SLIDES_DIR)/%.md $(GLOBAL_DEPS) $$(shell find $(SLIDES_DIR)/$$(dir $$*)assets -type f 2>/dev/null)
	@mkdir -p $(dir $@)
	@echo "  HTML: $< -> $@"
	@$(MARP) "$<" -o "$@"

# Pre-built HTML: copy from source to mirrored output path.
$(HTML_DIR)/%.html: $(SLIDES_DIR)/%.html
	@mkdir -p $(dir $@)
	@echo "  PREBUILT: $< -> $@"
	@cp "$<" "$@"

# Assets: symlink each source assets/ dir to its co-located output location.
assets: $(ASSET_LINK_OUT)

$(HTML_DIR)/%/assets: $(SLIDES_DIR)/%/assets | $(HTML_DIR)
	@mkdir -p $(dir $@)
	@if [ ! -L "$@" ]; then \
		rm -rf "$@" 2>/dev/null || true; \
		ln -s "$(abspath $<)" "$@"; \
		echo "  ASSETS: $< -> $@ (symlink)"; \
	fi

index: $(HTML_DIR) ## Generate index.html with links to all decks
	@echo "  INDEX: $(HTML_DIR)/index.html"
	@python3 scripts/generate-index.py $(SLIDES_DIR) $(HTML_DIR)

# --- PPTX ---

pptx: $(PPTX_OUT) ## Build PPTX presentations → dist/pptx/<deck>/

.SECONDEXPANSION:
$(PPTX_DIR)/%.pptx: $(SLIDES_DIR)/%.md $(GLOBAL_DEPS) $$(shell find $(SLIDES_DIR)/$$(dir $$*)assets -type f 2>/dev/null)
	@mkdir -p $(dir $@)
	@echo "  PPTX: $< -> $@"
	@$(MARP) --pptx-editable "$<" -o "$@"
	@uv run scripts/fix-pptx-margins.py "$@"

# --- PDF ---

pdf-full: $(PDF_OUT) ## Build full-content PDFs (no clipping) → dist/pdf-full/<deck>/

.SECONDEXPANSION:
$(PDF_FULL_DIR)/%.pdf: $(SLIDES_DIR)/%.md $(GLOBAL_DEPS) $$(shell find $(SLIDES_DIR)/$$(dir $$*)assets -type f 2>/dev/null)
	@mkdir -p $(dir $@)
	@echo "  PDF:  $< -> $@"
	@$(MARP) --no-stdin --pdf --allow-local-files "$<" -o "$@"

# --- Post-processing & serve ---

html-inline: html ## Inject image preloader script into HTML slides
	@python3 scripts/inline-images.py $(HTML_DIR)

serve: html-inline ## Serve password-protected HTML slides on port 8080
	python3 scripts/serve-auth.py $(HTML_DIR) --port 8080

test-decks: ## Headless test: frontend-slides decks never animate on backward nav
	@node -e "require('puppeteer').launch({headless:'new',executablePath:'$${CHROME_PATH:-/usr/bin/google-chrome}',args:['--no-sandbox']}).then(b=>b.close()).catch(()=>{})" 2>/dev/null || true
	@node scripts/test-deck-nav.js slides/capgemini-ai-agents/capgemini-ai-agents.html slides/capgemini-ai-agents/capgemini-ai-agents-original.html

deploy: html ## Publish to slides.develle.fr (rebuilds dist/html, served live by `make serve` on :8080)
	@echo "  DEPLOY: dist/html rebuilt — slides.develle.fr proxies (nginx@TinyButMighty) → TheBeast:8080 → serve-auth.py (live)."
	@echo "          The running 'make serve' picks up changes immediately. Hard-refresh (Ctrl+Shift+R) to bypass browser cache."
	@echo "          If 'make serve' is not running, start it: make serve"

sync: ## Sync PPTX files to Google Drive via rclone
	rclone sync $(PPTX_DIR)/ $(GDRIVE_REMOTE) --progress

# --- Checks ---

lint-authority-map: ## Verify authority-map.md and authority-map.yaml are in sync
	@python3 scripts/cite/lint_authority_map.py

check: lint-authority-map ## Detect slides that overflow (pixel-accurate, requires npm install)
	@node scripts/check-overflow-visual.js $(SLIDES_DIR)

check-citations: ## Warn about data slides missing source citations
	@bash scripts/check-citations.sh $(SLIDES_DIR)

dedup: ## Remove duplicate images from all asset directories
	@for d in $$(find $(SLIDES_DIR) -type d -name assets); do \
		python3 scripts/dedup-images.py "$$d"; \
	done

# --- Per-subdir pattern targets (iterate on one deck dir at a time) ---
# Stem is a top-level dir under slides/, e.g. `station-f` or `sorbonne-m2-2026`.
# Static-pattern filters against pre-computed *_OUT lists, so prereqs are real targets
# (no recursive $(MAKE) needed for the build step — only for `index`).

html-%: $$(HTML_OUT_$$*) $$(PREBUILT_OUT_$$*) $$(ASSET_OUT_$$*) ## Build HTML for slides/<NAME>/ only
	@$(MAKE) index

pptx-%: $$(PPTX_OUT_$$*) ## Build PPTX for slides/<NAME>/ only
	@true

pdf-full-%: $$(PDF_OUT_$$*) ## Build full-content PDFs for slides/<NAME>/ only
	@true

build-%: html-% pdf-full-% pptx-% ## Build HTML + PDF + PPTX for slides/<NAME>/ only
	@true

guide: ## Build student guide as DOCX → dist/guide/
	@bash scripts/install-pandoc.sh
	@mkdir -p $(GUIDE_DIR)
	$(PANDOC) docs/courses/sorbonne-m2/n8n-student-guide.md \
		-o $(GUIDE_DIR)/n8n-student-guide.docx \
		--metadata title="Guide n8n — Projet de Classification IA" \
		--metadata lang=fr
	@echo "  GUIDE: $(GUIDE_DIR)/n8n-student-guide.docx"

$(HTML_DIR):
	@mkdir -p $(HTML_DIR)

$(PPTX_DIR):
	@mkdir -p $(PPTX_DIR)

$(PDF_FULL_DIR):
	@mkdir -p $(PDF_FULL_DIR)

clean: ## Remove all build artifacts
	rip $(DIST_DIR) 2>/dev/null || true
