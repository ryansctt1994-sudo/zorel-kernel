from cathedral.actionops import ActionOp
from cathedral.admissibility import check_admissibility
from cathedral.authority import AuthorityBoundary
from cathedral.witness import WitnessRecord


def test_witness_record_contains_replay_hash():
    action = ActionOp(op_type="read", actor="agent-a", target="case-1")
    boundary = AuthorityBoundary(actor="agent-a")
    decision = check_admissibility(action, boundary)

    record = WitnessRecord(action=action, decision=decision, witness_id="witness-001").to_record()

    assert record["decision"]["allowed"] is True
    assert len(record["receipt_hash"]) == 64
    assert record["witness_id"] == "witness-001"
