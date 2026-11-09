# Roadmap

## Phase 0 — Repository conversion

- Rename repository from `zorel-kernel` to `cathedral-os` in GitHub settings.
- Keep coherent ZOREL provenance artifacts as historical evidence.
- Keep the main README focused on Cathedral OS execution architecture.

## Phase 1 — E1 scaffold

- Establish package layout.
- Add typed ActionOps, authority boundaries, admissibility decisions, witness records, and replay hashing.
- Add tests and reproduction scripts.

## Phase 2 — E2 local verification

- Expand test coverage.
- Add manifest validation.
- Add deterministic fixture receipts.
- Pin expected receipt hashes.

## Phase 3 — E3 replay receipts

- Generate signed or hash-pinned reproduction receipts.
- Store receipts under `receipts/`.
- Add replay CLI.

## Phase 4 — E4 independent witness

- Prepare cold-run witness package.
- Collect external witness verdicts.
- Record independent reproduction status.

## Phase 5 — E5 operational assurance

- Add deployment evidence.
- Add production or staging replay gates.
- Track sustained evidence over time.
