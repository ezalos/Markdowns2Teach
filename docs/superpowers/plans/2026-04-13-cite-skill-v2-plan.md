# `/cite` v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship v2 of the `/cite` skill family that moves judgment out of LLM subagents into deterministic Python validators, so tier assignment, quote-in-page verification, enum validation, and verification-command routing are all programmatic.

**Architecture:** Four small Python scripts under `scripts/cite/` encode the deterministic checks; each has pytest unit tests with tiny fixtures. The cite-research skill is rewritten so subagents return raw data + a preserved `page.txt`, and the orchestrator calls the validators between each subagent invocation. `tier_lookup.py` reads a new machine-readable `authority-map.yaml` that is linted in sync with the existing human `authority-map.md`.

**Tech Stack:** Python 3 + PyYAML (already available) + pytest (to be installed via pip). No network libs — validators are pure functions on local files. `pdftotext` (poppler-utils, already installed) + `marp` CLI (already installed) invoked by scripts/skills via Bash.

**Spec:** `docs/superpowers/specs/2026-04-13-cite-skill-v2-design.md`

---

## File Structure

| Path | Role | Task |
|------|------|------|
| `docs/references/authority-map.yaml` | Machine-readable tier lookup | 2 |
| `scripts/cite/__init__.py` | Empty; makes scripts/cite/ a package | 3 |
| `scripts/cite/tier_lookup.py` | url_domain → tier int or None | 4-5 |
| `scripts/cite/lint_authority_map.py` | Bidirectional sync check between .md and .yaml | 6-7 |
| `scripts/cite/validate_claim.py` | Schema + enum + quote-in-page substring validator | 8-9 |
| `scripts/cite/target_scope.py` | target .md path → verification shell command | 10-11 |
| `scripts/cite/tests/__init__.py` | Empty | 3 |
| `scripts/cite/tests/conftest.py` | pytest fixtures (sample claim, page text, yaml) | 3 |
| `scripts/cite/tests/test_tier_lookup.py` | Unit tests for tier_lookup | 4 |
| `scripts/cite/tests/test_lint_authority_map.py` | Unit tests for lint | 6 |
| `scripts/cite/tests/test_validate_claim.py` | Unit tests for validator | 8 |
| `scripts/cite/tests/test_target_scope.py` | Unit tests for target_scope | 10 |
| `Makefile` | Add `lint-authority-map` target wired into `check` | 12 |
| `~/.claude/skills/cite-scan/SKILL.md` | Add validation/page_text_file stubs to claim schema | 13 |
| `~/.claude/skills/cite-research/SKILL.md` | Major rewrite: narrow subagent + orchestrator validation loop | 14 |
| `~/.claude/skills/cite-apply/SKILL.md` | Step 6 uses target_scope.py instead of hardcoded make | 15 |
| `docs/references/cite-skill-backlog.md` | Move 5 v1 items to Resolved | 16 |

---

## Task 1: Install pytest

**Files:** none (environment only)

- [ ] **Step 1: Install pytest system-wide for the project**

Run:
```bash
pip3 install --user pytest
```

- [ ] **Step 2: Verify**

Run:
```bash
python3 -m pytest --version
```
Expected: prints pytest version (e.g., `pytest 8.x.x`).

- [ ] **Step 3: No commit** — environment change only, not tracked.

---

## Task 2: Seed `docs/references/authority-map.yaml`

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/docs/references/authority-map.yaml`

- [ ] **Step 1: Write the YAML file**

Write this exact content to `docs/references/authority-map.yaml`:

```yaml
# ABOUTME: Machine-readable authority roster; sibling to authority-map.md.
# ABOUTME: Read by scripts/cite/tier_lookup.py. Kept in sync with .md via scripts/cite/lint_authority_map.py.

tiers:
  1:
    name: "Primary sources (company IR, SEC filings, government)"
    publishers:
      - name: "SEC.gov"
        domains: ["sec.gov"]
        note: "US Securities and Exchange Commission"
      - name: "CFTC.gov"
        domains: ["cftc.gov"]
      - name: "EUR-Lex"
        domains: ["eur-lex.europa.eu"]
      - name: "European Parliament"
        domains: ["europarl.europa.eu"]
      - name: "European Commission"
        domains: ["ec.europa.eu", "digital-strategy.ec.europa.eu"]
      - name: "Anthropic"
        domains: ["anthropic.com"]
      - name: "OpenAI"
        domains: ["openai.com"]
      - name: "Mistral AI"
        domains: ["mistral.ai"]
      - name: "INSEE"
        domains: ["insee.fr"]
      - name: "Eurostat"
        domains: ["ec.europa.eu/eurostat"]
      - name: "U.S. Bureau of Labor Statistics"
        domains: ["bls.gov"]
      - name: "UK Office for National Statistics"
        domains: ["ons.gov.uk"]
  2:
    name: "Peer-reviewed academic"
    publishers:
      - name: "arXiv"
        domains: ["arxiv.org"]
      - name: "Nature"
        domains: ["nature.com"]
      - name: "Science"
        domains: ["science.org"]
      - name: "IEEE Xplore"
        domains: ["ieeexplore.ieee.org"]
      - name: "ACM Digital Library"
        domains: ["dl.acm.org"]
      - name: "The Lancet"
        domains: ["thelancet.com"]
      - name: "New England Journal of Medicine"
        domains: ["nejm.org"]
  3:
    name: "Tier-1 research firms and trackers"
    publishers:
      - name: "Gartner"
        domains: ["gartner.com"]
      - name: "McKinsey"
        domains: ["mckinsey.com"]
      - name: "Deloitte Insights"
        domains: ["deloitte.com"]
      - name: "IDC"
        domains: ["idc.com"]
      - name: "Forrester"
        domains: ["forrester.com"]
      - name: "Stanford HAI"
        domains: ["hai.stanford.edu"]
      - name: "OECD.AI"
        domains: ["oecd.ai"]
      - name: "Epoch AI"
        domains: ["epochai.org"]
      - name: "Our World in Data"
        domains: ["ourworldindata.org"]
      - name: "CB Insights"
        domains: ["cbinsights.com"]
      - name: "Statista"
        domains: ["statista.com"]
      - name: "SemiAnalysis"
        domains: ["semianalysis.com"]
      - name: "CEPS"
        domains: ["ceps.eu"]
  4:
    name: "Tier-1 press"
    publishers:
      - name: "Bloomberg"
        domains: ["bloomberg.com"]
      - name: "Reuters"
        domains: ["reuters.com"]
      - name: "Financial Times"
        domains: ["ft.com"]
      - name: "CNBC"
        domains: ["cnbc.com"]
      - name: "The New York Times"
        domains: ["nytimes.com"]
      - name: "The Wall Street Journal"
        domains: ["wsj.com"]
      - name: "The Economist"
        domains: ["economist.com"]
      - name: "The Information"
        domains: ["theinformation.com"]
      - name: "Les Échos"
        domains: ["lesechos.fr"]
      - name: "Le Monde"
        domains: ["lemonde.fr"]
  5:
    name: "Tier-2 press (flagged for review)"
    publishers:
      - name: "TechCrunch"
        domains: ["techcrunch.com"]
      - name: "The Verge"
        domains: ["theverge.com"]
      - name: "Ars Technica"
        domains: ["arstechnica.com"]
      - name: "Wired"
        domains: ["wired.com"]
      - name: "VentureBeat"
        domains: ["venturebeat.com"]
      - name: "MIT Technology Review"
        domains: ["technologyreview.com"]
  6:
    name: "Startup databases and aggregators (flagged for review)"
    publishers:
      - name: "Crunchbase"
        domains: ["crunchbase.com"]
      - name: "Sacra"
        domains: ["sacra.com"]
      - name: "PitchBook"
        domains: ["pitchbook.com"]
      - name: "Dealroom"
        domains: ["dealroom.co"]
      - name: "Wikipedia"
        domains: ["en.wikipedia.org", "fr.wikipedia.org"]
