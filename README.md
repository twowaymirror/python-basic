# Python basics

Playing around with some Python concepts

## Markdown

[Markdown specification]: https://spec.commonmark.org/0.30/ "Markdown specification"
[Markdown specification]

## Sphinx

[Starting a sphinx documentation from existing project]: https://docs.mozilla-releng.net/en/latest/adding_docs_to_existing_code.html#docs-from-scratch "starting sphinx project"
[Starting a sphinx documentation from existing project]

[Autodoc - Generating documentation from docstrings]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[Autodoc - Generating documentation from docstrings]

[Markdown in Sphinx]: https://www.sphinx-doc.org/en/master/usage/markdown.html
[Markdown in Sphinx]

[MyST]: https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html
[MyST] is a way to use Markdown in Sphinx

[Sphinx Docker image]:https://github.com/sphinx-doc/docker
[Sphinx Docker image]

[YouTube guide on how to add modules]: https://www.youtube.com/watch?v=b4iFyrLQQh4
[YouTube guide on how to add modules]

### Installed packages for Sphinx

* pip install sphinx
* pip install myst-parser

### Using Sphinx for generating documentation

It is important that there are __init__.py in the folders that is going to be part of the 
documentation.

sphinx-apidoc --maxdepth 6 --force --output-dir docs/src .

stopped using: make --always-make html
started using: sphinx-build -b html source build

***Good guides when troubleshooting***

[stack1]: https://stackoverflow.com/questions/59903051/sphinxs-autodocs-automodule-having-apparently-no-effect/59951675#59951675
[stack1]
