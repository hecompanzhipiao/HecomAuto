import logging
import socket
import string
import base64


try:
    import http.client as httplib
    from urllib import request as url_request
    from urllib import parse
except ImportError: # above is available in py3+, below is py2.7
    import httplib as httplib
    import urllib2 as url_request
    import urlparse as parse

from .command import Command
from .errorhandler import ErrorCode
from . import utils

LOGGER = logging.getLogger(__name__)

class RemoteConnection(object):
    _timeout = socket._GLOBAL_DEFAULT_TIMEOUT

    def __init__(self, remote_server_addr, keep_alive=False, resolve_ip=True):
        # Attempt to resolve the hostname and get an IP address.
        self.keep_alive = keep_alive
        parsed_url = parse.urlparse(remote_server_addr)
        addr = ""
        if parsed_url.hostname and resolve_ip:
            try:
                netloc = socket.gethostbyname(parsed_url.hostname)
                addr = netloc
                if parsed_url.port:
                    netloc += ':%d' % parsed_url.port
                if parsed_url.username:
                    auth = parsed_url.username
                    if parsed_url.password:
                        auth += ':%s' % parsed_url.password
                    netloc = '%s@%s' % (auth, netloc)
                remote_server_addr = parse.urlunparse(
                    (parsed_url.scheme, netloc, parsed_url.path,
                     parsed_url.params, parsed_url.query, parsed_url.fragment))
            except socket.gaierror:
                LOGGER.info('Could not get IP address for host: %s' % parsed_url.hostname)

        self._url = remote_server_addr
        if keep_alive:
            self._conn = httplib.HTTPConnection(
                str(addr), str(parsed_url.port), timeout=self._timeout)

        self._V6commands = {

        }
        self._V4commands = {

        }
    def execute(self,command,userStr=None,downlinkReqStr=None,body=None):
        pass
    def _request():
        pass





