from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .workPage import *

class homeMainTab(object):
    def __init__(self,driver):
        self._driver=driver
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/btn_maintab_work')))
        #....

    def getActivePage(self):
        pass
    def toWorkPages(self):
        buttonWork= WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/btn_maintab_work')))
        buttonWork.click()
        return workPage(self._driver)

