import argparse
import os
import subprocess
from typing import Tuple


def run_git(args, repo_path: str, timeout: int) -> Tuple[int, str, str]:
    result = subprocess.run(
        ["git", "-C", repo_path] + args, text=True, capture_output=True, timeout=timeout
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


parser = argparse.ArgumentParser(
    description="Update all git repositories under a directory"
)
parser.add_argument(
    "--timeout",
    type=int,
    default=30,
    help="Per-command timeout in seconds (default: 30)",
)
parser.add_argument(
    "--include-dirty",
    action="store_true",
    help="Process repositories even if they have uncommitted changes",
)
parser.add_argument(
    "--base",
    type=str,
    default=os.path.dirname(os.path.abspath(__file__)),
    help="Base directory to scan (default: script directory)",
)
args_ns = parser.parse_args()

# current directory
base_dir = args_ns.base
timeout_s = args_ns.timeout
include_dirty = args_ns.include_dirty

# Statistics
total = 0
success = 0
failed = 0
skipped = 0

print("🚀 Starting Git update for all repositories...\n")

for folder in os.listdir(base_dir):
    repo_path = os.path.join(base_dir, folder)
    if os.path.isdir(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
        total += 1
        print(f"📂 Repository: {folder}")

        try:
            # check for uncommitted changes
            try:
                rc, status_out, status_err = run_git(
                    ["status", "--porcelain"], repo_path, timeout_s
                )
            except subprocess.TimeoutExpired:
                print("   ❌ Timeout checking status")
                failed += 1
                continue
            if rc != 0:
                print(f"   ❌ Failed to check status: {status_err}")
                failed += 1
                continue
            if status_out and not include_dirty:
                print(
                    "   🚫 Skipping: repository has uncommitted changes (use --include-dirty to process)"
                )
                skipped += 1
                continue

            # find current branch
            try:
                rc, branch_out, branch_err = run_git(
                    ["rev-parse", "--abbrev-ref", "HEAD"], repo_path, timeout_s
                )
            except subprocess.TimeoutExpired:
                print("   ❌ Timeout getting branch name")
                failed += 1
                continue
            if rc != 0:
                print(f"   ❌ Could not determine branch: {branch_err}")
                failed += 1
                continue
            branch = branch_out

            print(f"   🌿 Current branch: {branch}")

            # First try a safe fast-forward only pull
            try:
                rc, out, err = run_git(["pull", "--ff-only"], repo_path, timeout_s)
            except subprocess.TimeoutExpired:
                print("   ❌ Timeout during fast-forward pull")
                failed += 1
                continue
            if rc == 0:
                print("   ✅ Successfully updated (fast-forward)!\n")
                success += 1
                continue
            else:
                print(
                    f"   ℹ️ Fast-forward not possible: {err or out} \n      → trying rebase with autostash..."
                )

            # Fallback: rebase with autostash to keep local changes safe
            try:
                rc, out, err = run_git(
                    ["pull", "--rebase", "--autostash"], repo_path, timeout_s
                )
            except subprocess.TimeoutExpired:
                print("   ❌ Timeout during rebase pull")
                failed += 1
                continue
            if rc == 0:
                print("   ✅ Successfully updated (rebase)!\n")
                success += 1
            else:
                print(f"   ❌ Update failed during rebase: {err or out}\n")
                failed += 1
        except subprocess.CalledProcessError as e:
            # unexpected CalledProcessError bubbling up
            print(f"   ❌ Git error: {getattr(e, 'stderr', '') or str(e)}\n")
            failed += 1
        except Exception as e:
            # Any non-git unexpected error; ensure we continue
            print(f"   ❌ Unexpected error: {e}\n")
            failed += 1

# Summary
print("📊 Update Summary")
print("-----------------")
print(f"🔎 Total repositories: {total}")
print(f"✅ Successful updates: {success}")
print(f"❌ Failed updates: {failed}")
print(f"⏭️ Skipped (dirty repos): {skipped}")
print(
    f"🎯 Success rate: {success}/{total} ({(success/total*100 if total else 0):.1f}%)"
)
