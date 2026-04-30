from collections import Counter
import time
from typing import Any

import pytest
import requests
from pytest import CaptureFixture, MonkeyPatch

import stats


class FakeResponse:
    def __init__(
        self,
        status_code: int = 200,
        payload: list[dict[str, Any]] | dict[str, int] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self._payload = payload or []
        self.headers = headers or {}

    def json(self) -> list[dict[str, Any]] | dict[str, int]:
        return self._payload


def test_load_config_requires_real_token(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(stats, "load_dotenv", lambda: None)
    monkeypatch.setenv("TOKEN", "your_token_here")
    monkeypatch.setenv("USERNAME", "alice")

    with pytest.raises(ValueError, match="TOKEN must be set"):
        stats.load_config()


def test_get_user_languages_counts_only_owned_repos(monkeypatch: MonkeyPatch) -> None:
    repos_page_1 = [
        {
            "name": "app",
            "owner": {"login": "alice"},
            "permissions": {"admin": True},
            "languages_url": "https://api.github.com/repos/alice/app/languages",
        },
        {
            "name": "fork",
            "owner": {"login": "someone_else"},
            "permissions": {"admin": False},
            "languages_url": "https://api.github.com/repos/someone_else/fork/languages",
        },
    ]

    def fake_get(
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, int] | None = None,
    ) -> FakeResponse:
        if url.endswith("/repos"):
            if params is not None:
                page = params.get("page", 1)
                if page == 1:
                    return FakeResponse(status_code=200, payload=repos_page_1)
            return FakeResponse(status_code=200, payload=[])

        if url.endswith("/languages"):
            return FakeResponse(
                status_code=200,
                payload={"Python": 120, "HTML": 30},
                headers={"X-RateLimit-Remaining": "10", "X-RateLimit-Reset": "0"},
            )

        return FakeResponse(status_code=404, payload=[])

    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.setattr(time, "sleep", lambda _seconds: None)

    language_counter, language_repos = stats.get_user_languages(
        username="alice",
        token="token",
        include_private=True,
        exclude_repos=set(),
        only_owned=True,
    )

    assert language_counter["Python"] == 120
    assert language_counter["HTML"] == 30
    assert language_repos["Python"] == {"app"}
    assert "fork" not in language_repos["Python"]


def test_print_language_stats_handles_empty_data(capsys: CaptureFixture[str]) -> None:
    stats.print_language_stats(Counter(), {})
    captured = capsys.readouterr()
    assert "No language data found." in captured.out


def test_print_language_stats_with_data(capsys: CaptureFixture[str]) -> None:
    counter: Counter[str] = Counter({"Python": 200, "TypeScript": 100})
    repos_map: dict[str, set[str]] = {
        "Python": {"repo1", "repo2"},
        "TypeScript": {"repo1"},
    }
    stats.print_language_stats(counter, repos_map)
    captured = capsys.readouterr()
    assert "Python" in captured.out
    assert "TypeScript" in captured.out
    # Python should be first (most bytes)
    assert captured.out.index("Python") < captured.out.index("TypeScript")


def test_load_config_raises_missing_username(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(stats, "load_dotenv", lambda: None)
    monkeypatch.setenv("TOKEN", "validtoken123")
    monkeypatch.delenv("USERNAME", raising=False)

    with pytest.raises(ValueError, match="USERNAME must be set"):
        stats.load_config()


def test_get_user_languages_excludes_repos(monkeypatch: MonkeyPatch) -> None:
    repos_page_1 = [
        {
            "name": "excluded_repo",
            "owner": {"login": "alice"},
            "permissions": {"admin": True},
            "languages_url": "https://api.github.com/repos/alice/excluded_repo/languages",
        },
        {
            "name": "included_repo",
            "owner": {"login": "alice"},
            "permissions": {"admin": True},
            "languages_url": "https://api.github.com/repos/alice/included_repo/languages",
        },
    ]

    def fake_get(
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, int] | None = None,
    ) -> FakeResponse:
        if url.endswith("/repos"):
            page = params.get("page", 1) if params else 1
            if page == 1:
                return FakeResponse(status_code=200, payload=repos_page_1)
            return FakeResponse(status_code=200, payload=[])
        if url.endswith("/languages"):
            return FakeResponse(
                status_code=200,
                payload={"Python": 100},
                headers={"X-RateLimit-Remaining": "10", "X-RateLimit-Reset": "0"},
            )
        return FakeResponse(status_code=404, payload=[])

    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.setattr(time, "sleep", lambda _seconds: None)

    counter, repos_map = stats.get_user_languages(
        username="alice",
        token="token",
        include_private=True,
        exclude_repos={"excluded_repo"},
        only_owned=False,
    )

    assert "included_repo" in repos_map.get("Python", set())
    assert "excluded_repo" not in repos_map.get("Python", set())


def test_get_user_languages_raises_on_http_error(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        requests, "get", lambda *a, **kw: FakeResponse(status_code=401, payload=[])
    )

    with pytest.raises(Exception, match="HTTP status: 401"):
        stats.get_user_languages(username="alice", token="token")


def test_get_user_languages_empty_repo_list(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        requests, "get", lambda *a, **kw: FakeResponse(status_code=200, payload=[])
    )

    counter, repos_map = stats.get_user_languages(username="alice", token="token")

    assert len(counter) == 0
    assert len(repos_map) == 0
