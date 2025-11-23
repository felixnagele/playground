import requests


def main():
    response = requests.get("https://api.github.com", timeout=10)

    if response.ok:
        data = response.json()
        print("GitHub API Root Endpoints:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error: Failed to fetch GitHub API (Status {response.status_code})")


if __name__ == "__main__":
    main()
