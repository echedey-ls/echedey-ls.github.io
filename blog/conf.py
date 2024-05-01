# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Echedey's personal blog"
copyright = "2024, Echedey Luis"
author = "Echedey Luis"
release = "0.0.1"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_immaterial",
]


templates_path = ["templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
source_suffix = ".rst"
# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
html_static_path = ["static"]

# -- Theme options -----------------------------------------------------------
# Set link name generated in the top bar.
html_title = project

# Material theme options (see theme.conf for more information)
html_theme_options = {
    "palette": {
        "scheme": "slate",  # Dark color scheme for the website
        "primary": "deep-purple",  # main color
        "accent": "purple",  # accent color
    },
    "font": False,  # Use the system font stack
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/echedey-ls/echedey-ls.github.io/",
    "repo_name": "echedey-ls.github.io",
    # If False, expand all TOC entries
    "globaltoc_collapse": False,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
}

# -- Blog options ------------------------------------------------------------
# https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html
blog_title = "Echedey's blog"
blog_path = "gsoc-2024"
blog_baseurl = "https://echedey-ls.github.io/echedey-ls/blog"
blog_authors = {
    "Echedey": ("Echedey Luis", "https://echedey-ls.github.io"),
}
blog_default_author = "Echedey"
# stick to ISO 8601
post_date_format = r"%Y-%m-%d"
post_date_format_short = r"%Y-%m-%d"
