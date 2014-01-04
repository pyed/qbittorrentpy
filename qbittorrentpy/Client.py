# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPDigestAuth
from Torrent import Torrent

class Client(object):
    """ handle qBittorrent API """

    def __init__(self, address='localhost', port=8080, username=None, password=None):
        self.address = address
        self.port = str(port)
        self.username = username
        self.password = password
        self.url = 'http://' + self.address + ':' + self.port

        self.session = requests.Session()
        self.session.auth = HTTPDigestAuth(self.username, self.password)

    def _GetRequest(self, url):
        url = self.url + url
        respond = self.session.get(url)

        return respond.json()

    def _PostRequest(self, url, data=None, files=None, echo=False):
        url = self.url + url
        respond = self.session.post(url, data=data, files=files)

        if echo: return respond.json()

    def _parse_input(self, torrent_id):
       torrents_dicts = self._GetRequest('/json/torrents')

       for d in torrents_dicts:
           if d['name'] == torrent_id or d['hash'] == torrent_id:
               return d

       raise ValueError("Invalid torrent id")

    def torrents(self):
        torrents_dicts = self._GetRequest('/json/torrents')

        return [x['name'] for x in torrents_dicts]

    def get_torrent(self, torrent_id):
        torrent_info = self._parse_input(torrent_id)

        return Torrent(torrent_info, self.session, self.url)

    def get_transinfo(self):
        return self._GetRequest('/json/transferInfo')

    def get_preferences(self):
        return self._GetRequest('/json/preferences')

    def add_torrentlink(self, link):
        self._PostRequest('/command/download',data={'urls': link})

    def add_torrentfile(self, tfile):
        self._PostRequest('/command/upload', files={'torrent': open(tfile, 'rb')})

    def pause_all(self):
        self._PostRequest('/command/pauseall')

    def resume_all(self):
        self._PostRequest('/command/resumeall')

    def get_downloadlimit(self):
        return self._PostRequest('/command/getGlobalDlLimit', echo=True)

    def get_uploadlimit(self):
        return self._PostRequest('/command/getGlobalUpLimit', echo=True)

    def set_downloadlimit(self, limit):
        self._PostRequest('/command/setGlobalDlLimit', data={'limit': limit})

    def set_uploadlimit(self, limit):
        self._PostRequest('/command/setGlobalUpLimit', data={'limit': limit})

    def set_preferences(self, **kwargs):
        import json
        self._PostRequest('/command/setPreferences', data={'json': json.dumps(kwargs)})

