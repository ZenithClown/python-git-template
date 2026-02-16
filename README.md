<div align = "center">

# Python GIT Template

[![GitHub Issues](https://img.shields.io/github/issues/ZenithClown/python-git-template?style=plastic)](https://github.com/ZenithClown/python-git-template/issues)
[![GitHub Forks](https://img.shields.io/github/forks/ZenithClown/python-git-template?style=plastic)](https://github.com/ZenithClown/python-git-template/network)
[![GitHub Stars](https://img.shields.io/github/stars/ZenithClown/python-git-template?style=plastic)](https://github.com/ZenithClown/python-git-template/stargazers)
[![LICENSE File](https://img.shields.io/github/license/ZenithClown/python-git-template?style=plastic)](https://github.com/ZenithClown/python-git-template/blob/master/LICENSE)

[![Code Linting (flake8)](https://github.com/ZenithClown/python-git-template/actions/workflows/code-linting.yml/badge.svg)](https://github.com/ZenithClown/python-git-template/actions/workflows/code-linting.yml)
[![Dependabot Updates](https://github.com/ZenithClown/python-git-template/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/ZenithClown/python-git-template/actions/workflows/dependabot/dependabot-updates)

</div>

<div align = "justify">

A *simple and modern template* for Python module development with additional workflows, code linting checks, etc. to quickly
build necessary file structure. The repository is build as a *template repository* that can be used to create the same directory
structure, branches (optional) and files. To create a repository from this template:

  * Select "Use this Template" > "Create New Repository" from the dropdown menu,
  * Optionally, you can include all the branches (not-recommended) from the menu, and
  * Follow the steps to create repository information and choose the visibility.

## Quick Start Guide

Introduced in 2019, users can now create a repository from templates in GitHub. To do this, simply head over to any repository
settings and enable "Template Repository" from the Options Menu. When creating a *new repository* from this template, you can
just click on **`Use this Template`** available in this repository (refer the picture below).

[![Use this Template](./assets/use_this_template_demo.png)](./assets/use_this_template_demo.png)

The template repository is not limited to GitHub, but can be widely used by using simple shell commands to copy and sync the
contents like below:

```bash
rsync -rh ~/source/directory /destination/directory
```

The above tool reflects the wide adaptibility and simplicity of usage of the code that provides forward integration with any
external models/libraries.

## Project License

This repository follows [MIT License](./LICENSE) but you're free to use any type of license; choose a type of
[*licese*](https://choosealicense.com/) as suitable for your project/required by your organization.

## GitHub Workflows

The project is configured with utility workflows for *continuous integration and development* for automating process like
dependency checks, code lintings, etc. The following workflows are available.

### Dependabot Updates

The [`workflow`](.github/dependabot.yml) can be used to automatically check for requirements that can be required by the
package. To use this, a `requirements.txt` file needs to be maintained, on which a new PR is automatically created when a new
release is available. To use this effectively, create two new labels `pip` and `dependencies` for the repository, as the
bot can automatically label the new pull requests accordingly.

### Code Linting using Flake8

Use the command `flake8 . --count --exit-zero --max-complexity=10 --statistics` to generate a report.

</div>
