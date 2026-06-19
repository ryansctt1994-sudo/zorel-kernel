"""Admissibility checks for typed actions."""

from dataclasses import dataclass

from cathedral.actionops import ActionOp
from cathedral.authority import AuthorityBoundary


@dataclass(frozen=True)
class AdmissibilityDecision:
    allowed: bool
    reason: str


def check_admissibility(action: ActionOp, boundary: AuthorityBoundary) -> AdmissibilityDecision:
    """Return whether an action is admissible under an authority boundary."""

    try:
        action.validate_shape()
    except ValueError as exc:
        return AdmissibilityDecision(False, f"invalid_action_shape: {exc}")

    if action.actor != boundary.actor:
        return AdmissibilityDecision(False, "actor_boundary_mismatch")

    if not boundary.permits(action.authority_required):
        return AdmissibilityDecision(False, "authority_not_granted")

    return AdmissibilityDecision(True, "admissible")
