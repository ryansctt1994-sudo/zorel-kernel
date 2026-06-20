# Cathedral OS

Cathedral OS is a governed execution architecture for AI systems.

Its core principle is simple:

> Capability is not authority.

Cathedral separates generation from execution through admissibility checks, typed actions, witness records, replay verification, and authority boundaries.

The goal is not faster automation.  
The goal is safer, auditable, replay-verifiable execution.

**Tagline:** Governed execution for systems where being wrong is expensive.

## Status

This repository is an early, evidence-first scaffold. It defines the package shape, core invariants, minimal executable primitives, reproduction scripts, and tests required to move from concept to independently reviewable implementation.

Current evidence level: **E1/E2 scaffold**

This repository does not claim production assurance, formal verification, independent audit, or operational safety certification. Promotion requires receipts, tests, replay evidence, and witness review.

## Repository layout

```text
cathedral-os/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
├── pyproject.toml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── INVARIANTS.md
│   ├── EVIDENCE_LADDER.md
│   ├── WITNESS_PROTOCOL.md
│   └── ROADMAP.md
├── src/
│   └── cathedral/
│       ├── __init__.py
│       ├── admissibility/
│       ├── actionops/
│       ├── witness/
│       ├── replay/
│       └── authority/
├── tests/
│   ├── test_admissibility.py
│   ├── test_actionops.py
│   ├── test_replay.py
│   └── test_witness.py
├── examples/
│   └── demo_actionop_flow.py
├── receipts/
│   └── README.md
└── scripts/
    ├── run_reproduce.sh
    └── verify_package.sh
```

## Install

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

## Reproduce

```bash
bash scripts/run_reproduce.sh
```

Expected result:

```text
pytest passes
package metadata imports
example action operation emits a replay-verifiable receipt
```

## Core concepts

Cathedral OS treats an AI action as inadmissible until the system can show:

1. the requested operation is typed;
2. the authority boundary permits it;
3. the admissibility check passes;
4. the action record is witnessed;
5. the resulting receipt can be replayed or independently inspected.

## Non-goals

Cathedral OS is not a chatbot framework, agent personality layer, prompt library, or mythology repository. Narrative history belongs outside the main execution path. The main repository is for implementation, tests, documentation, receipts, and reproducibility.

## License

MIT.
