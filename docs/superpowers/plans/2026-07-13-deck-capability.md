<!-- ABOUTME: Implementation plan for the deck capability design
     (docs/superpowers/specs/2026-07-13-deck-capability-design.md). -->

# Deck Capability Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the cross-project deck capability: portable intake bundles with datetime-versioned rsync drops, file-backed citation sources enforced by the gates, frontend-slides declared the default engine, citation validators consolidated on the global skill bundle, and a global `deck` skill for discovery.

**Architecture:** Source-side agents (any repo/machine) produce `deck-intake/` bundles per a portable spec and push immutable `intake_<datetime>/` drops into `docs/talks/<slug>/` (gitignored). Deck sessions in this repo build frontend-slides HTML under the existing citation gates, now extended with a `file:` source type (`data-file-source` deck markers, git-tracked or `local-only`+sha256 registry entries). The shared cite validators move to the global `~/Setup/skills/cite` bundle; this repo keeps only the deck-artifact linters.

**Tech Stack:** Python 3 (stdlib + pyyaml, pytest), GNU Make, rsync, git; frontend-slides skill for deck rendering; ~/Setup dotfiles fanout for skill deployment.

## Global Constraints

- Working repo: `/home/ezalos/42/Markdowns2Teach`, branch `main`, commit directly (Louis's repo — no feature branches, no push unless asked). Tasks 3 and 9 also commit in `/home/ezalos/Setup` (also Louis's — same rule).
- NEVER `rm` — use `rip` (recoverable graveyard). NEVER `--no-verify` on commits.
- Commit messages in this plan are plain ASCII on purpose — use them verbatim with `git commit -m`. If you change one, avoid em-dashes/apostrophes or use the Write-to-file + `git commit -F` pattern.
- New code files start with a 2-line `ABOUTME:` comment.
- Scripts are invoked `python3 scripts/<name>.py` (repo idiom). Tests: `python3 -m pytest scripts/tests/ -v` (pyyaml and pytest are available on system python3; fallback `uv run --with pytest --with pyyaml -- python3 -m pytest scripts/tests/ -v`).
- **Pinned conventions used across tasks (must match everywhere):**
  - Datetime suffix format: `YYYY-MM-DD-HHMM` (e.g. `intake_2026-07-13-1400`).
  - Landing zone: `docs/talks/<slug>/intake_<datetime>/` — gitignored, immutable per drop.
  - Requests: `docs/talks/<slug>/requests/REQUESTS-<datetime>.md` — committed.
  - Deck marker for file-backed claims: `data-file-source="<registry-id>"` on an element inside the slide's sources footer.
  - `sources.yml` file entry: required `id`, `file` (repo-relative path), `authority`, `title`; exactly one of `url`/`file` per entry; file entries are either **promoted** (file exists AND git-tracked) or **`verify: local-only`** (requires `sha256` + `reason`). Extra fields (`slides:`, `deck:`) are tolerated.

---

### Task 1: Intake landing zone + portable intake spec

**Files:**
- Modify: `.gitignore` (after line 77, the heuritech videos block)
- Create: `docs/references/deck-intake-spec.md`

**Interfaces:**
- Produces: the gitignore pattern `docs/talks/*/intake_*/` (Task 8 relies on it) and the intake-spec document that Task 9's skill points at (exact path `docs/references/deck-intake-spec.md`).

- [ ] **Step 1: Add the landing-zone ignore rule**

In `.gitignore`, insert after the `docs/talks/heuritech-agents/sources/videos/` block:

```gitignore
# Deck-intake drops (rsync landing zone) — heavy/personal source bundles, never
# auto-committed; cited artifacts are promoted deliberately or registered
# verify: local-only + sha256 (see docs/references/deck-intake-spec.md)
docs/talks/*/intake_*/
```

- [ ] **Step 2: Verify the pattern works**

Run:
```bash
mkdir -p docs/talks/_gitignore-probe/intake_2026-01-01-0000
touch docs/talks/_gitignore-probe/intake_2026-01-01-0000/x.bin
git check-ignore -v docs/talks/_gitignore-probe/intake_2026-01-01-0000/x.bin
rip docs/talks/_gitignore-probe
```
Expected: `check-ignore` prints the `.gitignore` line matching `docs/talks/*/intake_*/`. (Probe dir removed after.)

- [ ] **Step 3: Write `docs/references/deck-intake-spec.md`**

Full content:

````markdown
<!-- ABOUTME: Portable spec for deck-intake bundles: what a source-side agent produces so a
     deck can be built in Markdowns2Teach under its citation gates. Self-contained. -->

# Deck-intake spec (v1 — 2026-07-13)

