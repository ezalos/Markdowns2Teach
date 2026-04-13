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
