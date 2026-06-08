# Consolidated Keep List

## ZOREL / Cathedral-OS / Weaver-Lumen Thread Integration

**Repository**: `ryansctt1994-sudo/zorel-kernel`  
**Branch**: `main`  
**Evidence Stage**: `E3_RECEIPTED`  
**Last Updated**: June 8, 2026  
**Witness**: The Rabbit `(•ㅅ•)`  
**Stable Certificate Hash**: `33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5`

This file is the consolidated keep-list from the current chat thread. It preserves the named artifacts, code candidates, status templates, visual materials, text assets, and newly integrated repository evidence package. It also states the authority level of each item so that reviewers can distinguish executable evidence from context, drafts, and orientation material.

## 0. Repo-Level Evidence Package Already Sealed

Keep these at repository root.

| File | Authority Level | Why Keep |
|---|---:|---|
| `AUTHORSHIP_RECEIPT_E3_SEALED.py` | `RECEIPT_EVIDENCE` | Executable E3 authorship receipt generator. Produces stable SHA256 certificate hash. |
| `AUTHORSHIP_CERTIFICATE_FORMAL.md` | `RECEIPT_EVIDENCE` | Human-readable authorship/provenance certificate. |
| `RECEIPT_MANIFEST_E3.json` | `RECEIPT_EVIDENCE` | Machine-readable manifest for the sealed receipt package. |
| `CHRONICLE_AUTHORSHIP_ENTRY.json` | `RECEIPT_EVIDENCE` | Chronicle-ready authorship event entry. |
| `ARTIFACT_INDEX_COMPREHENSIVE.md` | `RECEIPT_EVIDENCE` | Reviewer-facing artifact-corpus index. |
| `KEEP_LIST.md` | `GOVERNANCE_CONTROL` | This consolidated preservation map. |
| `README.md` | `GOVERNANCE_CONTROL` | Public repository landing page and verification path. |

Verification command:

```bash
python3 AUTHORSHIP_RECEIPT_E3_SEALED.py
```

Expected hash:

```text
33f78bde8ba348bd24d291e8b871684e85f83a2687dae393a3a86079acdfe9f5
```

## 1. Artifacts You Can Open Now

These are current local/container artifact references from the chat. They should be preserved as source artifacts and, if moved into the repo, converted into repo-relative paths under `docs/web/` or `docs/visuals/`.

### Web Handoffs

| Artifact | Current Reference | Suggested Repo Target | Authority Level | Use |
|---|---|---|---:|---|
| Cathedral Preservation Topology v1.0 — Final Professional Handoff | `container:///mnt/data/cathedral_preservation_topology_v1_web_artifact_1_2d1a7db018e7.html` | `docs/web/cathedral_preservation_topology_v1.html` | `CONTEXTUAL` | Preservation topology, reviewer orientation, archive logic. |
| Intelligence ≠ Authority: A Governance Architecture for Post-Human Cognition | `container:///mnt/data/intelligence_not_authority_position_paper_web_artifact_1_216091bc7c70.html` | `docs/web/intelligence_not_authority_position_paper.html` | `JUSTIFICATION_ONLY` | Position paper anchoring the central invariant: intelligence/capability does not imply authority. |

### Visual

| Artifact | Current Reference | Suggested Repo Target | Authority Level | Use |
|---|---|---|---:|---|
| WEAVER-LUMEN v9.0 governance visual | `container:///mnt/data/weaver_lumen_v9_governance_209962b3.jpg` | `docs/visuals/weaver_lumen_v9_governance.jpg` | `ORIENTATION_ONLY` | Governance map and reviewer visual. Not an authority source by itself. |

Important note: `container:///` references are local artifact handles, not durable public GitHub URLs. Preserve the names and import the files into the repo when the bytes are available.

## 2. STATUS.md Templates — 00 to 10

Keep one `STATUS.md` per major folder. Each status file should include: Folder, Purpose, Authority Level, Allowed Contents, Forbidden Contents, Promotion Rule, Audit Owner, and Last Reviewed.

