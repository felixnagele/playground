#!/usr/bin/env bash
set -euo pipefail

TS_COMMON_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TS_REPO_ROOT="$(cd -- "${TS_COMMON_DIR}/../.." && pwd)"

TS_PROJECT_PATH=""
TS_PROJECT_DIR=""


ts_init_project() {
  local project_path="${1:-}"
  if [ -z "${project_path}" ]; then
    echo "Project path argument is required."
    exit 2
  fi

  TS_PROJECT_PATH="${project_path}"
  TS_PROJECT_DIR="${TS_REPO_ROOT}/${TS_PROJECT_PATH}"

  if [ ! -d "${TS_PROJECT_DIR}" ]; then
    echo "Project path not found: ${TS_PROJECT_DIR}"
    exit 2
  fi

  if [ ! -f "${TS_PROJECT_DIR}/package.json" ]; then
    echo "Missing package.json in project: ${TS_PROJECT_DIR}"
    exit 2
  fi
}


ts_npm_ci() {
  local ci_flags="${NPM_CI_FLAGS:---no-audit --no-fund}"
  # shellcheck disable=SC2086
  npm ci ${ci_flags}
}


ts_npm_install_tools() {
  local install_flags="${NPM_INSTALL_FLAGS:---no-audit --no-fund}"
  if [ "$#" -eq 0 ]; then
    return 0
  fi

  # shellcheck disable=SC2086
  npm install --no-save ${install_flags} "$@"
}


ts_has_test_script() {
  if ! grep -q '"test"[[:space:]]*:' package.json; then
    return 1
  fi

  if grep -Eqi '"test"[[:space:]]*:[[:space:]]*"[^"]*no[[:space:]]+test[[:space:]]+specified' package.json; then
    return 1
  fi

  return 0
}
