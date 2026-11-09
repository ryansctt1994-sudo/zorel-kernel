# Invariants

Cathedral OS starts from these invariants.

## I1 — Capability is not authority

An actor may be capable of producing an action without being authorized to execute it.

## I2 — No silent promotion

No action, artifact, result, or claim may move to a higher evidence level without an explicit receipt.

## I3 — Typed actions before execution

A proposed action must declare its type, actor, target, payload, and required authority.

## I4 — Boundary checks before execution

Authority boundaries must be checked before an operation is treated as admissible.

## I5 — Receipts must be deterministic

Two equivalent records must produce the same canonical receipt hash.

## I6 — Witness records must be inspectable

A third party should be able to inspect the action, decision, witness identifier, and receipt hash without relying on private context.

## I7 — Story is not authority

Historical, symbolic, or interpretive material may explain the project, but it must not authorize execution.
