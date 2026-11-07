"""Keep the README's "What the sealed receipt does not establish" section true.

The sealed receipt describes foundation files with placeholder checksums, and
those files are not in this repository. The README says so. These tests fail
if either fact changes without the README changing with it, so the
disclosure cannot go stale silently in either direction.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
PLACEHOLDER = "[SHA256 to be filled from repo]"


def _foundation_files() -> dict[str, dict[str, str]]:
    spec = importlib.util.spec_from_file_location("authorship_receipt", ROOT / "AUTHORSHIP_RECEIPT_E3_SEALED.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.FOUNDATION_FILES


FOUNDATION = _foundation_files()


def test_readme_discloses_placeholder_checksums():
    placeholders = [name for name, info in FOUNDATION.items() if info.get("checksum_placeholder") == PLACEHOLDER]
    assert placeholders, "no placeholder checksums left: update the README disclosure"
    assert "File checksums are placeholders" in README
    assert PLACEHOLDER in README


@pytest.mark.parametrize("name", sorted(FOUNDATION))
def test_readme_names_each_absent_foundation_file(name):
    # Hidden directories are skipped: CI checks out the claim auditor under
    # .claim-auditor/, which has its own test_no_liturgical_artifacts.py.
    present = any(
        not any(part.startswith(".") for part in path.relative_to(ROOT).parts) for path in ROOT.rglob(name)
    )
    assert not present, f"{name} is now in the repository: update the README disclosure"
    assert f"`{name}`" in README, f"README does not list {name} as absent"
