# https://github.com/executablebooks/sphinx-book-theme/blob/master/docs/conf.py

# TODO
# html_title = "<a href='https://thumpcc.github.io'>home</a>"
# html_logo = "path/to/logo.png"
# html_favicon = "path/to/favicon.ico"

# manpages_url = 'https://man7.org/linux/man-pages/man{section}/{page}.{section}.html'
manpages_url = 'https://linux.die.net/man/{section}/{page}'
numfig = True

rst_prolog = """
.. role:: python(code)
    :language: python

"""

templates_path = [
    '_files_common/templates',
]

exclude_patterns = [
    '_files_common',
    'README.md',
    '*thydev*', '**/*thydev*',
    '_snippets',
]

html_show_sphinx = False
html_show_copyright = False

# https://sphinx-book-theme.readthedocs.io/en/latest/
html_theme = 'sphinx_book_theme'

# https://sphinx-book-theme.readthedocs.io/en/latest/customize/
html_theme_options = {
    # 'logo_only'            : True,

    'navigation_with_keys' : True,
    # 'extra_navbar'         : None,
    # 'sidebar_hide_name'   : True,
    'use_download_button'  : False,
    'use_fullscreen_button': False,
    'use_sidenotes'        : True,

    # https://sphinx-book-theme.readthedocs.io/en/latest/components/source-files.html
    'repository_provider'  : 'github',
    'repository_url'       : 'https://thump.cc/thynotes.git',
    # 'path_to_docs'         : '',
    'repository_branch'    : 'main',
    'use_repository_button': True,
    'use_source_button'    : True,
    'use_edit_page_button' : True,
    'use_issues_button'    : True,

    'show_toc_level'       : 2,
    'article_footer_items' : ['footer-article.html']
}
html_last_updated_fmt = "%d-%b-%Y"

html_css_files = [
    'custom.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
]
html_js_files = [
    'custom.js',
]
html_static_path = ['_files_common/static']
html_extra_path = []
html_show_sourcelink = False

images_config = {
    'cache_path': '_files/sphinxcontrib.images'
}

source_suffix = {
    '.rst': 'restructuredtext',
    # '.ipynb': 'myst-nb',
    '.md' : 'markdown',
}

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#block-attributes
    "attrs_block",
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#inline-attributes
    "attrs_inline",
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3
myst_url_schemes = ("http", "https", "mailto")

autosectionlabel_prefix_document = True

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
# copybutton_copy_empty_lines = False
copybutton_line_continuation_character = "\\"
copybutton_here_doc_delimiter = "EOT"
copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

extensions = [
    # https://www.sphinx-doc.org/en/master/usage/extensions/index.html
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',

    # https://sphinx-autodoc2.readthedocs.io/en/latest/index.html
    # 'autodoc2',

    # If you are using MyST-NB in your documentation, do not activate `myst-parser`. It will
    # be automatically activated by `myst-nb`.
    'myst_parser',

    # https://myst-nb.readthedocs.io/en/latest/
    # 'myst_nb',

    # https://sphinx-tippy.readthedocs.io/en/latest/
    # 'sphinx_tippy',

    # https://sphinx-toolbox.readthedocs.io/en/latest/index.html
    'sphinx_toolbox.wikipedia',

    # https://sphinx-copybutton.readthedocs.io/en/latest/
    'sphinx_copybutton',

    # https://sphinx-design.readthedocs.io/en/latest/
    'sphinx_design',

    # https://sphinx-inline-tabs.readthedocs.io/en/latest/
    'sphinx_inline_tabs',

    # https://ablog.readthedocs.io/en/stable/
    'ablog',

    # https://numpydoc.readthedocs.io/en/latest/index.html
    'numpydoc',

    # https://ebp-sphinx-examples.readthedocs.io/en/latest/
    'sphinx_examples',

    # https://sphinx-tabs.readthedocs.io/en/latest/
    # 'sphinx_tabs.tabs',

    # https://sphinx-thebe.readthedocs.io/en/latest/
    # http://thebe.readthedocs.org/
    # 'sphinx_thebe',

    # Collapse admonitions
    # https://sphinx-togglebutton.readthedocs.io/en/latest/
    'sphinx_togglebutton',

    # https://sphinx-panels.readthedocs.io/en/sphinx-book-theme/
    # Not actively maintained. Use sphinx-design instead
    # 'sphinx_panels',

    # https://github.com/mgaitan/sphinxcontrib-mermaid
    'sphinxcontrib.mermaid',

    # https://sphinxcontrib-images.readthedocs.io/en/latest/
    'sphinxcontrib.images',

    # https://sphinxcontrib-youtube.readthedocs.io/en/latest/
    'sphinxcontrib.youtube',

    # https://sphinxcontrib-bibtex.readthedocs.io/en/latest/quickstart.html
    # 'sphinxcontrib.bibtex',

]

# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
# https://www.sphinx-doc.org/en/master/examples.html
intersphinx_mapping = {
    # 'thy_main'         : ('https://thy.readthedocs.io/', None),
    # 'thy_python'       : ('https://thy-python.readthedocs.io/', None),
    # 'thy_azure'        : ('https://thy-azure.readthedocs.io/', None),
    # 'thy_devops'       : ('https://thy-devops.readthedocs.io/', None),
    # 'thy_qknotes'      : ('https://thy-qknotes.readthedocs.io/', None),
    # 'thy_systems'      : ('https://thy-systems.readthedocs.io/', None),
    # 'thy_misc'         : ('https://thy-misc.readthedocs.io/', None),

    'sphinx'           : ('https://www.sphinx-doc.org/en/master/', None),
    'jupyterbook'      : ('https://jupyterbook.org/en/stable/', None),
    'myst_parser'      : ('https://myst-parser.readthedocs.io/en/latest/', None),
    'myst_nb'          : ('https://myst-nb.readthedocs.io/en/latest/', None),
    'sphinx_book_theme': ('https://sphinx-book-theme.readthedocs.io/en/stable/', None),

    'py3'              : ('https://docs.python.org/3/', None),
    'numpy'            : ('https://numpy.org/doc/stable/', None),
    'pandas'           : ('https://pandas.pydata.org/pandas-docs/stable', None),
    'pydevguide'       : ('https://devguide.python.org/', None),
    'python_guide_org' : ('https://docs.python-guide.org/', None),
    'django'           : ('https://docs.djangoproject.com/en/3.2/', 'https://docs.djangoproject.com/en/3.2/_objects/'),
    'jinja'            : ('https://jinja.palletsprojects.com/en/3.1.x/', None),
    'requests'         : ('https://requests.readthedocs.io/en/latest/', None),
    'podman'           : ('https://docs.podman.io/en/stable/', None),
    'molecule'         : ('https://molecule.readthedocs.io/en/stable/', None),
    'bs4'              : ('https://www.crummy.com/software/BeautifulSoup/bs4/doc/', None),
    'buildbot'         : ('https://docs.buildbot.net/latest/', None),
    'pypa'             : ('https://www.pypa.io/en/latest/', None),
    'waf'              : ('https://waf.io/apidocs/', None),
    'setuptools'       : ('https://setuptools.pypa.io/en/latest/', None),
    'ansible'          : ('https://docs.ansible.com/ansible/latest/', None),
    'conda'            : ('https://conda.io/en/latest/', None),
    'dnf'              : ('https://dnf.readthedocs.io/en/latest/', None),
    'pip'              : ('https://pip.pypa.io/en/stable/', None),
    'pelican'          : ('https://docs.getpelican.com/en/latest/', None),
    'rtfd'             : ('https://docs.readthedocs.io/en/stable/', None),
    'wagtail'          : ('https://docs.wagtail.org/en/stable/', None),
    'boto3'            : ('https://boto3.amazonaws.com/v1/documentation/api/latest/', None),
    'ceph'             : ('https://docs.ceph.com/en/latest/', None),
    'psycopg'          : ('https://www.psycopg.org/docs/', None),
    'sqlalchemy'       : ('https://docs.sqlalchemy.org/en/14/', None),

    'blender'          : ('https://docs.blender.org/manual/en/latest/', None),
    'blenderapi'       : ('https://docs.blender.org/api/current/', None),

    'circuitpython'    : ('https://docs.circuitpython.org/en/latest/', None),
    'micropython'      : ('https://docs.micropython.org/en/latest/', None),

    # ''     : ('', None),
    # ''     : ('', None),

    # objects.inv is not found
    # 'pygments'   : ('https://pygments.org/docs/', None),
    # 'selenium'   : ('https://www.selenium.dev/documentation/', None),
    # 'opencv'     : ('https://docs.opencv.org/4.x/', None),
}
