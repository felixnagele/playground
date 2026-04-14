from collections import Counter
from typing import Any

import pytest
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

    monkeypatch.setattr(stats.requests, "get", fake_get)
    monkeypatch.setattr(stats.time, "sleep", lambda _seconds: None)

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
