from pathlib import Path
from typing import Any
import subprocess

import backup
import requests
from pytest import MonkeyPatch


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

    assert result == [
        "https://github.com/user/repo1.git",
        "https://github.com/user/repo2.git",
    ]


def test_backup_repos_fails_without_sources(tmp_path: Path) -> None:
    code = backup.backup_repos(work_dir=tmp_path, username=None)
    assert code == 1


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

    assert code == 0


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

    assert len(cloned_urls) == 2
    assert code == 1


def test_fetch_public_repos_handles_timeout(monkeypatch: MonkeyPatch) -> None:
    def fake_get(*args: Any, **kwargs: Any) -> None:
        raise requests.exceptions.Timeout()

    monkeypatch.setattr(requests, "get", fake_get)

    result = backup.fetch_public_repos("user")

    assert result == []


def test_fetch_public_repos_handles_connection_error(monkeypatch: MonkeyPatch) -> None:
    def fake_get(*args: Any, **kwargs: Any) -> None:
        raise requests.exceptions.ConnectionError("no connection")

    monkeypatch.setattr(requests, "get", fake_get)

    result = backup.fetch_public_repos("user")

    assert result == []


def test_fetch_public_repos_handles_http_error(monkeypatch: MonkeyPatch) -> None:
    def fake_get(*args: Any, **kwargs: Any) -> FakeResponse:
        resp = FakeResponse(payload=[])

        def raise_http() -> None:
            raise requests.exceptions.HTTPError("404 Not Found")

        resp.raise_for_status = raise_http  # type: ignore[method-assign]
        return resp

    monkeypatch.setattr(requests, "get", fake_get)

    result = backup.fetch_public_repos("user")

    assert result == []


def test_clone_repo_creates_new_mirror(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    commands_run: list[list[str]] = []

    class FakeResult:
        returncode = 0
        stderr = ""

    def fake_run(cmd: list[str], **kwargs: Any) -> FakeResult:
        commands_run.append(cmd)
        return FakeResult()

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = backup.clone_repo("https://github.com/user/myrepo.git", tmp_path)

    assert result is True
    assert any("clone" in cmd for cmd in commands_run[0])


def test_clone_repo_updates_existing_mirror(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    (tmp_path / "myrepo.git").mkdir()
    commands_run: list[list[str]] = []

    class FakeResult:
        returncode = 0
        stderr = ""

    def fake_run(cmd: list[str], **kwargs: Any) -> FakeResult:
        commands_run.append(cmd)
        return FakeResult()

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = backup.clone_repo("https://github.com/user/myrepo.git", tmp_path)

    assert result is True
    assert any("remote" in cmd for cmd in commands_run[0])


def test_clone_repo_returns_false_on_failure(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    class FakeResult:
        returncode = 1
        stderr = "Authentication failed"

    monkeypatch.setattr(subprocess, "run", lambda cmd, **kwargs: FakeResult())

    result = backup.clone_repo("https://github.com/user/myrepo.git", tmp_path)

    assert result is False


def test_backup_repos_no_repos_from_username_returns_error(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(backup, "fetch_public_repos", lambda username: [])

    code = backup.backup_repos(work_dir=tmp_path, username="user")

    assert code == 1
