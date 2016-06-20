from .errorhandler import ErrorHandler
from .remote_connection import RemoteConnection
from .command import Command




class HecomMockClient(object):
    def __init__(self,server,Version=6):
        #版本不一样，支持的命令是不一样的

        self.command_executor=RemoteConnection()
        self.errorhandler=ErrorHandler()
        #self.paramChecker=
        #self.rsp_handler=RspHandler()
        #日志模块
        #self.LOG=

        pass

    def login(self,apiArgs):
        #要把header中的sessionid存下来
         self.execute(Command.LOGIN,apiArgs)

        #self.command_executor.setHeader(self._header)

    #测试通过
    def logout(self):
       
        return

    def verificationPhone(self, apiArgs):
      
        return

    def registerUser(self,  apiArgs):
        return
    def registerEnt(self,  apiArgs):
        return
     
    def updateEnt(self,  apiArgs):
        return
       
    def getEntDetail(self,  apiArgs):
        return
       
    def joinEnt(self,  apiArgs):
        return
       
    def examineJoinUser(self,  apiArgs):
        return
        
    def removeUser(self,  apiArgs):
        return
        
    def addDept(self,  apiArgs):
        return
      
    def updateDept(self,  apiArgs):
        return
        
    def searchOrg(self,  apiArgs):
        return
        
    def delDept(self,  apiArgs):
        return
        
    def updateEmployee(self,  apiArgs):
        return
       
    def addProduct(self,  apiArgs):
        return
        
    def searchProduct(self,  apiArgs):
        return
        
    def deleteProduct(self,  apiArgs):   
        return
       
    def addCustomer(self,  apiArgs):
        return
    
    def searchCustomer(self,  apiArgs):
        return
        
    def delCustomer(self,  apiArgs):
        return

    def uploadAttendance(self,filePath,  apiArgs):
        return

        #



    def execute(self,driver_command, userStr=None,downlinkReqStr=None,data=None):
        #header信息设置
        response = self.command_executor.execute(driver_command, userStr,downlinkReqStr,data)  #

















