# Local test reproduction record, 2026-11-12

Scope: a single local re-run of the receipt tests at two commits. It repeats what the hosted CI `receipt` job runs. It does not change the meaning of the `E3_RECEIPTED` label (authorship provenance only), it does not add an independent witness, and it does not establish any operational authority.

Who ran it: an AI coding session working in the repository owner's cloud container. Same operator and same infrastructure as the code under test.

## Environment

- Linux container, Python 3.13, pytest 8.4.2
- Command: `python -m pytest -q tests`
- Each ref was run from a clean checkout of that ref

## Results

| Ref | Result |
|---|---|
| `main` at `be1e54b` | 27 passed |
| PR #9 head `abd777e` | 35 passed |

The PR #9 head has 8 more tests than `main`. This record does not break down where they come from.

## Not covered by this record

- The `claim-audit` CI job. It needs the auditor from the `Weaver--Cathedral-` repository at a pinned commit, which was not available in this session.
- Python 3.10 to 3.12, which the hosted matrix also uses. Only 3.13 was run here.
- The seven foundation-file checksums that README.md lists as placeholders. They remain placeholders.
- Any reproduction of the offline shock experiment (PR #3).
- Any check by a party independent of the repository owner.
