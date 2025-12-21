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
`pip install uv`
`uv venv`
Linux/Mac
`source .venv/bin/activate`
Win
`.venv\Scripts\activate`
`uv sync`

### How to run

`python -m src.main`

### How to test

`pytest`

### Info

Import pattern: `from src.module import func`
Sibling import: `from src.sub_folder_1.test1 import calculate`
