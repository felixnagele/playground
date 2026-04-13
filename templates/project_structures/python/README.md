# Description

## Development

project root/

- .gitignore - git ignore rules
- pyproject.toml - project config & dependencies
- README.md - project info (this file)
- src/
  - main.py - main entry point
  - utils.py - shared utility functions
  - sub_folder_1/
    - test1.py - imports from utils
  - sub_folder_2/
    - test2.py - imports from sub_folder_1
- tests/
  - test_example.py - pytest example

## Setup

`cd project_folder`

Install [uv](https://github.com/astral-sh/uv) with standalone installers or your package manager of choice.

`uv sync`

Or use standard python venv and pip:

`python -m venv .venv`

`source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)

`pip install .`

### How to run

`uv run python -m src.main`

Or with standard python:

`python -m src.main`

### How to test

`uv run pytest`

Or with standard python:

`pytest`

### Info

Import pattern: `from src.module import func`
Sibling import: `from src.sub_folder_1.test1 import calculate`
