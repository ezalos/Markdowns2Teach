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

HREF_RE = re.compile(r'href="(https?://[^"]+)"')


def bare_domain_links(html: str):
    bad = []
    for url in HREF_RE.findall(html):
        host = (urlparse(url).hostname or "").lower()
        if host in ALLOW_HOSTS:
            continue
        path = urlparse(url).path or ""
        query = urlparse(url).query or ""
        # "bare domain" = no meaningful path and no query (e.g. https://anthropic.com or .../)
        if path.strip("/") == "" and not query:
            bad.append(url)
    return sorted(set(bad))


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
        bad = bare_domain_links(html)
        if bad:
            total += len(bad)
            print(f"FAIL  {f}: {len(bad)} bare-domain citation link(s) — must deep-link to the exact source:")
            for u in bad:
                print(f"    - {u}")
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
        if not bad and not dead:
            tail = " (all live)" if live else ""
            print(f"PASS  {f}: all source links deep-link to a specific page{tail}")
    if total:
        print(f"\n{total} problem(s) found. A citation must point to the exact, live source URL.")
        sys.exit(1)


if __name__ == "__main__":
    main()
