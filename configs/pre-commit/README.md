# Pre-commit

## How to install

Upgrade pip to the latest version

```bash
python -m pip install --upgrade pip
```

Install the pre-commit tool

```bash
pip install pre-commit
```

## How to use

Update pre-commit hooks in a specific config file

```bash
pre-commit autoupdate --config [file_path]
```

Or update pre-commit hooks using the config file's folder

```bash
pre-commit autoupdate
```

Test pre-commit hooks after the update

```bash
pre-commit run --all-files --config [file_path]
```

## Notes

- Deprecated (archived) repo: [mirrors-prettier](https://github.com/pre-commit/mirrors-prettier) - Consider searching for a better alternative, such as official Prettier solutions: [Prettier-Precommit](https://prettier.io/docs/precommit)
- This pre-commit config file could be added to the .github repo in a shared folder: shared/[file_path] and then referenced by each repo's pre-commit file
