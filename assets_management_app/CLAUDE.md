# Asset Management Application

A Python-based web API used by IT Huset to manage the different hardware and software assets.


## Requirements

1. The application should only expose List and Add operations
2. No authentication
3. Use in-memory data store, like dictionaries
4. Include a basic build pipeline that tests the application


## Repository Layout

The git repository root is one level above this directory (`Labb_2026-03-17/`). The root-level `.gitignore` covers:

- Python build artefacts and bytecode
- Virtual environments (`.venv/`, `venv/`, `env/`)
- Testing and coverage outputs (`.pytest_cache/`, `htmlcov/`, etc.)
- Environment / secret files (`.env`, `.env.*`)
- Shell config files (`.zshrc`, `.bashrc`, `.bash_profile`, `.profile`, etc.)
- Claude Code local settings (`.claude/`)
- IDE and OS files (`.vscode/`, `.idea/`, `.DS_Store`, etc.)

A more granular `.gitignore` for the app itself lives at `assets_management_app/.gitignore`.


## Development Setup

- Use a virtual environment: `python -m venv .venv && source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt` (if present)
- Never commit `.env` files or shell config files

