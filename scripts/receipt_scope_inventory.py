#!/usr/bin/env python3
"""Inspect the *present* receipt package without promoting its evidence stage.

The sealed certificate and legacy E3_RECEIPTED label are unchanged.
SHA-256 hashes printed here describe current local files; they are not
independent witness attestations, signatures, or runtime validation.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_file(root: Path, value: str) -> Path | None:
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        return None
    candidate = root / relative
    # Reject symlinked artifacts, including links through parent directories,
    # and paths that escape the selected checkout.
    resolved = candidate.resolve(strict=False)
    if not resolved.is_relative_to(root) or resolved != candidate:
        return None
    return candidate



# The sealed generator is data for this audit; never import or execute it.
# This narrow parser handles the project's frozen literal declarations only.
_DECLARATIONS = (
    "SEALED_AT",
    "AUTHORSHIP_MANIFEST",
    "FOUNDATION_FILES",
    "MASTER_INVARIANTS",
    "ATTESTATION",
    "WITNESS_SEAL",
)


def _literal(node: ast.AST, declared: dict):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in declared:
        return declared[node.id]
    if isinstance(node, ast.Dict):
        return {
            _literal(k, declared): _literal(v, declared)
            for k, v in zip(node.keys, node.values)
        }
    if isinstance(node, (ast.List, ast.Tuple)):
        result = [_literal(item, declared) for item in node.elts]
        return tuple(result) if isinstance(node, ast.Tuple) else result
    raise ValueError("Receipt declaration contains a nonliteral expression.")


def _parse_receipt_declarations(path: Path) -> dict:
    try:
        syntax = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeError) as exc:
        raise ValueError("Unparseable receipt declarations.") from exc

    declared = {}
    for node in syntax.body:
        name = None
        value = None
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name, value = node.target.id, node.value
        elif (isinstance(node, ast.Assign) and len(node.targets) == 1
              and isinstance(node.targets[0], ast.Name)):
            name, value = node.targets[0].id, node.value
        if name in _DECLARATIONS:
            if name in declared or value is None:
                raise ValueError("Duplicate or invalid receipt declaration: " + name)
            declared[name] = _literal(value, declared)

    if set(declared) != set(_DECLARATIONS):
        raise ValueError("Missing frozen receipt declarations.")
    return declared


def _declared_certificate_digest(declared: dict) -> str:
    # Reproduce the documented canonical receipt-data formula, not arbitrary
    # Python execution from a checked-out receipt generator.
    receipt_data = {
        "authorship_manifest": declared["AUTHORSHIP_MANIFEST"],
        "foundation_files": declared["FOUNDATION_FILES"],
        "master_invariants": declared["MASTER_INVARIANTS"],
        "attestation": declared["ATTESTATION"],
        "witness_seal": declared["WITNESS_SEAL"],
        "certificate_hash": None,
    }
    canonical = json.dumps(receipt_data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_inventory(root: Path) -> dict:
    root = root.resolve()
    manifest = json.loads((root / "RECEIPT_MANIFEST_E3.json").read_text(encoding="utf-8"))

    generator_path = _safe_file(root, "AUTHORSHIP_RECEIPT_E3_SEALED.py")
    if generator_path is None or not generator_path.is_file():
        raise ValueError("The sealed receipt source is missing or unsafe to inspect.")
    declarations = _parse_receipt_declarations(generator_path)

    recomputed = _declared_certificate_digest(declarations)
    declared = manifest["certificate_hash_sha256"]
    receipt_files = {}
    for item in manifest["receipt_files"]:
        name = item["path"]
        path = _safe_file(root, name)
        present = path is not None and path.is_file()
        receipt_files[name] = {
            "present": present,
            "sha256": _sha256_file(path) if present else None,
        }

    foundation = {}
    for name, info in sorted(declarations["FOUNDATION_FILES"].items()):
        path = _safe_file(root, name)
        present = path is not None and path.is_file()
        foundation[name] = {
            "present": present,
            "sha256": _sha256_file(path) if present else None,
            "declared_checksum": info.get("checksum_placeholder"),
            "independently_verified": False,
        }

    complete = bool(receipt_files) and all(item["present"] for item in receipt_files.values())
    metadata_check_passed = complete and declared == recomputed
    return {
        "scope": "local artifact inventory and receipt self-consistency only",
        "repository": manifest["repository"],
        "certificate_hash_declared": declared,
        "certificate_hash_recomputed": recomputed,
        "certificate_hash_matches": declared == recomputed,
        "generator_executed": False,
        "generator_declarations_parsed_statically": True,
        "receipt_files": receipt_files,
        "receipt_files_all_present": complete,
        "foundation_files": foundation,
        "foundation_files_missing": sorted(k for k, v in foundation.items() if not v["present"]),
        # Presence and agreement of self-reported metadata are NOT
        # content authentication: the receipt has no independent signed
        # per-file digest baseline and the generator is part of the checkout.
        "receipt_metadata_check_passed": bool(metadata_check_passed),
        "receipt_contents_authenticated": False,
        "independent_reproduction": False,
        "runtime_correctness": "NOT_ESTABLISHED",
        "operational_authority": "NONE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    inventory = build_inventory(args.root)
    print(json.dumps(inventory, indent=2, sort_keys=True))
    return 0 if inventory["receipt_metadata_check_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
