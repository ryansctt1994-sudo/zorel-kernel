# ZOREL-Λ Kernel — Lawful AI Architecture

Structural Sovereignty Prototype

> **Evidence terminology note:** this repository's historical `E3_RECEIPTED` label names an authorship/provenance receipt package. It is **not** E3 independent reproduction under the broader Weaver portfolio evidence ladder and grants no operational authority.

This repository contains ZOREL / Cathedral-OS provenance materials and a deterministic authorship receipt package. The receipt records provenance claims; it does not certify the correctness, safety, or deployment readiness of the broader system.

## Current Evidence Status

```text
AUTHORSHIP_PROVENANCE_RECEIPT
LEGACY_LABEL: E3_RECEIPTED
INDEPENDENT_REPRODUCTION: NOT_ESTABLISHED
RUNTIME_CORRECTNESS: NOT_ESTABLISHED_BY_THIS_RECEIPT
OPERATIONAL_AUTHORITY: NONE
```

The current receipt package records authorship intent, artifact-corpus metadata, foundation-file roles, and the Forge/Loom boundary. It is designed as provenance evidence: repository history, deterministic receipt hash, formal certificate, Chronicle-ready manifest, artifact index, and consolidated keep-list.

## Sealed Receipt Package

| File | Purpose | Status |
|---|---|---|
| `AUTHORSHIP_RECEIPT_E3_SEALED.py` | Executable receipt generator; emits human-readable certificate and machine-readable JSON | Sealed |
| `AUTHORSHIP_CERTIFICATE_FORMAL.md` | Formal Markdown authorship and provenance declaration | Sealed |
| `RECEIPT_MANIFEST_E3.json` | Machine-readable manifest containing the stable certificate hash and repository metadata | Active |
| `CHRONICLE_AUTHORSHIP_ENTRY.json` | Chronicle-ready entry for the authorship receipt | Active |
| `ARTIFACT_INDEX_COMPREHENSIVE.md` | Human-readable index of the described artifact corpus and categories | Active |
| `KEEP_LIST.md` | Consolidated preservation map from the current chat thread | Active |

## Stable Certificate Hash

```text
33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5
```

This hash is produced by `AUTHORSHIP_RECEIPT_E3_SEALED.py` using a deterministic sealed timestamp of `2026-06-07T00:00:00Z`.

## Verification

Run:

```bash
python3 AUTHORSHIP_RECEIPT_E3_SEALED.py
```

Expected certificate hash:

```text
33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5
```

Then compare the hash against:

1. `RECEIPT_MANIFEST_E3.json`
2. `CHRONICLE_AUTHORSHIP_ENTRY.json`
3. `KEEP_LIST.md`
4. the GitHub commit history for this repository

Steps 1–3 are automated as golden-hash tests, which CI runs on Python 3.10–3.13:

```bash
python -m pip install "pytest>=8,<9"
python -m pytest -q tests
```

The tests check that the hash reproduces, that it doesn't depend on `PYTHONHASHSEED`, that any field edit changes it, and that every document quoting it quotes the same value. They confirm the receipt bytes reproduce. They are not independent reproduction.

## What the sealed receipt does not establish

The certificate hash covers the receipt's text exactly as written. Some of that text is a placeholder or a declaration that nothing in this repository checks:

- **File checksums are placeholders.** All seven `foundation_files` entries carry `checksum_placeholder: "[SHA256 to be filled from repo]"`. The sealed hash binds those placeholder strings, not the contents of any file.
- **The foundation files are not in this repository.** `receipt.py`, `chronicle.py`, `governance_debt.py`, `evidence_ladder.py`, `constitution_loader.py`, `test_no_liturgical_artifacts.py` and `negative_invariants.yaml` are described, with stage labels such as `Frozen/Verified`, but none of them is here. The stage labels are declarations, not results.
- **The witness is a motif, not an independent party.** "The Rabbit" (•ㅅ•) is part of the declarant's own record, so the receipt is a self-attestation.

Filling in real checksums would change the certificate hash. That makes it a new receipt with a new seal and an owner decision, not an edit to this one. The sealed receipt is left unchanged.

## Master Operating Invariants

```text
CAPABILITY ≠ AUTHORITY
NO RECEIPT = NO PROMOTION
EXCEPTIONS ACCUMULATE DEBT
REALITY RETAINS VETO
No mechanism may silently convert uncertainty into authority
```

## Forge / Loom Boundary

Engineering artifacts may carry operational authority only when verified. Mythopoeic, symbolic, narrative, or design-philosophy material may guide interpretation but carries no normative computational authority.

The intended enforcement point is `test_no_liturgical_artifacts.py`. That test is not in this repository; an implementation exists in Weaver--Cathedral- (`tests/test_no_liturgical_artifacts.py`), and nothing here runs it.

## Integration placeholder

The repository does not establish a live deployed service. If this kernel is later embedded in a service, a metrics surface could use a route such as:

```text
GET https://<your-deploy>/metrics
```

Treat that route as an integration example, not evidence of an active endpoint. `Metrics.py` and `Kernel_status.py` return fixed literals (`RECKONING_ACTIVE`, `INCREASING`, `commit_hash: "live"`); nothing in them is measured.
