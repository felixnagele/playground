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
)


def should_ignore(path: str) -> bool:
    lower = path.lower()
    return lower.endswith(IGNORED_SUFFIXES)


def run_cmd(cmd, cwd):
    try:
        result = subprocess.run(
            cmd, cwd=cwd, shell=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: {e}"


def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))


def find_repos(start_path):
    repos = []
    for root, dirs, files in os.walk(start_path):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")
    return repos


def get_committed_files(repo_path):
    output = run_cmd("git ls-files", repo_path)
    return output.splitlines() if output else []


def check_eol(repo_path):
    system = platform.system().lower()

    if "windows" in system:
        cmd = 'git ls-files --eol | Select-String -NotMatch "i/lf"'
    else:
        cmd = 'git ls-files --eol | grep -v "i/lf"'

    output = run_cmd(cmd, repo_path)
    if output:
        print(f"\n❌ EOL PROBLEMS in {repo_path}:")
        print(output)


def check_trailing_whitespace(repo_path):
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
                    if line.rstrip("\n").rstrip("\r").endswith(" "):
                        print(f"❌ Trailing whitespace: {full_path}:{i}")
        except:
            pass


def process_path(path):
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


def main():
    if len(sys.argv) == 1:
        base = os.getcwd()
        print(f"🔎 Scanning current directory: {base}")
        process_path(base)
    else:
        target = os.path.abspath(sys.argv[1])
        print(f"🔎 Scanning path: {target}")
        process_path(target)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
