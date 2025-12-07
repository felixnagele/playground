# GitHub Stats

Test project for analyzing GitHub repository statistics.

## How to use

After cloning the respository, you have to create an .env file in the root directory with the following content:

```env
USERNAME=   # Your GitHub username
TOKEN=      # Personal access token
EXCLUDE_REPOS=   # Comma-separated repos to ignore
ONLY_OWNED=true  # Limit to repos you own
```

Then, install the required packages:

```bash
pip install requests python-dotenv
```

Finally, run the script:

```bash
python stats.py
```
