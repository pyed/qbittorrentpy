#!/usr/bin/env python

from setuptools import setup

config = {
        'name': 'qBittorrentPy',
        'version': 0.1,
        'description': 'python module interacts with qBittorrent API',
        'author': 'Abdulelah Alfntokh',
        'author_email': 'iAbdulelah@gmail.com',
        'url': 'http://github.com/pyed/qbittorrentpy',
        'packages': ['qbittorrentpy'],
        'install_requires': ['requests']
        }

setup(**config)

