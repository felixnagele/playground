import os
import subprocess
import sys
from pathlib import Path


def _utf8_env():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return env


def test_sync_script_help_works():
    script = Path(__file__).resolve().parents[1] / "sync.py"
    result = subprocess.run(
        [sys.executable, str(script), "--help"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=_utf8_env(),
        check=False,
    )

    assert result.returncode == 0
    assert "Update all git repositories under a directory" in result.stdout


def test_sync_script_handles_empty_base_directory(tmp_path):
    script = Path(__file__).resolve().parents[1] / "sync.py"
    result = subprocess.run(
        [sys.executable, str(script), "--base", str(tmp_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=_utf8_env(),
        check=False,
    )

    assert result.returncode == 0
    assert "Total repositories: 0" in result.stdout
