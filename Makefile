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

.PHONY: all preview build pptx html html-inline index check check-citations dedup clean sync serve guide pdf-full help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

all: build ## Build all outputs (HTML + PPTX)

preview: ## Launch Marp preview server
	$(MARP) --preview $(SLIDES_DIR)

build: html pptx pdf-full ## Build both HTML and PPTX

html: $(HTML_DIR) ## Build HTML slides → dist/html/
	@for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||'); \
		outfile="$(HTML_DIR)/$$slug-$$(basename $$f .md).html"; \
		echo "  HTML: $$f -> $$outfile"; \
		$(MARP) "$$f" -o "$$outfile"; \
	done
	@for d in $$(find $(SLIDES_DIR) -type d -name assets); do \
		echo "  ASSETS: $$d -> $(HTML_DIR)/assets/"; \
		mkdir -p "$(HTML_DIR)/assets"; \
		cp -ru "$$d/." "$(HTML_DIR)/assets/"; \
	done
	@$(MAKE) index

index: $(HTML_DIR) ## Generate index.html with links to all decks
	@echo "  INDEX: $(HTML_DIR)/index.html"
	@bash scripts/generate-index.sh $(SLIDES_DIR) $(HTML_DIR)

pptx: $(PPTX_DIR) ## Build PPTX presentations → dist/pptx/
	@for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||'); \
		outfile="$(PPTX_DIR)/$$slug-$$(basename $$f .md).pptx"; \
		echo "  PPTX: $$f -> $$outfile"; \
		$(MARP) --pptx-editable "$$f" -o "$$outfile"; \
		uv run scripts/fix-pptx-margins.py "$$outfile"; \
	done

html-inline: html ## Inject image preloader script into HTML slides
	@python3 scripts/inline-images.py $(HTML_DIR)

serve: html-inline ## Serve password-protected HTML slides on port 3901
	python3 scripts/serve-auth.py $(HTML_DIR) --port 3901

sync: ## Sync PPTX files to Google Drive via rclone
	rclone sync $(PPTX_DIR)/ $(GDRIVE_REMOTE) --progress

check: ## Detect slides that overflow (pixel-accurate, requires npm install)
	@node scripts/check-overflow-visual.js $(SLIDES_DIR)

check-citations: ## Warn about data slides missing source citations
	@bash scripts/check-citations.sh $(SLIDES_DIR)

dedup: ## Remove duplicate images from all asset directories
	@for d in $$(find $(SLIDES_DIR) -type d -name assets); do \
		python3 scripts/dedup-images.py "$$d"; \
	done

pdf-full: $(PDF_FULL_DIR) ## Build full-content PDFs (no clipping) → dist/pdf-full/
	@for f in $(SLIDE_FILES); do \
		slug=$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||'); \
		outfile="$(PDF_FULL_DIR)/$$slug-$$(basename $$f .md).pdf"; \
		echo "  PDF:  $$f -> $$outfile"; \
		$(MARP) --no-stdin --pdf --theme themes/sorbonne-fullpage.css \
			--theme-set ./themes --allow-local-files "$$f" -o "$$outfile"; \
	done

guide: ## Build student guide as DOCX → dist/guide/
	@bash scripts/install-pandoc.sh
	@mkdir -p $(GUIDE_DIR)
	$(PANDOC) docs/references/n8n-student-guide.md \
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
