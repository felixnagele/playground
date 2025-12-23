import os
import sys
import subprocess
import platform

IGNORED_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ico",
    ".bmp",
    ".tif",
    ".tiff",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".jar",
    ".war",
    ".ear",
    ".exe",
    ".dll",
    ".so",
    ".bin",
    ".mwb",
    ".mwb.bak",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".class",
    ".map",
    ".min.js",
    ".min.css",
    ".crx",
)


def should_ignore(path: str) -> bool:
    lower = path.lower()
    return lower.endswith(IGNORED_SUFFIXES)


def run_cmd(cmd: str, cwd: str) -> str:
    try:
        result = subprocess.run(
            cmd, cwd=cwd, shell=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        # Log the error and re-raise to avoid silently treating failures as output.
        print(f"❌ ERROR running command {cmd!r} in {cwd!r}: {e}", file=sys.stderr)
        raise


def is_git_repo(path: str) -> bool:
    return os.path.isdir(os.path.join(path, ".git"))


def find_repos(start_path: str) -> list[str]:
    repos = []
    for root, dirs, files in os.walk(start_path):
        if ".git" in dirs:
            repos.append(root)
            dirs[:] = [d for d in dirs if d != ".git"]
    return repos


def get_committed_files(repo_path: str) -> list[str]:
    output = run_cmd("git ls-files", repo_path)
    if not output:
        return []
    if output.startswith("ERROR:"):
        # Failed to list committed files; log and return an empty list.
        print(output, file=sys.stderr)
        return []
    return output.splitlines()


def check_eol(repo_path: str) -> None:
    system = platform.system().lower()

    if "windows" in system:
        cmd = 'git ls-files --eol | Select-String -NotMatch "i/lf"'
    else:
        cmd = 'git ls-files --eol | grep -v "i/lf"'

    output = run_cmd(cmd, repo_path)
    if output:
        print(f"\n❌ EOL PROBLEMS in {repo_path}:")
        print(output)


def check_trailing_whitespace(repo_path: str) -> None:
    committed_files = get_committed_files(repo_path)

    for rel_path in committed_files:
        if rel_path.endswith(".md"):
            continue
        if should_ignore(rel_path):
            continue

        full_path = os.path.join(repo_path, rel_path)
        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f, start=1):
                    if line.rstrip() != line.rstrip("\n\r"):
                        print(f"❌ Trailing whitespace: {full_path}:{i}")
        except (OSError, IOError) as e:
            print(f"⚠️ Could not read {full_path}: {e}", file=sys.stderr)


def process_path(path: str) -> None:
    if is_git_repo(path):
        print(f"\n📁 Checking repo: {path}")
        check_eol(path)
        check_trailing_whitespace(path)
        return

    repos = find_repos(path)
    if not repos:
        print(f"\n⚠️ No git repos found in: {path}")
        return

    for repo in repos:
        print(f"\n📁 Checking repo: {repo}")
        check_eol(repo)
        check_trailing_whitespace(repo)


def main() -> None:
    if len(sys.argv) == 1:
        base = os.getcwd()
        print(f"🔎 Scanning current directory: {base}")
        process_path(base)
    else:
        target = os.path.abspath(sys.argv[1])
        if not os.path.exists(target):
            print(f"❌ ERROR: Path does not exist: {target}", file=sys.stderr)
            return
        if not os.access(target, os.R_OK | os.X_OK):
            print(f"❌ ERROR: Path is not accessible: {target}", file=sys.stderr)
            return
        print(f"🔎 Scanning path: {target}")
        process_path(target)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