| Template | Authority Level | Folder Role |
|---|---:|---|
| `STATUS_00_AUTHORITY_AND_REGISTRIES.md` | `GOVERNANCE_CONTROL` | Root authority declarations, registries, receipt rules, constitutional boundaries. |
| `STATUS_01_EXECUTABLE_SPINE_AND_SOURCE_CANDIDATES.md` | `CANDIDATE_SPINE` | Code that may become executable authority after tests and receipts. |
| `STATUS_02_CHRONICLE_RECEIPTS_AND_MANIFESTS.md` | `RECEIPT_EVIDENCE` | Receipts, manifests, hashes, chronicle entries, provenance records. |
| `STATUS_03_HARDWARE_AND_INTERLOCKS.md` | `PHYSICAL_CONSTRAINT` | Hardware, interlocks, deployment boundaries, physical constraints. |
| `STATUS_04_FORMAL_AND_THEORETICAL_ARCHITECTURE.md` | `JUSTIFICATION_ONLY` | Formal/theoretical models that justify design but do not execute. |
| `STATUS_05_DMSI_SYMMIND_LINEAGE.md` | `CONTEXTUAL` | DMSI, Symmind, Symchaos, cognitive-ensemble lineage. |
| `STATUS_06_EXTERNAL_AI_RESEARCH_REFERENCES.md` | `CONTEXTUAL` | External papers, model reports, AI research references, related work. |
| `STATUS_07_GOVERNANCE_AND_DEPLOYMENT.md` | `CONTEXTUAL` | Governance playbooks, deployment notes, reviewer-facing operational plans. |
| `STATUS_08_ENGINEERING_SOPs.md` | `CONTEXTUAL` | Engineering practices, SOPs, checklists, reproducibility rules. |
| `STATUS_09_SYMBOLIC_ORIENTATION_ARCHIVE.md` | `ORIENTATION_ONLY / NON_AUTHORITY` | Mythopoeic, symbolic, narrative, aesthetic, or orientation material. |
| `STATUS_10_BACKGROUND_REFERENCE.md` | `CONTEXTUAL` | Background notes, low-authority references, retained context. |

Promotion rule for all STATUS folders: no file may increase authority level without a receipt, test evidence where applicable, and an updated Chronicle/manifest entry.

## 3. Code to Keep

These entries are preserved as named code candidates from the chat. Where the keep-list source says `null`, the filename and intent are preserved, but the body is not treated as recovered or executable.

| Path | Status | Authority Level | Keep Reason | Promotion Requirement |
|---|---:|---:|---|---|
| `tests/test_insight_generation_service.ts` | Fix 1 / body not recovered in pasted keep-list | `CANDIDATE_SPINE` | Intended test for insight generation service behavior. | Recover body, run test suite, receipt results. |
| `tests/test_observability_kernel_generates_insights.ts` | Fix 2 / body not recovered in pasted keep-list | `CANDIDATE_SPINE` | Intended test that observability kernel generates insights. | Recover body, run test suite, receipt results. |
| `src/insights/insightUpdaterService.ts` | Skeleton, `SPECIFIED ONLY` | `CANDIDATE_SPINE` | Service skeleton for updating insight records. | Implement, typecheck, test, receipt. |

Current rule: these names are keep-worthy, but not yet promoted to executable authority.

## 4. Text Assets to Keep

| Asset | Authority Level | Keep Reason | Suggested Target |
|---|---:|---|---|
| LinkedIn/Threads 150-word WEAVER-LUMEN v9.0 post | `CONTEXTUAL` | Public-facing short-form articulation of the governance system. | `docs/public/weaver_lumen_v9_post.md` |
| AGI/ASI contribution essay — 8 sections on Intelligence ≠ Authority | `JUSTIFICATION_ONLY` | Long-form positioning essay connecting the architecture to AGI/ASI governance. | `docs/essays/intelligence_not_authority_agi_asi.md` |

## 5. Connections to the Rest of the Thread

### Intelligence ≠ Authority → Core Invariant

The position paper and the ZOREL/Cathedral receipt package converge on the same central claim:

```text
CAPABILITY ≠ AUTHORITY
```

This is the operational bridge between the philosophical architecture and the executable repository. A system may be intelligent, capable, or persuasive without being authorized to act. Authority requires evidence, receipts, boundary checks, and replayable validation.

