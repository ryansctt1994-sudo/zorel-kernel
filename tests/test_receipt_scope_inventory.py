"""Evidence-scope checks for an unsigned *local* receipt inventory.

These tests do not upgrade the historical E3_RECEIPTED self-attestation.
"""

import json
import shutil
from pathlib import Path

import pytest

from scripts.receipt_scope_inventory import build_inventory

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def isolated_receipt(tmp_path):
    manifest = json.loads((ROOT / "RECEIPT_MANIFEST_E3.json").read_text())
    paths = {"RECEIPT_MANIFEST_E3.json", "AUTHORSHIP_RECEIPT_E3_SEALED.py"}
    paths.update(item["path"] for item in manifest["receipt_files"])
    for name in paths:
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, destination)
    return tmp_path


def test_current_receipt_is_consistent_but_has_no_operational_authority():
    result = build_inventory(ROOT)
    assert result["certificate_hash_matches"]
    assert result["receipt_files_all_present"]
    assert result["valid_receipt_package"]
    assert len(result["certificate_hash_declared"]) == 64
    assert result["independent_reproduction"] is False
    assert result["runtime_correctness"] == "NOT_ESTABLISHED"
    assert result["operational_authority"] == "NONE"


def test_all_existing_receipt_files_have_actual_sha256():
    result = build_inventory(ROOT)
    assert result["receipt_files"]
    assert all(item["present"] and len(item["sha256"]) == 64
               for item in result["receipt_files"].values())


def test_foundation_absence_and_placeholder_are_explicit():
    result = build_inventory(ROOT)
    assert result["foundation_files_missing"]
    for name in result["foundation_files_missing"]:
        assert not result["foundation_files"][name]["independently_verified"]
        assert result["foundation_files"][name]["declared_checksum"] == (
            "[SHA256 to be filled from repo]"
        )


def test_manifest_hash_mismatch_is_detected(isolated_receipt):
    path = isolated_receipt / "RECEIPT_MANIFEST_E3.json"
    data = json.loads(path.read_text())
    data["certificate_hash_sha256"] = "0" * 64
    path.write_text(json.dumps(data))
    result = build_inventory(isolated_receipt)
    assert result["certificate_hash_matches"] is False
    assert result["valid_receipt_package"] is False


def test_missing_receipt_artifact_is_detected(isolated_receipt):
    path = isolated_receipt / "ARTIFACT_INDEX_COMPREHENSIVE.md"
    path.unlink()
    result = build_inventory(isolated_receipt)
    assert not result["receipt_files_all_present"]
    assert not result["valid_receipt_package"]
    assert result["receipt_files"]["ARTIFACT_INDEX_COMPREHENSIVE.md"]["sha256"] is None
