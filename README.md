# ZOREL-Λ Kernel — Lawful AI Architecture

Structural Sovereignty Prototype │ `RECKONING_ACTIVE` │ `Φ_g INCREASING`

This repository contains the ZOREL / Cathedral-OS kernel materials and the sealed E3 authorship receipt package for Ryan (@TheraPantis).

## Current Evidence Status

`E3_RECEIPTED`

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

The intended enforcement point is `test_no_liturgical_artifacts.py`.

## Live Endpoint

```text
GET https://<your-deploy>/metrics
```
