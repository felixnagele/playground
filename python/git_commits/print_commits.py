import argparse
import os
from collections.abc import Iterator
from datetime import datetime

from git import Commit, Repo


def print_all_commits(repo_path: str) -> None:
    try:
        repo: Repo = Repo(repo_path)

        if repo.bare:
            print(f"Error: Repository at '{repo_path}' is bare or invalid.")
            return

        print("=" * 80)

        commits: Iterator[Commit] = repo.iter_commits()
        for commit in commits:
            commit_time: str = datetime.fromtimestamp(commit.committed_date).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            summary = (
                commit.summary.decode("utf-8")
                if isinstance(commit.summary, bytes)
                else commit.summary
            )
            message = commit.message.strip()
            message = message.decode("utf-8") if isinstance(message, bytes) else message

            print(f"Commit Hash: {commit.hexsha}")
            print(f"Author:      {commit.author.name} <{commit.author.email}>")
            print(f"Date/Time:   {commit_time}")
            print(f"Summary:     {summary}")
            if message != summary:
                print(f"Full Message:\n{message}")

            print("-" * 80)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", default=".", help="Path to the git repository")
    args: argparse.Namespace = parser.parse_args()

    print_all_commits(os.path.abspath(args.path))
