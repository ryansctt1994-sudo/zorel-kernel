"""Witness records for admissible action operations."""

from dataclasses import dataclass
from typing import Any

from cathedral.actionops import ActionOp
from cathedral.admissibility import AdmissibilityDecision
from cathedral.replay import canonical_receipt_hash


@dataclass(frozen=True)
class WitnessRecord:
    """A minimal witnessable record for an action decision."""

    action: ActionOp
    decision: AdmissibilityDecision
    witness_id: str

    def to_record(self) -> dict[str, Any]:
        record = {
            "action": self.action.to_record(),
            "decision": {
                "allowed": self.decision.allowed,
                "reason": self.decision.reason,
            },
            "witness_id": self.witness_id,
        }
        record["receipt_hash"] = canonical_receipt_hash(record)
        return record
