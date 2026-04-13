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
