# Architecture

Cathedral OS separates capability from authority through a small set of execution domains.

## Domains

1. **Generation** proposes actions but does not authorize execution.
2. **Admissibility** checks whether an action has sufficient structure and permission.
3. **ActionOps** represents proposed operations as typed records.
4. **Authority** declares boundaries for actors, roles, and operations.
5. **Witness** records decisions and produces reviewable evidence.
6. **Replay** provides deterministic receipt hashing and future replay hooks.

## Minimal flow

```text
ActionOp -> AuthorityBoundary -> AdmissibilityDecision -> WitnessRecord -> Receipt Hash
```

This flow is deliberately narrow. Cathedral should earn complexity through tested evidence, not through vocabulary.

## Design constraints

- Actions must be typed before execution.
- Authority must be explicit, not inferred from capability.
- Receipts must be deterministic.
- Witness records must be reviewable by a third party.
- Narrative material must not carry execution authority.
