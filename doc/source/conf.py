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
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))


# -- Project information -----------------------------------------------------

project = 'Minimal Sphinx Documentation with Latex and PDF generation'
copyright = '2023, Jacques LE THUAUT'
author = 'Jacques LE THUAUT'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.doctest',
	'sphinx.ext.imgmath',
	'sphinx.ext.todo', 
	'breathe',
	'sphinx.ext.napoleon'
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = ['.rst', '.md']
autosummary_generate = True


# -- Options for LATEX output -------------------------------------------------


latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
		\setmainfont{DejaVu Serif}
		\setsansfont{DejaVu Sans}
		\setmonofont{DejaVu Sans Mono}
	''',
    'preamble': r'''
		r'\input{path/to/your/template.tex}',
		\usepackage[titles]{tocloft}
		\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
		\setlength{\cftchapnumwidth}{0.75cm}
		\setlength{\cftsecindent}{\cftchapnumwidth}
		\setlength{\cftsecnumwidth}{1.25cm}
	''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'
