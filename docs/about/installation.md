# Installation

## Prerequisites

- Python >= 3.10
- pip >= 23.0 (recommended)

## From PyPI

Once the package is published, install it with:

```bash
pip install pkg-name
```

## From Source

Clone the repository and install in editable mode:

```bash
git clone https://github.com/ZenithClown/python-git-template.git
cd python-git-template
pip install -e .
```

## Development Setup

Install development and documentation dependencies:

```bash
pip install -e .
pip install pytest flake8
pip install -r docs/requirements-doc.txt
```

## Verifying the Installation

```python
import pkg_name
print(pkg_name.__version__)
```
