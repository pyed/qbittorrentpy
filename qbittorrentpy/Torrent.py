# -*- coding: utf-8 -*-
class Torrent(object):
    """ class to manage a Torrent """

    def __init__(self, info, session, url):
        self.thash = info['hash']
        self.name = info['name']
        self.size = info['size']
        self.bytes_size = self._bytes_size()

        self._session = session
        self._url = url
        self.info = info 

    def _GetRequest(self, url):
        url = self._url + url + self.thash
        respond = self._session.get(url)

        return respond.json()

    def _PostRequest(self, url, data={}, echo=False):
        url = self._url + url

        if not data.has_key('hashes'):  # 'hashes' passed via deletion/priority methods
            data['hash'] = self.thash

        respond = self._session.post(url, data=data)

        if echo: return respond.json()

    def _bytes_size(self):
        units = {
            'KiB': 1024,
            'MiB': 1048576,
            'GiB': 1073741824
            }
        
        return int(float(self.size[:-4]) * units[self.size[-3:]])
    def properties(self):
        return self._GetRequest('/json/propertiesGeneral/')

    def trackers(self):
        return self._GetRequest('/json/propertiesTrackers/')

    def files(self):
        return self._GetRequest('/json/propertiesFiles/')

    def add_tracker(self, tracker):
        self._PostRequest('/command/addTrackers', data={'urls': tracker})

    def pause(self):
        self._PostRequest('/command/pause')

    def resume(self):
        self._PostRequest('/command/resume')

    def delete(self):
        self._PostRequest('/command/delete', data={'hashes': self.thash})
    
    def delete_with_data(self):
        self._PostRequest('/command/deletePerm', data={'hashes': self.thash})

    def recheck(self):
        self._PostRequest('/command/recheck')

    def increase_priority(self):
        self._PostRequest('/command/increasePrio', data={'hashes': self.thash})

    def decrease_priority(self):
        self._PostRequest('/command/decreasePrio', data={'hashes': self.thash})

    def max_priority(self):
        self._PostRequest('/command/topPrio', data={'hashes': self.thash})

    def min_priority(self):
        self._PostRequest('/command/bottomPrio', data={'hashes': self.thash})

    def set_file_priority(self, ID, priority_number):
        self._PostRequest('/command/setFilePrio', data={'id': ID, 'priority': priority_number})

    def get_downloadlimit(self):
        return self._PostRequest('/command/getTorrentDlLimit', echo=True)

    def get_uploadlimit(self):
        return self._PostRequest('/command/getTorrentUpLimit', echo=True)

    def set_downloadlimit(self, limit):
        self._PostRequest('/command/setTorrentDlLimit', data={'limit': limit})

    def set_uploadlimit(self, limit):
        self._PostRequest('/command/setTorrentUpLimit', data={'limit': limit})


