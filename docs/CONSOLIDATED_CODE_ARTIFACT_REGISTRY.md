# Consolidated Code and Artifact Registry

Registry status: ACTIVE FOR REVIEW
Source state: Cathedral OS / Weaver Ecosystem consolidation from 2026-06-20
Repository branch: cathedral-os-scaffold
Evidence posture: preservation record only
Authority posture: non-authority-bearing

This document records names, evidence levels, artifacts, receipts, hashes, promotion boundaries, and frozen next-step sequencing for the Cathedral OS / Weaver Ecosystem. It is a registry, not a receipt. It does not promote the repository, the ecosystem, or any subsystem beyond its earned evidence level.

Core lock:

```text
No execution -> no receipt.
No receipt -> no authority.
No external witness -> no E3.5 / E4.
No promotion from prose.
```

## 1. Evidence and promotion codes

| Code | Meaning |
|---|---|
| E0 | Frozen spec / no measurement earned |
| E1 | Local diagnostic or interface scaffold |
| E2 | Coherent local implementation / scaffold / architecture |
| E2+ | Local reproduction package or locally tested witness package |
| E3 | Independent replay against pinned expected outputs |
| E3.5 | One signed independent reproduction |
| E4 | 2-of-3 signed independent witnesses |
| E5 | Sustained operational evidence |

Current global state:

| Component | Current evidence state |
|---|---|
| Cathedral OS / Weaver Ecosystem | E2 architectural consolidation / promotion locked |
| HudsonDriftAI_Patched_v5 + witness package | E2+ local |
| CI baseline restoration handoff | E1 local, not authority-bearing |
| CANON-OS + Weaver C11-C15 integration | E0 frozen spec |
| TriWeavon | E1/E2 claimed artifact, unverified package |
| Lucifer Latch | E2-sim candidate |
| Shock v1 | Pending finalized tests/fuzz/reproduction |

## 2. Constitutional codes and laws

- Capability is not authority.
- Vocabulary is not implementation.
- No Boundary. No Receipt. No Authority.
- Reality retains veto.
- Legitimacy is recomputed, never assumed.
- Specification is not implementation.
- Declared success is not replay-verified success.
- Architecture is not authority.

Promotion lock:

```text
No execution -> no receipt.
No receipt -> no authority.
No external witness -> no E3.5 / E4.
```

## 3. CANON-OS operators

| Operator | Role |
|---|---|
| The Chronicle | Provenance, custody, version history, memory |
| The Guardian | Thresholds, boundaries, permissions, safe crossing |
| Aphooph | Destructive collapse of distinctions |
| Harmonia | Preservation of necessary incompleteness |
| The Empty Chair | Absent witness / future participant |
| The Sacred Gap | Unclaimable future / unresolved space |
| The Cathedral | Unfinished living structure |
| The Forge | Execution, recomputation, hardware/ledger verification |
| The Loom | Creative, symbolic, unresolved, non-operational layer |
| Sanctuary | Sandbox for ambiguity / non-authority-bearing exploration |

## 4. Weaver / Forge / GEOMATRIA split

| Layer | Function |
|---|---|
| CANON-OS | Epistemic / provenance / constitutional vocabulary |
| Weaver's Covenant | Semantic and constitutional dual-lane governance |
| GEOMATRIA | Claim-boundary and structural compression discipline |
| The Forge | Execution and recomputation from primary states |
| The Loom | Creative semantic layer with no execution authority |

Core rule:

```text
Compute, do not trust.
Model-emitted text is raw input until recomputed or verified.
```

## 5. C11-C15 invariant expansion

| Code | Meaning | Status |
|---|---|---|
| C11 | Model Assumptions Drift | E0_NOT_EARNED |
| C12 | Model Escape / DELTA-OMEGA | E0_NOT_EARNED |
| C13 | Verifier Capacity Exceeded | E0_NOT_EARNED |
| C14 | Residual Gaps | E0_NOT_EARNED |
| C15 | Distributional Drift Monitoring | E0_NOT_EARNED |

Default state: WITHHELD
Measurement: not earned
Operational authority: none

Associated codes:

| Code | Meaning |
|---|---|
| DELTA-OMEGA | Model escape / container boundary violation signal |
| PO-026 | Meta-refusal when verifier capacity is exceeded |
| RED | Hardware fallback / Lucifer Latch danger state |
| WITHHELD | Passive refusal / no operational authority |

## 6. HudsonDriftAI codes

Tracked versions:

- HudsonDriftAI_Patched_v1
- HudsonDriftAI_Patched_v2
- HudsonDriftAI_Patched_v3
- HudsonDriftAI_Patched_v4
- HudsonDriftAI_Patched_v5

