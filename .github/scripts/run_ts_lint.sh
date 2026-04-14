#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
FALLBACK_CONFIG="${SCRIPT_DIR}/../eslint/default-typescript-eslint.config.mjs"

# shellcheck source=.github/scripts/ts_quality_common.sh
source "${SCRIPT_DIR}/ts_quality_common.sh"

ts_init_project "${1:-}"

if [ ! -f "${FALLBACK_CONFIG}" ]; then
  echo "Fallback ESLint config missing: ${FALLBACK_CONFIG}"
  exit 2
fi

cd "${TS_PROJECT_DIR}"
ts_npm_ci
ts_npm_install_tools eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin

HAS_FLAT_CONFIG=false
HAS_LEGACY_CONFIG=false

for config_file in eslint.config.js eslint.config.mjs eslint.config.cjs eslint.config.ts; do
  if [ -f "${config_file}" ]; then
    HAS_FLAT_CONFIG=true
    break
  fi
done

for config_file in .eslintrc .eslintrc.js .eslintrc.cjs .eslintrc.json .eslintrc.yaml .eslintrc.yml; do
  if [ -f "${config_file}" ]; then
    HAS_LEGACY_CONFIG=true
    break
  fi
done

if grep -q '"eslintConfig"' package.json; then
  HAS_LEGACY_CONFIG=true
fi

if [ "${HAS_FLAT_CONFIG}" = true ]; then
  echo "Using local flat ESLint config in ${TS_PROJECT_PATH}."
  npx eslint .
  exit 0
fi

if [ "${HAS_LEGACY_CONFIG}" = true ]; then
  echo "Using local legacy ESLint config in ${TS_PROJECT_PATH}."
  ESLINT_USE_FLAT_CONFIG=false npx eslint .
  exit 0
fi

echo "No local ESLint config found in ${TS_PROJECT_PATH}; using fallback config."
cp "${FALLBACK_CONFIG}" .ci-eslint.fallback.config.mjs
trap 'rm -f .ci-eslint.fallback.config.mjs' EXIT
npx eslint --config .ci-eslint.fallback.config.mjs .
