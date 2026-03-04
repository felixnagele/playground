import os
import sys
import subprocess
import json
from pathlib import Path


def load_config(custom_config_path=None):
    """Load default config (extensions, folders) + optional custom config (skip_repos)."""
    # Step 1: Always load default config
    default_config_path = Path(__file__).parent / ".checkignore.default.json"
    if not default_config_path.exists():
        print(
            "❌ Default config (.checkignore.default.json) is missing!", file=sys.stderr
        )
        sys.exit(1)

    try:
        with open(default_config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            print(f"📄 Loaded default config: {default_config_path.name}")
    except Exception as e:
        print(f"❌ Failed to load default config: {e}", file=sys.stderr)
        sys.exit(1)

    # Ensure skip_repos starts empty (not from default)
    config["skip_repos"] = []

    # Step 2: If custom config provided, load skip_repos from it
    if custom_config_path:
        custom_path = Path(custom_config_path).resolve()
        if not custom_path.exists():
            print(f"❌ Custom config not found: {custom_path}", file=sys.stderr)
            sys.exit(1)

        try:
            with open(custom_path, "r", encoding="utf-8") as f:
                custom_config = json.load(f)
                # Only take skip_repos from custom config
                config["skip_repos"] = custom_config.get("skip_repos", [])
                print(f"📄 Loaded skip_repos from: {custom_path}")
        except Exception as e:
            print(f"❌ Failed to load custom config: {e}", file=sys.stderr)
            sys.exit(1)

    return config


def should_ignore_file(path: str, config: dict) -> bool:
    """Check if file should be ignored based on extension."""
    lower = path.lower()
    for ext in config.get("ignored_extensions", []):
        if lower.endswith(ext.lower()):
            return True
    return False


def should_ignore_folder(folder_name: str, config: dict) -> bool:
    """Check if folder should be ignored."""
    return folder_name in config.get("ignored_folders", [])


def should_skip_repo(repo_path: str, config: dict) -> bool:
    """Check if entire repo should be skipped."""
    repo_name = Path(repo_path).name
    skip_list = config.get("skip_repos", [])

    # Check by name or full path
    if repo_name in skip_list:
        return True
    if str(Path(repo_path).resolve()) in skip_list:
        return True

    return False


def run_cmd(cmd: str, cwd: str) -> str:
    """Run shell command and return output."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, shell=True, capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"⚠️ Command failed: {e}", file=sys.stderr)
        return ""


def is_git_repo(path: str) -> bool:
    """Check if path is a git repository."""
    return os.path.isdir(os.path.join(path, ".git"))


def find_repos(start_path: str, config: dict) -> list[str]:
    """Find all git repositories, respecting ignored_folders."""
    repos = []
    for root, dirs, files in os.walk(start_path):
        # Remove ignored folders from search
        dirs[:] = [d for d in dirs if not should_ignore_folder(d, config)]

        if ".git" in dirs:
            repos.append(root)
            dirs[:] = [d for d in dirs if d != ".git"]  # Don't descend into .git

    return repos


def get_committed_files(repo_path: str) -> list[str]:
    """Get list of files tracked by git."""
    output = run_cmd("git ls-files", repo_path)
    if not output:
        return []
    return output.splitlines()


def check_eol(repo_path: str, config: dict) -> None:
    """Check for EOL (end-of-line) issues."""
    output = run_cmd("git ls-files --eol", repo_path)
    if not output:
        return

    issues = []
    for line in output.splitlines():
        if not line.strip():
            continue

        parts = line.split()
        if len(parts) < 4:
            continue

        index_eol = parts[0]  # i/lf, i/crlf, i/mixed, i/none
        filepath = " ".join(parts[3:])

        if should_ignore_file(filepath, config):
            continue

        # i/none = empty file or binary (no line endings) -> OK, not a problem
        # i/lf = correct line endings -> OK
        # i/crlf or i/mixed = problem -> Report
        if index_eol == "i/none" or index_eol == "i/lf":
            continue

        # Only report actual problems (CRLF or mixed line endings)
        issues.append(f"  {filepath}: {index_eol}")

    if issues:
        print(f"\n❌ EOL PROBLEMS in {repo_path}:")
        for issue in issues:
            print(issue)


def check_trailing_whitespace(repo_path: str, config: dict) -> None:
    """Check for trailing whitespace in files."""
    committed_files = get_committed_files(repo_path)
    max_file_size = 10 * 1024 * 1024  # 10 MB

    for rel_path in committed_files:
        # Skip markdown files (trailing spaces have meaning)
        if rel_path.endswith(".md"):
            continue

        if should_ignore_file(rel_path, config):
            continue

        full_path = os.path.join(repo_path, rel_path)

        # Check if file exists and is accessible
        if not os.path.exists(full_path):
            continue

        try:
            # Skip large files (likely binary or generated)
            file_size = os.path.getsize(full_path)
            if file_size == 0:
                # Empty files are fine, no whitespace possible
                continue
            if file_size > max_file_size:
                # Skip large files silently
                continue

            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                for i, line in enumerate(f, start=1):
                    # Check if line has trailing whitespace (excluding newlines)
                    stripped = line.rstrip("\n\r")
                    if stripped and stripped != stripped.rstrip():
                        print(f"❌ Trailing whitespace: {full_path}:{i}")
        except (OSError, IOError, UnicodeDecodeError):
            # Silently skip files we can't read (likely binary)
            pass


def check_repo(repo_path: str, config: dict) -> None:
    """Run all checks on a repository."""
    if should_skip_repo(repo_path, config):
        print(f"\n⏭️  Skipping: {repo_path}")
        return

    print(f"\n📁 Checking: {repo_path}")
    check_eol(repo_path, config)
    check_trailing_whitespace(repo_path, config)


def process_path(path: str, config: dict) -> None:
    """Process a path - either a single repo or search for repos."""
    if not os.path.exists(path):
        print(f"❌ ERROR: Path does not exist: {path}", file=sys.stderr)
        return

    if not os.access(path, os.R_OK | os.X_OK):
        print(f"❌ ERROR: Path is not accessible: {path}", file=sys.stderr)
        return

    if is_git_repo(path):
        check_repo(path, config)
        return

    repos = find_repos(path, config)
    if not repos:
        print(f"\n⚠️ No git repos found in: {path}")
        return

    for repo in repos:
        check_repo(repo, config)


def print_usage():
    print("Usage:")
    print("  python check.py [path] [--config <file>]")
    print()
    print("Arguments:")
    print(
        "  path                Optional: Directory to scan (default: current directory)"
    )
    print("  --config <file>     Optional: Config file for skip_repos only")
    print("  --help, -h          Show this help message")
    print()
    print("How it works:")
    print("  - Default config (.checkignore.default.json) is ALWAYS loaded")
    print("    → Contains: ignored_extensions, ignored_folders (committed)")
    print("  - Custom config (via --config) is optional")
    print("    → Contains: skip_repos only (personal, not committed)")
    print()
    print("Examples:")
    print("  python check.py")
    print("  python check.py /path/to/check")
    print("  python check.py --config .skip_repos.json")


def main() -> None:
    custom_config = None
    scan_path = None

    # Parse arguments
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] in ("--help", "-h"):
            print_usage()
            sys.exit(0)
        elif args[i] == "--config":
            if i + 1 >= len(args):
                print("❌ --config requires a config file path", file=sys.stderr)
                print_usage()
                sys.exit(1)
            custom_config = args[i + 1]
            i += 2
        elif args[i].startswith("--"):
            print(f"❌ Unknown option: {args[i]}", file=sys.stderr)
            print_usage()
            sys.exit(1)
        else:
            # Positional argument = scan path
            if scan_path is not None:
                print("❌ Multiple scan paths provided", file=sys.stderr)
                print_usage()
                sys.exit(1)
            scan_path = args[i]
            i += 1

    # Load config
    config = load_config(custom_config)

    # Determine scan path
    if scan_path is None:
        scan_path = os.getcwd()
    else:
        scan_path = os.path.abspath(scan_path)

    print(f"🔎 Scanning: {scan_path}")
    process_path(scan_path, config)
    print("\n✅ Done.")


if __name__ == "__main__":
    main()
