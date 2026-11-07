"""Golden-hash tests for the sealed authorship receipt.

These pin the claim the README makes: running AUTHORSHIP_RECEIPT_E3_SEALED.py
reproduces certificate hash 33f78bde... and every document that quotes the
hash quotes that same value. They check reproducibility of the receipt
bytes only. They do not establish independent reproduction or any runtime
correctness (see README "Current Evidence Status").
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
GOLDEN_HASH = "33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5"
HEX64 = re.compile(r"\b[0-9a-f]{64}\b")

# Documents that quote the certificate hash. Each must quote it at least once
# and must not quote any other 64-hex value.
QUOTING_DOCS = [
    "README.md",
    "KEEP_LIST.md",
    "ARTIFACT_INDEX_COMPREHENSIVE.md",
    "RECEIPT_MANIFEST_E3.json",
    "CHRONICLE_AUTHORSHIP_ENTRY.json",
]


def _load_generator():
    spec = importlib.util.spec_from_file_location("authorship_receipt", GENERATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def gen():
    return _load_generator()


def _hash_body(body: dict) -> str:
    """The algorithm the manifest declares, reimplemented independently."""
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def test_generator_reproduces_golden_hash(gen):
    assert gen.build_receipt()["certificate_hash"] == GOLDEN_HASH


def test_hash_matches_declared_algorithm(gen):
    receipt = gen.build_receipt()
    body = dict(receipt, certificate_hash=None)
    assert _hash_body(body) == receipt["certificate_hash"]


def test_build_is_repeatable_and_does_not_mutate_inputs(gen):
    before = copy.deepcopy(gen.AUTHORSHIP_MANIFEST)
    first = gen.build_receipt()["certificate_hash"]
    second = gen.build_receipt()["certificate_hash"]
    assert first == second == GOLDEN_HASH
    assert gen.AUTHORSHIP_MANIFEST == before


@pytest.mark.parametrize("seed", ["0", "1", "4242"])
def test_hash_is_independent_of_hash_seed(seed):
    code = (
        "import importlib.util,sys;"
        f"s=importlib.util.spec_from_file_location('r',{str(GENERATOR)!r});"
        "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
        "sys.stdout.write(m.build_receipt()['certificate_hash'])"
    )
    out = subprocess.run(
        [sys.executable, "-I", "-c", code],
        env={"PYTHONHASHSEED": seed},
        capture_output=True,
        text=True,
        check=True,
    )
    assert out.stdout == GOLDEN_HASH


def test_script_output_reports_golden_hash():
    out = subprocess.run(
        [sys.executable, str(GENERATOR)], capture_output=True, text=True, check=True
    )
    assert f"CERTIFICATE SHA256: {GOLDEN_HASH}" in out.stdout


@pytest.mark.parametrize(
    "path",
    [
        ("authorship_manifest", "evidence_stage"),
        ("master_invariants", 0),
        ("witness_seal", "seal_time"),
        ("attestation", "statement"),
    ],
)
def test_any_field_change_changes_hash(gen, path):
    body = dict(copy.deepcopy(gen.build_receipt()), certificate_hash=None)
    target = body
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = str(target[path[-1]]) + " "
    assert _hash_body(body) != GOLDEN_HASH


@pytest.mark.parametrize("name", QUOTING_DOCS)
def test_documents_quote_only_the_golden_hash(name):
    text = (ROOT / name).read_text(encoding="utf-8")
    found = set(HEX64.findall(text))
    assert GOLDEN_HASH in found, f"{name} does not quote the certificate hash"
    assert found == {GOLDEN_HASH}, f"{name} quotes other hashes: {sorted(found - {GOLDEN_HASH})}"


def test_manifest_fields_agree():
    manifest = json.loads((ROOT / "RECEIPT_MANIFEST_E3.json").read_text(encoding="utf-8"))
    assert manifest["certificate_hash_sha256"] == GOLDEN_HASH
    assert manifest["verification_expectation"]["certificate_hash_sha256"] == GOLDEN_HASH


def test_chronicle_entry_agrees():
    entry = json.loads((ROOT / "CHRONICLE_AUTHORSHIP_ENTRY.json").read_text(encoding="utf-8"))
    hashes = set(HEX64.findall(json.dumps(entry)))
    assert hashes == {GOLDEN_HASH}


def test_manifest_receipt_files_exist():
    manifest = json.loads((ROOT / "RECEIPT_MANIFEST_E3.json").read_text(encoding="utf-8"))
    missing = [f["path"] for f in manifest["receipt_files"] if not (ROOT / f["path"]).is_file()]
    assert not missing, f"manifest lists files that are not in the repo: {missing}"
