"""Authority boundary checks for Cathedral OS."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AuthorityBoundary:
    """Declares which authority levels an actor may exercise."""

    actor: str
    allowed_authorities: frozenset[str] = field(default_factory=lambda: frozenset({"standard"}))

    def permits(self, authority: str) -> bool:
        return authority in self.allowed_authorities
