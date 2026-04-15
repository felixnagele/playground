#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=.github/scripts/ts_quality_common.sh
source "${SCRIPT_DIR}/ts_quality_common.sh"

ts_init_project "${1:-}"

cd "${TS_PROJECT_DIR}"
ts_npm_ci
ts_npm_install_tools prettier

npx prettier --check .
