# ABOUTME: Fixtures for scripts/ linter tests; loads the hyphen-named linter
# ABOUTME: scripts as importable modules via importlib.
import importlib.util
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1]


def _load(script_name):
    spec = importlib.util.spec_from_file_location(
        script_name.replace("-", "_"), SCRIPTS / f"{script_name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def vs():
    return _load("verify-sources")


@pytest.fixture(scope="session")
def ccl():
    return _load("check-citation-links")
