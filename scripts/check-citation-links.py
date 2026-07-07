#!/usr/bin/env python3
# ABOUTME: Fails if any citation/source hyperlink in a deck points to a bare domain.
# ABOUTME: A source link MUST deep-link to the exact page — never just the publisher's domain.

"""
Why this exists: slide-building agents repeatedly hyperlinked citations to a
publisher's bare domain (https://anthropic.com) instead of the exact source
(https://www.youtube.com/watch?v=...). That is unacceptable in a sourced deck.
This linter scans built/​source decks and FAILS on any non-asset hyperlink whose
URL has no real path (scheme://host or scheme://host/). Wire into `make check`.

Usage: python3 scripts/check-citation-links.py <deck.html> [<deck2.html> ...]
       python3 scripts/check-citation-links.py --check-live <deck.html> ...

Default (offline, fast, wired into `make check`): FAIL on bare-domain links.
--check-live (network): ALSO FAIL on dead deep-links (4xx/5xx) — catches the
case where a link has a path but 404s (e.g. a stale /frontiercode slug). Run
this before publishing a deck.

Exit 0 = clean; 1 = problem(s) found (printed); 2 = bad args.
"""

import re
import sys
import urllib.request
from urllib.parse import urlparse

# Hosts that are legitimately referenced at domain/asset level (fonts, CDNs).
ALLOW_HOSTS = {
    "fonts.googleapis.com", "fonts.gstatic.com", "api.fontshare.com",
}

# Stricter bar (Louis, 2026-06-26): a citation must hit the EXACT page, so these
# are rejected even though they technically have a path —
#   INDEX_DENYLIST: known section/listing indexes, not a specific source.
#   REDIRECT_HOSTS: stale hosts that 301 to a canonical home; cite the canonical.
# Matched on the FULL host+path, so /news is rejected but /news/<article> passes.
INDEX_DENYLIST = {
    "anthropic.com/news", "anthropic.com/research", "anthropic.com/engineering",
    "anthropic.com/customers",
}
REDIRECT_HOSTS = {"docs.claude.com"}  # -> code.claude.com / platform.claude.com
# Single-page data sources whose ROOT genuinely IS the content (a live tracker/dashboard
# with no deeper permalink) — exempt from the bare-domain rule ONLY (still live-checked).
ROOT_SOURCES = {"botcommits.dev"}

HREF_RE = re.compile(r'href="(https?://[^"]+)"')


def _host_path(url: str):
    p = urlparse(url)
    host = (p.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    return host, (p.path or ""), (p.query or "")


def flag_links(html: str):
    """Offline citation problems: (url, reason). No network."""
    flagged = []
    for url in HREF_RE.findall(html):
        host, path, query = _host_path(url)
        if (urlparse(url).hostname or "").lower() in ALLOW_HOSTS:
            continue
        full_key = f"{host}/{path.strip('/')}" if path.strip("/") else host
        if not path.strip("/") and not query:
            if host not in ROOT_SOURCES:
                flagged.append((url, "bare domain — link the exact source page"))
        elif host in REDIRECT_HOSTS:
            flagged.append((url, f"stale-redirect host ({host}) — cite the canonical URL"))
        elif full_key in INDEX_DENYLIST:
            flagged.append((url, "section index / listing page — link the exact article"))
    # dedupe, stable
    seen, out = set(), []
    for item in flagged:
        if item[0] not in seen:
            seen.add(item[0]); out.append(item)
    return out


# Source-footer elements — every source they name MUST be a clickable <a>, so Louis can verify.
SRC_ELEM_RE = re.compile(
    r'<(div|small|p)\b[^>]*class="[^"]*(?:sources|loop-source|dual-cite|src-line)[^"]*"[^>]*>(.*?)</\1>', re.S)
DOMAIN_RE = re.compile(
    r'\b[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)*\.(?:com|org|io|ai|dev|net|us|co|uk|gov|edu|so)\b')


def unclickable_sources(html):
    """A source you can't click is a source you can't verify. Flag source-footer elements that
    (a) name a domain that is NOT inside an <a>, or (b) attribute a source with NO link at all."""
    bad = []
    for m in SRC_ELEM_RE.finditer(html):
        inner = m.group(2)
        text_all = re.sub(r"<[^>]+>", " ", inner)
        # strip the CLICKABLE parts (anchor contents + hrefs), leaving only non-clickable text
        unlinked = re.sub(r"<a\b[^>]*>.*?</a>", " ", inner, flags=re.S)
        unlinked = re.sub(r"<[^>]+>", " ", unlinked)
        for dom in set(DOMAIN_RE.findall(unlinked)):
            bad.append(("unlinked source (not clickable)", dom))
        if "<a " not in inner and re.search(r"\bSources?\s*:|\bSource\b|\[\d+\]", text_all):
            bad.append(("source line with NO clickable link", re.sub(r"\s+", " ", text_all).strip()[:70]))
    # dedupe
    seen, out = set(), []
    for it in bad:
        if it not in seen:
            seen.add(it); out.append(it)
    return out


def all_links(html: str):
    out = []
    for url in HREF_RE.findall(html):
        if (urlparse(url).hostname or "").lower() not in ALLOW_HOSTS:
            out.append(url)
    return sorted(set(out))


def dead_link(url: str):
    """Return an error string if url is dead (4xx/5xx), else None. Network."""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0 (compatible)"})
    try:
        urllib.request.urlopen(req, timeout=20).getcode()
        return None
    except urllib.error.HTTPError as e:
        # Some hosts reject HEAD or bot UAs (403/405/429) but the page is fine.
        if e.code in (403, 405, 429):
            return None
        return f"HTTP {e.code}"
    except Exception:
        try:  # retry with GET for HEAD-hostile servers
            req.method = "GET"
            urllib.request.urlopen(req, timeout=20)
            return None
        except urllib.error.HTTPError as e:
            return None if e.code in (403, 405, 429) else f"HTTP {e.code}"
        except Exception as e:
            return f"unreachable ({type(e).__name__})"


def main():
    args = sys.argv[1:]
    live = "--check-live" in args
    files = [a for a in args if a != "--check-live"]
    if not files:
        sys.exit("usage: check-citation-links.py [--check-live] <deck.html> [...]")
    total = 0
    for f in files:
        try:
            html = open(f, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"FAIL  {f}: {e}")
            total += 1
            continue
        bad = flag_links(html)
        if bad:
            total += len(bad)
            print(f"FAIL  {f}: {len(bad)} citation link(s) not pointing to the exact source:")
            for u, reason in bad:
                print(f"    - {u}  [{reason}]")
        unclick = unclickable_sources(html)
        if unclick:
            total += len(unclick)
            print(f"FAIL  {f}: {len(unclick)} NON-CLICKABLE source(s) — the reader cannot verify these:")
            for reason, what in unclick:
                print(f"    - {what}  [{reason}]")
        dead = []
        if live:
            for u in all_links(html):
                err = dead_link(u)
                if err:
                    dead.append((u, err))
            if dead:
                total += len(dead)
                print(f"FAIL  {f}: {len(dead)} dead citation link(s):")
                for u, err in dead:
                    print(f"    - {err}  {u}")
        if not bad and not unclick and not dead:
            tail = " (all live)" if live else ""
            print(f"PASS  {f}: every source is a clickable, exact link{tail}")
    if total:
        print(f"\n{total} problem(s) found. EVERY source must be an exact, live, CLICKABLE link.")
        sys.exit(1)


if __name__ == "__main__":
    main()
