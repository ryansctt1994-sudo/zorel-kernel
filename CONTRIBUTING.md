# Contributing

Cathedral OS accepts contributions that improve governed execution, reproducibility, tests, documentation, and evidence quality.

## Contribution rules

- Keep claims bounded to available evidence.
- Add or update tests with behavior changes.
- Prefer small, reviewable pull requests.
- Do not introduce narrative or symbolic material into the execution path.
- Document new invariants, assumptions, and failure modes.

## Evidence rule

A contribution that claims improved assurance must include the evidence needed to verify that claim.

## Local checks

```bash
python -m pip install -e .[dev]
pytest
bash scripts/verify_package.sh
```
