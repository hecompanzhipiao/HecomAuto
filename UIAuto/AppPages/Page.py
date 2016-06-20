# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging


__metaclass__=type
class Page(object):
    """docstring for Page"""
    def __init__(self,driver):
        self._driver=driver
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s%(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S',)
        logging.info('current activity is :'+ self._driver.current_activity)  

    def refresh(self):
        self.scrollDown()
        time.sleep(2)

    def skip(self):
        pass

    def pressBack(self):
        pass

    def scrollDown(self):
        width = self._driver.get_window_size()['width']
        height = self._driver.get_window_size()['height']
        self._driver.swipe(width/2,height/4,width/2,height*3/4,1000)