# -*- encoding: utf-8 -*-

"""
Python GIT & Docker Template for PyPI Package

The package provides a template repository to create a python package,
that can be seamlessly deployed on PyPI and configured via GIT and
Docker for added capabilities.

@author: Debmalya Pramanik
@copywright: 2021; Debmalya Pramanik
"""

import os

# ? package follows https://peps.python.org/pep-0440/
# ? https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
__version__ = open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r').read().strip()

# ! let's check for package hard dependencies which must be available
hard_dependencies = [] # all should be available in ../requirements.txt
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(e.name)

# ! raise an error during import if any hard package is missing
if missing_dependencies:
    raise ImportError(f"Missing hard dependencies: {missing_dependencies}")

# init-time Option Registrations
from .api import * # noqa: F401, F403 # pyright: ignore[reportMissingImports]
