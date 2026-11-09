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
    assert result["receipt_metadata_check_passed"]
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
    assert result["receipt_metadata_check_passed"] is False


def test_missing_receipt_artifact_is_detected(isolated_receipt):
    path = isolated_receipt / "ARTIFACT_INDEX_COMPREHENSIVE.md"
    path.unlink()
    result = build_inventory(isolated_receipt)
    assert not result["receipt_files_all_present"]
    assert not result["receipt_metadata_check_passed"]
    assert result["receipt_files"]["ARTIFACT_INDEX_COMPREHENSIVE.md"]["sha256"] is None


def test_inventory_never_claims_authenticated_receipt_content(isolated_receipt):
    # A changed file still exists; without independent signed expected
    # digests, the tool cannot establish its content integrity.
    target = isolated_receipt / "ARTIFACT_INDEX_COMPREHENSIVE.md"
    target.write_text(target.read_text() + "\nUnverified modification\n")
    result = build_inventory(isolated_receipt)
    assert result["receipt_metadata_check_passed"]
    assert result["receipt_contents_authenticated"] is False
    assert result["independent_reproduction"] is False


def test_symlink_to_external_receipt_file_is_rejected(isolated_receipt, tmp_path):
    target = isolated_receipt / "KEEP_LIST.md"
    target.unlink()
    outside = tmp_path / "outside_receipt.txt"
    outside.write_text("external bytes")
    target.symlink_to(outside)
    result = build_inventory(isolated_receipt)
    assert result["receipt_files"]["KEEP_LIST.md"]["present"] is False
    assert result["receipt_metadata_check_passed"] is False


def test_receipt_source_is_never_executed_during_inventory(isolated_receipt, tmp_path):
    # An untrusted repository file can contain arbitrary Python. The
    # inventory must parse the declarations without running the file.
    receipt = isolated_receipt / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
    side_effect = tmp_path / "untrusted_generator_ran.txt"
    receipt.write_text(
        receipt.read_text() +
        "\nfrom pathlib import Path\nPath(" + repr(str(side_effect)) +
        ").write_text('UNSAFE_EXECUTION')\n"
    )
    result = build_inventory(isolated_receipt)
    assert result["certificate_hash_matches"]
    assert result["generator_executed"] is False
    assert result["generator_declarations_parsed_statically"] is True
    assert not side_effect.exists()


def test_mutated_literal_receipt_declaration_breaks_hash_consistency(isolated_receipt):
    receipt = isolated_receipt / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
    source = receipt.read_text()
    assert '"total_artifacts": "120+"' in source
    receipt.write_text(source.replace('"total_artifacts": "120+"', '"total_artifacts": "999+"'))
    result = build_inventory(isolated_receipt)
    assert result["certificate_hash_matches"] is False
    assert result["receipt_metadata_check_passed"] is False


def test_receipt_declaration_calls_are_rejected_without_executing(isolated_receipt, tmp_path):
    receipt = isolated_receipt / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
    marker = tmp_path / "untrusted_expression_executed.txt"
    original = 'SEALED_AT = "2026-06-07T00:00:00Z"'
    source = receipt.read_text()
    assert original in source
    malicious = "SEALED_AT = __import__('pathlib').Path(" + repr(str(marker)) + ").write_text('unsafe')"
    receipt.write_text(source.replace(original, malicious))
    with pytest.raises(ValueError, match="nonliteral"):
        build_inventory(isolated_receipt)
    assert not marker.exists()


@pytest.mark.parametrize(
    ("name", "expected_error"),
    [
        ("RECEIPT_MANIFEST_E3.json", "manifest"),
        ("AUTHORSHIP_RECEIPT_E3_SEALED.py", "receipt source"),
    ],
)
def test_primary_evidence_symlinks_outside_root_are_rejected(
    isolated_receipt, tmp_path, name, expected_error
):
    target = isolated_receipt / name
    target.unlink()
    outside = tmp_path / ("external-" + name)
    outside.write_text("{}")
    target.symlink_to(outside)
    with pytest.raises(ValueError, match=expected_error):
        build_inventory(isolated_receipt)