```

- [ ] **Step 2: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/authority-map.yaml
git commit -m "feat(cite): add machine-readable authority-map.yaml"
```

---

## Task 3: Create `scripts/cite/` package scaffolding and pytest conftest

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/__init__.py` (empty)
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/__init__.py` (empty)
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/conftest.py`
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/fixtures/sample_authority_map.yaml`

- [ ] **Step 1: Create directories and empty __init__ files**

```bash
cd /home/ezalos/42/Markdowns2Teach
mkdir -p scripts/cite/tests/fixtures
touch scripts/cite/__init__.py
touch scripts/cite/tests/__init__.py
```

- [ ] **Step 2: Write conftest.py with shared fixtures**

Write to `scripts/cite/tests/conftest.py`:

```python
# ABOUTME: Shared pytest fixtures for scripts/cite/ tests.
# ABOUTME: Provides sample authority-map YAML, sample claim YAML, and sample page.txt.

from pathlib import Path
import pytest
import yaml

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_authority_map_path():
    return FIXTURES / "sample_authority_map.yaml"


@pytest.fixture
def sample_authority_map(sample_authority_map_path):
    with open(sample_authority_map_path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def sample_page_text():
    return (
        "Section A: Introduction\n\n"
        "The Flash Crash of May 6, 2010 erased approximately $1 trillion "
        "in market value within 36 minutes before rebounding.\n\n"
        "Section B: Details\n\n"
        "The Dow Jones Industrial Average plunged 998.5 points (about 9%) "
        "most within minutes.\n"
    )


@pytest.fixture
def valid_claim():
    return {
        "id": "claim-01",
        "location": {
            "file": "slides/session-01/A.md",
            "slide": "01 — Event",
            "line": 42,
        },
        "claim": {
            "text": "Le Flash Crash a effacé $1T en 36 minutes.",
            "type": "historical-event",
            "has_existing_source": False,
        },
        "proposed_source": {
            "url": "https://www.sec.gov/news/studies/2010/marketevents-report.pdf",
            "url_domain": "sec.gov",
            "publisher_org": "SEC/CFTC",
            "author": "Staff of the CFTC and SEC",
            "publication_date": "2010-09-30",
            "accessed_date": "2026-04-13",
            "quote": "The Flash Crash of May 6, 2010 erased approximately $1 trillion in market value within 36 minutes before rebounding.",
            "surrounding_paragraph": "The Flash Crash of May 6, 2010 erased approximately $1 trillion in market value within 36 minutes before rebounding.",
            "section_heading": "Section A: Introduction",
            "alignment_justification": "Quote directly confirms $1T and 36-minute duration.",
            "confidence": "high",
        },
        "status": "pending",
        "flag_reason": None,
        "proposed_action": None,
        "proposed_claim_update": None,
        "validation": None,
        "page_text_file": "claim-01.page.txt",
    }
```

- [ ] **Step 3: Write sample_authority_map.yaml**

Write to `scripts/cite/tests/fixtures/sample_authority_map.yaml`:

```yaml
tiers:
  1:
    name: "Primary"
    publishers:
      - name: "SEC"
        domains: ["sec.gov"]
      - name: "Anthropic"
        domains: ["anthropic.com", "investor.anthropic.com"]
  4:
    name: "Tier-1 press"
    publishers:
      - name: "Bloomberg"
        domains: ["bloomberg.com"]
  5:
    name: "Tier-2 press"
    publishers:
      - name: "TechCrunch"
        domains: ["techcrunch.com"]
```

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add scripts/cite/__init__.py scripts/cite/tests/__init__.py scripts/cite/tests/conftest.py scripts/cite/tests/fixtures/sample_authority_map.yaml
git commit -m "test(cite): scaffold scripts/cite/ package and pytest fixtures"
```

---

## Task 4: Write `test_tier_lookup.py` (TDD red)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/test_tier_lookup.py`

- [ ] **Step 1: Write the failing tests**

Write to `scripts/cite/tests/test_tier_lookup.py`:

```python
# ABOUTME: Tests for scripts.cite.tier_lookup - url_domain to tier integer lookup.

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "tier_lookup.py"


def run_tier_lookup(domain, authority_map_path):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), domain, "--map", str(authority_map_path)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr


def test_known_tier1_domain_returns_1(sample_authority_map_path):
    rc, stdout, _ = run_tier_lookup("sec.gov", sample_authority_map_path)
    assert rc == 0
    assert stdout == "1"


def test_known_tier4_domain_returns_4(sample_authority_map_path):
    rc, stdout, _ = run_tier_lookup("bloomberg.com", sample_authority_map_path)
    assert rc == 0
    assert stdout == "4"


def test_known_tier5_domain_returns_5(sample_authority_map_path):
    rc, stdout, _ = run_tier_lookup("techcrunch.com", sample_authority_map_path)
    assert rc == 0
    assert stdout == "5"


def test_unknown_domain_returns_null(sample_authority_map_path):
    rc, stdout, _ = run_tier_lookup("encyclopedia.pub", sample_authority_map_path)
    assert rc == 0
    assert stdout == "null"


def test_subdomain_matches_publisher_root(sample_authority_map_path):
    # investor.anthropic.com is explicitly listed → tier 1
    rc, stdout, _ = run_tier_lookup("investor.anthropic.com", sample_authority_map_path)
    assert rc == 0
    assert stdout == "1"


def test_unlisted_subdomain_of_known_root_returns_tier(sample_authority_map_path):
    # news.anthropic.com is NOT explicitly listed, but anthropic.com is.
    # Subdomain lookup should walk up the domain chain.
    rc, stdout, _ = run_tier_lookup("news.anthropic.com", sample_authority_map_path)
    assert rc == 0
    assert stdout == "1"


def test_case_insensitive_domain(sample_authority_map_path):
    rc, stdout, _ = run_tier_lookup("SEC.GOV", sample_authority_map_path)
    assert rc == 0
    assert stdout == "1"
```

- [ ] **Step 2: Run tests to verify they fail**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_tier_lookup.py -v
```
Expected: ALL FAIL with "No such file or directory" on tier_lookup.py.

---

## Task 5: Implement `scripts/cite/tier_lookup.py` (TDD green)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tier_lookup.py`

