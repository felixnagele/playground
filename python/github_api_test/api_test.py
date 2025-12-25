import requests


def main():
    """
    Fetch and display GitHub API root endpoints.
    """
    try:
        response = requests.get("https://api.github.com", timeout=10)
        if response.ok:
            data = response.json()
            print("GitHub API Root Endpoints:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print(f"Error: Failed to fetch GitHub API (Status {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error occurred - {e}")


if __name__ == "__main__":
    main()