**You are the source-side agent**: you work in the project a deck/talk will be made ABOUT.
Your deliverable is an **intake bundle**, not slides. Deck building, citation verification,
and publishing happen in another repo (`~/42/Markdowns2Teach` on Louis's machine — "the deck
repo") by another agent ("the deck agent"). This document is the complete contract between
you and them: you need nothing else from the deck repo to comply.

**Why quality matters:** the deck agent can only claim what you can back. Every number on a
slide must trace to an artifact or URL you provide; anything unbacked gets cut or comes back
to you as a request. A tight bundle means a deck built in one pass.

## 1. Bundle layout

Create `deck-intake/` at your project root:

```
deck-intake/
├── HANDOFF.md      # the core deliverable (first drop) — see §2
├── SYNC.md         # delivery endpoints, written at first push — see §5
├── figures/        # plots/screenshots/diagrams; each needs an asset-map row
├── data/           # small machine-readable files backing claims (JSON/CSV/JSONL)
└── assets/         # photos, logos, misc visuals
```

Omit empty subdirs. Filenames: kebab-case or snake_case, NO spaces.

## 2. HANDOFF.md — required sections

### Audience & occasion
Who is in the room, when, expected talk length, stakes.

### The story
The ARGUMENT the deck should make — 5–15 sentences of narrative arc (hook → tension →
resolution → takeaway). Not a slide list; the deck agent owns slide design.

### Verified numbers
A table of every number a slide might state. **No number outside this table may appear on a
slide.** Columns:

| # | claim | value | provenance | status | caveat |
|---|-------|-------|------------|--------|--------|
| N1 | final win-rate vs baseline | 0.7227 | data/eval_clean.json | clean | measured on the decontaminated split |
| N2 | first-run win-rate | 0.887 | data/eval_run1.json | CAVEAT | eval split later found contaminated — never show without this caveat |

- `provenance` = a bundle file (relative path) or an exact external URL.
- `status` is `clean` or `CAVEAT`. A CAVEAT row MUST carry its honesty caveat verbatim; the
  deck agent will print the caveat next to the number, or drop the number.

### Asset map
One row per file in the bundle. **A file with no row does not exist for the deck agent.**

| file | what it shows | how it was generated | claims it can back | sensitivity |
|------|---------------|----------------------|--------------------|-------------|
| figures/win_rate.png | win-rate by training step | scripts/plot_eval.py on data/eval_clean.json | N1 | PUBLIC |

### External sources
For every claim backed by the open web: the exact deep URL (never a bare domain, never a
section/index page) plus a VERBATIM quote from that page proving the claim. These pre-seed
the deck's citation registry, which is machine-verified character-by-character — a
paraphrase will fail the gate.

### Open calls
Decisions you explicitly leave to the deck agent (tone, what to cut first, which figure
variant), one bullet each.

## 3. Sensitivity marks

Mark every file with the STRICTEST applicable:

- **PUBLIC** — may be committed to the deck repo and shown on a slide.
- **PERSONAL** — contains personal/confidential information. Never committed deck-side,
  never shown without Louis's explicit approval. Prefer providing a redacted derivative.
- **HEAVY** — too big for git (rule of thumb: >2 MB single file or >1000 files). Stays in
  gitignored drops; the deck side cites it by checksum.

## 4. Drop protocol

- Every delivery is ONE new directory on the deck side:
  `docs/talks/<slug>/intake_<YYYY-MM-DD-HHMM>/` (your rsync target, their tree).
- A drop is **immutable** once pushed. Corrections and additions are a NEW drop — never
  edit or re-push into an existing one.
- The first drop carries `HANDOFF.md`. Every later drop carries `ANSWERS.md` instead (§6),
  with the same subdir layout for any new material.
- The deck agent reads the union of all drops; on same-path conflicts the newest drop wins.

## 5. SYNC.md + delivery commands

`<slug>` = short kebab-case deck name agreed with Louis (e.g. `rlaif-vlm`).
At FIRST push, write `deck-intake/SYNC.md`:

```
# SYNC — deck delivery endpoints
slug: <slug>
deck_host: <ssh host alias, or "local" if same machine>
talk_dir: ~/42/Markdowns2Teach/docs/talks/<slug>
pushed:
  - intake_<YYYY-MM-DD-HHMM>    # append one line per drop
```

Push a drop (remote; same machine = drop the `<deck_host>:` prefix):

```bash
rsync -av deck-intake/ <deck_host>:~/42/Markdowns2Teach/docs/talks/<slug>/intake_$(date +%Y-%m-%d-%H%M)/
```

Pull the talk dir (to read requests / see deck state — you can always pull, the deck side
never pushes to you):

```bash
rsync -av <deck_host>:~/42/Markdowns2Teach/docs/talks/<slug>/ ./deck-talk-mirror/
```

## 6. Requests round-trip

When the deck agent needs more, it writes numbered requests to
`docs/talks/<slug>/requests/REQUESTS-<datetime>.md` on the deck side. When Louis tells you
**"pull new requests"**:

1. Pull the talk dir (§5); read every `requests/REQUESTS-*.md` newer than your last drop.
2. Do the work — gather the data, produce the figure, answer the question, rerun the
   experiment. New material follows §2 quality: numbers-table rows, asset-map rows,
   sensitivity marks.
3. Write `ANSWERS.md`: name the REQUESTS file(s) answered at the top, then one section per
   request number stating what you provide, where it is in this drop, or why it cannot be
   provided.
4. Push as a NEW drop (§4/§5) and append it to `SYNC.md`'s `pushed:` list.

## 7. Quality checklist (self-verify before EVERY push)

- [ ] Every number a slide could state is in Verified numbers, with provenance
- [ ] Every CAVEAT number carries its honesty caveat verbatim
- [ ] Every file has an asset-map row: generation provenance + sensitivity mark
- [ ] Every external claim has an exact deep URL + verbatim quote (no bare domains)
- [ ] No spaces in filenames; no secrets or credentials anywhere in the bundle
- [ ] The story section argues something — a stranger could pitch the talk from it alone
- [ ] SYNC.md created (first push) or its `pushed:` list appended (later pushes)
````

- [ ] **Step 4: Commit**

```bash
git add .gitignore docs/references/deck-intake-spec.md
git commit -m "feat(deck): intake landing zone + portable deck-intake spec"
```

---

### Task 2: File-backed sources in the citation gates (TDD)

**Files:**
- Modify: `scripts/verify-sources.py` (full rewrite below; current file is 177 lines)
- Modify: `scripts/check-citation-links.py:100` (one-condition change + docstring note)
- Create: `scripts/tests/__init__.py`, `scripts/tests/conftest.py`, `scripts/tests/test_verify_sources.py`

**Interfaces:**
- Consumes: pinned conventions from Global Constraints (marker + registry schema).
- Produces: module-level functions in `verify-sources.py` used by tests and Task 8:
  `validate_schema(entries) -> list[str]`,
  `check_file_entry(entry, repo_root=REPO_ROOT, tracked=is_git_tracked) -> (list[str], list[str])`,
  `cross_check(cited_urls, cited_file_ids, entries) -> (list[str], list[str])`,
  `deck_file_source_ids(deck_html) -> list[str]`, `sha256_of(path) -> str`,
  `is_git_tracked(path, repo_root) -> bool`. Registry `file:` entries per pinned schema.

- [ ] **Step 1: Write the failing tests**

`scripts/tests/__init__.py`: empty file.

`scripts/tests/conftest.py`:

```python
# ABOUTME: Fixtures for scripts/ linter tests; loads the hyphen-named linter
# ABOUTME: scripts as importable modules via importlib.
import importlib.util
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1]


def _load(script_name):
    spec = importlib.util.spec_from_file_location(
        script_name.replace("-", "_"), SCRIPTS / f"{script_name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def vs():
    return _load("verify-sources")


@pytest.fixture(scope="session")
def ccl():
    return _load("check-citation-links")
```

`scripts/tests/test_verify_sources.py`:

```python
# ABOUTME: Unit tests for file-backed source support in verify-sources.py (schema,
# ABOUTME: promoted/local-only checks, deck cross-check) + the data-file-source
# ABOUTME: exemption in check-citation-links.py's non-clickable detector.
import hashlib


def entry(**kw):
    base = {"id": "e1", "authority": "internal", "title": "T"}
    base.update(kw)
    return base


class TestValidateSchema:
    def test_url_entry_with_quote_passes(self, vs):
        assert vs.validate_schema([entry(url="https://x.com/a", quote="q")]) == []

    def test_both_url_and_file_fails(self, vs):
        probs = vs.validate_schema([entry(url="https://x.com/a", file="d/x.json", quote="q")])
        assert any("exactly one of" in p for p in probs)

    def test_neither_url_nor_file_fails(self, vs):
        probs = vs.validate_schema([entry()])
        assert any("exactly one of" in p for p in probs)

    def test_plain_file_entry_needs_no_quote(self, vs):
        assert vs.validate_schema([entry(file="docs/x.md")]) == []

    def test_local_only_requires_sha256_and_reason(self, vs):
        probs = vs.validate_schema([entry(file="d/x.json", verify="local-only")])
        assert any("REQUIRES sha256" in p for p in probs)
        assert any("REQUIRES a reason" in p for p in probs)

    def test_unknown_verify_mode_on_file_fails(self, vs):
        probs = vs.validate_schema([entry(file="d/x.json", verify="link-only")])
        assert any("unknown verify mode" in p for p in probs)


class TestCheckFileEntry:
    def test_promoted_missing_file_fails(self, vs, tmp_path):
        probs, warns = vs.check_file_entry(
            entry(file="gone.md"), repo_root=tmp_path, tracked=lambda p, r: True)
        assert any("MISSING" in p for p in probs) and warns == []

    def test_promoted_untracked_fails(self, vs, tmp_path):
        (tmp_path / "a.md").write_text("x")
        probs, _ = vs.check_file_entry(
            entry(file="a.md"), repo_root=tmp_path, tracked=lambda p, r: False)
        assert any("not git-tracked" in p for p in probs)

    def test_promoted_tracked_ok(self, vs, tmp_path):
        (tmp_path / "a.md").write_text("x")
        probs, warns = vs.check_file_entry(
            entry(file="a.md"), repo_root=tmp_path, tracked=lambda p, r: True)
        assert probs == [] and warns == []

    def test_local_only_absent_warns_not_fails(self, vs, tmp_path):
        probs, warns = vs.check_file_entry(
            entry(file="gone.bin", verify="local-only", sha256="00", reason="heavy"),
            repo_root=tmp_path)
        assert probs == [] and any("ABSENT" in w for w in warns)

    def test_local_only_sha_match_ok(self, vs, tmp_path):
        p = tmp_path / "a.bin"
        p.write_bytes(b"data")
        good = hashlib.sha256(b"data").hexdigest()
        probs, warns = vs.check_file_entry(
            entry(file="a.bin", verify="local-only", sha256=good, reason="heavy"),
            repo_root=tmp_path)
        assert probs == [] and warns == []

    def test_local_only_sha_mismatch_fails(self, vs, tmp_path):
        p = tmp_path / "a.bin"
        p.write_bytes(b"data")
        probs, _ = vs.check_file_entry(
            entry(file="a.bin", verify="local-only", sha256="deadbeef", reason="heavy"),
            repo_root=tmp_path)
        assert any("MISMATCH" in p for p in probs)


class TestCrossCheck:
    def test_unregistered_file_marker_fails(self, vs):
        probs, _ = vs.cross_check([], ["mystery"], [entry(file="a.md")])
        assert any('UNREGISTERED file source: data-file-source="mystery"' in p for p in probs)

    def test_stale_file_entry_warns(self, vs):
        _, warns = vs.cross_check([], [], [entry(file="a.md")])
        assert any("'e1' is not cited" in w for w in warns)

    def test_registered_marker_clean(self, vs):
        probs, warns = vs.cross_check([], ["e1"], [entry(file="a.md")])
        assert probs == [] and warns == []


class TestDeckFileSourceIds:
    def test_extracts_unique_ids_in_order(self, vs):
        html = ('<span data-file-source="a">x</span>'
                '<span data-file-source="b">y</span>'
                '<span data-file-source="a">x</span>')
        assert vs.deck_file_source_ids(html) == ["a", "b"]


class TestUnclickableExemption:
    FOOTER = '<small class="sources">Sources : {inner}</small>'

    def test_file_source_line_without_anchor_passes(self, ccl):
        html = self.FOOTER.format(
            inner='[D1] <span data-file-source="probe-log">probe_log.jsonl</span>')
        assert ccl.unclickable_sources(html) == []

    def test_plain_text_source_line_still_fails(self, ccl):
        html = self.FOOTER.format(inner="[1] some report, trust me")
        assert any("NO clickable link" in reason for reason, _ in ccl.unclickable_sources(html))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest scripts/tests/ -v`
Expected: FAIL — `AttributeError: module 'verify_sources' has no attribute 'validate_schema'` (and the exemption test fails on the current `unclickable_sources`).

- [ ] **Step 3: Rewrite `scripts/verify-sources.py`**

Replace the whole file with:

```python
#!/usr/bin/env python3
# ABOUTME: Enforces the deck sources contract: every citation href must exist in a curated
# ABOUTME: sources.yml with a VERBATIM quote, and each quote is live-verified (fetch + grep).

"""
Why this exists (Louis, 2026-07-09): a deck shipped whose PDF export showed bare-domain
citation labels — unverifiable sources in the artifact actually read. The href-only linter
(check-citation-links.py) passed, because it never looks at what the reader sees nor at
whether the source actually SAYS what we cite. This tool closes that hole:

  1. Every deck ships with a sibling `sources.yml` — the curated source-of-truth registry.
  2. Every registry entry records the FULL exact URL + a VERBATIM quote (character-by-
     character string that appears on the page) proving the source says what we cite.
  3. This script cross-checks deck <-> registry (no unregistered citation, no dead entry)
     and live-verifies each entry: URL must be reachable AND the quote must be found in
     the fetched page (whitespace/entity-normalized exact substring match).
  4. Entries that genuinely cannot be text-verified (JS-only walls, auth gates) must say
     `verify: link-only` with a `reason:` — and they are printed LOUDLY, never silent.

File-backed sources (2026-07-13, deck-capability design): claims backed by repo artifacts
instead of web pages use a `file:` entry (repo-relative path) and are marked in the deck
with data-file-source="<id>". Two modes:
  - promoted (default): the file must exist AND be git-tracked;
  - verify: local-only (+ sha256 + reason): heavy/personal artifacts living in gitignored
    intake drops — checksum-verified when present, LOUDLY warned when absent, never silent.
File checks are local disk operations, so they run in --offline mode too.
Contract cousin: the /cite skill's validate_claim.py (~/Setup/skills/cite/scripts/)
implements the same verbatim-quote idea for prose claims — shared CONTRACT, independent
code, on purpose. Read the 2026-07-13 deck-capability design before unifying or forking.
Spec: docs/references/deck-intake-spec.md
Design: docs/superpowers/specs/2026-07-13-deck-capability-design.md

Usage:
  python3 scripts/verify-sources.py <deck.html> [--registry <sources.yml>] [--offline]

Default registry: sources.yml next to the deck. --offline skips network (schema +
cross-check + file checks) for fast pre-commit runs; full (live) mode is REQUIRED before
any share/deploy/PDF export.

Exit 0 = clean; 1 = violations (printed); 2 = bad args / missing registry.
"""

import hashlib
import html as htmllib
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

import yaml

HREF_RE = re.compile(r'<a\s+[^>]*href="(https?://[^"]+)"', re.S)
FILE_SRC_RE = re.compile(r'data-file-source="([^"]+)"')
# same allow-list philosophy as check-citation-links.py: assets aren't citations
ALLOW_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com", "api.fontshare.com"}
GATED_CODES = (401, 403, 405, 429)  # exists but bot/auth-gated
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
REPO_ROOT = Path(__file__).resolve().parents[1]


def norm(s: str) -> str:
    """Normalize for character-by-character comparison across HTML noise:
    unescape entities, unify unicode (quotes/dashes), collapse whitespace."""
    s = htmllib.unescape(s)
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("‑", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def fetch(url: str):
    """Return (status, body_text) — status is int, or a string error tag."""
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.getcode(), r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return f"unreachable ({type(e).__name__})", ""


def deck_citation_urls(deck_html: str):
    urls = []
    for u in HREF_RE.findall(deck_html):
        host = re.sub(r"^www\.", "", re.match(r"https?://([^/]+)", u).group(1).lower())
        if host in ALLOW_HOSTS:
            continue
        if u not in urls:
            urls.append(u)
    return urls


def deck_file_source_ids(deck_html: str):
    ids = []
    for i in FILE_SRC_RE.findall(deck_html):
        if i not in ids:
            ids.append(i)
    return ids


def canon(u: str) -> str:
    """Loose URL identity: scheme + www + trailing-slash insensitive."""
    u = re.sub(r"^https?://", "", u).lstrip()
    u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")


def is_git_tracked(path: Path, repo_root: Path) -> bool:
    r = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "--error-unmatch",
         str(path.relative_to(repo_root))],
        capture_output=True)
    return r.returncode == 0


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_schema(entries):
    """Field-level registry checks. Returns a list of problem strings."""
    problems = []
    for e in entries:
        eid = e.get("id", "<missing-id>")
        for field in ("id", "authority", "title"):
            if not e.get(field):
                problems.append(f"registry entry '{eid}': missing required field '{field}'")
        has_url, has_file = bool(e.get("url")), bool(e.get("file"))
        if has_url == has_file:
            problems.append(f"registry entry '{eid}': exactly one of 'url' or 'file' is required")
        elif has_url:
            if e.get("verify") == "link-only":
                if not e.get("reason"):
                    problems.append(f"registry entry '{eid}': verify: link-only REQUIRES a reason")
            elif not e.get("quote"):
                problems.append(f"registry entry '{eid}': missing verbatim 'quote' (or verify: link-only + reason)")
        else:
            if e.get("verify") == "local-only":
                if not e.get("sha256"):
                    problems.append(f"registry entry '{eid}': verify: local-only REQUIRES sha256")
                if not e.get("reason"):
                    problems.append(f"registry entry '{eid}': verify: local-only REQUIRES a reason")
            elif e.get("verify"):
                problems.append(f"registry entry '{eid}': unknown verify mode '{e.get('verify')}' for a file source")
    return problems


def check_file_entry(e, repo_root=REPO_ROOT, tracked=is_git_tracked):
    """Verify one file: entry against the working tree. Returns (problems, warnings).
    Local disk operation — runs in offline AND live modes."""
    problems, warnings = [], []
    eid, rel = e.get("id", "?"), e["file"]
    p = repo_root / rel
    if e.get("verify") == "local-only":
        if not p.exists():
            warnings.append(f"LOCAL-ONLY artifact ABSENT '{eid}': {rel} — {e.get('reason')} "
                            "(not on this clone; re-pull the intake drop to verify)")
        elif e.get("sha256") and sha256_of(p) != e["sha256"]:
            problems.append(f"'{eid}': sha256 MISMATCH for {rel} — artifact changed since the "
                            "claim was verified; re-verify the claim and update sha256")
    else:
        if not p.exists():
            problems.append(f"'{eid}': file source MISSING: {rel}")
        elif not tracked(p, repo_root):
            problems.append(f"'{eid}': file source {rel} is not git-tracked — promote it (commit) "
                            "or mark verify: local-only + sha256 + reason")
    return problems, warnings


def cross_check(cited_urls, cited_file_ids, entries):
    """Deck <-> registry cross-check for both source kinds. Returns (problems, warnings)."""
    problems, warnings = [], []
    by_canon = {canon(e["url"]): e for e in entries if e.get("url")}
    file_by_id = {e["id"]: e for e in entries if e.get("file") and e.get("id")}
    for u in cited_urls:
        if canon(u) not in by_canon:
            problems.append(f"deck cites UNREGISTERED source: {u}  -> add it to the registry with a verbatim quote")
    for i in cited_file_ids:
        if i not in file_by_id:
            problems.append(f'deck cites UNREGISTERED file source: data-file-source="{i}"  -> add a file: entry')
    cited_canon = {canon(u) for u in cited_urls}
    for c, e in by_canon.items():
        if c not in cited_canon:
            warnings.append(f"registry entry '{e['id']}' is not cited by the deck (stale? remove or keep deliberately)")
    for i in file_by_id:
        if i not in cited_file_ids:
            warnings.append(f"registry file entry '{i}' is not cited by the deck (stale? remove or keep deliberately)")
    return problems, warnings


def main():
    args = [a for a in sys.argv[1:]]
    offline = "--offline" in args
    args = [a for a in args if a != "--offline"]
    reg_path = None
    if "--registry" in args:
        i = args.index("--registry")
        reg_path = Path(args[i + 1])
        del args[i:i + 2]
    if len(args) != 1:
        sys.exit("usage: verify-sources.py <deck.html> [--registry sources.yml] [--offline]")
    deck_path = Path(args[0])
    if reg_path is None:
        reg_path = deck_path.parent / "sources.yml"
    if not reg_path.exists():
        print(f"FAIL  no sources registry at {reg_path} — every deck MUST have one.")
        print("      Create it: one entry per source (id, url|file, authority, title, quote).")
        sys.exit(2)

    deck_html = deck_path.read_text(encoding="utf-8", errors="replace")
    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8"))
    entries = reg.get("sources", [])

    problems = validate_schema(entries)
    warnings = []

    cited = deck_citation_urls(deck_html)
    cited_file_ids = deck_file_source_ids(deck_html)
    p, w = cross_check(cited, cited_file_ids, entries)
    problems += p
    warnings += w

    # ---- file-backed sources: verified on local disk, offline AND live ----
    for e in entries:
        if e.get("file"):
            p, w = check_file_entry(e)
            problems += p
            warnings += w

    # ---- live verification (URL entries only) ----
    if not offline:
        for e in entries:
            url, eid = e.get("url"), e.get("id", "?")
            if not url:
                continue
            status, body = fetch(url)
            if isinstance(status, str):
                problems.append(f"'{eid}': {status}  {url}")
                continue
            if status >= 400 and status not in GATED_CODES:
                problems.append(f"'{eid}': HTTP {status} (dead)  {url}")
                continue
            if e.get("verify") == "link-only":
                warnings.append(f"LINK-ONLY (unverifiable quote) '{eid}': {e.get('reason')}  {url}")
                continue
            if status in GATED_CODES:
                warnings.append(f"'{eid}': HTTP {status} gated — page exists but quote can't be text-checked  {url}")
                continue
            hay = norm(body)
            hay_text = norm(re.sub(r"<script\b.*?</script>|<style\b.*?</style>|<[^>]+>", " ", body, flags=re.S))
            needle = norm(e["quote"])
            if needle not in hay and needle not in hay_text:
                problems.append(f"'{eid}': quote NOT FOUND character-by-character on page  {url}\n"
                                f"        quote: {e['quote'][:100]!r}")

    for w in warnings:
        print(f"WARN  {w}")
    if problems:
        print(f"FAIL  {deck_path.name}: {len(problems)} sources-contract violation(s):")
        for p in problems:
            print(f"    - {p}")
        print("\nEVERY citation must be registered: URLs with a live-verified verbatim quote,")
        print("file artifacts committed (promoted) or local-only with a matching sha256.")
        sys.exit(1)
    mode = "offline (schema + cross-check + files)" if offline else "LIVE (fetch + verbatim quote grep + files)"
    print(f"PASS  {deck_path.name}: {len(cited)} cited URL(s) + {len(cited_file_ids)} file source(s) all registered & verified [{mode}]")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Exempt file-source markers in `check-citation-links.py`**

In `unclickable_sources()` (line 100), change:

```python
        if "<a " not in inner and re.search(r"\bSources?\s*:|\bSource\b|\[\d+\]", text_all):
```
to:
```python
        if "<a " not in inner and "data-file-source" not in inner \
                and re.search(r"\bSources?\s*:|\bSource\b|\[\d+\]", text_all):
```

And in the docstring of `unclickable_sources` append: `Elements carrying data-file-source
are exempt — those sources are file artifacts verified by verify-sources.py, not links.`

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest scripts/tests/ -v`
Expected: all PASS.

- [ ] **Step 6: Regression on the three existing decks**

Run:
```bash
make verify-sources check-citation-links
```
Expected: `PASS` for capgemini-ai-agents (x2 files), heuritech-agents, rlaif-vlm — same
outcomes as before the change (URL-only registries; `0 file source(s)` in the PASS lines).

- [ ] **Step 7: Commit**

```bash
git add scripts/verify-sources.py scripts/check-citation-links.py scripts/tests/
git commit -m "feat(cite-gates): file-backed sources (data-file-source markers, promoted or local-only+sha256)"
```

---

### Task 3: Port cite test coverage to ~/Setup (BEFORE deleting the mirror)

**Files (all in `/home/ezalos/Setup`):**
- Modify: `skills/cite/scripts/tests/test_validate_claim.py`, `tests/test_tier_lookup.py`, `tests/test_lint_authority_map.py` (port any missing cases)
- Modify: `skills/cite-correct/SKILL.md` (promotion default)

**Interfaces:**
- Consumes: the repo's `scripts/cite/tests/` (still present — this task runs before Task 4 deletes them).
- Produces: the global test suite as the sole owner of validator coverage; Task 4 may then delete the repo mirror.

- [ ] **Step 1: Diff each repo test file against its global counterpart**

```bash
cd /home/ezalos/42/Markdowns2Teach
for f in test_validate_claim test_tier_lookup test_lint_authority_map; do
  echo "=== $f ==="
  diff scripts/cite/tests/$f.py /home/ezalos/Setup/skills/cite/scripts/tests/$f.py || true
done
```

- [ ] **Step 2: Port missing test functions**

Decision rule: a repo test function is "missing" if its name is absent from the global file
AND no global test asserts the same behavior. Port each missing one into the global file,
adapting to the global contract (layered `--map` in tier_lookup, expanded STATUS/ACTION
enums in validate_claim, `memory/` default paths in lint_authority_map). Do NOT port
anything testing `target_scope.py` (repo-specific router, retired with the mirror).

- [ ] **Step 3: Run the global suite**

Run: `python3 -m pytest /home/ezalos/Setup/skills/cite/scripts/tests/ -v`
Expected: all PASS.

- [ ] **Step 4: Document the promotion default in cite-correct**

```bash
grep -n "if a project overlay exists" /home/ezalos/Setup/skills/cite-correct/SKILL.md
```
At that sentence (it offers writing promotions to the global map OR a project overlay),
append: `Default: the global base map. Project overlays hold only repo-specific entries.`

- [ ] **Step 5: Add the contract cross-reference in validate_claim.py**

In `/home/ezalos/Setup/skills/cite/scripts/validate_claim.py`, add one comment line right
after the ABOUTME block:

```python
# Contract cousin: Markdowns2Teach's scripts/verify-sources.py applies the same
# verbatim-quote idea to deck artifacts — shared CONTRACT, independent code, on purpose
# (2026-07-13 deck-capability design in that repo). Do not unify or fork blindly.
```

- [ ] **Step 6: Commit in ~/Setup**

```bash
cd /home/ezalos/Setup
git add skills/cite/scripts/ skills/cite-correct/SKILL.md
git commit -m "test(cite): absorb Markdowns2Teach mirror test coverage; document promotion default"
```

---

### Task 4: Switch make to the global lint script; delete the frozen mirror

**Files:**
- Modify: `Makefile:152-153` (the `lint-authority-map` target)
- Delete (rip): `scripts/cite/` (entire directory)

**Interfaces:**
- Consumes: Task 3 done (coverage ported). Global script `~/.claude/skills/cite/scripts/lint_authority_map.py` already accepts `--md` / `--yaml` (verified 2026-07-13).
- Produces: `make lint-authority-map` running the deployed global script against this repo's map files.

- [ ] **Step 1: Point the Makefile at the deployed script**

Replace:
```make
lint-authority-map: ## Verify authority-map.md and authority-map.yaml are in sync
	@python3 scripts/cite/lint_authority_map.py
```
with:
```make
lint-authority-map: ## Verify the repo authority-map overlay (.md/.yaml) is in sync — canonical script lives in the global cite skill
	@python3 $$HOME/.claude/skills/cite/scripts/lint_authority_map.py \
	  --md docs/references/authority-map.md --yaml docs/references/authority-map.yaml
```
(Recipe lines start with a TAB, not spaces.)

- [ ] **Step 2: Verify the target passes before deletion**

Run: `make lint-authority-map`
Expected: `authority-map.md and authority-map.yaml are in sync.`

- [ ] **Step 3: Delete the mirror and check for dangling references**

```bash
rip scripts/cite
grep -rn "scripts/cite" Makefile scripts/ docs/references/ CLAUDE.md || echo "clean"
```
Expected: the only hits are in `CLAUDE.md` (rewritten in Task 7) and historical spec/plan
docs under `docs/superpowers/` (left as history). If `docs/references/cite-skill-backlog.md`
references the path, update that line to point at `~/Setup/skills/cite/scripts/`.

- [ ] **Step 4: Confirm make still works end to end**

Run: `make lint-authority-map && python3 -m pytest scripts/tests/ -v`
Expected: lint PASS; the Task 2 suite still green (it never imported scripts/cite).

- [ ] **Step 5: Commit**

```bash
git add -A Makefile scripts/cite docs/references/cite-skill-backlog.md
git commit -m "refactor(cite): retire frozen scripts/cite mirror; make uses the global skill script"
```

---

### Task 5: Trim the authority map to a true overlay

**Files:**
- Modify: `docs/references/authority-map.md` (full replacement)
- Modify: `docs/references/authority-map.yaml` (full replacement)

**Interfaces:**
- Consumes: Task 4's Makefile target (validates the overlay).
- Produces: an overlay the /cite skill layers over the global base (`--map` base, `--map` overlay — later wins).

- [ ] **Step 1: Confirm the two copies are still byte-identical with the global base**

```bash
diff docs/references/authority-map.yaml /home/ezalos/Setup/skills/cite/memory/authority-map.yaml && \
diff docs/references/authority-map.md /home/ezalos/Setup/skills/cite/memory/authority-map.md
```
Expected: no output (identical). **If they differ**: STOP — entries were added locally since
2026-07-13; port the repo-only entries into the global base (commit in ~/Setup) first, then
continue.

- [ ] **Step 2: Replace `docs/references/authority-map.yaml`**

```yaml
# ABOUTME: Per-project authority-map OVERLAY for /cite — layered over the global base at
# ABOUTME: ~/.claude/skills/cite/memory/authority-map.yaml (later --map wins).
# Trimmed to a true overlay 2026-07-13 (was a byte-identical copy of the global base;
# see docs/superpowers/specs/2026-07-13-deck-capability-design.md).
# Add ONLY repo-specific entries here: course-specific French sources, deck-specific
# publishers, tier overrides for this repo's audience.
tiers: {}
```

- [ ] **Step 3: Replace `docs/references/authority-map.md`**

```markdown
<!-- ABOUTME: Human-readable mirror of authority-map.yaml — this repo's OVERLAY over the
     global /cite base map. Kept in sync by make lint-authority-map. -->

# Authority map — Markdowns2Teach overlay

The global base roster lives at `~/.claude/skills/cite/memory/authority-map.md` (source:
`~/Setup/skills/cite/memory/`). This file holds ONLY repo-specific additions and overrides;
/cite layers it over the base via repeatable `--map` (later wins). The byte-identical
duplication of the base was removed 2026-07-13 (deck-capability design).

*(No overlay entries yet. To add one, create a `## Tier N — <label>` section with
`- `domain.tld` — rationale` bullets, mirror it in authority-map.yaml, and run
`make lint-authority-map`.)*
```

- [ ] **Step 4: Verify lint passes on the trimmed pair**

Run: `make lint-authority-map`
Expected: `authority-map.md and authority-map.yaml are in sync.` (both parse to zero
domains — in sync).

- [ ] **Step 5: Commit**

```bash
git add docs/references/authority-map.md docs/references/authority-map.yaml
git commit -m "refactor(cite): trim authority map to a true overlay over the global base"
```

---

### Task 6: The deck-loop workflow doc + demote the Marp workflow

**Files:**
- Create: `docs/references/workflow-new-deck.md`
- Modify: `docs/references/workflow-new-slides.md` (header note only)

**Interfaces:**
- Consumes: paths/conventions from Tasks 1-2 (intake spec, file sources).
- Produces: `docs/references/workflow-new-deck.md` — pointed at by CLAUDE.md (Task 7) and the global skill (Task 9).

- [ ] **Step 1: Write `docs/references/workflow-new-deck.md`**

Full content:

````markdown
<!-- ABOUTME: THE deck-building workflow for sessions in this repo: from intake drops to a
     shipped, citation-gated frontend-slides deck. Marp is plan B (workflow-new-slides.md). -->

# Workflow — new deck (frontend-slides, the default engine)

Scope: ANY new deck — standalone talk or Sorbonne course deck. The default engine is
**frontend-slides** (self-contained HTML, fixed 1920x1080 stage). **Marp is plan B**: use it
only with a stated reason (e.g. editable PPTX handouts for students, bulk Markdown edits
across many decks), record the reason in the deck README or a manifest comment, then follow
`workflow-new-slides.md` — and still ship a `sources.yml`.

## 0. Inputs

- **Cross-project decks**: intake drops at `docs/talks/<slug>/intake_<datetime>/`, produced
  by a source-side agent per `docs/references/deck-intake-spec.md`. The bundle is the union
  of drops (newest wins). The first drop carries `HANDOFF.md`: audience, story, verified
  numbers (with honesty caveats), asset map with sensitivity marks, external sources, open
  calls. Read ALL drops before building; `ANSWERS.md` files respond to earlier requests.
- **Repo-native decks** (course decks, self-sourced talks): write the same `HANDOFF.md`
  yourself at `docs/talks/<slug>/HANDOFF.md` (committed) before building. Same quality bar;
  no rsync involved.

## 1. Build

- Deck dir: `slides/<slug>/` — self-contained `.html` named `<slug>.html`, generated with
  the frontend-slides skill from portable Markdown content (keep it in
  `slides/<slug>/content/` if the deck will be regenerated).
- Every regeneration must satisfy `docs/references/html-deck-interaction-standards.md`
  (macOS-safe forward-only reveals, wheel nav, deep-link citations, no-overlap on the
  fixed stage).
- Data charts: NEVER hand-drawn SVG — `scripts/charts/deck_chart.py` per
  `docs/references/deck-charts.md`.
- Seed `slides/<slug>/sources.yml` from HANDOFF's External sources table (URL entries with
  verbatim quotes) and its asset map (file entries).

## 2. Provenance & citations (the gates)

- **External claims**: clickable exact deep links with `[n]` markers; registry entry with a
  verbatim quote. `python3 scripts/check-citation-links.py <deck> --check-live` and
  `python3 scripts/verify-sources.py <deck>` must pass — see CLAUDE.md's non-negotiable.
- **Internal artifacts** (experiment data, project files from the bundle): mark the claim's
  footer element with `data-file-source="<registry-id>"` and register a `file:` entry.
  Then EITHER promote the artifact — copy it out of the gitignored drop to a committed
  location (`docs/talks/<slug>/` or the deck assets) after a size + sensitivity check —
  OR register it `verify: local-only` + `sha256` + `reason` (heavy/personal artifacts).
- **PERSONAL-marked files**: never committed, never promoted or shown without Louis's
  explicit approval. Prefer redacted derivatives.
- Run `make check` (offline gates) and `make test-decks` (nav + overlap) after every build.

## 3. Critique loop

Iterate until the deck holds:
- Read the deck as the audience would; check every slide against HANDOFF's story and
  verified-numbers table (numbers not in the table do not go on slides; CAVEAT numbers
  carry their caveat).
- When material is missing, escalate in order:
  1. **Re-pull** — the source side may have pushed a new drop; list `intake_*/` dirs newer
     than the last one you read.
  2. **Request** — write `docs/talks/<slug>/requests/REQUESTS-<YYYY-MM-DD-HHMM>.md`:
     numbered items, each *what / why / preferred form*. Commit it and tell Louis
     "requests ready for <slug>" — he relays "pull new requests" to the source agent, which
     answers with a new `intake_<datetime>/` drop containing `ANSWERS.md`.
  3. **Derive** — produce what you need from drops already present (charts, crops,
     recomputation), with subagents where useful.

## 4. Ship

1. `slides/index.manifest.yml`: add the deck (`date`, `prebuilt_html`).
2. `make check && make test-decks` — clean.
3. `make export-pdf-<slug>` — the LIVE gate (fetches every URL, greps quotes, verifies file
   sources) then builds the link-annotated PDF with a References page.
4. `make deploy` — publish to slides.develle.fr.
````

- [ ] **Step 2: Demote the Marp workflow**

In `docs/references/workflow-new-slides.md`, insert immediately after the ABOUTME comment
block (before the first heading):

```markdown
> **PLAN B — Marp.** The default engine for ALL new decks is frontend-slides: start at
> `docs/references/workflow-new-deck.md`. Use this Marp workflow only with a stated reason
> recorded in the deck README or manifest comment (e.g. editable PPTX handouts), and ship a
> `sources.yml` alongside (same contract as HTML decks). (Engine policy: 2026-07-13
> deck-capability design.)
```

- [ ] **Step 3: Commit**

```bash
git add docs/references/workflow-new-deck.md docs/references/workflow-new-slides.md
git commit -m "docs(deck): workflow-new-deck as the default path; Marp workflow demoted to plan B"
```

---

### Task 7: CLAUDE.md updates

**Files:**
- Modify: `CLAUDE.md` (five edits)

**Interfaces:**
- Consumes: everything shipped in Tasks 1-6 (paths must exist before CLAUDE.md points at them).

- [ ] **Step 1: Rewrite the "Two build systems" block**

Replace the block starting `**Two build systems:**` (both engine bullets) with:

```markdown
**Two build systems — frontend-slides is the DEFAULT, Marp is plan B:**
- **frontend-slides** (the `/frontend-slides` skill) — DEFAULT for every new deck, talks AND
  future course editions: polished standalone HTML generated from portable Markdown content
  (e.g. `slides/capgemini-ai-agents/`). The committed `.html` is copied into
  `dist/html/<deck>/` by `make html` and linked from the index via a `prebuilt_html` entry
  in `slides/index.manifest.yml`. Start at `docs/references/workflow-new-deck.md`.
