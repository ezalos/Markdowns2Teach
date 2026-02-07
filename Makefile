# ABOUTME: Build automation for Marp slide decks.
# ABOUTME: Provides targets for preview, build (HTML+PPTX), and clean.

SLIDES_DIR := slides
DIST_DIR := dist
MARP := marp

# Find all .md files under slides/
SLIDE_FILES := $(shell find $(SLIDES_DIR) -name '*.md' -type f)

.PHONY: all preview build pptx html check dedup clean help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

all: build ## Build all outputs (HTML + PPTX)

preview: ## Launch Marp preview server
	$(MARP) --preview $(SLIDES_DIR)

build: html pptx ## Build both HTML and PPTX

html: $(DIST_DIR) ## Build HTML slides
	@for f in $(SLIDE_FILES); do \
		outdir=$(DIST_DIR)/$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||'); \
		mkdir -p "$$outdir"; \
		outfile="$$outdir/$$(basename $$f .md).html"; \
		echo "  HTML: $$f -> $$outfile"; \
		$(MARP) "$$f" -o "$$outfile"; \
	done

pptx: $(DIST_DIR) ## Build PPTX presentations
	@for f in $(SLIDE_FILES); do \
		outdir=$(DIST_DIR)/$$(dirname $$f | sed 's|^$(SLIDES_DIR)/||'); \
		mkdir -p "$$outdir"; \
		outfile="$$outdir/$$(basename $$f .md).pptx"; \
		echo "  PPTX: $$f -> $$outfile"; \
		$(MARP) "$$f" -o "$$outfile"; \
	done

check: ## Warn about slides likely to overflow
	@bash scripts/check-overflow.sh 15 $(SLIDES_DIR)

dedup: ## Remove duplicate images from all asset directories
	@for d in $$(find $(SLIDES_DIR) -type d -name assets); do \
		python3 scripts/dedup-images.py "$$d"; \
	done

$(DIST_DIR):
	mkdir -p $(DIST_DIR)

clean: ## Remove all build artifacts
	rm -rf $(DIST_DIR)
