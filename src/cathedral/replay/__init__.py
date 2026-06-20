"""Replay and receipt hashing utilities."""

import hashlib
import json
from typing import Any


def canonical_json(record: dict[str, Any]) -> str:
    """Serialize a record deterministically for replay comparison."""

    return json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_receipt_hash(record: dict[str, Any]) -> str:
    """Return a deterministic SHA-256 hash for a receipt-like record."""

    return hashlib.sha256(canonical_json(record).encode("utf-8")).hexdigest()