- **Marp** (PLAN B — requires a stated reason recorded in the deck README or a manifest
  comment, e.g. editable PPTX handouts) — Markdown decks under `slides/<deck>/` →
  `dist/{html,pptx,pdf-full}/<deck>/`, preserving the source layout. Incremental per-file
  pattern rules. New Marp decks also ship a `sources.yml` (same contract as HTML decks).
```

- [ ] **Step 2: Add the deck-capability section**

Insert a new section immediately after the "Build Commands" section:

```markdown
## Deck capability — cross-project intake

Decks about OTHER projects are fed by intake bundles, not by reading the source repo:
a source-side agent (any repo, any machine) follows `docs/references/deck-intake-spec.md`
and rsyncs immutable drops into `docs/talks/<slug>/intake_<YYYY-MM-DD-HHMM>/` (gitignored —
sources can be heavy or personal). The deck session builds `slides/<slug>/` per
`docs/references/workflow-new-deck.md`. Need more material? Write
`docs/talks/<slug>/requests/REQUESTS-<datetime>.md` (committed) and tell Louis — the source
agent pulls the talk dir, answers, and pushes a new drop with `ANSWERS.md`. Discovery from
other repos: the global `deck` skill (`~/Setup/skills/deck/`).

Internal artifacts are first-class citable sources: mark the claim with
`data-file-source="<id>"` and add a `file:` entry to `sources.yml` — committed (promoted
after a size + sensitivity check) or `verify: local-only` + `sha256` + `reason` for
heavy/personal files. Enforced by `scripts/verify-sources.py` in offline AND live modes.
PERSONAL-flagged material is never committed or shown without Louis's explicit approval.
```

- [ ] **Step 3: Amend the non-negotiable citation section**

In the `## ⚠️ NON-NEGOTIABLE` section, add one bullet after the sources.yml bullet:

