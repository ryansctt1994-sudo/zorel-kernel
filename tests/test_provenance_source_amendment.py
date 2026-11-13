"""Validate a source-only amendment; never equate it with an attestation."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
AMENDMENT = ROOT / "provenance/amendments/zorel-source-amendment-pr11.json"
SCHEMA = ROOT / "provenance/schemas/source-amendment-v1.schema.json"
GOLDEN = "33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5"


def _no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for k, v in pairs:
        if k in result:
            raise ValueError("duplicate JSON member")
        result[k] = v
    return result


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_no_duplicate_keys)


def _check(value: Any, rule: dict[str, Any], schema: dict[str, Any]) -> None:
    """Exercise the closed subset of JSON Schema used by this source record."""
    if "$ref" in rule:
        assert rule["$ref"].startswith("#/$defs/")
        _check(value, schema["$defs"][rule["$ref"].split("/")[-1]], schema)
        return
    if "const" in rule:
        assert type(value) is type(rule["const"]) and value == rule["const"]
    if "enum" in rule:
        assert value in rule["enum"]
    kind = rule.get("type")
    if kind == "object":
        assert isinstance(value, dict)
        assert set(rule["required"]) <= set(value)
        if rule.get("additionalProperties") is False:
            assert set(value) <= set(rule["properties"])
        for k, v in value.items():
            if k in rule["properties"]:
                _check(v, rule["properties"][k], schema)
    elif kind == "array":
        assert isinstance(value, list)
        assert rule.get("minItems", 0) <= len(value)
        assert len(value) <= rule.get("maxItems", len(value))
        if rule.get("uniqueItems"):
            assert len({json.dumps(v, sort_keys=True) for v in value}) == len(value)
        for item in value:
            _check(item, rule["items"], schema)
    elif kind == "string":
        assert isinstance(value, str)
        assert len(value) >= rule.get("minLength", 0)
        if "pattern" in rule:
            assert re.fullmatch(rule["pattern"], value) is not None
        if rule.get("format") == "date":
            assert date.fromisoformat(value).isoformat() == value
    elif kind is not None:
        raise AssertionError(f"schema type not supported by test: {kind}")


def _assert_valid(record: dict[str, Any]) -> None:
    schema = _load(SCHEMA)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    _check(record, schema, schema)
    assert record["historical_certificate"]["sha256"] == GOLDEN
    assert record["source"]["baseline_main_commit"] == "be1e54bfa6b08f5212e2df08241239eaefe210b9"
    assert record["source"]["repair_commit"] == "764b8c7b62fbb3b40a830e918caf98a2e3d35e2f"


def test_amendment_follows_closed_schema_and_evidence_pins() -> None:
    _assert_valid(_load(AMENDMENT))


@pytest.mark.parametrize(
    ("path", "replacement"),
    [
        (("boundaries", "operational_authority"), "GRANTED"),
        (("boundaries", "independent_witness"), "ATTESTED"),
        (("review", "merge_authorization"), "APPROVED"),
        (("amendment", "historical_reseal_performed"), True),
        (("historical_certificate", "sha256"), "0" * 64),
        (("source", "repaired_git_blob_sha1"), "invalid"),
        (("evidence", "green_result"), "E3_PROMOTED"),
    ],
)
def test_false_claim_mutants_refused(path: tuple[str, ...], replacement: Any) -> None:
    mutated = copy.deepcopy(_load(AMENDMENT))
    obj = mutated
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = replacement
    with pytest.raises(AssertionError):
        _assert_valid(mutated)


def test_extra_and_missing_claims_refused() -> None:
    extra = _load(AMENDMENT)
    extra["false_external_attestation"] = True
    with pytest.raises(AssertionError):
        _assert_valid(extra)
    missing = _load(AMENDMENT)
    del missing["review"]
    with pytest.raises(AssertionError):
        _assert_valid(missing)


def test_amended_source_git_blob_matches_record() -> None:
    content = SOURCE.read_bytes()
    git_blob = hashlib.sha1(b"blob " + str(len(content)).encode("ascii") + b"\0" + content)
    record = _load(AMENDMENT)
    assert git_blob.hexdigest() == record["source"]["repaired_git_blob_sha1"]
    assert record["source"]["baseline_git_blob_sha1"] != git_blob.hexdigest()


def test_original_certificate_still_recomputes_without_resealing() -> None:
    spec = importlib.util.spec_from_file_location("source_amendment_receipt", SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    receipt = module.build_receipt()
    body = dict(receipt, certificate_hash=None)
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(canonical).hexdigest() == GOLDEN
    assert receipt["certificate_hash"] == _load(AMENDMENT)["historical_certificate"]["sha256"]
    manifest = _load(ROOT / "RECEIPT_MANIFEST_E3.json")
    assert manifest["certificate_hash_sha256"] == GOLDEN
    assert manifest["verification_expectation"]["certificate_hash_sha256"] == GOLDEN
