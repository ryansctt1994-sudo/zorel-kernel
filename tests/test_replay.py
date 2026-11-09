from cathedral.replay import canonical_json, canonical_receipt_hash


def test_canonical_json_is_order_stable():
    left = {"b": 2, "a": 1}
    right = {"a": 1, "b": 2}

    assert canonical_json(left) == canonical_json(right)


def test_receipt_hash_is_order_stable():
    left = {"b": 2, "a": 1}
    right = {"a": 1, "b": 2}

    assert canonical_receipt_hash(left) == canonical_receipt_hash(right)
