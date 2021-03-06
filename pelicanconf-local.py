#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Members of the ML-KA group'
SITENAME = u'Machine Learning - Karlsruhe'
SITEURL = '//127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub/ML-KA', 'http://127.0.0.1:8000/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/mlkarlsruhe'),
          # ('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

PLUGIN_PATHS = ['./pelican-bootstrapify',
                './pelican_plugin-render_math',
                './simple_footnotes',
                './pelican-toc']
PLUGINS = ['bootstrapify',
           'pelican_plugin-render_math',
           'simple_footnotes',
           'toc']

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
