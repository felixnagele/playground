from unittest.mock import MagicMock
import pytest
import requests
from pytest import CaptureFixture, MonkeyPatch


def test_github_api_minimal(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.status_code = 200
    mock_response.json.return_value = {"foo": "bar"}

    monkeypatch.setattr(requests, "get", lambda url, **kwargs: mock_response)

    try:
        response = requests.get("https://api.github.com", timeout=10)
        if response.ok:
            data = response.json()
            print("GitHub API Root Endpoints:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print(f"Error: Failed to fetch GitHub API (Status {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error occurred - {e}")

    captured = capsys.readouterr()
    assert "GitHub API Root Endpoints:" in captured.out
    assert "foo: bar" in captured.out
