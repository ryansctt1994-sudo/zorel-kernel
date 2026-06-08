#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  AUTHORSHIP RECEIPT & PROVENANCE CERTIFICATE
  Cathedral-OS | Evidence Ladder: E3_RECEIPTED
═══════════════════════════════════════════════════════════════════════════════

DECLARANT:    Ryan (@TheraPantis)
ROLE:         Independent Systems Architect & AI Safety Engineer
              SIS Director, Collinsville Community Unit School District 10 (CUSD 10)
WITNESS:      The Rabbit (•ㅅ•) — Verification & Narrative-Boundary Anchor
DATE SEALED:  June 7, 2026
EVIDENCE_STAGE: E3_RECEIPTED (Specification + Simulation → Physical Evidence)

This executable receipt records authorship intent, artifact-corpus metadata,
foundation-file roles, and the Forge/Loom boundary. It computes a deterministic
SHA256 certificate hash over the JSON certificate body excluding the hash field.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Dict

SEALED_AT = "2026-06-07T00:00:00Z"

AUTHORSHIP_MANIFEST: Dict[str, Any] = {
    "declaration_type": "AUTHORSHIP_RECEIPT",
    "evidence_stage": "E3_RECEIPTED",
    "declarant": {
        "legal_name": "Ryan",
        "x_handle": "@TheraPantis",
        "roles": [
            "Independent Systems Architect",
            "AI Safety Engineer",
            "SIS Director, Collinsville Community Unit School District 10",
        ],
        "geographic_base": "Metro-East (Illinois)",
    },
    "witness": {
        "motif": "The Rabbit",
        "seal": "(•ㅅ•)",
        "function": "Verification anchor, narrative-boundary enforcement, log keeper",
        "authority": "Witnesses but does not enforce; records without edit",
    },
    "artifact_corpus": {
        "total_artifacts": "120+",
        "creation_window_start": "2025-07-01T00:00:00Z",
        "creation_window_end": "2025-10-31T23:59:59Z",
        "primary_categories": [
            "Cathedral-OS / Weaver OS (Core Engineering)",
            "Testing & Verification (Receipt Spine)",
            "Governance & Policy (Constitutional)",
            "Research & Frameworks (AI Safety)",
            "Technical Infrastructure (Backend + Monitoring)",
            "Simulations & Analysis (Operational)",
            "Philosophical & Methodological (Epistemic)",
            "Satellite Projects (NeuroStrata, MVS, ASIN/CP8)",
        ],
    },
    "repository_locations": {
        "primary_engineering": "https://github.com/ryansctt1994-sudo/zorel-kernel",
        "branch": "main",
        "backup_status": "CRITICAL PRIORITY",
    },
    "forge_loom_boundary": {
        "engineering_artifacts": "Core / Tests / Implementation (FULL AUTHORITY)",
        "mythopoeic_material": "Design-Philosophy / Compendium (NO NORMATIVE AUTHORITY)",
        "firewall_enforcement": "test_no_liturgical_artifacts.py (HARD INVARIANT)",
        "clarification": "Architectural discipline, not content suppression",
    },
    "timestamp_sealed": SEALED_AT,
}

