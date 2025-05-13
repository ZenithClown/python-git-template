# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

PKG = "pkg-name" # Edit with your package name

# ? insert the project paths to let sphinx recognize/find packages
sys.path.append(os.path.abspath(os.path.join("..")))

project = "Package Name"
copyright = "2021, Debmalya Pramanik"
author = "Debmalya Pramanik"
release = open(os.path.abspath(os.path.join("..", PKG, "VERSION")), "r").read()

# import all working modules for autodoc features

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# html_logo = 'assets/images/logo.jpg'
html_favicon = 'assets/images/favicon/favicon.ico'
