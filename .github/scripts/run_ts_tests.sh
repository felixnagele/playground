#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=.github/scripts/ts_quality_common.sh
source "${SCRIPT_DIR}/ts_quality_common.sh"

ts_init_project "${1:-}"

cd "${TS_PROJECT_DIR}"
ts_npm_ci

if ! ts_has_test_script; then
  echo "No tests configured for ${TS_PROJECT_PATH}, skipping test run."
  exit 0
fi

CI=true npm test
