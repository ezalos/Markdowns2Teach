# ABOUTME: Build automation for Marp slide decks.
# ABOUTME: Provides targets for preview, build (HTML+PPTX), sync to GDrive, and clean.

SLIDES_DIR := slides
DIST_DIR := dist
HTML_DIR := $(DIST_DIR)/html
PPTX_DIR := $(DIST_DIR)/pptx
PDF_FULL_DIR := $(DIST_DIR)/pdf-full
MARP := marp
GDRIVE_REMOTE := gdrive:Travail/Formations/Sorbonne/AutoDecks

# Find all .md files under slides/
SLIDE_FILES := $(shell find $(SLIDES_DIR) -name '*.md' -type f)

GUIDE_DIR := $(DIST_DIR)/guide
PANDOC := $(shell command -v pandoc 2>/dev/null || echo "$(HOME)/.local/bin/pandoc")

.PHONY: all preview build pptx html html-inline index check check-citations lint-authority-map dedup clean sync serve deploy guide pdf-full help html-% pptx-% pdf-full-% build-%

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@printf "\n  Per-subdir pattern targets (scope to slides/<NAME>/):\n"
	@printf "    \033[36m%-15s\033[0m %s\n" "html-<NAME>"     "e.g. make html-station-f"
	@printf "    \033[36m%-15s\033[0m %s\n" "pptx-<NAME>"     "e.g. make pptx-session-04"
	@printf "    \033[36m%-15s\033[0m %s\n" "pdf-full-<NAME>" "e.g. make pdf-full-station-f"
	@printf "    \033[36m%-15s\033[0m %s\n" "build-<NAME>"    "HTML + PPTX + PDF for one subdir"

all: build ## Build all outputs (HTML + PPTX)

preview: ## Launch Marp preview server
	$(MARP) --preview $(SLIDES_DIR)

build: html pptx pdf-full ## Build both HTML and PPTX

html: $(HTML_DIR) ## Build HTML slides → dist/html/
	@set -e; \
	for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(HTML_DIR)/$$slug-$$(basename $$f .md).html"; \
		echo "  HTML: $$f -> $$outfile"; \
		$(MARP) "$$f" -o "$$outfile"; \
	done
	@for d in $$(find $(SLIDES_DIR) -type d -name assets); do \
		echo "  ASSETS: $$d -> $(HTML_DIR)/assets/"; \
		mkdir -p "$(HTML_DIR)/assets"; \
		cp -ru "$$d/." "$(HTML_DIR)/assets/"; \
	done
	@for h in $$(find $(SLIDES_DIR) -maxdepth 2 -name '*.html' -type f); do \
		echo "  PREBUILT: $$h -> $(HTML_DIR)/$$(basename $$h)"; \
		cp "$$h" "$(HTML_DIR)/$$(basename $$h)"; \
	done
	@$(MAKE) index
	@if [ -x .private/build-hook.sh ]; then .private/build-hook.sh "$(HTML_DIR)"; fi

index: $(HTML_DIR) ## Generate index.html with links to all decks
	@echo "  INDEX: $(HTML_DIR)/index.html"
	@python3 scripts/generate-index.py $(SLIDES_DIR) $(HTML_DIR)

pptx: $(PPTX_DIR) ## Build PPTX presentations → dist/pptx/
	@set -e; \
	for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(PPTX_DIR)/$$slug-$$(basename $$f .md).pptx"; \
		echo "  PPTX: $$f -> $$outfile"; \
		$(MARP) --pptx-editable "$$f" -o "$$outfile"; \
		uv run scripts/fix-pptx-margins.py "$$outfile"; \
	done

html-inline: html ## Inject image preloader script into HTML slides
	@python3 scripts/inline-images.py $(HTML_DIR)

serve: html-inline ## Serve password-protected HTML slides on port 8080
	python3 scripts/serve-auth.py $(HTML_DIR) --port 8080

deploy: html ## Publish to slides.develle.fr (rebuilds dist/html, served live by `make serve` on :8080)
	@echo "  DEPLOY: dist/html rebuilt — slides.develle.fr proxies (nginx@TinyButMighty) → TheBeast:8080 → serve-auth.py (live)."
	@echo "          The running 'make serve' picks up changes immediately. Hard-refresh (Ctrl+Shift+R) to bypass browser cache."
	@echo "          If 'make serve' is not running, start it: make serve"

sync: ## Sync PPTX files to Google Drive via rclone
	rclone sync $(PPTX_DIR)/ $(GDRIVE_REMOTE) --progress

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

pdf-full: $(PDF_FULL_DIR) ## Build full-content PDFs (no clipping) → dist/pdf-full/
	@set -e; \
	for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(PDF_FULL_DIR)/$$slug-$$(basename $$f .md).pdf"; \
		echo "  PDF:  $$f -> $$outfile"; \
		$(MARP) --no-stdin --pdf \
			--allow-local-files "$$f" -o "$$outfile"; \
	done

# --- Per-subdir pattern rules (iterate on one deck dir at a time) ---
# Usage: make build-station-f  /  make html-station-f  /  make pptx-session-04
# The pattern stem `$*` is the first-level directory under slides/.

html-%: $(HTML_DIR) ## Build HTML for slides/<NAME>/ only (e.g. make html-station-f)
	@set -e; \
	for f in $$(find $(SLIDES_DIR)/$* -name '*.md' -type f); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(HTML_DIR)/$$slug-$$(basename $$f .md).html"; \
		echo "  HTML: $$f -> $$outfile"; \
		$(MARP) "$$f" -o "$$outfile"; \
	done
	@for d in $$(find $(SLIDES_DIR)/$* -type d -name assets); do \
		echo "  ASSETS: $$d -> $(HTML_DIR)/assets/"; \
		mkdir -p "$(HTML_DIR)/assets"; \
		cp -ru "$$d/." "$(HTML_DIR)/assets/"; \
	done
	@$(MAKE) index

pptx-%: $(PPTX_DIR) ## Build PPTX for slides/<NAME>/ only
	@set -e; \
	for f in $$(find $(SLIDES_DIR)/$* -name '*.md' -type f); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(PPTX_DIR)/$$slug-$$(basename $$f .md).pptx"; \
		echo "  PPTX: $$f -> $$outfile"; \
		$(MARP) --pptx-editable "$$f" -o "$$outfile"; \
		uv run scripts/fix-pptx-margins.py "$$outfile"; \
	done

pdf-full-%: $(PDF_FULL_DIR) ## Build full-content PDFs for slides/<NAME>/ only
	@set -e; \
	for f in $$(find $(SLIDES_DIR)/$* -name '*.md' -type f); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||' | tr '/' '-'); \
		outfile="$(PDF_FULL_DIR)/$$slug-$$(basename $$f .md).pdf"; \
		echo "  PDF:  $$f -> $$outfile"; \
		$(MARP) --no-stdin --pdf \
			--allow-local-files "$$f" -o "$$outfile"; \
	done

build-%: html-% pptx-% pdf-full-% ## Build HTML+PPTX+PDF for slides/<NAME>/ only
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
	mkdir -p $(HTML_DIR)

$(PPTX_DIR):
	mkdir -p $(PPTX_DIR)

$(PDF_FULL_DIR):
	mkdir -p $(PDF_FULL_DIR)

clean: ## Remove all build artifacts
	rip $(DIST_DIR) 2>/dev/null || true
