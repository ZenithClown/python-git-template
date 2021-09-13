
<h1 align = "center">
	Python GIT Template <br>
	<a href="https://github.com/ZenithClown/python-git-template/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ZenithClown/python-git-template?style=plastic"></a>
	<a href="https://github.com/ZenithClown/python-git-template/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ZenithClown/python-git-template?style=plastic"></a>
	<a href="https://github.com/ZenithClown/python-git-template/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ZenithClown/python-git-template?style=plastic"></a>
	<img src = "https://img.shields.io/badge/python-3.6-lightgrey?style=plastic&logo=python">
	<br>
	<a href = "https://www.linkedin.com/in/dpramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/linkedin.svg"/></a>
	<a href = "https://github.com/ZenithClown"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/github.svg"/></a>
	<a href = "https://gitlab.com/ZenithClown/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/gitlab.svg"/></a>
	<a href = "https://www.researchgate.net/profile/Debmalya_Pramanik2"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/researchgate.svg"/></a>
	<a href = "https://www.kaggle.com/dPramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/kaggle.svg"/></a>
	<a href = "https://app.pluralsight.com/profile/Debmalya-Pramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/pluralsight.svg"/></a>
	<a href = "https://stackoverflow.com/users/6623589/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/stackoverflow.svg"/></a>
</h1>

<p align = "justify"><b>TEMPLATE Design</b> built specifically for python Language, with necessary file structure as required. <strike>This TEMPLATE DOES NOT COME with a LICENSE File, but you can easily add a required license from GitHub. However, special files like .gitignore .gitattributes are included.</strike> The TEMPLATE now includes as LICENSE file, and other files are kept as is.</p>

<p><strike>

Follow the steps to create a new license file as below:
- Open the Repository
- Click "Add file" > "Create a New File"
- Type the name of the File as: LICENSE or LICENSE.txt or LICENSE.md
- Click on "Choose a License Template"
- Review and Submit
- Commit Changes as Required

</strike></p>

**NOTE:** some optional usage, specifications, and helpful links are as below:
  1. You can add GitHub Repository Badges from [Shields IO](https://shields.io/) - if this is a Public Repository;
  2. TAB (size = 4) has been used for indentation, except this file (README.md).
  3. `.github/workflows` is added however, it is recomended that you create your own workflows either using **GitHub Actions** or on your own.
  4. Basic `docker` files are added for convention, modify it as per requirement. Recomended to delete the file, if not required.
  5. The repository uses `markdown` instead of `rich text format`, so make necessary changes to file extension/type as required.

## Quick Start Guide
<p align = "justify">Introduced in 2019, users can now create a repository from templates in GitHub. To do this, simply head over to any repository settings and enable "Template Repository" from the Options Menu. When creating a <i>new repository</i> from this template, you can just click on <b><code>Use this template</code></b> available in this repository (refer the picture below).</p>

<img alt = "use_this_template_demo" src = "./assets/use_this_template_demo.png">

### Creating a NEW Repository from Template
<p align = "justify">Template Repository is not limited to GitHub, and you can setup your own local-file structure for the same. The following describes the usage of <code>rsync</code> which is available in most linux distros, <a href = "https://linux.die.net/man/1/rsync">more information on rsync</a>.</p>

```bash
# Note the use of rsync
rsync -rh ~/source/directory /destination/directory
```

## Setup Information
<p align = "justify">The template provides a <i>general</i> structure that I use (highly motivated from pandas dir and coding structure). There needs to be several things that need to be changed, just after initializing with the template, which are as follows:</p>

- `PKG` variable under `setup.py` has to be replaced with the module name and directory name `pkg-name`,
- Define High-Level Version Name (like 0.0.1, 0.1, 1.1, etc.) in `pkg-name/VERSION` file, to be interpreted by `setup.py`, and
- Define/Check/Update Author Name, Copyright Information (if any) in `setup.py` and `pkg-name/__init__.py`.

**TIP:** Install using `pip` by moving into the parent directory, with the following folder:
```bash
debmalya@machine:~$ ls -l
drwxrwxr-x 3 debmalya debmalya    4096 Aug 30 12:04  PYTHON_GIT_TEMPLATE
```
Finally, install it via:
```python
pip install ./PYTHON_GIT_TEMPLATE # Normal Installation
pip install -e ./PYTHON_GIT_TEMPLATE # Installation in Editable Mode
```

## flake8 Convention
Use the command `flake8 . --count --exit-zero --max-complexity=10 --statistics` to generate a report.
