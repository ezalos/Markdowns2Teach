#!/usr/bin/env python3
# ABOUTME: Given a target .md path, print the verification shell command /cite-apply should run.
# ABOUTME: Targets under slides/ use the full make chain; elsewhere uses targeted check-citations + marp syntax check.

import argparse
import sys
from pathlib import Path


def command_for(target_path):
    p = Path(target_path)
    parts = p.parts
    # slides/ anywhere in path → full make chain
    if "slides" in parts:
        return "make check && make check-citations && make html"
    # Otherwise, derive a repo-relative containing directory for check-citations.sh
    path_str = str(p)
    containing_dir = None
    for root_marker in ("docs/references", "docs/research", "docs/notes"):
        if root_marker in path_str:
            after = path_str.split(root_marker, 1)[1].lstrip("/")
            # after = "test-fixtures/cite-fixture.md" or "ai-market-intelligence/report.md"
            if "/" in after:
                sub = after.rsplit("/", 1)[0]
                containing_dir = f"{root_marker}/{sub}"
            else:
                containing_dir = root_marker
            break
    if containing_dir is None:
        containing_dir = str(p.parent) if str(p.parent) else "."
    return f"bash scripts/check-citations.sh {containing_dir} && marp --no-stdin {target_path}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Path to the target .md file")
    args = parser.parse_args()
    print(command_for(args.target))
    sys.exit(0)


if __name__ == "__main__":
    main()
