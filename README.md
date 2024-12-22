# Python Template 🐍
A template for a python project for 2025

Features:
- [x] 📦 [`uv`](https://docs.astral.sh/uv/) as package manager
- [x] 💅 [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting
- [x] 🧪 [`pytest`](https://docs.pytest.org/en/stable/) 
- [x] 🧹 [`Makefile`](Makefile) with code quality checks
- [ ] 🐳 Optimized Docker Image
- [x] 🦾 GitHub actions:
    - [x] auto publish to [`pypi`](https://pypi.org/) on push on `main`
    - [ ] auto creating a new tag on push on `main`, sync versions
    - [x] run `tests` and `lint` on `dev` and `main` when a PR is open

## Getting started

### Installation

To set it up and run

```bash
uv venv
uv sync
```
Then

```bash
python main.py
```

Will output a random joke

```
Why did the cow in the pasture get promoted at work? ...  Because he is OUT-STANDING in his field!
```

### Development

You can install in `editable` mode the library

```bash
uv pip install -e .
```

You can now run, for example, a function defined as `scripts` in the [`pyproject.toml`](pyproject.toml)

```bash
make_me_laugh
```

### Linting

```
ruff check
```


### Formatting

```
ruff format
```

## CI/CD

### Tets
Tests inside `/tests` are run using [`pytest`](https://docs.pytest.org/en/stable/) on PR both on `dev` and `main`

### Publish Package
 In order to publish to [pypi](https://pypi.org/) you need to create a secret called `UV_PUBLISH_TOKEN` with your [pypi access token](https://pypi.org/manage/account/) under **API tokens**.