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
