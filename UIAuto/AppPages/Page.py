from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


__metaclass__=type
class Page(object):
    """docstring for Page"""
    def __init__(self,driver):
        self._driver=driver
        
    def refresh(self):
        pass

    def skip(self):
        pass

    def pressBack(self):
        pass