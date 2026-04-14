#!/usr/bin/env bash
set -euo pipefail

PROJECT_PATH="${1:-}"
if [ -z "${PROJECT_PATH}" ]; then
  echo "Usage: bash .github/scripts/run_ts_lint.sh <project_path>"
  exit 2
fi

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
PROJECT_DIR="${ROOT_DIR}/${PROJECT_PATH}"
FALLBACK_CONFIG="${ROOT_DIR}/.github/eslint/default-typescript-eslint.config.mjs"

if [ ! -d "${PROJECT_DIR}" ]; then
  echo "Project path not found: ${PROJECT_DIR}"
  exit 2
fi

if [ ! -f "${FALLBACK_CONFIG}" ]; then
  echo "Fallback ESLint config missing: ${FALLBACK_CONFIG}"
  exit 2
fi

cd "${PROJECT_DIR}"

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
  echo "Using local flat ESLint config in ${PROJECT_PATH}."
  npx eslint .
  exit 0
fi

if [ "${HAS_LEGACY_CONFIG}" = true ]; then
  echo "Using local legacy ESLint config in ${PROJECT_PATH}."
  ESLINT_USE_FLAT_CONFIG=false npx eslint .
  exit 0
fi

echo "No local ESLint config found in ${PROJECT_PATH}; using fallback config."
cp "${FALLBACK_CONFIG}" .ci-eslint.fallback.config.mjs
trap 'rm -f .ci-eslint.fallback.config.mjs' EXIT
npx eslint --config .ci-eslint.fallback.config.mjs .
