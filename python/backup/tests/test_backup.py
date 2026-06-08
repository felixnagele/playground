from pathlib import Path
from typing import Any

import requests
from pytest import MonkeyPatch

import backup


class FakeResponse:
    def __init__(
        self,
        payload: list[dict[str, str]],
        links: dict[str, dict[str, str]] | None = None,
    ) -> None:
        self._payload = payload
        self.links = links or {}

    def raise_for_status(self) -> None:
        return None

    def json(self) -> list[dict[str, str]]:
        return self._payload


def test_fetch_public_repos_handles_pagination(monkeypatch: MonkeyPatch) -> None:
    responses = [
        FakeResponse(
            [{"clone_url": "https://github.com/user/repo1.git"}],
            links={"next": {"url": "https://api.github.com/page2"}},
        ),
        FakeResponse(
            [
                {"clone_url": "https://github.com/user/repo2.git"},
            ]
        ),
    ]

    def fake_get(*args: Any, **kwargs: Any) -> FakeResponse:
        return responses.pop(0)

    monkeypatch.setattr(requests, "get", fake_get)

    result = backup.fetch_public_repos("user")

    expected = [
        "https://github.com/user/repo1.git",
        "https://github.com/user/repo2.git",
    ]
    if not result == expected:
        raise AssertionError(f"Expected {result} to equal {expected}")


def test_backup_repos_fails_without_sources(tmp_path: Path) -> None:
    code = backup.backup_repos(work_dir=tmp_path, username=None)
    if not code == 1:
        raise AssertionError(f"Expected code 1, got {code}")


def test_backup_repos_from_username_success(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        backup,
        "fetch_public_repos",
        lambda username: ["https://github.com/user/repo1.git"],
    )
    monkeypatch.setattr(backup, "clone_repo", lambda url, target: True)

    code = backup.backup_repos(work_dir=tmp_path, username="user")

    if not code == 0:
        raise AssertionError(f"Expected code 0, got {code}")


def test_backup_repos_reads_private_file_and_reports_failures(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    private_file = tmp_path / "backups" / "repos_private.txt"
    private_file.parent.mkdir(parents=True, exist_ok=True)
    private_file.write_text(
        "# comment line\nhttps://github.com/user/private1.git\nhttps://github.com/user/private2.git\n",
        encoding="utf-8",
    )

    cloned_urls = []

    def fake_clone(url: str, target: Path) -> bool:
        cloned_urls.append(url)
        return not url.endswith("private2.git")

    monkeypatch.setattr(backup, "clone_repo", fake_clone)

    code = backup.backup_repos(work_dir=tmp_path, username=None)

    if not len(cloned_urls) == 2:
        raise AssertionError(f"Expected 2 cloned URLs, got {len(cloned_urls)}")
    if not code == 1:
        raise AssertionError(f"Expected code 1, got {code}")
