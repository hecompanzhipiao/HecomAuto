import logging
import requests
from command import *
import json


LOGGER = logging.getLogger(__name__)

class RemoteConnection(object):
    #_timeout = socket._GLOBAL_DEFAULT_TIMEOUT

    def __init__(self, host,headers):
        self._headers=headers
        self._host=host

    
    def execute(self,command,userStr=None,downlinkReqStr=None,body=None):
        command_info = V6Command.V6Commands[command] #TODO 根据版本不同切换command

        url = self._geturl(command_info[1],userStr,downlinkReqStr)

        if userStr :
            jsonStr=str(json.dumps(userStr))
            rsp  =  requests.request(method=command_info[0],url=url,params={'userStr':jsonStr},data=body,headers=self._headers)
        elif downlinkReqStr :
            jsonStr=str(json.dumps(downlinkReqStr))
            rsp  =  requests.request(method=command_info[0],url=url,params={'downlinkReqStr':jsonStr},data=body,headers=self._headers)
        else:
            rsp  =  requests.request(method=command_info[0],url=url,data=body,headers=self._headers)
        return rsp
  

    def _geturl(self,apiUrl,userStr,downlinkReqStr):

        if '{entCode}' in apiUrl or '{authUrl}' in apiUrl:
            if  not self._headers.has_key('entCode') :
                raise RuntimeError('could not get entcode, maybe not logged in')
            url = apiUrl.replace("host:port",self._host).replace("@@","mobile-0.0.1-SNAPSHOT") \
                                .replace("##","rcm") \
                                .replace("{entCode}",self._headers['entCode'])  \
                                .replace("{authUrl}",'http://'+self._host+'/mobile-0.0.1-SNAPSHOT/rcm/e/'+self._headers['entCode']) 
        else:
            url=apiUrl.replace('host:port',self._host).replace("@@","mobile-0.0.1-SNAPSHOT").replace("##","rcm")


        return url

    def  addHeaders(self,dictHeader):
        pass

    def  setHeaders(self,headers):
        self._headers=headers



