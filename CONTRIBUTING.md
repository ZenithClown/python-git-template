# Contributing to python-git-template

Thank you for your interest in contributing! Here are the guidelines to get started.

## Development Setup

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/ZenithClown/python-git-template.git
   cd python-git-template
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   pip install pytest flake8
   ```

3. **Install pre-commit hooks:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Coding Standards

- Python style is enforced by [flake8](https://flake8.pycqa.org/) with settings in `.flake8`.
- Max line length: **88 characters**.
- All public classes, functions, and methods must have docstrings.
- Use [reST-style docstrings](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists).

## Running Tests

```bash
python -m pytest tests/ -v --tb=short
```

## Building Documentation

```bash
cd docs
pip install -r requirements-doc.txt
make html
```

## Submitting Changes

1. Create a new branch: `git checkout -b feature/my-feature`
2. Make your changes and commit with a descriptive message.
3. Push the branch: `git push origin feature/my-feature`
4. Open a pull request against `master`.
5. Ensure all CI checks pass.

## Reporting Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) issue template.

## Requesting Features

Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) issue template.
