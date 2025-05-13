#!/usr/bin/env python
# -*- encoding: utf-8 -*-

### --- IF REQUIRED - ADD LICENSING INFORMATION (HERE) --- ###

import os
from setuptools import setup
from setuptools import find_packages

PKG = "pkg-name" # Edit with your package name

# Version File Implementation: https://stackoverflow.com/a/7071358
VERSIONFILE = os.path.join(PKG, 'VERSION')
try:
    VERSION = open(VERSIONFILE, 'rt').read() # always read as str()
except FileNotFoundError as err:
    raise RuntimeError(f'is PKG = {PKG} correctly defined? {err}')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name         = PKG,
    version      = VERSION,
    author       = "Debmalya Pramanik",
    author_email = "",

    description                   = "<SHORT PROJECT DESCRIPTION>",
    long_description              = long_description,
    long_description_content_type = "text/markdown",

    url         = "<project url>",
    packages    = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: Apache Software License" # Change as Required
    ],
    python_requires  = ">=3.10",  # Specify Requirement
    install_requires = [] # Add/Edit as Required
)
