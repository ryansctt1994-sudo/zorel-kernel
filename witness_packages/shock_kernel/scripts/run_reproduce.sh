#!/usr/bin/env bash
set -euo pipefail

# Cathedral OS / shock_kernel reproduction runner
# Purpose:
#   Collect reproducibility facts for a witness.
#   This runner does NOT declare REPRODUCED.
#   The witness receipt and signature determine the verdict.

# ---------------------------------------------------------------------
# PRECONDITION — must happen before this script is run:
#
# 1. Witness obtains release package and signed digest/checksum file.
# 2. Witness verifies signature out-of-band:
#
#      gpg --verify SHA256SUMS.txt.asc SHA256SUMS.txt
#      sha256sum -c SHA256SUMS.txt
#
#    or equivalent cosign/minisign verification.
#
# 3. Only after the authenticated package digest matches may the witness
#    unpack the package and run this script.
#
# This script verifies package-local integrity after unpacking, but the
# external trust anchor is the signed release digest, not the internal
# manifest.
# ---------------------------------------------------------------------

export TZ=UTC
export LC_ALL=C
export LANG=C
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-0}"

export PIP_NO_INDEX=1
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PYTHONDONTWRITEBYTECODE=1

SEEDS=("0" "1" "42" "1337")
ROOT_MODULE="${ROOT_MODULE:-cathedral.shock_kernel.core}"
LEDGER_MODULE="${LEDGER_MODULE:-cathedral.shock_kernel.ledger}"
EXPECTED_RESULTS="${EXPECTED_RESULTS:-EXPECTED_RESULTS.json}"
PACKAGE_MANIFEST="${PACKAGE_MANIFEST:-PACKAGE_MANIFEST.sha256}"
VENDOR_MANIFEST="${VENDOR_MANIFEST:-vendor/MANIFEST.sha256}"
LOCKFILE="${LOCKFILE:-requirements.lock}"
RECEIPTS_DIR="${RECEIPTS_DIR:-receipts}"

mkdir -p "${RECEIPTS_DIR}"

log() {
  printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "${RECEIPTS_DIR}/run_reproduce.log"
}

hash_file() {
  sha256sum "$1" | awk '{print $1}'
}

require_file() {
  if [ ! -f "$1" ]; then
    echo "ERROR: required file missing: $1" >&2
    exit 1
  fi
}

require_dir() {
  if [ ! -d "$1" ]; then
    echo "ERROR: required directory missing: $1" >&2
    exit 1
  fi
}

log "phase 0: checking required files and directories"

require_file "${EXPECTED_RESULTS}"
require_file "${PACKAGE_MANIFEST}"
require_file "${LOCKFILE}"
require_file "${VENDOR_MANIFEST}"
require_dir "vendor"
require_dir "src"
require_dir "tests"

log "phase 0: rejecting placeholder expected results"

python - <<'PY'
import json
import sys
from pathlib import Path

path = Path("EXPECTED_RESULTS.json")
data = json.loads(path.read_text(encoding="utf-8"))

serialized = json.dumps(data, sort_keys=True)
bad_markers = [
    "<INSERT_",
    "INSERT_",
    "TODO",
    "TBD",
    "PLACEHOLDER",
    "REPLACE_ME",
    "sha256:<FULL_HASH>",
]

found = [m for m in bad_markers if m in serialized]
if found:
    print(f"ERROR: EXPECTED_RESULTS.json still contains placeholders: {found}", file=sys.stderr)
    sys.exit(1)

policy = data.get("comparison_policy", {})
if policy.get("full_digest_comparisons_only") is not True:
    print("ERROR: full_digest_comparisons_only must be true", file=sys.stderr)
    sys.exit(1)

if policy.get("prefixes_allowed_for_verdict") is not False:
    print("ERROR: prefixes_allowed_for_verdict must be false", file=sys.stderr)
    sys.exit(1)

print("EXPECTED_RESULTS.json has no placeholders and enforces full-digest comparisons")
PY

log "phase 0: verifying package-local manifest before mutation"

sha256sum -c "${PACKAGE_MANIFEST}" 2>&1 | tee "${RECEIPTS_DIR}/phase0_package_manifest.log"

log "phase 0: verifying vendored wheel manifest"

sha256sum -c "${VENDOR_MANIFEST}" 2>&1 | tee "${RECEIPTS_DIR}/phase0_vendor_manifest.log"

log "phase 0: recording static artifact hashes"

{
  echo "EXPECTED_RESULTS.sha256=$(hash_file "${EXPECTED_RESULTS}")"
  echo "PACKAGE_MANIFEST.sha256=$(hash_file "${PACKAGE_MANIFEST}")"
  echo "VENDOR_MANIFEST.sha256=$(hash_file "${VENDOR_MANIFEST}")"
  echo "requirements.lock.sha256=$(hash_file "${LOCKFILE}")"
} | tee "${RECEIPTS_DIR}/static_hashes.txt"

log "phase 1: creating virtual environment"

python -m venv .venv

if [ ! -f ".venv/bin/activate" ]; then
  echo "ERROR: virtualenv activation script missing: .venv/bin/activate" >&2
  exit 1
fi

# shellcheck disable=SC1091
. .venv/bin/activate

log "phase 1: recording python and pip versions"

{
  echo "python_executable=$(command -v python)"
  echo "python_version=$(python --version 2>&1)"
  echo "pip_version=$(python -m pip --version 2>&1)"
} | tee "${RECEIPTS_DIR}/python_pip_versions.txt"

log "phase 1: installing offline hash-locked dependencies from vendored wheelhouse"

python -m pip install \
  --no-index \
  --find-links vendor \
  --require-hashes \
  --no-deps \
  -r "${LOCKFILE}" \
  2>&1 | tee "${RECEIPTS_DIR}/pip_install.log"

