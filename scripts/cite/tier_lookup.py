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