```markdown
- **Internal artifacts** (experiment data, project files) are citable via `file:` registry
  entries marked `data-file-source="<id>"` in the deck — committed, or
  `verify: local-only` + `sha256` + `reason` when heavy/personal. They complement, never
  replace, the clickable-link rule for externally-sourced claims.
```

- [ ] **Step 4: Update the Citation Audit section**

Replace the paragraph + bullet list starting `**Repo-local pieces (build-only mirror, NOT
used by the skill):**` (through the `23 unit tests` bullet) with:

```markdown
**Repo-local mirror removed (2026-07-13):** the shared validators are canonical in the
global skill bundle (`~/Setup/skills/cite/scripts/`, deployed at
`~/.claude/skills/cite/scripts/`); `make lint-authority-map` calls the deployed
`lint_authority_map.py` with this repo's map paths. The deck-artifact linters
(`scripts/check-citation-links.py`, `scripts/verify-sources.py`) remain repo-canonical —
they enforce the deck-specific contract (registry + verbatim quotes + file sources) and
have no global counterpart. Tests: `python3 -m pytest scripts/tests/ -v`.
```

Also update the authority-map paragraph below it: replace the sentence saying the repo map
"is this repo's roster, and doubles as the optional per-project overlay" with:

```markdown
**Authority map:** `docs/references/authority-map.{md,yaml}` is a true OVERLAY (repo-specific
entries only) over the global base at `~/.claude/skills/cite/memory/authority-map.yaml`;
/cite layers it via repeatable `--map` (later wins). Promotions default to the global base.
```

