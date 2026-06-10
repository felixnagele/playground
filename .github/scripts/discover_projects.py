#!/usr/bin/env python3
"""Discover testable Python and TypeScript projects for CI matrices."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUPPORTED_LOCKFILES: set[str] = {
    "pnpm-lock.yaml",
    "package-lock.json",
    "yarn.lock",
    "bun.lockb",
}


def detect_lockfile(project_dir: Path) -> str | None:
    for lockfile in SUPPORTED_LOCKFILES:
        if (project_dir / lockfile).exists():
            return lockfile
    return None


def discover_python_projects() -> list[str]:
    projects_root = ROOT / "python"
    projects: list[str] = []

    if not projects_root.is_dir():
        return projects

    for child in sorted(projects_root.iterdir()):
        if not child.is_dir() or child.name.startswith((".", "__")):
            continue
        if (child / "pyproject.toml").is_file():
            projects.append(child.name)

    return projects


def discover_typescript_projects() -> list[str]:
    projects_root = ROOT / "typescript"
    projects: list[str] = []
    missing_lockfile: list[str] = []

    if not projects_root.is_dir():
        return projects

    for child in sorted(projects_root.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if not (child / "package.json").is_file():
            continue

        lockfile = detect_lockfile(child)
        if lockfile:
            projects.append(child.name)
        else:
            missing_lockfile.append(child.name)

    if missing_lockfile:
        msg = (
            f"TypeScript project(s) with package.json but no supported lockfile"
            f" ({', '.join(sorted(SUPPORTED_LOCKFILES))}): {missing_lockfile}"
        )
        print(f"::warning::{msg}")

    return projects


def write_github_output(name: str, value: list[str]) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return

    with Path(output_path).open("a", encoding="utf-8") as f:
        f.write(f"{name}={json.dumps(value)}\n")


def main() -> int:
    python_projects = discover_python_projects()
    typescript_projects = discover_typescript_projects()

    print(f"Discovered Python projects: {python_projects}")
    print(f"Discovered TypeScript projects: {typescript_projects}")

    if not python_projects and not typescript_projects:
        print("::warning::No projects discovered of any language type.")

    write_github_output("python_projects", python_projects)
    write_github_output("typescript_projects", typescript_projects)

    return 0


if __name__ == "__main__":
    sys.exit(main())
