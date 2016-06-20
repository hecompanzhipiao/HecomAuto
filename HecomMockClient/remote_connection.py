import logging
import requests




LOGGER = logging.getLogger(__name__)

class RemoteConnection(object):
    _timeout = socket._GLOBAL_DEFAULT_TIMEOUT

    def __init__(self, remote_server_addr):
        self._header={}
        self._server=remote_server_addr

    
    def execute(self,command,userStr=None,downlinkReqStr=None,body=None):
        
        pass
    def _request():
        pass





