# -*- coding: utf-8 -*-

"""
Capture and Define Custom Warnings for Package

Define all custom warning classes here. Each warning should inherit from
an appropriate built-in warning (``UserWarning``, ``DeprecationWarning``,
etc.) or from the base :class:`PkgNameWarning` class for package-level
warnings.

:NOTE: Rename ``PkgNameWarning`` to match your actual package name when
       using this template (e.g. ``MyPackageWarning``).
"""


class PkgNameWarning(UserWarning):
    """
    Base Warning for pkg-name

    All custom warnings in this package should inherit from this class.
    This makes it easy for callers to filter all package-specific warnings
    with a single ``warnings.filterwarnings`` call.

    :NOTE: Rename this class to match your actual package name when using
           this template (e.g. ``MyPackageWarning``).
    """

    pass
