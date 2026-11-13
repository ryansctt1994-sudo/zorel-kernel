"""Regression: callers cannot rewrite the generator's sealed provenance template.

This tests only deterministic receipt construction and module state isolation.
It makes no authorship, signature, external-witness or E3 assurance claim.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

GENERATOR = Path(__file__).resolve().parents[1] / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
GOLDEN_HASH = "33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5"


def _isolated_generator():
    spec = importlib.util.spec_from_file_location("receipt_isolation_fixture", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_mutating_returned_receipt_cannot_change_source_template():
    gen = _isolated_generator()
    original = gen.build_receipt()
    assert original["certificate_hash"] == GOLDEN_HASH
    originals = {
        name: copy.deepcopy(getattr(gen, name))
        for name in (
            "AUTHORSHIP_MANIFEST", "FOUNDATION_FILES", "MASTER_INVARIANTS",
            "ATTESTATION", "WITNESS_SEAL",
        )
    }

    # Each nested object was returned to an ordinary caller: it is NOT
    # authorized to mutate the module's canonical template through aliases.
    original["authorship_manifest"]["declarant"]["legal_name"] = "UNTRUSTED"
    original["foundation_files"]["receipt.py"]["checksum_placeholder"] = "FAKE"
    original["master_invariants"].append("UNTRUSTED")
    original["attestation"]["timeline_evidence"][0]["work"] = "UNTRUSTED"
    original["witness_seal"]["message"] = "UNTRUSTED"

    for name, expected in originals.items():
        assert getattr(gen, name) == expected, f"returned receipt leaked mutable alias to {name}"
    fresh = gen.build_receipt()
    assert fresh["certificate_hash"] == GOLDEN_HASH
    assert fresh["authorship_manifest"]["declarant"]["legal_name"] != "UNTRUSTED"
    assert fresh["foundation_files"]["receipt.py"]["checksum_placeholder"] != "FAKE"
    assert "UNTRUSTED" not in fresh["master_invariants"]


def test_separate_receipts_have_disjoint_mutable_subtrees():
    gen = _isolated_generator()
    first = gen.build_receipt()
    second = gen.build_receipt()
    for key in ("authorship_manifest", "foundation_files", "master_invariants",
                "attestation", "witness_seal"):
        assert first[key] is not second[key], f"{key} aliases another caller's receipt"
    first["attestation"]["timeline_evidence"][0]["status"] = "UNTRUSTED"
    assert second["attestation"]["timeline_evidence"][0]["status"] != "UNTRUSTED"


def test_canonical_json_still_reproduces_original_certificate():
    gen = _isolated_generator()
    text = gen.generate_receipt_json()
    parsed = json.loads(text)
    assert parsed["certificate_hash"] == GOLDEN_HASH
    assert parsed == gen.build_receipt()
