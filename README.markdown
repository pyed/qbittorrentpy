Simple python module to interact with qBittorrent/qBittorrent API
============================================================

*How to use*
~~~~~ python
import qbittorrentpy
c = qbittorrentpy.Client('localhost', port=9091)

c.torrents()
#[Out]# [u'ubuntu-12.04.3-alternate-amd64.iso']

c.get_transinfo()
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

c.add_torrentlink('http://releases.ubuntu.com/13.10/ubuntu-13.10-desktop-amd64.iso.torrent')

c.torrents()
#[Out]# [u'ubuntu-12.04.3-alternate-amd64.iso', u'ubuntu-13.10-desktop-amd64.iso']

c.add_torrentfile('/Users/pyed/Desktop/ubuntu-13.10-server-amd64.iso.torrent')

c.torrents()
#[Out]# [u'ubuntu-13.10-server-amd64.iso',
#[Out]#  u'ubuntu-12.04.3-alternate-amd64.iso',
#[Out]#  u'ubuntu-13.10-desktop-amd64.iso']

c.get_preferences()
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

