from pathlib import Path

import pytest
import check
from pytest import MonkeyPatch


def test_should_ignore_file_case_insensitive() -> None:
    config = {"ignored_extensions": [".png", ".JPG"]}

    assert check.should_ignore_file("image.PNG", config)
    assert check.should_ignore_file("photo.jpg", config)
    assert not check.should_ignore_file("notes.txt", config)


def test_should_skip_repo_by_name_and_absolute_path(tmp_path: Path) -> None:
    repo_dir = tmp_path / "my_repo"
    repo_dir.mkdir()

    by_name_config = {"skip_repos": ["my_repo"]}
    by_path_config = {"skip_repos": [str(repo_dir.resolve())]}

    assert check.should_skip_repo(str(repo_dir), by_name_config)
    assert check.should_skip_repo(str(repo_dir), by_path_config)


def test_find_repos_respects_ignored_folders(tmp_path: Path) -> None:
    repo_ok = tmp_path / "repo_ok"
    (repo_ok / ".git").mkdir(parents=True)

    ignored_repo = tmp_path / "node_modules" / "repo_ignored"
    (ignored_repo / ".git").mkdir(parents=True)

    config = {"ignored_folders": ["node_modules"]}
    repos = check.find_repos(str(tmp_path), config)

    assert str(repo_ok) in repos
    assert str(ignored_repo) not in repos


def test_get_committed_files_splits_output(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(check, "run_cmd", lambda cmd, cwd: "a.py\nb.py")

    files = check.get_committed_files("dummy")

    assert files == ["a.py", "b.py"]


def test_get_committed_files_empty_output(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(check, "run_cmd", lambda cmd, cwd: "")

    files = check.get_committed_files("dummy")

    assert files == []


def test_should_ignore_folder() -> None:
    config = {"ignored_folders": ["node_modules", "__pycache__"]}

    assert check.should_ignore_folder("node_modules", config)
    assert check.should_ignore_folder("__pycache__", config)
    assert not check.should_ignore_folder("src", config)
    assert not check.should_ignore_folder("", config)


def test_is_git_repo(tmp_path: Path) -> None:
    assert not check.is_git_repo(str(tmp_path))

    (tmp_path / ".git").mkdir()
    assert check.is_git_repo(str(tmp_path))


def test_check_eol_reports_crlf_issues(
    monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    eol_output = (
        "i/crlf  w/crlf  attr/               file.py\n"
        "i/lf    w/lf    attr/               ok.py"
    )
    monkeypatch.setattr(check, "run_cmd", lambda cmd, cwd: eol_output)

    check.check_eol("dummy", {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert "file.py" in captured.out
    assert "ok.py" not in captured.out


def test_check_eol_ignores_files_with_matching_extension(
    monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        check,
        "run_cmd",
        lambda cmd, cwd: "i/crlf  w/crlf  attr/               image.PNG",
    )

    check.check_eol("dummy", {"ignored_extensions": [".png"]})

    captured = capsys.readouterr()
    assert "image.PNG" not in captured.out


def test_check_eol_silent_when_no_issues(
    monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        check, "run_cmd", lambda cmd, cwd: "i/lf    w/lf    attr/               ok.py"
    )

    check.check_eol("dummy", {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert captured.out == ""


def test_check_eol_handles_empty_output(
    monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(check, "run_cmd", lambda cmd, cwd: "")

    check.check_eol("dummy", {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert captured.out == ""


def test_check_trailing_whitespace_detects_issues(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    bad_file = tmp_path / "bad.py"
    bad_file.write_text("line with trailing   \n", encoding="utf-8")
    monkeypatch.setattr(check, "get_committed_files", lambda repo_path: ["bad.py"])

    check.check_trailing_whitespace(str(tmp_path), {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert "bad.py" in captured.out


def test_check_trailing_whitespace_clean_file(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    clean_file = tmp_path / "clean.py"
    clean_file.write_text("clean line\n", encoding="utf-8")
    monkeypatch.setattr(check, "get_committed_files", lambda repo_path: ["clean.py"])

    check.check_trailing_whitespace(str(tmp_path), {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert captured.out == ""


def test_check_trailing_whitespace_skips_markdown(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    md_file = tmp_path / "README.md"
    md_file.write_text("trailing spaces   \n", encoding="utf-8")
    monkeypatch.setattr(check, "get_committed_files", lambda repo_path: ["README.md"])

    check.check_trailing_whitespace(str(tmp_path), {"ignored_extensions": []})

    captured = capsys.readouterr()
    assert "README.md" not in captured.out


def test_check_trailing_whitespace_skips_ignored_extensions(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    img_file = tmp_path / "image.png"
    img_file.write_text("data   \n", encoding="utf-8")
    monkeypatch.setattr(check, "get_committed_files", lambda repo_path: ["image.png"])

    check.check_trailing_whitespace(str(tmp_path), {"ignored_extensions": [".png"]})

    captured = capsys.readouterr()
    assert "image.png" not in captured.out


def test_process_path_nonexistent(capsys: pytest.CaptureFixture[str]) -> None:
    config: dict[str, list[str]] = {
        "ignored_folders": [],
        "skip_repos": [],
        "ignored_extensions": [],
    }

    check.process_path("/definitely/does/not/exist/xyz", config)

    captured = capsys.readouterr()
    assert "does not exist" in captured.err


def test_process_path_single_git_repo(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    (tmp_path / ".git").mkdir()
    called: list[str] = []
    monkeypatch.setattr(check, "check_repo", lambda path, cfg: called.append(path))
    config: dict[str, list[str]] = {
        "ignored_folders": [],
        "skip_repos": [],
        "ignored_extensions": [],
    }

    check.process_path(str(tmp_path), config)

    assert called == [str(tmp_path)]


def test_process_path_directory_with_repos(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    repo1 = tmp_path / "repo1"
    (repo1 / ".git").mkdir(parents=True)
    repo2 = tmp_path / "repo2"
    (repo2 / ".git").mkdir(parents=True)

    called: list[str] = []
    monkeypatch.setattr(check, "check_repo", lambda path, cfg: called.append(path))
    config: dict[str, list[str]] = {
        "ignored_folders": [],
        "skip_repos": [],
        "ignored_extensions": [],
    }

    check.process_path(str(tmp_path), config)

    assert sorted(called) == sorted([str(repo1), str(repo2)])


def test_process_path_no_repos_found(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    config: dict[str, list[str]] = {
        "ignored_folders": [],
        "skip_repos": [],
        "ignored_extensions": [],
    }

    check.process_path(str(tmp_path), config)

    captured = capsys.readouterr()
    assert "No git repos found" in captured.out


def test_check_repo_skips_when_in_skip_list(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    config = {
        "ignored_extensions": [],
        "ignored_folders": [],
        "skip_repos": [tmp_path.name],
    }

    check.check_repo(str(tmp_path), config)

    captured = capsys.readouterr()
    assert "Skipping" in captured.out