log "phase 1: installing local package without dependency resolution"

python -m pip install -e . --no-deps \
  2>&1 | tee "${RECEIPTS_DIR}/pip_editable_install.log"

log "phase 1: recording dependency state"

python -m pip freeze --all 2>&1 | tee "${RECEIPTS_DIR}/pip_freeze.log"
python -m pip check 2>&1 | tee "${RECEIPTS_DIR}/pip_check.log"

log "phase 2: running pytest seed matrix"

for seed in "${SEEDS[@]}"; do
  log "pytest run with PYTHONHASHSEED=${seed}"
  PYTHONHASHSEED="${seed}" pytest \
    2>&1 | tee "${RECEIPTS_DIR}/pytest_seed_${seed}.log"
done

log "phase 2: running root seed matrix through installed module path"

for seed in "${SEEDS[@]}"; do
  log "root emission with PYTHONHASHSEED=${seed}"
  PYTHONHASHSEED="${seed}" python -m "${ROOT_MODULE}" --emit-root-only \
    2>&1 | tee "${RECEIPTS_DIR}/root_seed_${seed}.log"
done

log "phase 2: running ledger seal through installed module path"

PYTHONHASHSEED=0 python -m "${LEDGER_MODULE}" --seal \
  2>&1 | tee "${RECEIPTS_DIR}/seal.log"

log "phase 2: comparing observed roots to EXPECTED_RESULTS.json"

python - <<'PY'
import json
import re
import sys
from pathlib import Path

expected = json.loads(Path("EXPECTED_RESULTS.json").read_text(encoding="utf-8"))

roots = expected.get("expected_roots", {})
expected_published = roots.get("published_root_sha256")
expected_sealed = roots.get("sealed_integrity_root_sha256")

if not expected_published or not re.fullmatch(r"[0-9a-fA-F]{64}", expected_published):
    print("ERROR: expected published_root_sha256 missing or not full SHA-256", file=sys.stderr)
    sys.exit(1)

if not expected_sealed or not re.fullmatch(r"[0-9a-fA-F]{64}", expected_sealed):
    print("ERROR: expected sealed_integrity_root_sha256 missing or not full SHA-256", file=sys.stderr)
    sys.exit(1)

seed_values = ["0", "1", "42", "1337"]
observed = {}

for seed in seed_values:
    path = Path("receipts") / f"root_seed_{seed}.log"
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    candidates = re.findall(r"\b[0-9a-fA-F]{64}\b", text)
    if not candidates:
        print(f"ERROR: no full SHA-256 root found in {path}", file=sys.stderr)
        sys.exit(1)
    observed_root = candidates[-1].lower()
    observed[seed] = observed_root
    if observed_root != expected_published.lower():
        print(
            f"ERROR: root mismatch for seed {seed}: expected {expected_published}, observed {observed_root}",
            file=sys.stderr,
        )
        sys.exit(1)

seal_text = Path("receipts/seal.log").read_text(encoding="utf-8", errors="replace")
seal_candidates = re.findall(r"\b[0-9a-fA-F]{64}\b", seal_text)
if not seal_candidates:
    print("ERROR: no full SHA-256 sealed root found in receipts/seal.log", file=sys.stderr)
    sys.exit(1)

observed_seal = seal_candidates[-1].lower()
if observed_seal != expected_sealed.lower():
    print(
        f"ERROR: sealed root mismatch: expected {expected_sealed}, observed {observed_seal}",
        file=sys.stderr,
    )
    sys.exit(1)

Path("receipts/observed_roots.json").write_text(
    json.dumps(
        {
            "observed_seed_roots": observed,
            "observed_sealed_integrity_root": observed_seal,
            "all_full_digest_comparisons_passed": True,
        },
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)

print("All observed roots match expected full digests")
PY

log "phase 3: collecting environment facts"

{
  echo "date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "uname=$(uname -a)"
  echo "python=$(python --version 2>&1)"
  echo "pip=$(python -m pip --version 2>&1)"
  echo "TZ=${TZ}"
  echo "LC_ALL=${LC_ALL}"
  echo "LANG=${LANG}"
  echo "SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH}"
  echo "PIP_NO_INDEX=${PIP_NO_INDEX}"
  echo "PYTHONDONTWRITEBYTECODE=${PYTHONDONTWRITEBYTECODE}"
  echo "ROOT_MODULE=${ROOT_MODULE}"
  echo "LEDGER_MODULE=${LEDGER_MODULE}"
} | tee "${RECEIPTS_DIR}/environment.txt"

log "phase 3: hashing receipt byproducts"

find "${RECEIPTS_DIR}" -type f ! -name "byproducts.sha256" -print0 \
  | sort -z \
  | xargs -0 sha256sum \
  | tee "${RECEIPTS_DIR}/byproducts.sha256"

log "phase 3: writing fact summary"

cat > "${RECEIPTS_DIR}/FACTS_ONLY_SUMMARY.txt" <<'EOF'
This runner completed without declaring a witness verdict.

Facts collected:
- package-local manifest verification completed
- vendored wheel manifest verification completed
- offline dependency install completed
- local editable install completed without dependency resolution
- pytest seed matrix completed
- root seed matrix completed
- sealed root comparison completed
- full-digest comparisons completed
- environment facts collected
- byproduct hashes collected

This file is not a witness receipt.
This file does not declare REPRODUCED.
A signed human witness receipt is required for E3.5.
2-of-3 signed independent reproductions are required for E4.
EOF

log "done: reproduction facts collected"
log "done: runner does not declare REPRODUCED"
log "next: witness completes and signs WITNESS_RECEIPT_TEMPLATE.json"
