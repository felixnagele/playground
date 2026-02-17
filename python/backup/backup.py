import subprocess
import sys
import requests
from pathlib import Path
from datetime import datetime
from typing import List, Optional


def fetch_public_repos(username: str, timeout: int = 10) -> List[str]:
    """Fetch all public repos for a GitHub user."""
    repos = []
    url = f"https://api.github.com/users/{username}/repos"

    while url:
        try:
            resp = requests.get(
                url, params={"per_page": 100, "type": "public"}, timeout=timeout
            )
            resp.raise_for_status()
        except requests.exceptions.Timeout:
            print("⚠ Timeout fetching repos from GitHub API", file=sys.stderr)
            break
        except requests.exceptions.ConnectionError as e:
            print(f"⚠ Network error: {e}", file=sys.stderr)
            break
        except requests.exceptions.HTTPError as e:
            print(f"⚠ GitHub API error: {e}", file=sys.stderr)
            break

        repos.extend([r["clone_url"] for r in resp.json()])

        # Safe pagination check
        url = ""
        if hasattr(resp, "links") and resp.links:
            url = resp.links.get("next", {}).get("url")

    return repos


def clone_repo(url: str, target: Path) -> bool:
    """Clone a single repo as mirror, update if exists."""
    repo_name = url.rstrip("/").split("/")[-1].replace(".git", "")
    target_path = target / f"{repo_name}.git"

    # Update existing mirror instead of failing
    if target_path.exists():
        print(f"  ↻ {repo_name} (updating existing mirror)")
        result = subprocess.run(
            ["git", "-C", str(target_path), "remote", "update", "--prune"],
            capture_output=True,
            text=True,
        )
    else:
        result = subprocess.run(
            ["git", "clone", "--mirror", url, str(target_path)],
            capture_output=True,
            text=True,
        )

    if result.returncode != 0:
        print(f"  ✗ {repo_name}: {result.stderr.strip()}", file=sys.stderr)
        return False

    print(f"  ✓ {repo_name}")
    return True


def backup_repos(
    work_dir: Optional[Path] = None, username: Optional[str] = None
) -> int:
    if work_dir is None:
        work_dir = Path.cwd()

    backups_dir = work_dir / "backups"
    private_file = backups_dir / "repos_private.txt"

    # Validate at least one source exists
    has_username = username is not None
    has_private_file = private_file.exists()

    if not has_username and not has_private_file:
        print("❌ Error: No backup source specified", file=sys.stderr)
        print(
            f"   Provide --username for public repos OR create {private_file}",
            file=sys.stderr,
        )
        return 1

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_target = backups_dir / f"github_backup_{timestamp}"
    backup_target.mkdir(parents=True, exist_ok=True)

    failed = []
    total = 0

    # Public repos from GitHub API
    if username:
        print(f"\n📦 Fetching public repos for @{username}...")
        public_urls = fetch_public_repos(username)

        if not public_urls:
            print("   ⚠ No public repos found or API error", file=sys.stderr)
        else:
            print(f"   Found {len(public_urls)} public repos\n")
            print("🔓 Backing up PUBLIC repos:")

            for url in public_urls:
                total += 1
                if not clone_repo(url, backup_target):
                    failed.append(url)

    # Private repos from file
    if has_private_file:
        print("\n🔐 Backing up PRIVATE repos:")
        private_urls = [
            line.strip()
            for line in private_file.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
        print(f"   Found {len(private_urls)} repos in repos_private.txt\n")

        for url in private_urls:
            total += 1
            if not clone_repo(url, backup_target):
                failed.append(url)

    # Handle case where sources exist but no repos found
    if total == 0:
        print("\n⚠ No repositories to backup", file=sys.stderr)
        backup_target.rmdir()  # Clean up empty directory
        return 1

    # Summary
    print(f"\n{'='*50}")
    print(f"✅ Backup completed: {backup_target}")
    print(f"   Total: {total} | Success: {total - len(failed)} | Failed: {len(failed)}")

    if failed:
        print("\n❌ Failed repos:")
        for url in failed:
            print(f"   - {url}")
        return 1

    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Backup GitHub repos")
    parser.add_argument("--username", "-u", help="GitHub username for public repos")
    parser.add_argument("--work-dir", "-w", help="Working directory (default: CWD)")

    args = parser.parse_args()
    work_path = Path(args.work_dir) if args.work_dir else None

    sys.exit(backup_repos(work_path, args.username))
