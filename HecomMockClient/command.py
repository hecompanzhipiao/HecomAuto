


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
    #url 组成有6个部分 scheme netloc path param query fragment:
    V6Commands={
        Command.LOGIN: ('GET','http://host:port/@@/##/common/user/login.do'),
        Command.LOGOUT: ('GET','http://host:port/@@/##/common/user/logout.do'),
        Command.VERIFICATION_PHONE: ('GET','http://host:port/@@/##/common/user/verificationPhone.do'),
        Command.REGISTER_USER: ('GET','http://host:port/@@/##/common/user/registerUser.do'),
        Command.REGISTER_ENT: ('GET','http://host:port/@@/##/common/user/registerEnt.do'),
        Command.UPDATE_ENT: ('GET','{authUrl}/ent/updateEnt.do'),
        Command.GET_ENT_DETAIL: ('GET','{authUrl}/ent/getEntDetail.do'),
        Command.JOIN_ENT: ('GET','http://host:port/@@/##/common/user/joinEnt.do'),
        Command.EXAMINE_JOIN_USER : ('GET','http://host:port/@@/rcm/e/{entCode}/user/examineJoinUser.do'),
        Command.REMOVE_USER: ('GET','http://host:port/@@/##/e/{entCode}/user/removeUser.do'),
        Command.ADD_DEPT: ('GET','{authUrl}/organization/addDept.do'),
        Command.UPDATE_DEPT : ('GET','{authUrl}/organization/updateDept.do'),
        Command.SEARCH_ORG : ('GET','{authUrl}/organization/syncAllOrganization.do'),
        Command.DEL_DEPT: ('GET','{authUrl}/organization/deleteOrganization.do'),
        Command.UPDATE_EMPLOYEE : ('GET','{authUrl}/organization/updateEmployee.do'),
        Command.ADD_PRODUCT: ('GET','{authUrl}/product/addProduct.do'),
        Command.SEARCH_PRODUCT: ('GET','{authUrl}/product/syncProduct.do'),
        Command.DEL_PRODUCT: ('GET','{authUrl}/product/deleteProduct.do'),
        Command.ADD_CUSTOMER: ('GET','{authUrl}/customer/addCustomer.do'),
        Command.SEARCH_CUSTOMER: ('GET','{authUrl}/customer/syncCustomer.do'),
        Command.DEL_CUSTOMER : ('GET','{authUrl}/customer/deleteCustomer.do'),
        Command.UPLOAD_ATTENDANCE : ('POST','{authUrl}/attendanceManage/uploadAttendance.do'),

    }
