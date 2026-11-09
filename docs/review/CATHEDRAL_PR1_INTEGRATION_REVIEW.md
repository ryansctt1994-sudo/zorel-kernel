# Cathedral OS PR #1 — additive integration trial

**Purpose:** test the existing Cathedral OS scaffold against the current
ZOREL main branch without changing either branch or accepting the old
scaffold's README as a replacement for current receipt disclosures.

## Pinned input references

- Current `main`: `be1e54bfa6b08f5212e2df08241239eaefe210b9`
- Cathedral scaffold PR #1: `45a74580ff37135fdfb0f8e936e29fdef51ec6c7`
- Separate offline runner PR #3: `c9ba16309196ec4ec4303cc7b023177f95ef11f4` (not included here)

This trial is a new branch based on the **main** commit above. It contains
the 24 additive file paths from PR #1, of which **23 retain identical
blob bytes**. The `docs/CONSOLIDATED_CODE_ARTIFACT_REGISTRY.md` source
used unsupported assurance wording; the candidate now describes those
thresholds and permission boundaries as proposals without implying executed
security checks. This was required by the original CI claim audit. This
is a **review-candidate documentation clarification**, not an edit to PR #1
or a `claims.json` waiver. The original exact bytes remain available on
PR #1 at the SHA above.

It is intentionally a single-parent snapshot for testing; no merge or
rebase was performed on PR #1 or PR #3.

## Reconciliation decisions used *only* in this trial

Current main versions are retained **unchanged** for the five paths that
also differ in the scaffold:

1. `.gitignore`
2. `Kernel_status.py`
3. `Metrics.py`
4. `README.md`
5. `requirements.txt`

These decisions specifically preserve main's disclosure text, including
the distinction between authorship receipts and independent reproduction,
plus the explicit placeholder status of metrics and status reporters.
The original scaffold README remains visible in PR #1 history; it was not
copied over the current README.

The scaffold's `pyproject.toml` now uses the current main README as
packaging long description. This is a **review item**, not a claim that the
mixed package identity has been reconciled. Keep main's Flask requirement
because main still contains `Metrics.py` importing Flask.

## Verification interpretation

Run the exact candidate through the existing main GitHub CI: receipt/golden
disclosure tests on Python 3.10–3.13 and the existing pinned claim auditor.
Also run scaffold's eight new tests and explicitly check that all are
collected and executed; a passing old receipt test alone does not prove the
new scaffold behavior.

The separate shock-kernel runner in PR #3 is **not** included: its default
`cathedral.shock_kernel` modules and its external witness inputs have not
been supplied or reproduced. The candidate establishes no external witness,
operational authority, deployed service, or evidence-stage promotion.

This is an integration investigation only. **DO NOT MERGE.** Before a
production branch is changed, the maintainer must separately review the
five main/scaffold differences, packaging metadata, any claim-audit result,
and the independent reproduction prerequisites.
