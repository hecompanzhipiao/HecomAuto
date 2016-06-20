


class Command(object):

    LOGIN  = "login"
    LOGOUT  = "logout"
    VERIFICATION_PHONE =  "verifcationPhone"
    REGISTER_USER = "registerUser"


    REGISTER_ENT = "registerEnt"
    UPDATE_ENT  =  "updateEnt"
    GET_ENT_DETAIL  =  "getEntDetail"
    
    JOIN_ENT  =  "joinEnt"

    EXAMINE_JOIN_USER  =  "examineJoinUser"
    REMOVE_USER  =  "removeUser"

    ADD_DEPT  =  "addDept"
    UPDATE_DEPT = "updateDept"
    SEARCH_ORG = "searchOrg"
    DEL_DEPT = "delDept"

    UPDATE_EMPLOYEE = "updateEmployee"

    ADD_PRODUCT  =  "addProduct"
    SEARCH_PRODUCT = "searchProduct"
    DEL_PRODUCT = "delProduct"

    ADD_CUSTOMER = "addCustomer"
    SEARCH_CUSTOMER = "searchCustomer"
    DEL_CUSTOMER = "delCustomer"



    UPLOAD_ATTENDANCE = "uploadAttendance"


   
   


class V6Command(object):
    #url 组成有6个部分 scheme netloc path param query fragment
    def getCommandsInfo(comands):
        return 
    V6Commands={
        Command.LOGIN: ('GET','/@@/##/common/user/login.do'),

    }
