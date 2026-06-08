import argparse
import os
from datetime import datetime
from typing import Generator
from git import Repo, Commit


def print_all_commits(repo_path: str) -> None:
    try:
        repo: Repo = Repo(repo_path)

        if repo.bare:
            print(f"Error: Repository at '{repo_path}' is bare or invalid.")
            return

        print("=" * 80)

        commit_generator: Generator[Commit, None, None] = repo.iter_commits()
        for commit in commit_generator:
            commit_time: str = datetime.fromtimestamp(commit.committed_date).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            print(f"Commit Hash: {commit.hexsha}")
            print(f"Author:      {commit.author.name} <{commit.author.email}>")
            print(f"Date/Time:   {commit_time}")
            print(f"Summary:     {commit.summary}")
            if commit.message.strip() != commit.summary:
                print(f"Full Message:\n{commit.message.strip()}")

            print("-" * 80)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", default=".", help="Path to the git repository")
    args: argparse.Namespace = parser.parse_args()

    print_all_commits(os.path.abspath(args.path))
