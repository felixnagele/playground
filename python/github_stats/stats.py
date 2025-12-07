import requests
from collections import Counter, defaultdict
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
# Check for placeholder or obvious invalid token values
if not TOKEN or TOKEN.lower() in {"your_token_here", "changeme", "", None}:
    raise ValueError("TOKEN must be set to a valid value in .env file")
if not USERNAME:
    raise ValueError("USERNAME must be set in .env file")
EXCLUDE_REPOS = os.getenv("EXCLUDE_REPOS", "")
ONLY_OWNED = os.getenv("ONLY_OWNED", "false").lower() == "true"

# Turn comma-separated string into a set of repo names
EXCLUDE_SET = {r.strip() for r in EXCLUDE_REPOS.split(",") if r.strip()}


def get_user_languages(
    username=None,
    token=None,
    include_private=True,
    exclude_repos=None,
    only_owned=False,
):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Use /user/repos if token is provided and include_private=True
    if include_private and token:
        repos_url = "https://api.github.com/user/repos"
    else:
        repos_url = f"https://api.github.com/users/{username}/repos"

    repos = []
    page = 1
    while True:
        resp = requests.get(
            repos_url, headers=headers, params={"per_page": 100, "page": page}
        )
        if resp.status_code != 200:
            # Avoid leaking sensitive info in error messages
            raise Exception(f"Error fetching repos: {resp.status_code}")
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1

    language_counter = Counter()
    language_repos = defaultdict(set)

    for repo in repos:
        repo_name = repo["name"]

        # Skip excluded repos
        if exclude_repos and repo_name in exclude_repos:
            print(f"Skipping excluded repo: {repo_name}")
            continue

        # Skip repos not owned by the user if ONLY_OWNED is true
        if only_owned:
            owner_login = repo.get("owner", {}).get("login")
            is_admin = repo.get("permissions", {}).get("admin", False)
            if owner_login is None or username is None:
                print(f"Skipping repo due to missing owner or username: {repo_name}")
                continue
            if owner_login.lower() != username.lower() and not is_admin:
                print(f"Skipping non-owned repo: {repo_name}")
                continue

        lang_url = repo["languages_url"]
        resp = requests.get(lang_url, headers=headers)
        # Rate limit handling
        remaining = int(resp.headers.get("X-RateLimit-Remaining", 1))
        reset = int(resp.headers.get("X-RateLimit-Reset", 0))
        if remaining <= 1:
            wait_time = max(0, reset - int(time.time()))
            print(f"Rate limit reached. Waiting {wait_time} seconds until reset...")
            time.sleep(wait_time + 1)
        else:
            time.sleep(0.1)  # Small delay between requests
        if resp.status_code == 200:
            langs = resp.json()
            language_counter.update(langs)
            for lang in langs.keys():
                language_repos[lang].add(repo_name)
        else:
            print(f"Skipping {repo_name} due to error {resp.status_code}")

    return language_counter, language_repos


def print_language_stats(language_counter, language_repos):
    total_bytes = sum(language_counter.values())
    if total_bytes == 0:
        print("No language data found.")
        return

    print(f"\n=== Language Usage Across Profile ({USERNAME}) ===")
    for lang, bytes_of_code in language_counter.most_common():
        percent = (bytes_of_code / total_bytes) * 100
        bar = "█" * int(percent // 2)
        repos_list = ", ".join(sorted(language_repos[lang]))
        print(f"{lang:15} {percent:6.2f}% {bar}  | Repos: {repos_list}")


if __name__ == "__main__":
    languages, language_repos = get_user_languages(
        username=USERNAME,
        token=TOKEN,
        include_private=True,
        exclude_repos=EXCLUDE_SET,
        only_owned=ONLY_OWNED,
    )
    print_language_stats(languages, language_repos)
