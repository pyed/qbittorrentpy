Simple python module to interact with [qBittorrent](https://github.com/qbittorrent/qBittorrent)
---------------------------------

Requestemetns
------
    * [requests](https://github.com/kennethreitz/requests)

How to install ?
-----
`python setup.py install`

How to use ?
------

the `Client` object:
~~~~~ python
import qbittorrentpy
c = qbittorrentpy.Client('localhost', username='me', password='you', port=9091)        # connect to qbittorent

c.torrents()    # return torrents list
#[Out]# [u'ubuntu-12.04.3-alternate-amd64.iso']

c.get_transinfo()       # return the current speeds
#[Out]# {u'dl_info': u'D: 5.2 KiB/s - T: 143.8 KiB', u'up_info': u'U: 0 B/s - T: 0 B'}

c.pause_all()

c.get_transinfo()
#[Out]# {u'dl_info': u'D: 0 B/s - T: 347.2 KiB', u'up_info': u'U: 0 B/s - T: 0 B'}

c.resume_all()

c.set_downloadlimit(1234)

c.get_downloadlimit()
#[Out]# 1234

c.set_uploadlimit(4321)

c.get_uploadlimit()
#[Out]# 4321

c.add_torrentlink('http://releases.ubuntu.com/13.10/ubuntu-13.10-desktop-amd64.iso.torrent')  # add torrent via link

c.torrents()
#[Out]# [u'ubuntu-12.04.3-alternate-amd64.iso', u'ubuntu-13.10-desktop-amd64.iso']            # now it's there

c.add_torrentfile('/Users/pyed/Desktop/ubuntu-13.10-server-amd64.iso.torrent')                # add local torrent file

c.torrents()
#[Out]# [u'ubuntu-13.10-server-amd64.iso',              # added via local file
#[Out]#  u'ubuntu-12.04.3-alternate-amd64.iso',
#[Out]#  u'ubuntu-13.10-desktop-amd64.iso']             # added via link

c.get_preferences()     # dump all the preferences
#[Out]# {u'alt_dl_limit': 10,
#[Out]#  u'alt_up_limit': 1,
#[Out]#  u'anonymous_mode': False,
#[Out]#  u'autorun_enabled': False,
#[Out]#  u'autorun_program': u'/Users/pyed/Dropbox/Scripts/qBitnew.py "%n" "%f"',
#[Out]#  u'bypass_local_auth': True,
#[Out]#  u'dht': False,
#[Out]#  u'dhtSameAsBT': True,
#[Out]#  u'dht_port': 6881,
#[Out]#  u'dl_limit': 1,
#[Out]#  u'dont_count_slow_torrents': False,
#[Out]#  u'download_in_scan_dirs': [False],
#[Out]#  u'dyndns_domain': u'changeme.dyndns.org',
#[Out]#  u'dyndns_enabled': False,
#[Out]#  u'dyndns_password': None,
#[Out]#  u'dyndns_service': 0,
#[Out]#  u'dyndns_username': None,
#[Out]#  u'enable_utp': True,
#[Out]#  u'encryption': 2,
#[Out]#  u'export_dir': None,
#[Out]#  u'export_dir_enabled': False,
#[Out]#  u'incomplete_files_ext': False,
#[Out]#  u'ip_filter_enabled': False,
#[Out]#  u'ip_filter_path': None,
#[Out]#  u'limit_tcp_overhead': False,
#[Out]#  u'limit_utp_rate': True,
#[Out]#  u'listen_port': 30812,
#[Out]#  u'locale': u'en_US',
#[Out]#  u'lsd': True,
#[Out]#  u'mail_notification_auth_enabled': False,
#[Out]#  u'mail_notification_email': None,
#[Out]#  u'mail_notification_enabled': False,
#[Out]#  u'mail_notification_password': None,
#[Out]#  u'mail_notification_smtp': u'smtp.changeme.com',
#[Out]#  u'mail_notification_ssl_enabled': False,
#[Out]#  u'mail_notification_username': None,
#[Out]#  u'max_active_downloads': 3,
#[Out]#  u'max_active_torrents': 5,
#[Out]#  u'max_active_uploads': 3,
#[Out]#  u'max_connec': 500,
#[Out]#  u'max_connec_per_torrent': 100,
#[Out]#  u'max_uploads_per_torrent': 4,
#[Out]#  u'pex': True,
#[Out]#  u'preallocate_all': False,
#[Out]#  u'proxy_auth_enabled': False,
#[Out]#  u'proxy_ip': u'0.0.0.0',
#[Out]#  u'proxy_password': None,
#[Out]#  u'proxy_peer_connections': False,
#[Out]#  u'proxy_port': 8080,
#[Out]#  u'proxy_type': -1,
#[Out]#  u'proxy_username': None,
#[Out]#  u'queueing_enabled': False,
#[Out]#  u'save_path': u'/Users/pyed/Downloads',
#[Out]#  u'scan_dirs': [u'/Users/pyed/Downloads'],
#[Out]#  u'schedule_from_hour': 8,
#[Out]#  u'schedule_from_min': 0,
#[Out]#  u'schedule_to_hour': 20,
#[Out]#  u'schedule_to_min': 0,
#[Out]#  u'scheduler_days': 0,
#[Out]#  u'scheduler_enabled': False,
#[Out]#  u'ssl_cert': u'',
#[Out]#  u'ssl_key': u'',
#[Out]#  u'temp_path': u'/Users/pyed/Downloads/temp',
#[Out]#  u'temp_path_enabled': False,
#[Out]#  u'up_limit': 4,
#[Out]#  u'upnp': True,
#[Out]#  u'use_https': False,
#[Out]#  u'web_ui_password': u'c2a23454365762345645235647c09cdd',
#[Out]#  u'web_ui_port': 9091,
#[Out]#  u'web_ui_username': u'admin'}

~~~~~

the `Torrent` object

~~~~~ python
import qbittorrentpy
c = qbittorrentpy.Client('127.0.0.1', username='admin', password='qbit', port=9091)

c.torrents()    # check on torrents names
#[Out]# [u'ubuntu-13.10-server-amd64.iso',
#[Out]#  u'ubuntu-12.04.3-alternate-amd64.iso',
#[Out]#  u'ubuntu-13.10-desktop-amd64.iso']

t = c.get_torrent('ubuntu-13.10-server-amd64.iso')      # select torrent by name, you can select it via hash as well 

t.name
#[Out]# u'ubuntu-13.10-server-amd64.iso'

t.thash
#[Out]# u'6a36de201df2f1b2c817474c3075ff0eaa8c7785'

t.size
#[Out]# u'672.0 MiB'

t.bytes_size
#[Out]# 704643072

t.pause()
t.recheck()
t.resume()

t.add_tracker('http://announce.tracker.io')

t.trackers()
#[Out]# [{u'msg': u'',
#[Out]#   u'num_peers': u'50',
#[Out]#   u'status': u'Working',
#[Out]#   u'url': u'http://torrent.ubuntu.com:6969/announce'},
#[Out]#  {u'msg': u'',
#[Out]#   u'num_peers': u'0',
#[Out]#   u'status': u'Not working',
#[Out]#   u'url': u'http://announce.tracker.io'},
#[Out]#  {u'msg': u'',
#[Out]#   u'num_peers': u'0',
#[Out]#   u'status': u'Not contacted yet',
#[Out]#   u'url': u'http://ipv6.torrent.ubuntu.com:6969/announce'}]

t.files()
#[Out]# [{u'is_seed': False,
#[Out]#   u'name': u'ubuntu-13.10-server-amd64.iso',
#[Out]#   u'priority': 1,
#[Out]#   u'progress': 0,
#[Out]#   u'size': u'672.0 MiB'}]

t.set_downloadlimit(1337)
t.set_uploadlimit(7331)

t.get_downloadlimit()
#[Out]# 1337

t.get_uploadlimit()
#[Out]# 7331

t.increase_priority()
t.max_priority()
t.delete()      # delete and keep files

c.torrents()
#[Out]# [u'ubuntu-12.04.3-alternate-amd64.iso', u'ubuntu-13.10-desktop-amd64.iso']

t = c.get_torrent(c.torrents()[0])
t.name
#[Out]# u'ubuntu-12.04.3-alternate-amd64.iso'

t.delete_with_data()    # delete with files, be careful

~~~~~