Key constants:

```python
SCALE = 1_000_000
HC_MASS_LOSS = 444_000
LOCK_888 = 888_000
CALM_THRESHOLD = 80_000
GOOD_TILT = 527_400
BAD_TILT = 472_600
TILT_PROB = 150_000
ALPHA = 900_000
LR_MIN = 500_000
LR_MAX = 2_500_000
```

Hudson status:

| Field | Value |
|---|---|
| Lane | Lane 1 / SPECULATIVE |
| Current version | HudsonDriftAI_Patched_v5 |
| Controller | Pure integer kernel |
| Bridge | CONDUCTOR-style transition receipt |
| Property tests | Locally reported passing |
| Witness package | Generated locally |
| External witness | Pending |
| Status | E2+ local, not E3/E4 |

Important functions and files:

- hudson_controller.py
- HudsonControllerState
- hudson_transition()
- hudson_tilt_ppm()
- grad_norm_to_ppm()
- validate_grad_norm_ppm()
- conductor_state_transition_bridge.py
- make_hudson_transition_receipt()
- hudson_conductor_step()

## 7. CONDUCTOR / a717 / kernel family

Tracked names:

- a717 execution kernel
- CONDUCTOR
- GORR
- Shock v0
- Shock v1
- Authority / Provenance scaffold
- Phi Comparator
- Cathedral Authority Suite
- CBOR witnesses
- Chronicle Gate CI
- WEAVER_OS_AUTHORITY_AUDIT
- Golden Hash/v3 54/54 claim

Current status:

```text
a717 / CONDUCTOR family: E2 architectural/local scaffold
Shock v1: pending finalized tests/fuzz/reproduction package
CBOR witnesses: scaffolded/local
External witness quorum: not earned
```

## 8. Lucifer Latch / hardware path

Tracked artifacts:

- Lucifer Latch
- Icarus simulation
- Verilator simulation
- RED fallback
- dynamic Icarus receipt

Current status:

```text
Lucifer Latch: E2-sim candidate
Dynamic Icarus/Verilator receipt: pending
Constitutional priority: highest
```

## 9. AI admission / OPA / Tekton artifacts

Uploaded or discussed artifacts:

- ai_admission.rego.txt
- ai_admission_test.rego.txt
- OPA AI admission policy
- Tekton admission pipeline
- emit-signed-audit task
- fail-if-denied task
- opa-ai-admission task
- mythos-glasswing-scan task
- jq-merge task

Policy status:

```text
Frontier critical findings: fail-closed positive terminal allow-gate
raw_critical: blocks production unless signed false-positive clearance or signed remediation
raw_high: unresolved policy decision
OPA execution: pending unless externally run
Production authority: none
```

Key frontier fields:

- scan_required
- scan_completed
- last_scan_days_ago
- raw_critical
- raw_high
- triage_status
- validated_critical
- unresolved_critical
- cleared_false_positive
- triage_record_signed
- triage_record_digest
- remediation_record_signed
- remediation_record_digest

## 10. Mythos / Glasswing / frontier model governance

Tracked names:

- Claude Mythos
- Project Glasswing
- Frontier Model Access Governance
- frontier_model_authorization
- frontier_model_scan
- frontier_model_finding
- frontier_model_triage
- frontier_model_remediation

Status:

```text
Interface defined
Tool unbound
Not deployment authority
Not runtime firewall
Not AI-SPM
Evidence role only
```

## 11. Reversal Q-Learning / offline RL governance

Tracked names:

- Reversal Q-Learning
- RQL
- offline_rl
- flow_policy
- rl_policy

Required governance fields:

- dataset_hash_verified
- reward_spec_reviewed
- critic_validated
- sim_validation_passed
- action_bounds_verified
- safety_envelope_attached
- real_world_rollout_approved

Core rule:

```text
Better offline RL performance is not safe autonomy.
```

## 12. Representation governance

Tracked names and fields:

- Aristotelian Representation Hypothesis
- representation_alignment
- local_neighborhood_alignment
- width_depth_bias_corrected
- permutation_null_calibration
- global_similarity_only
- knn_overlap_at_10
- recall_at_20_delta
- ranking_tau
- cross_modal_neighborhood_agreement

Core rule:

```text
Local correspondence is useful evidence.
Global similarity is not functional equivalence.
```

## 13. TriWeavon extension

Tracked names:

- TriWeavon
- Chrome MV3 extension
- ws://127.0.0.1:8088
- Cloudflare AI Vectorize
- tab handoff tracking
- browser lag/cache optimization
- local WebSocket bridge

