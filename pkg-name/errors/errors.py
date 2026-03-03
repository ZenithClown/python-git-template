# -*- coding: utf-8 -*-

"""
Capture and Define Custom Errors for Package

Define all custom exception classes here. Each exception should inherit
from an appropriate built-in exception (``ValueError``, ``TypeError``, etc.)
or from the base :class:`PkgNameError` class for package-level exceptions.

:NOTE: Rename ``PkgNameError`` to match your actual package name when using
       this template (e.g. ``MyPackageError``).
"""


class PkgNameError(Exception):
    """
    Base Exception for pkg-name

    All custom exceptions in this package should inherit from this class.
    This makes it easy for callers to catch all package-specific errors
    with a single ``except PkgNameError`` clause.

    :NOTE: Rename this class to match your actual package name when using
           this template (e.g. ``MyPackageError``).
    """

    pass
