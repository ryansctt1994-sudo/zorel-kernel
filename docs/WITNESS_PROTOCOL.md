# Witness Protocol

The witness protocol defines how a reviewer should evaluate a Cathedral OS run.

## Witness duties

A witness should verify that the repository installs from a clean checkout, the test suite passes, the example flow produces a deterministic receipt hash, the receipt is inspectable without private context, and any claimed evidence level matches the observed result.

## Minimal witness command set

```bash
python -m venv .venv
python -m pip install -e .[dev]
pytest
python examples/demo_actionop_flow.py
```

## Verdict format

```text
Repository:
Commit:
Environment:
Commands run:
Observed result:
Receipt hash:
Verdict: REPRODUCED | NOT REPRODUCED | INCONCLUSIVE
Witness:
Date:
Notes:
```

## Promotion rule

A witness verdict may support promotion only when the commands, environment, observed output, and receipt hash are recorded.
