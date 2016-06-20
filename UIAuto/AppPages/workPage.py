#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Page import *

class workPage(Page):
    """docstring for workPage"""
    def __init__(self,driver):
        super(workPage,self).__init__(driver)
    #获得 工作管理  日程办公 里的工作项等对象 没有返回空, 名字相同时category必填
    def isCategoryExist(self,name):
        pass
    def getWorkItem(self,category=None,name=None):
        if not category:
            xpath='//android.widget.TextView[@text=\''+name+'\'][@resource-id=\'com.hecom.sales:id/icon_desc\']'
            return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            
        else:
            return
        return
    # 当安装插件后，套件显示不全，需要上拉
    def _scrollupCategory():
        pass



