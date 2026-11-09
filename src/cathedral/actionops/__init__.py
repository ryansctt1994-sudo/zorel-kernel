"""Typed action operation records."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ActionOp:
    """A typed operation request that must pass governance before execution."""

    op_type: str
    actor: str
    target: str
    payload: dict[str, Any] = field(default_factory=dict)
    authority_required: str = "standard"

    def to_record(self) -> dict[str, Any]:
        return {
            "op_type": self.op_type,
            "actor": self.actor,
            "target": self.target,
            "payload": self.payload,
            "authority_required": self.authority_required,
        }

    def validate_shape(self) -> None:
        if not self.op_type.strip():
            raise ValueError("op_type is required")
        if not self.actor.strip():
            raise ValueError("actor is required")
        if not self.target.strip():
            raise ValueError("target is required")
        if not self.authority_required.strip():
            raise ValueError("authority_required is required")
