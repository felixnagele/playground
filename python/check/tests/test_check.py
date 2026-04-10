import check


def test_should_ignore_file_case_insensitive():
    config = {"ignored_extensions": [".png", ".JPG"]}

    assert check.should_ignore_file("image.PNG", config)
    assert check.should_ignore_file("photo.jpg", config)
    assert not check.should_ignore_file("notes.txt", config)


def test_should_skip_repo_by_name_and_absolute_path(tmp_path):
    repo_dir = tmp_path / "my_repo"
    repo_dir.mkdir()

    by_name_config = {"skip_repos": ["my_repo"]}
    by_path_config = {"skip_repos": [str(repo_dir.resolve())]}

    assert check.should_skip_repo(str(repo_dir), by_name_config)
    assert check.should_skip_repo(str(repo_dir), by_path_config)


def test_find_repos_respects_ignored_folders(tmp_path):
    repo_ok = tmp_path / "repo_ok"
    (repo_ok / ".git").mkdir(parents=True)

    ignored_repo = tmp_path / "node_modules" / "repo_ignored"
    (ignored_repo / ".git").mkdir(parents=True)

    config = {"ignored_folders": ["node_modules"]}
    repos = check.find_repos(str(tmp_path), config)

    assert str(repo_ok) in repos
    assert str(ignored_repo) not in repos


def test_get_committed_files_splits_output(monkeypatch):
    monkeypatch.setattr(check, "run_cmd", lambda cmd, cwd: "a.py\nb.py")

    files = check.get_committed_files("dummy")

    assert files == ["a.py", "b.py"]
