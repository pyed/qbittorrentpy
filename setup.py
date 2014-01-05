#! /usr/bin/env python

from distutils.core import setup

config = {
        'name': 'qBittorrentPy',
        'version': '0.1',
        'description': 'python module to interact with qBittorrent API',
        'author': 'Abdulelah Alfntokh',
        'author_email': 'iAbdulelah@gmail.com',
        'url': 'http://github.com/pyed/qbittorrentpy',
        'packages': ['qbittorrentpy'],
        }

setup(**config)

