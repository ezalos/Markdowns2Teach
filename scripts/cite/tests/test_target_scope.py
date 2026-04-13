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
