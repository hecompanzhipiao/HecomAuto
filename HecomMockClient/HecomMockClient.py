#from .Rsphandler import *


from remote_connection import RemoteConnection
from command import Command
import logging



class HecomMockClient(object):
    def __init__(self,server,clientType,tid,version='6.0'):
        #版本不一样，支持的命令是不一样的

        #self.clientRsphandler=RspHandler()  # result 非0全部抛异常
        #self.paramChecker=
        #self.rsp_handler=RspHandler()
        #日志模块
        #self.LOG=

        self._host=server
        self._version=version
        self._clientType=clientType
        self._tid=tid
        self._headers={"version":self._version,"tid":self._tid,"clientType":self._clientType}
        self.command_executor=RemoteConnection(server,self._headers)


    def handle_response(self,rsp,exceptcode= '0'):
        if rsp.status_code!=200 :
            rsp.raise_for_status()
        #判断是非为json数据
        try:
            jsonRsp=rsp.json()
        except:
            raise RuntimeError( "decode json failed")
        else:
            logging.info('Got Response  : %s' % jsonRsp)

            if jsonRsp['result']!= exceptcode : 
                raise RuntimeError("command execute failed: %s return resultcode %s desc %s" % (self.currentCommand,jsonRsp['result'],jsonRsp['desc']))
            return jsonRsp



    def login(self,telPhone,pwd):
        #要把header中的sessionid存下来
        m=hashlib.md5()
        m.update(pwd)
        pwd=m.hexdigest()
        account={"telPhone":telPhone,"password":pwd}
        rsp = self.execute(Command.LOGIN,userStr=account)
        jsonRsp = self.handle_response(Command.LOGIN,rsp)
        #rsp.raise_for_status()
        
        if jsonRsp.has_key('data') :
            self._accountInfo=jsonRsp['data']
            #print self._accountInfo
            logging.info('accountInfo  %s ' % (self._accountInfo))
            self._headers["entCode"]=self._accountInfo["entCode"]
            self._headers["loginId"]=self._accountInfo["imLoginId"]
            self._headers["uid"]=self._accountInfo["uid"]
            self._headers["sessionId"]=self._accountInfo["sessionId"]
            self.command_executor.setHeaders(self._headers)

            logging.info('headers change  %s' % (self._headers))
            return self._accountInfo
        raise RuntimeError("get accountInfo Failed" )
        return jsonRsp
        #self.command_executor.setHeader(self._header)

    #测试通过
    def logout(self,apiArgs):
        rsp =self.execute(Command.LOGOUT,userStr=apiArgs)   
        return self.handle_response(rsp)

    def verificationPhone(self, apiArgs):
        rsp =self.execute(Command.VERIFICATION_PHONE,userStr=apiArgs)   
        return self.handle_response(rsp,exceptcode='3')

    def registerUser(self,  apiArgs):
        rsp =self.execute(Command.REGISTER_USER,userStr=apiArgs)   
        return self.handle_response(rsp)    

    def registerEnt(self,  apiArgs):
        rsp =self.execute(Command.REGISTER_ENT,userStr=apiArgs)   
        return self.handle_response(rsp)   
     
    def updateEnt(self,  apiArgs):
        rsp =self.execute(Command.UPDATE_ENT,userStr=apiArgs)   
        return self.handle_response(rsp)       

    def getEntDetail(self,  apiArgs):
        rsp =self.execute(Command.GET_ENT_DETAIL,userStr=apiArgs)   
        return self.handle_response(rsp)       

    def joinEnt(self,  apiArgs):
        rsp =self.execute(Command.JOIN_ENT,userStr=apiArgs)   
        return self.handle_response(rsp)       

    def examineJoinUser(self,  apiArgs):
        rsp =self.execute(Command.EXAMINE_JOIN_USER,userStr=apiArgs)   
        return self.handle_response(rsp)      

    def removeUser(self,  apiArgs):
        rsp =self.execute(Command.REMOVE_USER,userStr=apiArgs)   
        return self.handle_response(rsp)   

    def addDept(self,  apiArgs):
        rsp =self.execute(Command.ADD_DEPT,userStr=apiArgs)   
        return self.handle_response(rsp)

      
    def updateDept(self,  apiArgs):
        rsp =self.execute(Command.UPDATE_DEPT,userStr=apiArgs)   
        return self.handle_response(rsp)  

    def searchOrg(self,  apiArgs):
        rsp =self.execute(Command.SEARCH_ORG,userStr=apiArgs)   
        return self.handle_response(rsp)    

    def delDept(self,  apiArgs):
        rsp =self.execute(Command.DEL_DEPT,userStr=apiArgs)   
        return self.handle_response(rsp)    

    def updateEmployee(self,  apiArgs):
        rsp =self.execute(Command.UPDATE_EMPLOYEE,userStr=apiArgs)   
        return self.handle_response(rsp)  

    def addProduct(self,  apiArgs):
        rsp =self.execute(Command.ADD_PRODUCT,userStr=apiArgs)   
        return self.handle_response(rsp)  

    def searchProduct(self,  apiArgs):
        rsp =self.execute(Command.SEARCH_PRODUCT,userStr=apiArgs)   
        return self.handle_response(rsp) 

    def deleteProduct(self,  apiArgs):   
        rsp =self.execute(Command.DEL_PRODUCT,userStr=apiArgs)   
        return self.handle_response(rsp)   

    def addCustomer(self,  apiArgs):
        rsp =self.execute(Command.ADD_CUSTOMER,userStr=apiArgs)   
        return self.handle_response(rsp)   

    def searchCustomer(self,  apiArgs):
        rsp =self.execute(Command.SEARCH_CUSTOMER,userStr=apiArgs)   
        return self.handle_response(rsp)   

    def delCustomer(self,  apiArgs):
        rsp =self.execute(Command.DEL_CUSTOMER,userStr=apiArgs)   
        return self.handle_response(rsp)

    def uploadAttendance(self,filePath,  apiArgs):
        rsp =self.execute(Command.UPLOAD_ATTENDANCE,userStr=apiArgs)   
        return self.handle_response(rsp)
        #



    def execute(self,driver_command, userStr=None,downlinkReqStr=None,data=None):
        #self.command_executor.setHeaders(self._headers)
        self.currentCommand=driver_command
        response = self.command_executor.execute(driver_command, userStr,downlinkReqStr,data)  #
        return response



















