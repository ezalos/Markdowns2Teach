# ABOUTME: Shared pytest fixtures for scripts/cite/ tests.
# ABOUTME: Provides sample authority-map YAML, sample claim YAML, and sample page.txt.

from pathlib import Path
import pytest
import yaml

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_authority_map_path():
    return FIXTURES / "sample_authority_map.yaml"


@pytest.fixture
def sample_authority_map(sample_authority_map_path):
    with open(sample_authority_map_path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def sample_page_text():
    return (
        "Section A: Introduction\n\n"
        "The Flash Crash of May 6, 2010 erased approximately $1 trillion "
        "in market value within 36 minutes before rebounding.\n\n"
        "Section B: Details\n\n"
        "The Dow Jones Industrial Average plunged 998.5 points (about 9%) "
        "most within minutes.\n"
    )


@pytest.fixture
def valid_claim():
    return {
        "id": "claim-01",
        "location": {
            "file": "slides/session-01/A.md",
            "slide": "01 — Event",
            "line": 42,
        },
        "claim": {
            "text": "Le Flash Crash a effacé $1T en 36 minutes.",
            "type": "historical-event",
            "has_existing_source": False,
        },
        "proposed_source": {
            "url": "https://www.sec.gov/news/studies/2010/marketevents-report.pdf",
            "url_domain": "sec.gov",
            "publisher_org": "SEC/CFTC",
            "author": "Staff of the CFTC and SEC",
            "publication_date": "2010-09-30",
            "accessed_date": "2026-04-13",
            "quote": "The Flash Crash of May 6, 2010 erased approximately $1 trillion in market value within 36 minutes before rebounding.",
            "surrounding_paragraph": "The Flash Crash of May 6, 2010 erased approximately $1 trillion in market value within 36 minutes before rebounding.",
            "section_heading": "Section A: Introduction",
            "alignment_justification": "Quote directly confirms $1T and 36-minute duration.",
            "confidence": "high",
        },
        "status": "pending",
        "flag_reason": None,
        "proposed_action": None,
        "proposed_claim_update": None,
        "validation": None,
        "page_text_file": "claim-01.page.txt",
    }
