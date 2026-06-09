# AGENTS.md

Personal playground monorepo. MIT License. No external contributions.

## Structure

Projects live in language-grouped root directories (`python/`, `typescript/`, etc.).
Each subdirectory is an independent project with its own config files.
No root workspace — work inside the specific project directory.

## CI/CD

GitHub Actions auto-discovers testable projects. Per-project quality gate order:
format → lint → type-check → tests. All testable projects must pass for the
pipeline to succeed.

See CI workflows (`.github/workflows/`) and the discovery script
(`.github/scripts/discover_projects.py`) for exact project detection criteria.

## Conventions

- All code, comments, config, commits, PRs: **English**. Chat may use German.
- LF line endings enforced for `.sh` files (`.gitattributes`).
- Pre-commit config is at `configs/pre-commit/` (not root).
- Review rules in `.github/copilot-instructions.md`.
