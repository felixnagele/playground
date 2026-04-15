#!/usr/bin/env python3
"""Discover Python and TypeScript test projects for GitHub Actions matrices."""

from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def discover_python_projects() -> list[str]:
    projects_root = ROOT / "python"
    projects: list[str] = []

    if not projects_root.exists():
        return projects

    for child in sorted(projects_root.iterdir()):
        if not child.is_dir():
            continue

        if child.name.startswith(".") or child.name.startswith("__"):
            continue

        projects.append(child.name)

    return projects


def discover_typescript_projects() -> list[str]:
    projects_root = ROOT / "typescript"
    projects: list[str] = []

    if not projects_root.exists():
        return projects

    for child in sorted(projects_root.iterdir()):
        if not child.is_dir():
            continue

        package_json_path = child / "package.json"
        lockfile_path = child / "package-lock.json"

        if not package_json_path.exists() or not lockfile_path.exists():
            continue

        projects.append(child.name)

    return projects


def write_github_output(name: str, value: list[str]) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return

    with Path(output_path).open("a", encoding="utf-8") as output_file:
        output_file.write(f"{name}={json.dumps(value)}\n")


def main() -> int:
    python_projects = discover_python_projects()
    typescript_projects = discover_typescript_projects()

    print(f"Discovered Python projects: {python_projects}")
    print(f"Discovered TypeScript projects: {typescript_projects}")

    write_github_output("python_projects", python_projects)
    write_github_output("typescript_projects", typescript_projects)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