- [ ] **Step 1: Write the implementation**

Write to `scripts/cite/tier_lookup.py`:

```python
#!/usr/bin/env python3
# ABOUTME: Look up authority tier for a URL domain against docs/references/authority-map.yaml.
# ABOUTME: Outputs tier integer (1-6) or "null" on stdout. No LLM judgment — pure lookup.

import argparse
import sys
from pathlib import Path

import yaml

DEFAULT_MAP = Path(__file__).resolve().parents[2] / "docs/references/authority-map.yaml"


def load_map(path):
    with open(path) as f:
        return yaml.safe_load(f)


def _domain_chain(domain):
    """Yield the domain and each parent (news.foo.com → news.foo.com, foo.com)."""
    parts = domain.split(".")
    for i in range(len(parts) - 1):
        yield ".".join(parts[i:])


def lookup(domain, authority_map):
    domain = domain.strip().lower()
    if not domain:
        return None
    domain_to_tier = {}
    for tier_num, tier_data in authority_map.get("tiers", {}).items():
        for publisher in tier_data.get("publishers", []):
            for d in publisher.get("domains", []):
                domain_to_tier[d.lower()] = int(tier_num)
    # Exact match first, then walk up subdomains
    for candidate in _domain_chain(domain):
        if candidate in domain_to_tier:
            return domain_to_tier[candidate]
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="URL domain to look up (e.g., sec.gov)")
    parser.add_argument("--map", default=str(DEFAULT_MAP), help="Path to authority-map.yaml")
    args = parser.parse_args()

    authority_map = load_map(args.map)
    tier = lookup(args.domain, authority_map)
    print("null" if tier is None else str(tier))
    sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run tests to verify they pass**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_tier_lookup.py -v
```
Expected: ALL 7 tests PASS.

- [ ] **Step 3: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add scripts/cite/tier_lookup.py scripts/cite/tests/test_tier_lookup.py
git commit -m "feat(cite): add tier_lookup.py with subdomain-walking domain matcher"
```

---

## Task 6: Write `test_lint_authority_map.py` (TDD red)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/test_lint_authority_map.py`
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/fixtures/sample_authority_map.md` (paired with the yaml from Task 3)

- [ ] **Step 1: Write sample_authority_map.md matching the yaml fixture**

Write to `scripts/cite/tests/fixtures/sample_authority_map.md`:

```markdown
# Sample authority map (test fixture)

## Tier 1 — Primary

- **SEC** (`sec.gov`)
- **Anthropic** (`anthropic.com`, `investor.anthropic.com`)

## Tier 4 — Tier-1 press

- **Bloomberg** (`bloomberg.com`)

## Tier 5 — Tier-2 press

- **TechCrunch** (`techcrunch.com`)
```

- [ ] **Step 2: Write the failing tests**

Write to `scripts/cite/tests/test_lint_authority_map.py`:

```python
# ABOUTME: Tests for scripts.cite.lint_authority_map - bidirectional sync check between .md and .yaml.

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "lint_authority_map.py"
FIXTURES = Path(__file__).parent / "fixtures"


def run_lint(md_path, yaml_path):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--md", str(md_path), "--yaml", str(yaml_path)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def test_in_sync_files_pass():
    rc, _, _ = run_lint(FIXTURES / "sample_authority_map.md", FIXTURES / "sample_authority_map.yaml")
    assert rc == 0


def test_yaml_extra_domain_fails(tmp_path):
    extra_yaml = tmp_path / "extra.yaml"
    extra_yaml.write_text((FIXTURES / "sample_authority_map.yaml").read_text()
                          + "      - name: \"GhostPublisher\"\n        domains: [\"ghost.example\"]\n")
    rc, _, stderr = run_lint(FIXTURES / "sample_authority_map.md", extra_yaml)
    assert rc == 1
    assert "ghost.example" in stderr


def test_md_missing_yaml_entry_fails(tmp_path):
    trimmed_md = tmp_path / "trimmed.md"
    trimmed_md.write_text("# Only\n\n## Tier 1 — Primary\n\n- **SEC** (`sec.gov`)\n")
    rc, _, stderr = run_lint(trimmed_md, FIXTURES / "sample_authority_map.yaml")
    assert rc == 1
    # Bloomberg (tier 4) is in yaml but not in trimmed md
    assert "bloomberg.com" in stderr.lower() or "Bloomberg" in stderr
