# Objective

This template repository provides a starting point for building a Python package
intended for distribution on [PyPI](https://pypi.org/). It includes:

- A well-structured package layout under `pkg-name/`
- Modern packaging via `pyproject.toml` (PEP 517/518/621)
- GitHub Actions CI for linting and testing
- Sphinx documentation configured for ReadTheDocs
- Docker support for containerised deployment
- Pre-commit hooks for local code quality checks

## How to Use This Template

1. Click **Use this template** on GitHub to create a new repository.
2. Rename the `pkg-name/` directory to your package name (use underscores, not hyphens).
3. Update `pyproject.toml` with your package name, description, and URLs.
4. Update `README.md` with your project's description and usage examples.
5. Start adding your code to the `api/`, `core/`, and `config/` submodules.
