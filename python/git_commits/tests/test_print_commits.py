from unittest.mock import MagicMock, patch

import pytest
from git import Commit, Repo

from print_commits import print_all_commits


@pytest.fixture
def mock_commit() -> MagicMock:
    commit: MagicMock = MagicMock(spec=Commit)
    commit.hexsha = "abc123fff"
    commit.author.name = "John Doe"
    commit.author.email = "john@example.com"
    commit.committed_date = 1717809600
    commit.summary = "Fix critical bug"
    commit.message = "Fix critical bug\n\nDetailed description here."
    return commit


@pytest.fixture
def mock_repo(mock_commit: MagicMock) -> MagicMock:
    repo: MagicMock = MagicMock(spec=Repo)
    repo.bare = False
    repo.iter_commits.return_value = [mock_commit]
    return repo


@patch("print_commits.Repo")
def test_print_all_commits_success(
    mock_repo_class: MagicMock, mock_repo: MagicMock
) -> None:
    mock_repo_class.return_value = mock_repo

    try:
        print_all_commits("/fake/path")
    except Exception as e:
        pytest.fail(f"Execution failed: {e}")


@patch("print_commits.Repo")
def test_print_all_commits_bare_repo(
    mock_repo_class: MagicMock, mock_repo: MagicMock, capsys: pytest.CaptureFixture[str]
) -> None:
    mock_repo.bare = True
    mock_repo_class.return_value = mock_repo

    print_all_commits("/fake/path")

    captured = capsys.readouterr()
    if "Error: Repository at '/fake/path' is bare or invalid." not in captured.out:
        raise AssertionError(f"Expected error message in {captured.out!r}")


@patch("print_commits.Repo")
def test_print_all_commits_exception_handling(
    mock_repo_class: MagicMock, capsys: pytest.CaptureFixture[str]
) -> None:
    mock_repo_class.side_effect = Exception("Git command failed")

    print_all_commits("/invalid/path")

    captured = capsys.readouterr()
    if "An error occurred: Git command failed" not in captured.out:
        raise AssertionError(f"Expected error message in {captured.out!r}")
