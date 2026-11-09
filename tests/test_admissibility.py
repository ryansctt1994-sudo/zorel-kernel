from cathedral.actionops import ActionOp
from cathedral.admissibility import check_admissibility
from cathedral.authority import AuthorityBoundary


def test_admissibility_allows_permitted_action():
    action = ActionOp(op_type="read", actor="agent-a", target="case-1")
    boundary = AuthorityBoundary(actor="agent-a", allowed_authorities=frozenset({"standard"}))

    decision = check_admissibility(action, boundary)

    assert decision.allowed is True
    assert decision.reason == "admissible"


def test_admissibility_blocks_ungranted_authority():
    action = ActionOp(op_type="delete", actor="agent-a", target="case-1", authority_required="admin")
    boundary = AuthorityBoundary(actor="agent-a", allowed_authorities=frozenset({"standard"}))

    decision = check_admissibility(action, boundary)

    assert decision.allowed is False
    assert decision.reason == "authority_not_granted"


def test_admissibility_blocks_actor_boundary_mismatch():
    action = ActionOp(op_type="read", actor="agent-a", target="case-1")
    boundary = AuthorityBoundary(actor="agent-b", allowed_authorities=frozenset({"standard"}))

    decision = check_admissibility(action, boundary)

    assert decision.allowed is False
    assert decision.reason == "actor_boundary_mismatch"
