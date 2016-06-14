#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Page import *


class examinePage(Page):
    """docstring for examinePage"""
    #在构造函数中查找该界面一定要有的控件， 没有查找到直接失败， 截屏，截屏规则，
    def __init__(self, driver):
        self._driver=driver
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'审批\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.RadioButton[@text=\'我审批的\']')))

        #self._driver.wait_element_by_xpath('//android.widget.TextView[@text=\'审批\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')
        #self._driver.wait_element_by_xpath('//android.widget.RadioButton[@text=\'我审批的\']')

    def addLeaveExamine(self):
        addbutton = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/top_right_btn')))
        addbutton.click()
        self._driver.tap([(573,227)],500)  #请假按钮坐标 需要优化计算坐标的方法
        return leaveExaminePage(self._driver)

    def addOutExamine(self):
        pass
    def addBussinessOutExamine(self):
        pass    
    def addCommonOutExamine(self):
        pass

    def toLatestCreatedExamineDetailPage(self):
        pass            
    def getCreateBymeList(self):
        pass
    def getApproveBymeList(self):
        pass

class ExamineDetailPage(Page):
    def __init__(self, driver):
        self._driver=driver
    def getDetails(self):
        #com.hecom.sales:id/approve_use_day
        #com.hecom.sales:id/approve_start_time
        #com.hecom.sales:id/approve_end_time
        #com.hecom.sales:id/approve_desc  包括类型和描述
        useday=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_use_day'))).text
        starttime=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_start_time'))).text
        endtime=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_end_time'))).text
        approve_desc=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/approve_desc'))).text
        return 


    def cancel(self):
        pass


class leaveExaminePage(Page):
    """docstring for leaveExaminePage"""
    def __init__(self, driver):
        self._driver=driver
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'请假\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))
        #text="请假" resource-id="com.hecom.sales:id/top_activity_name" class="android.widget.TextView"
    def setType(self,type):
        pass


    def setTime(self,start,end,duration):
        pass


    def setReason(self,reason):
        reasonEdit = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/apply_pick_reason')))
        reasonEdit.click()
        reasonEdit.send_keys(reason)
        #self._driver.set_value(reasonEdit,reason)
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()

    def setPhoto(self):
        pass

    def toSetApproverPage(self):
        #需要删除历史选择的人
        allEmployers = self._driver.find_elements_by_id('com.hecom.sales:id/persons_header')

        while len(allEmployers) > 1:
            allEmployers[0].click()  #点击第一个审批人删除他
            allEmployers = self._driver.find_elements_by_id('com.hecom.sales:id/persons_header')
    
            employer = self._driver.find_element_by_id('com.hecom.sales:id/persons_header')
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
        self._driver=driver
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
        return leaveExaminePage(self._driver)
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








        

        