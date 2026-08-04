# Template Python
[![Tests](https://github.com/LevonBecker/template_python/actions/workflows/tests.yml/badge.svg)](https://github.com/LevonBecker/template_python/actions/workflows/tests.yml)

Minimal skeleton for a Python repository: invoke tasks, a couple of shared modules, uv for
environment/dependency management, and CI (ruff, pylint, pytest, yamllint, actionlint). No AI-agent
tooling — see [`template_ai_python`](https://github.com/LevonBecker/template_ai_python), which forks
this repo and adds that layer on top.

## Setup
```bash
./setup.sh     # macOS/Linux
.\setup.ps1    # Windows (PowerShell)
```

Creates a `.venv` with `uv` and installs dependencies. Update `properties.yml` with the local repo
path before running tasks.

## Project Structure
```
pyproject.toml    # Dependencies (Python >=3.14), ruff/pylint/pytest config
invoke.yml        # Invoke config (auto_dash_names: false)
setup.sh          # Shell-based setup script (uv venv + uv sync)
properties.yml    # Project configuration (repo path/remote, template path/remote)
modules/
  common/         # cli.py, properties.py, utils.py — shared helpers
  setup/          # properties.py — creates properties.yml (no-op if it exists), called by setup.sh/setup.ps1; templates/properties/*.yml — tier fragments
tasks/
  __init__.py     # Wires the invoke Collection (debug, ruff, setup, tests) plus top-level aliases (fix, test)
  combos.py       # Top-level aliases: fix, test
  debug.py        # debug.env — print cwd + sorted env vars
  ruff.py         # ruff.fix, ruff.format
  setup.py        # setup.properties — creates/stamps properties.yml
  tests.py        # tests.actionlint, tests.pylint, tests.pytest, tests.rufflint, tests.yamllint
.github/
  copilot-instructions.md # What this repo is, for GitHub Copilot
  workflows/
    tests.yml       # CI: ruff + pylint + pytest + yamllint + actionlint, on PRs to development/main
.vscode/
  extensions.json # Recommended VS Code extensions
  settings.json   # Ruff formatter + Python interpreter settings
```

## Invoke Tasks
```sh
uv run --no-sync invoke             # List all available tasks
uv run --no-sync invoke test        # Ruff + Pylint + pytest + yamllint + actionlint
uv run --no-sync invoke fix         # Ruff autocorrect + format
uv run --no-sync invoke setup.properties # Create/stamp properties.yml
```

## Modules
| Module | Purpose |
|--------|---------|
| [`modules/common/`](modules/common/README.md) | CLI helpers, `properties.yml` config reader, output/utility helpers |
| [`modules/setup/`](modules/setup/README.md) | Creates `properties.yml` (no-op if it exists) from tier fragments, called by `setup.sh`/`setup.ps1` |

See [modules/README.md](modules/README.md) for full details.

## CI
GitHub Actions runs Ruff, Pylint, pytest, yamllint, and actionlint on every pull request targeting
`development` or `main` via `.github/workflows/tests.yml`.
