# Evidence Ladder

Cathedral OS uses evidence levels to prevent overclaiming.

## E0 — Concept

A design idea exists, but there is no executable artifact.

## E1 — Scaffold

Repository structure, documentation, and minimal code exist. Claims are architectural, not validated.

## E2 — Local verification

Tests pass locally. Deterministic behavior is demonstrated under controlled conditions.

## E3 — Replay receipt

A run produces a receipt that can be inspected and replayed against pinned expectations.

## E4 — Independent witness

An external reviewer reproduces the result without private context and signs or records a witness verdict.

## E5 — Operational assurance

The system demonstrates sustained reliability in a production or production-like environment with continuous evidence capture.

## Current status

This scaffold targets E1 and prepares the path toward E2. Any higher claim must include receipts.
