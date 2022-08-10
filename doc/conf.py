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

import datetime
import xml.etree.ElementTree as ET

# -- Project information -----------------------------------------------------

project = 'SSH-MITM'
author = 'SSH-MITM Dev-Team'
copyright = f'{datetime.datetime.now().year}, {author}'  # pylint: disable=redefined-builtin

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_sitemap',
    'sphinx_reredirects',
    'sphinx_design',
    'notfound.extension',
]

html_theme = "pydata_sphinx_theme"
html_sidebars = {
    "index": [],
    "**": ["sidebar-nav-bs"]
}
html_title = "SSH-MITM"
html_logo = "_static/ssh-mitm-logo.svg"


html_theme_options = {
    "logo": {
        "text": "SSH-MITM",
    },
    "github_url": "https://github.com/ssh-mitm/ssh-mitm",
    "navbar_end": ["navbar-icon-links.html", "search-field.html"],
    "navbar_align": "left",

    "page_sidebar_items": ["page-toc", "edit-this-page"],
    "footer_items": ["copyright"],
    "show_prev_next": False,
    "navigation_with_keys": False,
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/ssh-mitm",
            "icon": "fab fa-python",
        }
    ],
    "show_toc_level": 1,
    "use_edit_page_button": True,
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "ssh-mitm",
    "github_repo": "ssh-mitm",
    "github_version": "develop",
    "doc_path": "doc",
}

notfound_no_urls_prefix = True

master_doc = 'index'
html_permalinks = False
html_baseurl = 'https://docs.ssh-mitm.at/'
autosectionlabel_maxdepth = 1
html_extra_path = ['robots.txt']

# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

redirects = {
    # CVEs
    "puttydos": "vulnerabilities/CVE-2021-33500.html",
    'CVE-2016-20012': 'vulnerabilities/CVE-2016-20012.html',
    'CVE-2018-15473': 'vulnerabilities/CVE-2018-15473.html',
    'CVE-2018-15599': 'vulnerabilities/CVE-2018-15599.html',
    'CVE-2018-15919': 'vulnerabilities/CVE-2018-15919.html',
    'CVE-2018-20685': 'vulnerabilities/CVE-2018-20685.html',
    'CVE-2019-16905': 'vulnerabilities/CVE-2019-16905.html',
    'CVE-2019-6109': 'vulnerabilities/CVE-2019-6109.html',
    'CVE-2019-6110': 'vulnerabilities/CVE-2019-6110.html',
    'CVE-2019-6111': 'vulnerabilities/CVE-2019-6111.html',
    'CVE-2020-12062': 'vulnerabilities/CVE-2020-12062.html',
    'CVE-2020-14002': 'vulnerabilities/CVE-2020-14002.html',
    'CVE-2020-14145': 'vulnerabilities/CVE-2020-14145.html',
    'CVE-2020-15778': 'vulnerabilities/CVE-2020-15778.html',
    'CVE-2021-28041': 'vulnerabilities/CVE-2021-28041.html',
    'CVE-2021-33500': 'vulnerabilities/CVE-2021-33500.html',
    'CVE-2021-36367': 'vulnerabilities/CVE-2021-36367.html',
    'CVE-2021-36368': 'vulnerabilities/CVE-2021-36368.html',
    'CVE-2021-36369': 'vulnerabilities/CVE-2021-36369.html',
    'CVE-2021-36370': 'vulnerabilities/CVE-2021-36370.html',
    'CVE-2021-41617': 'vulnerabilities/CVE-2021-41617.html',
    'CVE-2022-29154': 'vulnerabilities/CVE-2022-29154.html'
}


# -- Options for PDF output --------------------------------------------------

sd_fontawesome_latex = True



# -- Helper functions ----------------------------------------------------------

def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    filename = app.outdir + "/sitemap-docs.xml"
    print("Generating sitemap-docs.xml in %s" % filename)

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = html_baseurl + link

    ET.ElementTree(root).write(filename)


def setup(app):
    app.connect('build-finished', create_sitemap)
