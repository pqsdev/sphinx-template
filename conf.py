# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import date

# -- Project information -----------------------------------------------------

project = 'Plantilla documentación Sphinx'
copyright = f"{date.today().year}, YUUDJ"
author = 'YUUDJ'

master_doc = "index"

# The full version, including alpha/beta/rc tags
release = 'https://gitlab.com/pages/sphinx'
language = "es"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinxext.opengraph',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.swaggerui'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# markdown
myst_html_meta = {
    "description lang=en": "metadata description",
    "description lang=es": "descripcion de metadata",
    "keywords": "Sphinx, MyST",
    "property=og:locale":  "es_AR"
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db',
                    '.DS_Store', '.vscode', '.devcontainer', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_theme_path = ["_themes", ]
html_logo = "_static/logo-wide.svg"
html_favicon = "_static/logo-square.svg"
html_title = "Sphinx doc template"
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/pqsdev/sphynx-template",
    "repository_url": "https://github.com/pqsdev/sphynx-template",
    "repository_branch": "main",
    "path_to_docs": "/",
    "use_repository_button": True,
    "use_edit_page_button": True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# OpenGraph metadata
ogp_site_url = "https://pqs.com.ar"
# This is the image that GitHub stores for our social media previews
ogp_image = "https://avatars.githubusercontent.com/u/23339726"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image">',
]
