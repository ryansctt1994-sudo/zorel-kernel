from cathedral.actionops import ActionOp
from cathedral.admissibility import check_admissibility
from cathedral.authority import AuthorityBoundary
from cathedral.witness import WitnessRecord


def main() -> None:
    action = ActionOp(op_type="read", actor="agent-a", target="case-1", payload={"purpose": "demo"})
    boundary = AuthorityBoundary(actor="agent-a", allowed_authorities=frozenset({"standard"}))
    decision = check_admissibility(action, boundary)
    witness = WitnessRecord(action=action, decision=decision, witness_id="demo-witness")
    record = witness.to_record()

    print("Cathedral OS demo action flow")
    print(f"allowed={record['decision']['allowed']}")
    print(f"reason={record['decision']['reason']}")
    print(f"receipt_hash={record['receipt_hash']}")


if __name__ == "__main__":
    main()
