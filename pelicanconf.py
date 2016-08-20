#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from os.path import expanduser

AUTHOR = u'Geoff van der Meer'
SITENAME = u'pseudofish'

PLUGIN_PATHS = [expanduser('~') + '/src/pelican-plugins']
PLUGINS = ['sitemap','org_reader','cjk-auto-spacing',]

FEED_ATOM = 'atom.xml'
FEED_MAX_ITEMS = 15

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

IGNORE_FILES = ['*.#*']

THEME = 'themes/pseudofish'
CSS_FILE = 'main.css'
TYPOGRIFY = True
CJK_AUTO_SPACING_TITLE = True

ORG_READER_EMACS_LOCATION = '/usr/local/bin/emacs'

LINKS =  ()
SOCIAL = ()

DEFAULT_PAGINATION = 20

STATIC_PATHS = ['images']

FILES_TO_COPY = (('extras/robots.txt', 'robots.txt'),
                 ('extras/favicon.ico', 'favicon.ico'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
