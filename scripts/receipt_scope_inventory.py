#!/usr/bin/env python3
"""Inspect the *present* receipt package without promoting its evidence stage.

The sealed certificate and legacy E3_RECEIPTED label are unchanged.
SHA-256 hashes printed here describe current local files; they are not
independent witness attestations, signatures, or runtime validation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
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


def build_inventory(root: Path) -> dict:
    root = root.resolve()
    manifest = json.loads((root / "RECEIPT_MANIFEST_E3.json").read_text(encoding="utf-8"))

    generator_path = root / "AUTHORSHIP_RECEIPT_E3_SEALED.py"
    spec = importlib.util.spec_from_file_location("zorel_authorship_receipt", generator_path)
    if spec is None or spec.loader is None:
        raise ValueError("Unable to load the original receipt generator.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    recomputed = module.build_receipt()["certificate_hash"]
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
    for name, info in sorted(module.FOUNDATION_FILES.items()):
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
