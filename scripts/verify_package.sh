#!/usr/bin/env bash
set -e

python -m pip install -e .[dev]
pytest
python examples/demo_actionop_flow.py
