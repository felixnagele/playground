# GitHub Stats

Test project for analyzing GitHub repository statistics.

## How to use

After cloning the repository, you have to create an .env file in the `python/github_stats/` directory with the following content:

```env
USERNAME=   # Your GitHub username
TOKEN=      # Personal access token (classic or fine-grained)
EXCLUDE_REPOS=   # Comma-separated repos to ignore
ONLY_OWNED=true  # Limit to repos you own
```

### Security and Token Setup

1. **Add `.env` to `.gitignore`**  
   To prevent accidentally committing sensitive tokens, add `.env` to your `.gitignore` file:
   ```gitignore
   .env
Then, install the required packages:

```bash
pip install requests python-dotenv
```

Finally, run the script:

```bash
python stats.py
```
