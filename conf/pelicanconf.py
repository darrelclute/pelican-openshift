#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from datetime import date

# Plugin settings, do not alter path without altering build script
PLUGIN_PATH = 'OPENSHIFT_DATA_DIR/pelican-plugins'
# Uncomment the following line to enable plugins, add or subtract as desired
# PLUGINS = ['assets', 'sitemap', 'gravatar']

# General Settings
SITEURL = u'http://SITE-URL'
SITENAME = u'SITE-NAME'
FEEDURL = SITEURL
AUTHOR = u'SITE-AUTHOR'

# Added drafts to article exclusion
ARTICLE_EXCLUDES = ('pages', 'drafts')

# Uncomment the following line to have the static content from theme at / instead of /theme, alter to change to desire.
#THEME_STATIC_DIR = ''