```

- [ ] **Step 3: Run tests to verify they fail**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_lint_authority_map.py -v
```
Expected: ALL FAIL (script doesn't exist).

---

## Task 7: Implement `scripts/cite/lint_authority_map.py` (TDD green)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/lint_authority_map.py`

- [ ] **Step 1: Write the implementation**

Write to `scripts/cite/lint_authority_map.py`:

```python
#!/usr/bin/env python3
# ABOUTME: Lint that authority-map.md and authority-map.yaml describe the same tiered publisher roster.
# ABOUTME: Exit 0 = in sync. Exit 1 = drift, stderr = list of mismatches.

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MD = REPO_ROOT / "docs/references/authority-map.md"
DEFAULT_YAML = REPO_ROOT / "docs/references/authority-map.yaml"


def parse_md_domains(md_text):
    """Return set of (tier, domain) pairs extracted from bullets in authority-map.md."""
    pairs = set()
    current_tier = None
    tier_heading = re.compile(r"^##\s+Tier\s+(\d)\s+—")
    # bullet with domain in backticks: - **Name** (`domain.com`) — ...
    bullet_domains = re.compile(r"`([^`]+)`")
    for line in md_text.splitlines():
        m = tier_heading.match(line)
        if m:
            current_tier = int(m.group(1))
            continue
        if current_tier is None or not line.lstrip().startswith("-"):
            continue
        for d in bullet_domains.findall(line):
            # Filter glob-like entries: "investor.*" or "ir.*" — skip.
            if "*" in d:
                continue
            pairs.add((current_tier, d.lower()))
    return pairs


def yaml_domains(yaml_data):
    pairs = set()
    for tier_num, tier_data in yaml_data.get("tiers", {}).items():
        for publisher in tier_data.get("publishers", []):
            for d in publisher.get("domains", []):
                pairs.add((int(tier_num), d.lower()))
    return pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--md", default=str(DEFAULT_MD))
    parser.add_argument("--yaml", default=str(DEFAULT_YAML))
    args = parser.parse_args()

    md_pairs = parse_md_domains(Path(args.md).read_text())
    yml_pairs = yaml_domains(yaml.safe_load(Path(args.yaml).read_text()))

    errors = []
    only_in_yaml = yml_pairs - md_pairs
    only_in_md = md_pairs - yml_pairs
    for tier, domain in sorted(only_in_yaml):
        errors.append(f"tier {tier}: '{domain}' in yaml but not in md")
    for tier, domain in sorted(only_in_md):
        errors.append(f"tier {tier}: '{domain}' in md but not in yaml")

    if errors:
        print("authority-map.md and authority-map.yaml disagree:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print("authority-map.md and authority-map.yaml are in sync.")
    sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run tests**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_lint_authority_map.py -v
```
Expected: ALL PASS.

- [ ] **Step 3: Verify against real files**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 scripts/cite/lint_authority_map.py
```

Expected: one of two outcomes:
- "in sync." → commit in next step
- List of drifts → update `authority-map.md` or `authority-map.yaml` to match. The most likely drift is that some publishers exist in the .md via paragraphs (not backtick-domain bullets) like "Company investor relations — any URL matching `investor.*`" (glob pattern, filtered out), which is fine. If the linter reports glob-patterns as drift, double-check the filter logic in `parse_md_domains`.

Also check for real drift: if the baseline `.md` lists publishers that didn't make it into the `.yaml` (Task 2), add them to the `.yaml` now (or remove them from the `.md` if they were aspirational).

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add scripts/cite/lint_authority_map.py scripts/cite/tests/test_lint_authority_map.py scripts/cite/tests/fixtures/sample_authority_map.md
# also add any .yaml or .md fixes from Step 3
git add docs/references/authority-map.yaml docs/references/authority-map.md
git commit -m "feat(cite): add lint_authority_map.py and sync .md/.yaml roster"
```

---

## Task 8: Write `test_validate_claim.py` (TDD red)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/test_validate_claim.py`

- [ ] **Step 1: Write the failing tests**

Write to `scripts/cite/tests/test_validate_claim.py`:

```python
# ABOUTME: Tests for scripts.cite.validate_claim - schema + enum + quote-in-page substring validation.

import subprocess
import sys
from pathlib import Path

import yaml

SCRIPT = Path(__file__).parent.parent / "validate_claim.py"


def run_validate(tmp_path, claim_data, page_text):
    yaml_path = tmp_path / "claim-01.yaml"
    page_path = tmp_path / "claim-01.page.txt"
    yaml_path.write_text(yaml.safe_dump(claim_data, sort_keys=False))
    page_path.write_text(page_text)
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(yaml_path), str(page_path)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def test_valid_claim_passes(tmp_path, valid_claim, sample_page_text):
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 0, stderr


def test_missing_required_field_fails(tmp_path, valid_claim, sample_page_text):
    del valid_claim["proposed_source"]["url"]
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "url" in stderr


def test_invalid_status_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["status"] = "sourced"  # not in enum
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "status" in stderr


def test_invalid_confidence_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["proposed_source"]["confidence"] = "certain"  # not in enum
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "confidence" in stderr


def test_quote_not_in_page_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["proposed_source"]["quote"] = "This sentence does not appear in the page text."
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "quote" in stderr.lower()


def test_surrounding_paragraph_not_in_page_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["proposed_source"]["surrounding_paragraph"] = (
        "Fabricated paragraph that cannot be found in the page."
    )
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "surrounding_paragraph" in stderr.lower()


def test_malformed_publication_date_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["proposed_source"]["publication_date"] = "September 2010"  # not YYYY-MM-DD
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "publication_date" in stderr


def test_url_domain_mismatch_fails(tmp_path, valid_claim, sample_page_text):
    valid_claim["proposed_source"]["url_domain"] = "wrong-domain.com"
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 1
    assert "url_domain" in stderr


def test_whitespace_normalization_passes(tmp_path, valid_claim, sample_page_text):
    # Add extra runs of whitespace to the quote; validator should still find it.
    valid_claim["proposed_source"]["quote"] = (
        "The  Flash Crash of  May 6, 2010   erased approximately $1 trillion "
        "in market value within 36 minutes before rebounding."
    )
    rc, _, stderr = run_validate(tmp_path, valid_claim, sample_page_text)
    assert rc == 0, stderr
```

- [ ] **Step 2: Run tests to verify they fail**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_validate_claim.py -v
```
Expected: ALL 9 tests FAIL (script doesn't exist).

---

## Task 9: Implement `scripts/cite/validate_claim.py` (TDD green)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/validate_claim.py`

- [ ] **Step 1: Write the implementation**

Write to `scripts/cite/validate_claim.py`:

```python
#!/usr/bin/env python3
# ABOUTME: Validate a claim YAML against schema, enums, and quote-in-page substring rules.
# ABOUTME: Exit 0 = valid. Exit 1 = invalid, stderr = human-readable failure list.

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import yaml

STATUS_ENUM = {
    "pending", "auto-approved", "approved", "rejected", "needs-rework",
    "flagged-low-reputation", "flagged-unsourceable", "flagged-stale-stat",
    "flagged-validation-failed",
}
PROPOSED_ACTION_ENUM = {None, "add-citation", "update-claim-value", "soften-language", "none"}
CONFIDENCE_ENUM = {"high", "medium", "low"}
RECENCY_ENUM = {"fresh", "recent", "stale", "historical-event", "unknown", None}

REQUIRED_LOCATION = {"file", "slide", "line"}
REQUIRED_CLAIM = {"text", "type", "has_existing_source"}
REQUIRED_SOURCE = {
    "url", "url_domain", "publisher_org", "publication_date", "accessed_date",
    "quote", "surrounding_paragraph", "section_heading",
    "alignment_justification", "confidence",
}


def _normalize_whitespace(s):
    return re.sub(r"\s+", " ", s).strip()


def _registered_domain(url):
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def validate(claim, page_text):
    errors = []

    # Top-level required fields
    for field in ("id", "location", "claim", "proposed_source", "status"):
        if field not in claim:
            errors.append(f"missing top-level field: {field}")

    loc = claim.get("location") or {}
    for field in REQUIRED_LOCATION:
        if field not in loc:
            errors.append(f"missing location.{field}")

    clm = claim.get("claim") or {}
    for field in REQUIRED_CLAIM:
        if field not in clm:
            errors.append(f"missing claim.{field}")

    src = claim.get("proposed_source") or {}
    for field in REQUIRED_SOURCE:
        if field not in src:
            errors.append(f"missing proposed_source.{field}")

    # Enum checks
    if claim.get("status") not in STATUS_ENUM:
        errors.append(f"status '{claim.get('status')}' not in enum {sorted(STATUS_ENUM)}")
    if claim.get("proposed_action") not in PROPOSED_ACTION_ENUM:
        errors.append(
            f"proposed_action '{claim.get('proposed_action')}' not in enum"
        )
    if src.get("confidence") not in CONFIDENCE_ENUM:
        errors.append(
            f"proposed_source.confidence '{src.get('confidence')}' not in enum"
        )
    if "recency_verdict" in src and src["recency_verdict"] not in RECENCY_ENUM:
        errors.append(
            f"proposed_source.recency_verdict '{src.get('recency_verdict')}' not in enum"
        )

    # publication_date format
    pub_date = src.get("publication_date")
    if pub_date is not None:
        try:
            datetime.strptime(str(pub_date), "%Y-%m-%d")
        except ValueError:
            errors.append(f"publication_date '{pub_date}' is not YYYY-MM-DD")

    # url_domain matches the parsed domain of url
    url = src.get("url")
    url_domain = src.get("url_domain")
    if url and url_domain:
        parsed = _registered_domain(url)
        if url_domain.lower() != parsed:
            errors.append(
                f"url_domain '{url_domain}' does not match parsed domain '{parsed}' of url"
            )

    # Quote and surrounding_paragraph must appear verbatim (whitespace-normalized) in page_text
    normalized_page = _normalize_whitespace(page_text)
    for field in ("quote", "surrounding_paragraph"):
        value = src.get(field)
        if value is None:
            continue
        normalized_value = _normalize_whitespace(value)
        if normalized_value and normalized_value not in normalized_page:
            errors.append(
                f"proposed_source.{field} does not appear verbatim in page.txt"
            )

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("claim_yaml", help="Path to claim-NN.yaml")
    parser.add_argument("page_txt", help="Path to claim-NN.page.txt")
    args = parser.parse_args()

    try:
        claim = yaml.safe_load(Path(args.claim_yaml).read_text())
    except yaml.YAMLError as e:
        print(f"YAML parse error: {e}", file=sys.stderr)
        sys.exit(1)
    page_text = Path(args.page_txt).read_text()

    errors = validate(claim, page_text)
    if errors:
        print(f"validation failed for {args.claim_yaml}:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run tests**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_validate_claim.py -v
```
Expected: ALL 9 PASS.

- [ ] **Step 3: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add scripts/cite/validate_claim.py scripts/cite/tests/test_validate_claim.py
git commit -m "feat(cite): add validate_claim.py with quote-in-page substring check"
```

---

## Task 10: Write `test_target_scope.py` (TDD red)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/tests/test_target_scope.py`

- [ ] **Step 1: Write the failing tests**

Write to `scripts/cite/tests/test_target_scope.py`:

```python
# ABOUTME: Tests for scripts.cite.target_scope - map target .md path to verification shell command.

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "target_scope.py"


def run_target_scope(target):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), target],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr


def test_slides_target_returns_make_check():
    rc, stdout, _ = run_target_scope("slides/session-05/A-regulation-ethique.md")
    assert rc == 0
    assert "make check" in stdout
    assert "make check-citations" in stdout
    assert "make html" in stdout


def test_docs_references_target_returns_fixture_command():
    rc, stdout, _ = run_target_scope("docs/references/test-fixtures/cite-fixture.md")
    assert rc == 0
    assert "check-citations.sh docs/references/test-fixtures" in stdout
    assert "marp" in stdout


def test_docs_research_target_returns_fixture_command():
    rc, stdout, _ = run_target_scope("docs/research/ai-market-intelligence/report.md")
    assert rc == 0
    assert "check-citations.sh docs/research/ai-market-intelligence" in stdout


def test_absolute_path_slides_target():
    rc, stdout, _ = run_target_scope("/home/ezalos/42/Markdowns2Teach/slides/session-01/A-genai-fondamentaux.md")
    assert rc == 0
    assert "make check" in stdout
```

- [ ] **Step 2: Run tests to verify they fail**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_target_scope.py -v
```
Expected: ALL 4 FAIL (script doesn't exist).

---

## Task 11: Implement `scripts/cite/target_scope.py` (TDD green)

**Files:**
- Create: `/home/ezalos/42/Markdowns2Teach/scripts/cite/target_scope.py`

- [ ] **Step 1: Write the implementation**

Write to `scripts/cite/target_scope.py`:

```python
#!/usr/bin/env python3
# ABOUTME: Given a target .md path, print the verification shell command /cite-apply should run.
# ABOUTME: Targets under slides/ use the full make chain; elsewhere uses targeted check-citations + marp syntax check.

import argparse
import sys
from pathlib import Path


def command_for(target_path):
    p = Path(target_path)
    # Normalize to a repo-relative path if absolute
    parts = p.parts
    if "slides" in parts:
        idx = parts.index("slides")
        rel = Path(*parts[idx:])
        if rel.parts[0] == "slides":
            return "make check && make check-citations && make html"
    # Fallback: targeted check-citations on the containing dir + marp syntax render
    containing_dir = str(p.parent) if p.is_absolute() or "/" in str(p) else str(p.parent)
    # When the path is absolute and inside the repo, reduce to repo-relative containing dir
    for root_marker in ("docs/references", "docs/research", "docs/notes"):
        if root_marker in str(p):
            rel_dir = str(p).split(root_marker, 1)[1].lstrip("/")
            rel_containing = f"{root_marker}/{rel_dir.rsplit('/', 1)[0]}" if "/" in rel_dir else root_marker
            containing_dir = rel_containing
            break
    return f"bash scripts/check-citations.sh {containing_dir} && marp --no-stdin {target_path}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Path to the target .md file")
    args = parser.parse_args()
    print(command_for(args.target))
    sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run tests**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/test_target_scope.py -v
```
Expected: ALL 4 PASS.

- [ ] **Step 3: Smoke test**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
python3 scripts/cite/target_scope.py slides/session-05/A-regulation-ethique.md
python3 scripts/cite/target_scope.py docs/references/test-fixtures/cite-fixture.md
```
Expected: first prints `make check && make check-citations && make html`; second prints `bash scripts/check-citations.sh docs/references/test-fixtures && marp --no-stdin docs/references/test-fixtures/cite-fixture.md`.

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add scripts/cite/target_scope.py scripts/cite/tests/test_target_scope.py
git commit -m "feat(cite): add target_scope.py for verification command routing"
```

---

## Task 12: Wire `lint_authority_map.py` into `make check`

**Files:**
- Modify: `/home/ezalos/42/Markdowns2Teach/Makefile`

- [ ] **Step 1: Read current Makefile to find the `check` target**

```bash
grep -n "^check:" /home/ezalos/42/Markdowns2Teach/Makefile
```

- [ ] **Step 2: Add a dedicated `lint-authority-map` target and prepend it to `check`**

Using the Edit tool, find the line starting with `check:` and add a new target above it. Also add the new prerequisite to `check`. For example, if the current check line is:

```makefile
check:
	@node scripts/check-overflow-visual.js slides/
```

Replace with:

```makefile
lint-authority-map:
	@python3 scripts/cite/lint_authority_map.py

check: lint-authority-map
	@node scripts/check-overflow-visual.js slides/
```

Adapt if the exact Makefile content differs. The key changes:
- New target `lint-authority-map` that runs the script
- `check` depends on `lint-authority-map` so it runs first

- [ ] **Step 3: Verify**

Run:
```bash
cd /home/ezalos/42/Markdowns2Teach
make lint-authority-map
```
Expected: `authority-map.md and authority-map.yaml are in sync.` with exit 0.

Then:
```bash
make -n check  # dry-run, shows the command chain
```
Expected: `lint-authority-map` appears first.

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add Makefile
git commit -m "chore(make): add lint-authority-map gate to make check"
```

---

## Task 13: Update `cite-scan` SKILL.md to write validation/page_text_file stubs

**Files:**
- Modify: `/home/ezalos/.claude/skills/cite-scan/SKILL.md`

- [ ] **Step 1: Read the current Step 3 YAML template**

Open `/home/ezalos/.claude/skills/cite-scan/SKILL.md`. Locate the YAML template inside "### Step 3: Extract claims from target file" (around the `id: claim-NN` block).

- [ ] **Step 2: Extend the template**

Using Edit, replace this block:

```yaml
id: claim-NN               # zero-padded counter starting at 01
location:
  file: <path>
  slide: "<slide number and title, if the claim is inside a numbered slide>"
  line: <line number of the claim in the file>
claim:
  text: "<verbatim claim text>"
  type: <number|named-stat|company-fact|benchmark|pricing|forecast|historical-event>
  has_existing_source: <true if the claim has a [N] marker on the same line or existing slide-level Sources line, else false>
proposed_source: {}        # empty — filled by /cite-research
status: pending
flag_reason: null
proposed_action: null
proposed_claim_update: null
```

With:

```yaml
id: claim-NN               # zero-padded counter starting at 01
location:
  file: <path>
  slide: "<slide number and title, if the claim is inside a numbered slide>"
  line: <line number of the claim in the file>
claim:
  text: "<verbatim claim text>"
  type: <number|named-stat|company-fact|benchmark|pricing|forecast|historical-event>
  has_existing_source: <true if the claim has a [N] marker on the same line or existing slide-level Sources line, else false>
proposed_source: {}        # empty — filled by /cite-research
status: pending
flag_reason: null
proposed_action: null
proposed_claim_update: null
validation: null           # filled by /cite-research after validate_claim.py passes
page_text_file: null       # filled by /cite-research as "claim-NN.page.txt"
```

- [ ] **Step 3: Verify**

Run:
```bash
grep -c "validation: null" /home/ezalos/.claude/skills/cite-scan/SKILL.md
grep -c "page_text_file: null" /home/ezalos/.claude/skills/cite-scan/SKILL.md
```
Expected: both return `1`.

- [ ] **Step 4: No commit** — skill files live outside the repo and are not version-controlled here.

---

## Task 14: Rewrite `cite-research` SKILL.md (biggest change)

**Files:**
- Modify: `/home/ezalos/.claude/skills/cite-research/SKILL.md`

This task replaces Step 2 (subagent prompt) and adds a new orchestrator validation loop. The rewrite is large; do it in sub-steps for clarity.

- [ ] **Step 1: Update the frontmatter `description`**

Replace:
```yaml
description: Phase 2 of the /cite pipeline — for each pending claim, spawn a subagent to find a source, Tavily-extract the page, and fill the claim schema with the exact supporting quote. Updates outline.md with categorized sections. No source-file edits.
```

With:
```yaml
description: Phase 2 of the /cite pipeline — subagents find sources and extract raw quotes + page text to claim-NN.page.txt. Orchestrator runs scripts/cite/validate_claim.py and scripts/cite/tier_lookup.py to finalize each claim deterministically. Retries once with error feedback on validation failure.
```

- [ ] **Step 2: Replace the Step 2 subagent prompt template**

Using Edit, replace the entire "### Step 2: Dispatch parallel research subagents" section (from its heading up to "### Step 3: Post-research authority refinement") with:

```markdown
### Step 2: Dispatch parallel research subagents

Use the `Agent` tool to spawn up to **5 concurrent** subagents. Each subagent is given **exactly one** claim. Use `subagent_type: general-purpose`.

The subagent returns **raw data only** — it does NOT assign `authority_tier`, `recency_verdict`, or `status`. Those are computed deterministically by the orchestrator in Step 3 using `scripts/cite/tier_lookup.py` and simple date math.

**Subagent prompt template** (substitute placeholders):

```
You are a source researcher for a specific factual claim. Your job is to find
ONE page that contains text supporting the claim, SAVE that page text verbatim
to disk, and extract metadata into a YAML file. You do NOT judge authority
tier, recency, or approval status — an orchestrator does that after you return.

## Claim to source
- Text: "{claim.text}"
- Type: {claim.type}
- Located in: {location.file}, slide "{location.slide}", line {location.line}

## Extraction with fallback chain

1. Try `mcp__tavily__tavily_search` (max 3 queries with different site: filters
   or date windows). Pick the single most promising URL.

2. Extract the page content using this fallback chain, stopping at the first
   layer that returns non-empty, non-truncated content:

   a. `mcp__tavily__tavily_extract` with `extract_depth: "advanced"` and
      `format: "markdown"`.
   b. `WebFetch` on the same URL.
   c. If URL ends in `.pdf`:
      `curl -sL <URL> -o /tmp/cite-{claim.id}.pdf && pdftotext /tmp/cite-{claim.id}.pdf -`
      via Bash.

3. SAVE the full extracted page content to:
   `docs/citation-audit/{slug}/claims/{claim.id}.page.txt`
   — verbatim, no editing, no combining with other sources.

4. Log every fallback invocation (what layer was needed) to:
   `docs/citation-audit/{slug}/caveats.md` under `## Tool-level`.

## Anti-fabrication contract (HARD RULE)

Every character of `quote` and `surrounding_paragraph` MUST appear verbatim in
the page.txt you just saved. If the saved page text does not contain the exact
sentence supporting the claim:

- Set `confidence: low`
- Use whatever actually-extracted sentence best matches, even if imperfect
- Note the gap in `alignment_justification`
- Do NOT splice content from a different source to fill gaps
- Do NOT paraphrase

A validator script (scripts/cite/validate_claim.py) will run after you return
and will REJECT your output if `quote` or `surrounding_paragraph` isn't
findable in page.txt. Your output will be discarded and you'll be re-dispatched
once with the specific error. After a second failure the claim is flagged.

## Fields to return (write to docs/citation-audit/{slug}/claims/{claim.id}.yaml)

Preserve all fields from the existing stub (id, location, claim). Fill:

```yaml
proposed_source:
  url: <final URL>
  url_domain: <bare domain of url, e.g. "sec.gov" — no www., no path>
  publisher_org: <organization that owns the URL, e.g., "U.S. Securities and Exchange Commission">
  author: <author or null>
  publication_date: <YYYY-MM-DD or null if not determinable>
  accessed_date: <today's date YYYY-MM-DD>
  quote: <single sentence from page.txt supporting the claim, verbatim>
  surrounding_paragraph: <full paragraph around the quote, verbatim>
  section_heading: <heading of the section the paragraph lives under, or null>
  alignment_justification: <one sentence explaining why the quote supports the claim>
  confidence: <high | medium | low>
page_text_file: "{claim.id}.page.txt"
```

Do NOT write `authority_tier`, `recency_verdict`, `status`, `flag_reason`,
`proposed_action`, or `proposed_claim_update`. The orchestrator fills those.
Leave `status: pending` unchanged.

## If error-feedback is provided

If this is a retry, you will be given `--error-feedback "<message>"`. Address
the specific errors listed. If the feedback says `quote does not appear
verbatim in page.txt`, re-open page.txt and find text that actually matches.
If the feedback says `url_domain does not match parsed domain of url`, fix the
url_domain field to be just the bare domain (no subdomain unless the
subdomain is what you want recorded).
```

Launch the subagents in parallel (single message, multiple Agent tool calls) in batches of 5. Wait for each batch before launching the next.

### Step 3: Orchestrator validation + deterministic finalization

For each claim whose subagent has returned, run this loop:

1. **Validate**: run `python3 scripts/cite/validate_claim.py docs/citation-audit/<slug>/claims/<claim-id>.yaml docs/citation-audit/<slug>/claims/<claim-id>.page.txt` via Bash. If exit 0, proceed to step 3. If exit 1, continue to step 2.

2. **Retry once with feedback**: re-dispatch the research subagent with the same prompt PLUS `--error-feedback "<stderr from validator>"` prepended. When the subagent returns, re-run the validator. If still exit 1:
   - Set `status: flagged-validation-failed`
   - Set `flag_reason: "validator rejected output twice: <stderr>"`
   - Set `validation.attempts: 2` and `validation.validated_at` to now
   - Log the failure to `caveats.md` under `## Research-level`
   - Continue to next claim (do not run steps 3–5)

3. **Tier lookup**: run `python3 scripts/cite/tier_lookup.py <url_domain>`. Capture stdout (integer `1-6` or `null`). Assign to `proposed_source.authority_tier` (integer or `null`).

4. **Recency verdict**: compute from `publication_date` and today's date:
   - No publication_date → `unknown`
   - Event before 2020-01-01 → `historical-event`
   - publication_date within 180 days of today → `fresh`
   - Within 180-365 days → `recent`
   - More than 365 days → `stale`
   Write to `proposed_source.recency_verdict`.

5. **Status**: compute deterministically:
   - `tier ∈ {1,2,3,4}` AND `recency ∈ {fresh, recent, historical-event}` → `auto-approved`
   - `tier ∈ {5,6}` OR `tier == null` → `flagged-low-reputation`
   - Otherwise → `flagged-low-reputation`
   Write to `status`. Set `flag_reason` accordingly (or `null` if auto-approved). Set `proposed_action: add-citation` if auto-approved, else leave `null`.

6. **Validation block**: set
   ```yaml
   validation:
     validated_at: <ISO-8601 now>
     quote_found_in_page: true
     surrounding_paragraph_found_in_page: true
     enum_valid: true
     attempts: 1  # or 2 if retry was needed
   ```
```

- [ ] **Step 3: Update Step 5 (status report) to mention deterministic finalization**

Find the section:
```markdown
### Step 5: Report to user
```

In the summary string, change the budget line from:
```
- <caveats> caveats logged
- <new-authorities> publishers added to per-run authority overlay
```

To:
```
- <caveats> caveats logged
- <validation-retries> claims needed one validation retry
- <validation-failures> claims flagged-validation-failed after second attempt
- <new-authorities> publishers added to per-run authority overlay
```

- [ ] **Step 4: Verify structure**

Run:
```bash
grep -c "^### Step" /home/ezalos/.claude/skills/cite-research/SKILL.md
grep -c "scripts/cite/validate_claim.py" /home/ezalos/.claude/skills/cite-research/SKILL.md
grep -c "scripts/cite/tier_lookup.py" /home/ezalos/.claude/skills/cite-research/SKILL.md
grep -c "Anti-fabrication contract" /home/ezalos/.claude/skills/cite-research/SKILL.md
```
Expected: Step count still 5, both script paths referenced at least once, anti-fabrication clause present.

- [ ] **Step 5: No commit** — skill files live outside the repo.

---

## Task 15: Update `cite-apply` SKILL.md to use `target_scope.py`

**Files:**
- Modify: `/home/ezalos/.claude/skills/cite-apply/SKILL.md`

- [ ] **Step 1: Read current Step 6**

Open `/home/ezalos/.claude/skills/cite-apply/SKILL.md` and locate Step 6.

- [ ] **Step 2: Replace the hardcoded verification block**

Find:
```markdown
- Apply the patched content to the target file (use Edit with the original → patched substrings, not a full file rewrite — keeps diff surgical)
- Run in order:
  ```bash
  make check
  make check-citations
  make html
  ```
- Capture each exit code. Report pass/fail per step.
- If any fail: report the failure, do NOT revert. Louis fixes manually (per spec §8).
```

Replace with:
```markdown
- Apply the patched content to the target file (use Edit with the original → patched substrings, not a full file rewrite — keeps diff surgical)
- Determine the verification command for the target path:
  ```bash
  VERIFY_CMD=$(python3 scripts/cite/target_scope.py <target-file>)
  eval "$VERIFY_CMD"
  ```
  This auto-routes: targets under `slides/` get the full `make check && make check-citations && make html` chain; targets elsewhere (e.g., `docs/references/`, `docs/research/`) get targeted `check-citations.sh <dir> && marp --no-stdin <target>` which runs in seconds.
- Capture exit codes. Report pass/fail.
- If any fail: report the failure, do NOT revert. Louis fixes manually (per spec §8).
```

- [ ] **Step 3: Verify**

Run:
```bash
grep -c "target_scope.py" /home/ezalos/.claude/skills/cite-apply/SKILL.md
grep "^### Step 6" /home/ezalos/.claude/skills/cite-apply/SKILL.md
```
Expected: `target_scope.py` appears at least once; Step 6 heading still present.

- [ ] **Step 4: No commit** — skill files live outside the repo.

---

## Task 16: Move v1 backlog items to Resolved with v2 reference

**Files:**
- Modify: `/home/ezalos/42/Markdowns2Teach/docs/references/cite-skill-backlog.md`

- [ ] **Step 1: Read current file**

```bash
cat /home/ezalos/42/Markdowns2Teach/docs/references/cite-skill-backlog.md
```

- [ ] **Step 2: Move the entire `## 2026-04-13 — docs-references-test-fixtures-cite-fixture (initial integration test)` block from `## Open` to under `## Resolved`, and add a resolution note**

Using Edit, find the block starting with `## 2026-04-13 — docs-references-test-fixtures-cite-fixture (initial integration test)` and ending with the last bullet of that block (the pdftotext fallback item). Cut it from `## Open`.

Paste it under `## Resolved` with this header preface:

```markdown
## Resolved

### v2 (2026-04-13) — see `docs/superpowers/specs/2026-04-13-cite-skill-v2-design.md`

All 5 items below addressed by the v2 implementation. Quote-in-page substring check + page.txt preservation fix fabrication; tier lookup moved to `scripts/cite/tier_lookup.py` (not subagent judgment); enum validation via `scripts/cite/validate_claim.py`; verification command routing via `scripts/cite/target_scope.py`; PDF fallback chain (tavily advanced → WebFetch → pdftotext) documented in the cite-research subagent prompt.

<paste the 5-item block that was under ## Open here>
```

The `## Open` section should be left with just:
```markdown
## Open

_(No open items. `/cite-apply` appends here when new caveats are surfaced.)_
```

- [ ] **Step 3: Verify**

Run:
```bash
grep -c "^### v2" /home/ezalos/42/Markdowns2Teach/docs/references/cite-skill-backlog.md
grep -A2 "^## Open" /home/ezalos/42/Markdowns2Teach/docs/references/cite-skill-backlog.md
```
Expected: one `### v2` section exists; `## Open` has "No open items" line.

- [ ] **Step 4: Commit**

```bash
cd /home/ezalos/42/Markdowns2Teach
git add docs/references/cite-skill-backlog.md
git commit -m "docs(cite): mark v1 backlog items as resolved in v2"
```

---

## Task 17: Integration test: re-run cite-fixture end-to-end on v2

**Files:** no new files; exercises the full pipeline against the existing fixture.

- [ ] **Step 1: Reset previous bundle and fixture**

```bash
cd /home/ezalos/42/Markdowns2Teach
rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/
git checkout docs/references/test-fixtures/cite-fixture.md
```

- [ ] **Step 2: Run cite-scan**

Invoke:
```
/cite-scan docs/references/test-fixtures/cite-fixture.md
```

Verify:
```bash
ls docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/
grep -l "validation: null" docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.yaml | wc -l
grep -l "page_text_file: null" docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.yaml | wc -l
```
Expected: 5 yaml files, each with both `validation: null` and `page_text_file: null` stubs.

- [ ] **Step 3: Run cite-research**

Invoke:
```
/cite-research docs-references-test-fixtures-cite-fixture
```

Verify each claim has a sibling page.txt:
```bash
ls docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/*.page.txt | wc -l
```
Expected: 5.

Verify claim-01 (Flash Crash) NOW lands at `flagged-low-reputation` if the subagent picks encyclopedia.pub, OR `auto-approved` if the subagent picks the SEC primary URL. Either is valid v2 behavior — what must NOT happen is `authority_tier: 1` with `url_domain: encyclopedia.pub`.

```bash
cat docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/claim-01.yaml
```
Check:
- If `url_domain: encyclopedia.pub` → `authority_tier: null` and `status: flagged-low-reputation`
- If `url_domain: sec.gov` → `authority_tier: 1` and `status: auto-approved`

Run a spot validator against each claim manually to confirm the enforcement worked:
```bash
for f in docs/citation-audit/docs-references-test-fixtures-cite-fixture/claims/claim-*.yaml; do
  base="${f%.yaml}"
  python3 scripts/cite/validate_claim.py "$f" "${base}.page.txt" && echo "OK: $f" || echo "FAIL: $f"
done
```
Expected: all 5 report OK.

- [ ] **Step 4: Manually edit one flagged claim (if any) to `approved`**

If claim-01 (or any other) landed as `flagged-low-reputation`, edit its YAML to `status: approved` so cite-apply has something to apply there. Pick your preferred source URL — if you leave it as-is and mark approved, the flagged-tier URL will still be cited.

- [ ] **Step 5: Run cite-apply**

Invoke:
```
/cite-apply docs-references-test-fixtures-cite-fixture
```

Verify:
- Diff preview looks correct (claim-01 through claim-05 get `[N]` markers + Sources footers per slide)
- Verification command chosen by `target_scope.py` runs in seconds, not 2+ minutes
- Both `bash scripts/check-citations.sh docs/references/test-fixtures` and `marp --no-stdin docs/references/test-fixtures/cite-fixture.md` succeed

- [ ] **Step 6: Regression: run `make check` on the real slides/ project**

```bash
cd /home/ezalos/42/Markdowns2Teach
make lint-authority-map    # should pass fast
make check-citations       # should pass
```
Expected: both succeed. (`make check` with full Puppeteer render is optional and slow; it's already known-working pre-v2.)

- [ ] **Step 7: Clean up**

```bash
rm -rf docs/citation-audit/docs-references-test-fixtures-cite-fixture/
git checkout docs/references/test-fixtures/cite-fixture.md
```

- [ ] **Step 8: No commit** — integration test is a verification step, artifacts were all gitignored.

---

## Task 18: Final review

**Files:** none (review-only)

- [ ] **Step 1: Run the full test suite**

```bash
cd /home/ezalos/42/Markdowns2Teach
python3 -m pytest scripts/cite/tests/ -v
```
Expected: all tests PASS (total ~23 tests across the 4 scripts).

- [ ] **Step 2: Confirm git history**

```bash
git log --oneline -15
```
Expected commits in order (newest first):
- `docs(cite): mark v1 backlog items as resolved in v2`
- `chore(make): add lint-authority-map gate to make check`
- `feat(cite): add target_scope.py for verification command routing`
- `feat(cite): add validate_claim.py with quote-in-page substring check`
- `feat(cite): add lint_authority_map.py and sync .md/.yaml roster`
- `feat(cite): add tier_lookup.py with subdomain-walking domain matcher`
- `test(cite): scaffold scripts/cite/ package and pytest fixtures`
- `feat(cite): add machine-readable authority-map.yaml`
- (and earlier: the v2 spec commit `docs: add /cite v2 design spec ...`)

- [ ] **Step 3: Confirm all 4 skills still discoverable**

In a fresh Claude Code session (or reload), confirm that the Skill tool lists: `cite`, `cite-scan`, `cite-research`, `cite-apply`. All frontmatter should parse cleanly.

- [ ] **Step 4: Confirm the 4 skill YAML descriptions are updated**

```bash
head -5 /home/ezalos/.claude/skills/cite-research/SKILL.md | grep description
```
Expected: description mentions "validate_claim.py" and "tier_lookup.py" and "retries once".

---

## Self-Review Checklist (run mentally before declaring complete)

**Spec coverage:**
- §1 architecture shift → Task 14 (cite-research orchestrator loop)
- §2 new artifacts → Tasks 2, 3, 5, 7, 9, 11
- §3 validator contracts → Tasks 5 (tier_lookup), 7 (lint), 9 (validate_claim), 11 (target_scope)
- §4 authority-map.yaml format → Task 2
- §5 behavior per skill → Tasks 13 (cite-scan), 14 (cite-research), 15 (cite-apply)
- §6 schema additions → Tasks 13 (stubs), 14 (orchestrator fills validation{} block)
- §7 traceability → Task 16 (resolved backlog section)
- §8 critical files → all covered
- §9 testing → Tasks 4, 6, 8, 10 (unit tests), 17 (integration), 18 (final)

**Placeholder scan:** no TBD / TODO / "similar to Task N" / "handle edge cases" in this plan.

**Type consistency:**
- Script names match across tasks: `tier_lookup.py`, `validate_claim.py`, `lint_authority_map.py`, `target_scope.py`
- YAML field names consistent: `url_domain`, `publication_date`, `page_text_file`, `validation.attempts`
- Status enum values match across validator (Task 9) and cite-research orchestrator (Task 14)
- Recency verdict enum matches across validator and orchestrator
- Path conventions: `scripts/cite/` (not `scripts/cite/bin/` or similar)

**Scope:** one plan for one spec — appropriate size, ~18 tasks, each self-contained.
