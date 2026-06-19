import pytest

from cathedral.actionops import ActionOp


def test_actionop_to_record_is_typed():
    action = ActionOp(op_type="write", actor="agent-a", target="record-1", payload={"x": 1})

    assert action.to_record()["op_type"] == "write"
    assert action.to_record()["authority_required"] == "standard"


def test_actionop_rejects_missing_actor():
    action = ActionOp(op_type="write", actor=" ", target="record-1")

    with pytest.raises(ValueError, match="actor is required"):
        action.validate_shape()
