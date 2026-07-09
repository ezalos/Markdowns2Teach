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

Usage:
  python3 scripts/verify-sources.py <deck.html> [--registry <sources.yml>] [--offline]

Default registry: sources.yml next to the deck. --offline skips network (schema +
cross-check only) for fast pre-commit runs; full (live) mode is REQUIRED before any
share/deploy/PDF export.

Exit 0 = clean; 1 = violations (printed); 2 = bad args / missing registry.
"""

import html as htmllib
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

import yaml

HREF_RE = re.compile(r'<a\s+[^>]*href="(https?://[^"]+)"', re.S)
# same allow-list philosophy as check-citation-links.py: assets aren't citations
ALLOW_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com", "api.fontshare.com"}
GATED_CODES = (401, 403, 405, 429)  # exists but bot/auth-gated
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}


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


def canon(u: str) -> str:
    """Loose URL identity: scheme + www + trailing-slash insensitive."""
    u = re.sub(r"^https?://", "", u).lstrip()
    u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")


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
        print("      Create it: one entry per source (id, url, authority, title, quote).")
        sys.exit(2)

    deck_html = deck_path.read_text(encoding="utf-8", errors="replace")
    reg = yaml.safe_load(reg_path.read_text(encoding="utf-8"))
    entries = reg.get("sources", [])

    problems, warnings = [], []

    # ---- schema ----
    by_canon = {}
    for e in entries:
        eid = e.get("id", "<missing-id>")
        for field in ("id", "url", "authority", "title"):
            if not e.get(field):
                problems.append(f"registry entry '{eid}': missing required field '{field}'")
        if e.get("verify") == "link-only":
            if not e.get("reason"):
                problems.append(f"registry entry '{eid}': verify: link-only REQUIRES a reason")
        elif not e.get("quote"):
            problems.append(f"registry entry '{eid}': missing verbatim 'quote' (or verify: link-only + reason)")
        if e.get("url"):
            by_canon[canon(e["url"])] = e

    # ---- cross-check deck <-> registry ----
    cited = deck_citation_urls(deck_html)
    for u in cited:
        if canon(u) not in by_canon:
            problems.append(f"deck cites UNREGISTERED source: {u}  -> add it to {reg_path.name} with a verbatim quote")
    cited_canon = {canon(u) for u in cited}
    for c, e in by_canon.items():
        if c not in cited_canon:
            warnings.append(f"registry entry '{e['id']}' is not cited by the deck (stale? remove or keep deliberately)")

    # ---- live verification ----
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
        print("\nEVERY citation must be registered with a full URL + live-verified verbatim quote.")
        sys.exit(1)
    mode = "offline (schema + cross-check)" if offline else "LIVE (fetch + verbatim quote grep)"
    print(f"PASS  {deck_path.name}: {len(cited)} cited sources all registered & verified [{mode}]")


if __name__ == "__main__":
    main()