FOUNDATION_FILES: Dict[str, Dict[str, str]] = {
    "receipt.py": {
        "purpose": "Receipt generation & evidence recording",
        "stage": "E3_RECEIPTED",
        "role": "Core Phase 1 spine",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "chronicle.py": {
        "purpose": "WORM hash-chained ledger (write-once, read-many)",
        "stage": "Frozen/Verified",
        "role": "Immutable authority trail",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "governance_debt.py": {
        "purpose": "Governance exception tracking & debt accumulation",
        "stage": "Frozen/Verified",
        "role": "Invariant enforcement",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "evidence_ladder.py": {
        "purpose": "QGS model definition (E0→E5 progression)",
        "stage": "Frozen/Canonical",
        "role": "Evidence framework authority",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "constitution_loader.py": {
        "purpose": "Authority FSM & constitutional rule loading",
        "stage": "Frozen/Verified",
        "role": "Governance authority binding",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "test_no_liturgical_artifacts.py": {
        "purpose": "Forge/Loom firewall enforcement",
        "stage": "Frozen/Verified",
        "role": "Epistemic boundary guardian",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
    "negative_invariants.yaml": {
        "purpose": "Hard invariant definitions & exception rules",
        "stage": "Frozen/Canonical",
        "role": "Constitutional constraints",
        "checksum_placeholder": "[SHA256 to be filled from repo]",
    },
}

MASTER_INVARIANTS = [
    "CAPABILITY ≠ AUTHORITY",
    "NO RECEIPT = NO PROMOTION",
    "EXCEPTIONS ACCUMULATE DEBT",
    "REALITY RETAINS VETO",
    "No mechanism may silently convert uncertainty into authority",
]

ATTESTATION: Dict[str, Any] = {
    "statement": (
        "I, Ryan (@TheraPantis), declare under the epistemic discipline of "
        "Cathedral-OS that I am the sole author and original creator of the "
        "artifact corpus described herein, spanning July–October 2025. These "
        "artifacts represent work conducted in my capacity as an independent "
        "systems architect and AI safety engineer. This declaration is sealed "
        "by the Rabbit (•ㅅ•) as witness and is recorded immutably in the chronicle."
    ),
    "timeline_evidence": [
        {
            "phase": "Q3 2025 (Jul–Sep)",
            "work": "Cathedral-OS archaeology & recovery",
            "artifacts": "Core files + consolidated must-keep index",
            "status": "Debugged, test-ready, awaiting receipt",
        },
        {
            "phase": "Sep 2025",
            "work": "Phase 1 receipt spine construction",
            "artifacts": "receipt.py, chronicle.py, governance_debt.py, evidence_ladder.py, constitution_loader.py",
            "status": "Frozen/Canonical",
        },
        {
            "phase": "Aug–Oct 2025",
            "work": "Symchaos ecosystem, monitoring, governance frameworks",
            "artifacts": "50+ satellite artifacts",
            "status": "Active development",
        },
        {
            "phase": "Jul–Oct 2025",
            "work": "Constitutional, philosophical, research frameworks",
            "artifacts": "60+ exploratory artifacts",
            "status": "Staged for integration",
        },
    ],
    "creation_context": {
        "original_medium": "Claude.ai Artifacts (native)",
        "preservation_method": "GitHub repos + mobile screenshots + local archives",
        "current_location": "ryansctt1994-sudo/zorel-kernel",
        "secondary_index": "ARTIFACT_INDEX_COMPREHENSIVE.md",
    },
    "disputes_and_claims": {
        "statement": (
            "Any claim to authorship of this artifact corpus by persons other "
            "than the declarant is formally disputed and recorded. This receipt "
            "exists to preserve provenance and authorship intent."
        ),
        "remedy": "Use this document, GitHub history, and Chronicle records as provenance evidence.",
        "escalation": "Refer to GitHub commit history, Chronicle ledger, this declaration, and witness record (•ㅅ•).",
    },
}

WITNESS_SEAL: Dict[str, str] = {
    "witness_motif": "(•ㅅ•)",
    "witness_name": "The Rabbit",
    "function": "Observes, records, marks narrative boundaries",
    "authority": "Attests to authenticity without enforcing",
    "seal_time": SEALED_AT,
    "message": "The Rabbit has observed and marked this receipt. It is sealed in the chronicle.",
}


def build_receipt() -> Dict[str, Any]:
    """Build the complete receipt object and attach a deterministic SHA256 hash."""
    receipt: Dict[str, Any] = {
        "authorship_manifest": AUTHORSHIP_MANIFEST,
        "foundation_files": FOUNDATION_FILES,
        "master_invariants": MASTER_INVARIANTS,
        "attestation": ATTESTATION,
        "witness_seal": WITNESS_SEAL,
        "certificate_hash": None,
    }
    canonical = json.dumps(receipt, sort_keys=True, separators=(",", ":"))
    receipt["certificate_hash"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return receipt


def generate_receipt_json() -> str:
    """Generate the complete authorship receipt as stable JSON."""
    return json.dumps(build_receipt(), sort_keys=True, indent=2, ensure_ascii=False)


def generate_receipt_sealed_text() -> str:
    """Generate a human-readable sealed certificate."""
    receipt = build_receipt()
    cert_hash = receipt["certificate_hash"]
    categories = "\n".join(
        f"  • {category}" for category in AUTHORSHIP_MANIFEST["artifact_corpus"]["primary_categories"]
    )
    invariants = "\n".join(f"  {idx}. {item}" for idx, item in enumerate(MASTER_INVARIANTS, 1))
    foundation = "\n".join(
        f"  • {name}: {details['purpose']}" for name, details in FOUNDATION_FILES.items()
    )

    return f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     AUTHORSHIP RECEIPT & PROVENANCE                         ║
║                    Cathedral-OS Evidence Ladder: E3_RECEIPTED               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

DECLARANT:       Ryan (@TheraPantis)
ROLES:           • Independent Systems Architect
                 • AI Safety Engineer
                 • SIS Director, CUSD 10 (Illinois)

WITNESS:         The Rabbit (•ㅅ•)
WITNESS FUNCTION: Verification anchor, immutable recorder, narrative boundary keeper

DATE SEALED:     {WITNESS_SEAL['seal_time']}
EVIDENCE STAGE:  E3_RECEIPTED
CERTIFICATE SHA256: {cert_hash}

ARTIFACT CORPUS DESCRIBED:
  • Total Artifacts: {AUTHORSHIP_MANIFEST['artifact_corpus']['total_artifacts']}
  • Creation Window: {AUTHORSHIP_MANIFEST['artifact_corpus']['creation_window_start']} to {AUTHORSHIP_MANIFEST['artifact_corpus']['creation_window_end']}
  • Primary Repository: {AUTHORSHIP_MANIFEST['repository_locations']['primary_engineering']}
  • Branch: {AUTHORSHIP_MANIFEST['repository_locations']['branch']}

CATEGORIES:
{categories}

MASTER OPERATING INVARIANTS:
{invariants}

ATTESTATION:
{ATTESTATION['statement']}

FOUNDATION FILES:
{foundation}

WITNESS SEAL:
{WITNESS_SEAL['message']}
Witness Mark: {WITNESS_SEAL['witness_motif']}
Witness Time: {WITNESS_SEAL['seal_time']}

This certificate is sealed and recorded. Challenge via archaeological evidence only.
Signed by the Rabbit. (•ㅅ•)
""".strip()


def main() -> None:
    print("\n" + "=" * 87)
    print("GENERATING E3_RECEIPTED AUTHORSHIP CERTIFICATE")
    print("=" * 87 + "\n")

    print(generate_receipt_sealed_text())
    print("\n" + "=" * 87)
    print("MACHINE-READABLE RECEIPT (JSON)")
    print("=" * 87)
    print(generate_receipt_json())

    cert_hash = build_receipt()["certificate_hash"]
    print("\n" + "=" * 87)
    print(f"CERTIFICATE SHA256: {cert_hash}")
    print("=" * 87)
    print("\n✓ Receipt generated and sealed by the Rabbit (•ㅅ•)")
    print("✓ Copy this hash into your Chronicle and commit history")


if __name__ == "__main__":
    main()