- [ ] **Step 5: Fix stale tree references**

In the Directory Structure tree: change the `├── scripts/` comment line to drop `cite/`
(e.g. `# generate-index.py, check-overflow-visual.js, verify-sources.py, ...`) and change
the `└── dist/` line to `# Generated output (gitignored): html/ pptx/ pdf-full/ pdf-export/`.

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(claude.md): deck capability, engine default + plan B, cite consolidation"
```

---

### Task 8: rlaif-vlm provenance retrofit (acceptance exercise)

**Files:**
- Move: `docs/talks/rlaif-vlm/examples/` → `docs/talks/rlaif-vlm/intake_<datetime>/examples/` (untracked → gitignored)
- Modify: `slides/rlaif-vlm/rlaif-vlm.html` (add `data-file-source` markers)
- Modify: `slides/rlaif-vlm/sources.yml` (add `file:` entries)

**Interfaces:**
- Consumes: Task 1 (gitignore), Task 2 (`file:` support, marker convention).
- Produces: proof the machinery expresses the deck that inspired it (spec's acceptance criterion).

- [ ] **Step 1: Move the untracked provenance into an intake drop**

Use the current datetime for `<DT>` (format `YYYY-MM-DD-HHMM`):

```bash
DT=$(date +%Y-%m-%d-%H%M)
mkdir -p docs/talks/rlaif-vlm/intake_$DT
mv docs/talks/rlaif-vlm/examples docs/talks/rlaif-vlm/intake_$DT/examples
git check-ignore -v docs/talks/rlaif-vlm/intake_$DT/examples/data_sanity_16k.jsonl
git status --short docs/talks/rlaif-vlm/
```
Expected: `check-ignore` matches the `docs/talks/*/intake_*/` rule; `git status` shows
NOTHING untracked under `docs/talks/rlaif-vlm/` anymore.

- [ ] **Step 2: Identify the internally-backed claims**

Read `docs/talks/rlaif-vlm/HANDOFF-deck-agent.md` (its verified numbers + asset mapping)
and scan the deck's source footers:

```bash
grep -no 'class="[^"]*\(sources\|src-line\|loop-source\|dual-cite\)[^"]*"[^>]*>' slides/rlaif-vlm/rlaif-vlm.html
```

Select AT LEAST three slide claims whose backing is an internal artifact, covering both
modes — e.g.: a metrics claim backed by a committed `docs/talks/rlaif-vlm/results/*.json`
(promoted mode), a before/after probe visual backed by
`intake_<DT>/examples/probes_16k/probe_log.jsonl` (local-only mode), and a preference-pair
claim backed by `intake_<DT>/examples/rlaif/preferences.jsonl` (local-only mode). The
HANDOFF's asset-provenance map is the authority for which file backs which claim.

- [ ] **Step 3: Mark the claims in the deck**

Inside each selected slide's sources-footer element, add a marker span, e.g.:

```html
<span class="file-src" data-file-source="probe-log-16k">probe_log.jsonl</span>
```

Match the deck's existing footer styling conventions (separator ` · `, label text short).
Do not touch any other markup.

- [ ] **Step 4: Register the entries in `slides/rlaif-vlm/sources.yml`**

For each marker, append an entry. Promoted (committed) example:

```yaml
  - id: eval-results-16k
    file: docs/talks/rlaif-vlm/results/<actual-file>.json
    authority: internal - RLAIF-VLM experiment artifact
    title: "Eval results, 16k-step run"
    slides: [<n>]
```

Local-only example (compute the hash: `sha256sum <path>` and paste the 64-hex digest):

```yaml
  - id: probe-log-16k
    file: docs/talks/rlaif-vlm/intake_<DT>/examples/probes_16k/probe_log.jsonl
    authority: internal - RLAIF-VLM experiment artifact
    title: "Probe log, 16k-step run"
    verify: local-only
    sha256: "<64-hex from sha256sum>"
    reason: raw experiment data in a gitignored intake drop (heavy)
    slides: [<n>]
```

Registry ids must equal the `data-file-source` values from Step 3, character for character.

- [ ] **Step 5: Run the gates**

```bash
python3 scripts/verify-sources.py slides/rlaif-vlm/rlaif-vlm.html --offline
python3 scripts/check-citation-links.py slides/rlaif-vlm/rlaif-vlm.html
make check
make test-decks
```
Expected: verify-sources `PASS ... + 3 file source(s) ...` (no ABSENT warnings — the drop is
on this machine); check-citation-links `PASS`; `make check` clean; `make test-decks` clean
(the deck HTML changed — nav/overlap regression must stay green; needs Chrome + DISPLAY,
see memory notes on headful runs).

- [ ] **Step 6: Commit**

```bash
git add slides/rlaif-vlm/rlaif-vlm.html slides/rlaif-vlm/sources.yml
git commit -m "feat(rlaif-vlm): cite internal artifacts as file sources (acceptance of the deck-capability design)"
```
(The `intake_*` drop itself is gitignored and stays out of the commit — that is the point.)

---

### Task 9: Global surface — the `deck` skill + capability index line (~/Setup)

**Files (all in `/home/ezalos/Setup` unless noted):**
- Create: `skills/deck/SKILL.md`
- Modify: the SOURCE of `~/.claude/CLAUDE.md` (resolve with `readlink -f`)

**Interfaces:**
- Consumes: `docs/references/deck-intake-spec.md` and `workflow-new-deck.md` (Tasks 1, 6) at their absolute paths.
- Produces: `~/.claude/skills/deck` (fanout symlink) — global discovery for the capability.

- [ ] **Step 1: Write `~/Setup/skills/deck/SKILL.md`**

Full content:

````markdown
---
name: deck
description: Use when Louis wants a slide deck / talk / presentation made ABOUT the current project or from its results — e.g. "make a deck from this", "prepare slides for the demo", "turn this into a talk". Outside ~/42/Markdowns2Teach this means producing a deck-intake bundle per the portable spec and rsyncing it there — NOT building slides here. Inside ~/42/Markdowns2Teach, follow its deck workflow. Deck building and its citation gates live in ~/42/Markdowns2Teach.
---

# deck — route deck work to where the gates live

Deck building, citation verification (sources.yml + live verbatim-quote checks), and
publishing happen ONLY in `~/42/Markdowns2Teach` ("M2T"), under that repo's CLAUDE.md
rules. Everywhere else, deck work means producing source material.

## Router

1. **cwd inside `~/42/Markdowns2Teach`** → open `docs/references/workflow-new-deck.md` and
   follow it. Stop reading this skill.
2. **Anywhere else — you are SOURCE-SIDE.** Your deliverable is an intake bundle, not
   slides:
   - Read the portable spec at `~/42/Markdowns2Teach/docs/references/deck-intake-spec.md`.
     If this machine does not have that repo, ask Louis to paste or `share-file` it.
   - Produce `deck-intake/` in this project per the spec (HANDOFF.md with story, verified
     numbers + honesty caveats, asset map with sensitivity marks, external sources with
     verbatim quotes). Self-verify the spec's quality checklist.
   - Push the first drop (same machine: drop the host prefix):
     `rsync -av deck-intake/ <m2t-host>:~/42/Markdowns2Teach/docs/talks/<slug>/intake_$(date +%Y-%m-%d-%H%M)/`
   - Record the endpoints in `deck-intake/SYNC.md` (spec §5). Tell Louis the drop is
     pushed; a deck session in M2T takes it from there.
3. **Louis says "pull new requests"** → rsync the talk dir down, read new
   `requests/REQUESTS-*.md`, do the work, push a NEW `intake_<datetime>/` drop containing
   `ANSWERS.md` (spec §6).

## Hard rules

- NEVER build deck HTML source-side — the citation gates only exist in M2T.
- NEVER modify a previously pushed `intake_*/` drop — drops are immutable; push a new one.
- Sensitivity marks (PUBLIC / PERSONAL / HEAVY) are mandatory for every file.
````

- [ ] **Step 2: Deploy the fanout and verify**

```bash
cd /home/ezalos/Setup && .venv/bin/python -m src_dotfiles deploy
readlink ~/.claude/skills/deck
```
Expected: `readlink` prints `/home/ezalos/Setup/skills/deck`. (The `skills` dotfile entry
has `fanout: true` — each child of `~/Setup/skills/` is symlinked individually; no
`dotfiles.json` edit is needed for a new child. If deploy complains, invoke the
`add-dotfile` skill instead of hand-editing anything.)

- [ ] **Step 3: Add the capability-index line to global CLAUDE.md**

```bash
readlink -f ~/.claude/CLAUDE.md
```
Edit THE RESOLVED SOURCE FILE (it lives under `~/Setup`; editing a deployed symlink target
edits the source — but confirm the path is inside ~/Setup before editing). In its
`## Skills` section, add:

```markdown
- To make a deck/talk about ANY project, use the `deck` skill — deck building + citation gates live in ~/42/Markdowns2Teach.
```

- [ ] **Step 4: Commit in ~/Setup**

```bash
cd /home/ezalos/Setup
git add skills/deck/ dotfiles/
git commit -m "feat(skills): global deck skill routing deck work to Markdowns2Teach"
```
(Adjust the `git add` paths to wherever the resolved CLAUDE.md source actually lives.)

- [ ] **Step 5: End-to-end smoke of the discovery surface**

Run: `ls -la ~/.claude/skills/deck/ && head -5 ~/.claude/skills/deck/SKILL.md`
Expected: symlinked dir; frontmatter starts `name: deck`. New Claude sessions on this
machine now see the skill's name+description globally.

---

## Execution order & dependencies

1 → 2 → {3 → 4 → 5} and {6 → 7} in either order after 2; 8 requires 1+2+6; 9 requires 1+6.
Strictly: Task 3 MUST complete before Task 4 (coverage ported before deletion); Task 7 last
of the doc tasks (CLAUDE.md points at files that must exist); Task 8 after 7 is cleanest.
Sequential 1→9 satisfies everything.

## Deferred / follow-ups (not in this plan)

- First real cross-project deck using the full rsync round-trip (validates SYNC.md +
  REQUESTS in anger — the rlaif retrofit only validates provenance).
- `docs/references/cite-skill-backlog.md`: add an entry noting the consolidation if the
  backlog tracks such changes.