Status:

```text
Claimed artifact
Package not inspected
Evidence: E1/E2 claim
Production-grade claim: not accepted
Next step: upload ZIP/source + manifest + hashes + local test receipt
```

## 14. CI baseline restoration handoff artifacts

Uploaded artifacts:

- SHA256SUMS.txt
- README.md
- CI_BASELINE_RESTORATION_RECEIPT.json
- ci-baseline-restoration-a7d07ac.bundle
- 0001-Restore-CI-baseline-verifier-boundary-ordering-fixtu.patch
- ci-baseline-restoration-handoff-a7d07ac.tar.gz

Verified uploaded hashes:

| Artifact | SHA-256 |
|---|---|
| patch | 4076841f5f83fa772334f0724a6e63127ab025e8b4855ad9195ca473165daf2b |
| bundle | 54a1fe6a3c5ca0c01a3269d099fe4823a3c2a1090215f95e293b01fc76a29359 |
| receipt | a665b7b5158cd03406d690c94d46411de9423e4ab42e2fa3fe02697be881decf |
| README | e2be2e0aada4fbbbba01b2210796ac66d16a9454004af902c81f003a0336d45f |
| ci-baseline-restoration-handoff-a7d07ac.tar.gz | b1bcb3de591ad6922100405f19c11275f6d718a14fc01520b01cbd36b46261a0 |

README restriction:

```text
The package is not a promotion receipt.
The package is not externally witnessed.
The package is not authority-bearing.
Only PR CI green on GitHub restores the repo baseline.
```

Receipt status:

```text
receipt_type: CI_BASELINE_RESTORATION_RECEIPT
evidence_label: E1_LOCAL_CI_GREEN_BASELINE
authority_bearing: false
promotion: false
external_witness: false
parent_commit: b6b76f1
repair_commit: a7d07aca6f95e09010e0ddd928690158cc95ddd9
```

Recorded gate classes:

- ruff
- mypy
- pytest
- build
- CLI smoke

## 15. Repo / CI codes

| Code or branch | Meaning |
|---|---|
| b6b76f1 | Parent baseline commit |
| a7d07ac | CI baseline restoration repair commit |
| 190d6c3 | Later receipt commit, not included in patch range |
| fix/ci-baseline-restoration | Restoration branch |
| weaver/ddm-simulation-harness-e0 | Future harness branch, frozen until PR CI green |

Gate commands:

```bash
ruff check .
mypy triadic_controls src
pytest -q
python -m build
weaver-release-guard --help
weaver-release-guard generate --help
weaver-release-guard verify --help
```

Expected restored results:

```text
ruff: pass
mypy: pass
pytest: 56 passed
build: OK
CLI smoke: OK
```

## 16. SimulationHarness future artifact

Planned artifacts:

- SimulationHarness.py
- synthetic_ledger_fixture.json
- telemetry_noise_profile.json
- thresholds.json
- c11_assumption_drift_curve.json
- c12_escape_red_trigger.json
- c13_capacity_failure_curve.json
- c14_residual_gap_curve.json
- LOCAL_SIM_RECEIPT.json
- WITNESS_RECEIPT.template.json

Frozen rules:

```text
SimulationHarness remains frozen until:
1. CI baseline restoration PR is merged.
2. main is CI-green.
3. branch weaver/ddm-simulation-harness-e0 is cut from green main.
```

Synthetic fixture caveat:

```text
Synthetic results prove mechanical pipeline behavior only.
They do not prove detector generalization to real drift.
```

Witness attestation requirement:

```text
Ed25519 signed over:
commit_sha
fixture_digest
telemetry_window_digest
simulation_receipt_digest
test_command
observed_result
timestamp_utc
```

## 17. Priority queue

1. Apply CI baseline restoration patch to live repo.
2. Push fix/ci-baseline-restoration.
3. Open PR.
4. Confirm GitHub CI green across matrix.
5. Merge only after review.
6. Cut weaver/ddm-simulation-harness-e0 from green main.
7. Build SimulationHarness candidate branch.
8. Produce LOCAL_SIM_RECEIPT.
9. Seek external witness.
10. Resume Lucifer Latch / Shock v1 / HudsonDrift witness tracks.

## 18. Current final state

```text
Artifact registry: consolidated
CI handoff package: internally verified
Live repo baseline: pending PR CI
SimulationHarness: frozen
Promotion: locked
External witnesses: 0
```

Final kernel:

```text
Keep the registry.
Keep the codes.
Keep the artifacts.
No drift.
No promotion from prose.
Next truth: live PR CI on GitHub.
```