### Cathedral Preservation Topology → Receipt / Chronicle Layer

The preservation topology connects directly to:

- `AUTHORSHIP_RECEIPT_E3_SEALED.py`
- `RECEIPT_MANIFEST_E3.json`
- `CHRONICLE_AUTHORSHIP_ENTRY.json`
- `ARTIFACT_INDEX_COMPREHENSIVE.md`
- this `KEEP_LIST.md`

Together, these form the archive spine: index → receipt → manifest → Chronicle entry → repository history.

### WEAVER-LUMEN v9.0 Visual → Reviewer Orientation

The governance visual should be kept as orientation material. It can help reviewers understand the system map, but it should not be treated as executable evidence. It belongs under `ORIENTATION_ONLY` unless paired with tests, receipts, or implementation.

### STATUS Templates → Authority Boundary Enforcement

The 00–10 STATUS template set is the folder-level enforcement mechanism. It prevents mixed-authority repositories where symbolic documents, theoretical models, code, receipts, and deployment instructions are blended without labels.

The strongest rule to retain:

```text
Every folder declares what kind of authority it can and cannot contain.
```

### Code Candidates → Candidate Spine Only

The TypeScript test/service files connect to the future observability and insight-generation layer. They should be preserved, but because their bodies were not present in the final keep-list, they remain `CANDIDATE_SPINE`, not verified implementation.

### LSOC / GISSE-v1 → Model-Relative Diagnostic Only

The LSOC crisis replay engine and gauge-invariant stress diagnostics are useful as a diagnostic research instrument. Their authority status should remain model-relative unless their data, code, replay scripts, and test receipts are committed.

Recommended status: `JUSTIFICATION_ONLY` or `CANDIDATE_SPINE`, depending on whether code is present.

### CVP / Constitutional Verification Program → Governance Lineage

The CVP material connects to this repo through the same evidence discipline: replayable receipts, admissibility rules, rejection records, and authority-bound promotion. It should be preserved as governance lineage and not merged into executable authority without tests.

Recommended status: `CONTEXTUAL` until implemented.

### MAI-Thinking / Frontier Data-Factory Lessons → External Research Reference

The MAI-Thinking discussion is useful because it reinforces a practical lesson for ZOREL/Cathedral: frontier-scale systems improve through disciplined data curation, evaluation hygiene, decontamination, mixture control, and hill-climbing loops. That maps cleanly to Cathedral’s receipt logic:

```text
No data/eval claim should promote without provenance, contamination checks, and recorded evidence.
```

Recommended status: `STATUS_06_EXTERNAL_AI_RESEARCH_REFERENCES.md` / `CONTEXTUAL`.

## 6. Authority Levels Used in This Keep List

| Level | Meaning |
|---|---|
| `GOVERNANCE_CONTROL` | Controls repository organization, promotion, or admissibility. |
| `RECEIPT_EVIDENCE` | Evidence-bearing receipt, manifest, hash, or Chronicle artifact. |
| `CANDIDATE_SPINE` | Code or implementation candidate not yet verified as operational authority. |
| `PHYSICAL_CONSTRAINT` | Hardware, interlock, or deployment boundary. |
| `JUSTIFICATION_ONLY` | Theoretical or argumentative support; cannot execute or authorize. |
| `CONTEXTUAL` | Useful background or lineage. |
| `ORIENTATION_ONLY / NON_AUTHORITY` | Symbolic, visual, narrative, or mythopoeic orientation only. |

## 7. Next Preservation Actions

1. Import the two HTML handoffs into `docs/web/` when source files are available.
2. Import the governance image into `docs/visuals/` when source file is available.
3. Create actual folder-level `STATUS.md` files using the 00–10 template map.
4. Recover the TypeScript test bodies before treating them as executable.
5. Add any recovered code to the manifest only after tests pass.
6. Keep symbolic/orientation assets under non-authority folders.

## 8. Final Rule

Nothing in this keep-list automatically promotes an artifact to authority. It preserves what should not be lost and labels what each item is allowed to mean.

The Rabbit witnesses. `(•ㅅ•)`
