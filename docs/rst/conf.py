# -*- coding: utf-8 -*-
"""Config file for Sphinx-docs."""
from __future__ import unicode_literals

import os
import mock
import sys

import sphinx_py3doc_enhanced_theme


mock_modules = [
    'matplotlib',
    ]

for modulename in mock_modules:
    sys.modules[modulename] = mock.Mock()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    ]

todo_include_todos = True

exclude_patterns = [
    'i_*',
    ]

if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'
    # https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html
    spelling_word_list_filename = ['../spelling_wordlist.txt']

source_suffix = '.rst'
master_doc = 'index'
project = 'PyTorch Ranking'
year = '2021'
author = 'Alexander Zagniotov'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.0.1'

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/azagniotov/pytorch-ranking/issues/%s', '#'),  # noqa: E501
    'pr': ('https://github.com/azagniotov/pytorch-ranking/pull/%s', 'PR #'),  # noqa: E501
    }

# codecov io closes connection if host is accessed too repetitively.
# codecov links are ignored here for the same reason there's a sleep
# in the .travis.yml file
# see https://github.com/codecov/codecov-python/issues/158
linkcheck_ignore = [

    ]

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/azagniotov/pytorch-ranking',
    }

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
    }
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
