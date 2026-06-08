from pathlib import Path

from pytest import MonkeyPatch

import check


def test_should_ignore_file_case_insensitive() -> None:
    config = {"ignored_extensions": [".png", ".JPG"]}

    if not check.should_ignore_file("image.PNG", config):
        raise AssertionError("Expected image.PNG to be ignored")
    if not check.should_ignore_file("photo.jpg", config):
        raise AssertionError("Expected photo.jpg to be ignored")
    if check.should_ignore_file("notes.txt", config):
        raise AssertionError("Expected notes.txt not to be ignored")


def test_should_skip_repo_by_name_and_absolute_path(tmp_path: Path) -> None:
    repo_dir = tmp_path / "my_repo"
    repo_dir.mkdir()

    by_name_config = {"skip_repos": ["my_repo"]}
    by_path_config = {"skip_repos": [str(repo_dir.resolve())]}

    if not check.should_skip_repo(str(repo_dir), by_name_config):
        raise AssertionError("Expected repo to be skipped by name")
    if not check.should_skip_repo(str(repo_dir), by_path_config):
        raise AssertionError("Expected repo to be skipped by path")


def test_find_repos_respects_ignored_folders(tmp_path: Path) -> None:
    repo_ok = tmp_path / "repo_ok"
    (repo_ok / ".git").mkdir(parents=True)

    ignored_repo = tmp_path / "node_modules" / "repo_ignored"
    (ignored_repo / ".git").mkdir(parents=True)

    config = {"ignored_folders": ["node_modules"]}
    repos = check.find_repos(str(tmp_path), config)

    if str(repo_ok) not in repos:
        raise AssertionError(f"Expected {repo_ok} in repos")
    if str(ignored_repo) in repos:
        raise AssertionError(f"Expected {ignored_repo} not in repos")


def test_get_committed_files_splits_output(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(check, "_run_git", lambda args, cwd: "a.py\nb.py")

    files = check.get_committed_files("dummy")

    if not files == ["a.py", "b.py"]:
        raise AssertionError(f"Expected {files} == ['a.py', 'b.py']")
