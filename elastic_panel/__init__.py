# -*- coding: utf-8 -*-

"""
elastic_panel
~~~~~~~~~~~~~~

:copyright: (c) 2014 by Benoit Chabord
:license: See LICENSE for more details.

"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("django-elasticsearch-debug-toolbar")
except PackageNotFoundError:
    __version__ = "unknown"


__title__ = "elastic_panel"
__author__ = "Benoit Chabord"
__copyright__ = "Copyright 2014 Benoit Chabord"

VERSION = __version__
