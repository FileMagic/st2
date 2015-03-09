# -*- coding: utf-8 -*-
#
# StackStorm documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  7 21:52:49 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import itertools

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../st2common'))
sys.path.insert(0, os.path.abspath('./_themes'))

from st2common import __version__

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',

    # Add theme as extension so sitemap.xml is generated
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'StackStorm'
copyright = u'2014, StackStorm Inc'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# the __version__ is 0.8.1 or 0.9dev
# the version is short 0.8 version, to refer docs.
version = '.'.join(__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = __version__


def previous_version(ver):
    # XXX: on incrementing major version, minor version counter is lost!
    major, minor = ver.split('.')
    minor = int("".join(itertools.takewhile(str.isdigit, minor)))
    return ".".join([major, str(minor - 1)])

# The short versions of two previous releases, e.g. 0.8 and 0.7
version_minus_1 = previous_version(version)
version_minus_2 = previous_version(version_minus_1)

# extlink configurator sphinx.ext.extlinks
extlinks = {
    'github_st2': ('https://github.com/StackStorm/st2/blob/master/%s', None),
    'github_mistral': ('https://github.com/StackStorm/mistral/blob/master/%s', None),
    'github_contrib':
        ('https://github.com/StackStorm/st2contrib/blob/master/%s', None),
    'github_devenv': ('https://github.com/StackStorm/devenv/blob/master/%s', None)
}

# Inserted at the bottom of all rst files.
# Use for variables substitutions
rst_epilog = """
.. |st2| replace:: StackStorm
.. _st2contrib: http://www.github.com/stackstorm/st2contrib
.. _st2incubator: http://www.github.com/stackstorm/st2incubator
"""

# Show or hide TODOs. See http://sphinx-doc.org/ext/todo.html
todo_include_todos = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# dzimine: '**/._*' exclues files my Sublime creates on NFS mount.
exclude_patterns = [
    '**/._*',
    'engage.rst',  # included file
    'install/on_complete.rst',  # included file
    'todo.rst',  # included file
    'authentication.rst'  # not included right now
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'base_url': 'http://docs.stackstorm.com/'
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
html_theme_path = ["_themes", ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'StackStormDoc'

# Variables to be used by templates
html_context = {
    'github_repo': 'StackStorm/st2',
    'github_version': 'master',
    'conf_py_path': '/docs/source/',
    'display_github': True,
    'source_suffix': source_suffix,
    'versions': [
        ('latest', 'http://docs.stackstorm.com/latest'),
        (version, 'http://docs.stackstorm.com/latest'),
        (version_minus_1, 'http://docs.stackstorm.com/%s' % version_minus_1),
        (version_minus_2, 'http://docs.stackstorm.com/%s' % version_minus_2),
    ],
    'current_version': version
}


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'stackstorm', u'StackStorm Documentation',
     [u'StackStorm team'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'StackStorm', u'StackStorm Documentation',
     u'StackStorm team', 'StackStorm', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
