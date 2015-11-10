#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jungledroid'
SITENAME = 'Jungledroid'
#SITEURL = ''
SITEURL = 'http://jungledroid.gitcafe.io'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'
#custom default config 
DEFAULT_DATE = 'fs'
STATIC_PATHS = ['images','duoshuo']
#THEME = 'themes/pelican-elegant-1.3'
#THEME = 'niu-x2'
THEME = 'pelican-themes/gum'
#THEME = 'pelican-themes/notmyidea-cms'
#THEME = 'pelican-themes/pelican-bootstrap3'
#THEME = 'pelican-themes/notebook'

DUOSHUO_SITENAME = "jungledroid"

EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
}


#custom the config
DISPLAY_CATEGORIES_ON_MENU  = False
OUTPUT_RETENTION = ['.git']
JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
