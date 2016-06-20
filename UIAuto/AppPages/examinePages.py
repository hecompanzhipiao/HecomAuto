#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Page import *
import time


class examinePage(Page):
    """docstring for examinePage"""
    #在构造函数中查找该界面一定要有的控件， 没有查找到直接失败， 截屏，截屏规则，
    def __init__(self, driver):
        super(examinePage,self).__init__(driver)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'审批\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))
        self._myWaitApproveButton=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.RadioButton[@text=\'我审批的\']')))
        self._myCreatedButton=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.RadioButton[@text=\'我发起的\']')))
        self._addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))

        #self._driver.wait_element_by_xpath('//android.widget.TextView[@text=\'审批\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')
        #self._driver.wait_element_by_xpath('//android.widget.RadioButton[@text=\'我审批的\']')

    def addLeaveExamine(self):
        #addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))
        time.sleep(2)
        self._addbutton.click()
        self._driver.tap([(573,227)],500)  #请假按钮坐标 需要优化计算坐标的方法
        return editExaminePage(self._driver,'请假')

    def addOutExamine(self):
        #addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))
        time.sleep(2)
        self._addbutton.click()
        self._driver.tap([(566,309)],500)  #请假按钮坐标 需要优化计算坐标的方法
        return editExaminePage(self._driver,'外出')

    def addBussinessOutExamine(self):
        #addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))
        time.sleep(2)
        self._addbutton.click()
        self._driver.tap([(571,392)],500)  #请假按钮坐标 需要优化计算坐标的方法
        return editExaminePage(self._driver,'出差')
    
    def addCommonExamine(self):
        #addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))
        time.sleep(2)
        self._addbutton.click()
        self._driver.tap([(567,487)],500)  #请假按钮坐标 需要优化计算坐标的方法
        return editExaminePage(self._driver,'通用')

        #type 有请假申请 外出申请 出差申请，通用申请
    def toLatestCreatedExamineDetailPage(self,examineType):
        #'//android.widget.RadioButton[@text=\'我审批的\']'
        xpath = '//android.widget.TextView[@text=\''+examineType+'\']'
        self._myCreatedButton.click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        return  examineDetailPage(self._driver) 

    def toLatestWaitAprroveExamineDetailPage(self):
        self._myWaitApproveButton.click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'待审批\']'))).click()
        return  examineDetailPage(self._driver) 
          
    def getCreateBymeList(self):
        pass
    def getApproveBymeList(self):
        pass

class examineDetailPage(Page):
    def __init__(self, driver):
        super(examineDetailPage,self).__init__(driver)
    def getDetails(self):
        #com.hecom.sales:id/approve_use_day
        #com.hecom.sales:id/approve_start_time
        #com.hecom.sales:id/approve_end_time
        #com.hecom.sales:id/approve_desc  包括类型和描述
        useday=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_use_day'))).text
        starttime=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_start_time'))).text
        endtime=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_end_time'))).text
        approve_desc=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_desc'))).text
        return {'useday':useday,'starttime':starttime,'endtime':endtime,'approve_desc':approve_desc}
    def getApproveDesc(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_desc'))).text
    def getStartTime(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_start_time'))).text
    def getEndTime(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_end_time'))).text
    def getUseDay(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_use_day'))).text

    def agree(self,reason):
        #'//android.widget.TextView[@text=\'同意\']'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_agree_img'))).click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text=\'请输入原因\']'))).send_keys(reason)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text=\'确定\']'))).click()
        return examinePage(self._driver)
        #who 是带拼音的
    def deliver(self,reason,who):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_transfer_img'))).click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text=\'请输入原因\']'))).send_keys(reason)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text=\'确定\']'))).click()
        approverListPage(self._driver).selectPersons(who)
        return examinePage(self._driver)

    def reject(self,reason):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_refuse_img'))).click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text=\'请输入原因\']'))).send_keys(reason)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text=\'确定\']'))).click()
        return examinePage(self._driver)
    def cancle():
        pass


class editExaminePage(Page):
    """docstring for leaveExaminePage"""
    def __init__(self, driver,examineType=None):
        super(editExaminePage,self).__init__(driver)
        if examineType:
            xpath='//android.widget.TextView[@text=\''+examineType+'\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']'
            WebDriverWait(self._driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        #text="请假" resource-id="com.hecom.sales:id/top_activity_name" class="android.widget.TextView"
    def setType(self,type):
        pass


    def setTime(self,start,end,duration):
        pass

    def setExamineTitle(self,title):
        edit=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/apply_common_content')))
        edit.send_keys(title)
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()
    def setDestnation(self,loc):
        edit=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/apply_bussiness_address')))
        edit.send_keys(loc)
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()


    def setReason(self,reason):
        reasonEdit = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/apply_pick_reason')))
        #reasonEdit.click()
        reasonEdit.send_keys(reason)
        #self._driver.set_value(reasonEdit,reason)
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()

    def setPhoto(self):
        pass

    def toSetApproverPage(self):
        #需要删除历史选择的人
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/persons_header')))
        allEmployers = self._driver.find_elements_by_id('com.hecom.sales:id/persons_header')

        while len(allEmployers) > 1:
            allEmployers[0].click()  #点击第一个审批人删除他
            allEmployers = self._driver.find_elements_by_id('com.hecom.sales:id/persons_header')
    
            employer =  WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/persons_header')))

            employer.click()
        return approverListPage(self._driver)
        #selectApprovers.selectPersons(namelist) 
        #确保返回请假申请页面
        #WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'请假\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))

    def submit(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'提交\'][@resource-id=\'com.hecom.sales:id/top_right_btn_text\']'))).click()
        return examinePage(self._driver)


class approverListPage(Page):
    """docstring for approverListPage"""
    def __init__(self, driver):
        super(approverListPage,self).__init__(driver)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'审批人\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))
    def getAllPersons():
        pass
    def searchPerson():
        pass
        #选择人员点击确定
        #persons 带pinyin 格式 ［name，pinyin］，［name2，pinyin］
    def selectPersons(self,persons):
        # 使用搜索功能，因为列表太长上隐藏的元素搜索不到
        #'//android.widget.TextView[@resource-id=\'com.hecom.sales:id/name_of_friend\'][@text=\'小小潘\']'
        for person in persons :
            #first = self._driver.find_element_by_id('com.hecom.sales:id/name_of_friend')
            self.search(person).click()    

    def confirm(self):
        #self._driver.find_element_by_id('com.hecom.sales:id/top_right_text').click()
        WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_text'))).click()
        return editExaminePage(self._driver)
    def search(self,person):
        searchgroup=WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/search_group_name')))
        searchgroup.click()
        #删除已输入字符
        while searchgroup.text and searchgroup.text != '搜索' :
            self._driver.long_press_keycode(67)
            searchgroup=WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/search_group_name')))

        searchgroup.send_keys(person[1])
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()
        xpath = '//android.widget.TextView[@resource-id=\'com.hecom.sales:id/name_of_friend\'][@text=\''+person[0]+'\']'
        return  WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))








        

        