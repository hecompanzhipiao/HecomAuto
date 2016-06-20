from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Page import *
import time


class dailyReportPage(Page):

    def __init__(self,driver):
        super(dailyReportPage,self).__init__(driver)
        #self._driver=driver
        self.work_daily_mine=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/rb_work_daily_mine')))
        #self.work_daily_subordinate=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/rb_work_daily_subordinate')))

        self.addreport=WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/iv_top_right')))
        #使用这个方法时，日报内容不能过长
    def toReportDetailByContent(self,content):
        self.work_daily_mine.click()
        self.refresh()
        xpath='//android.widget.TextView[@text=\''+content+'\'][@resource-id=\'com.hecom.sales:id/tv_workdaily_item_mine_content\']'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        return dailyReportDetailsPage(self._driver)

    def toMyLatestReport(self):
        self.refresh()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_workdaily_item_mine_content'))).click()
        return dailyReportDetailsPage(self._driver)


    

    #转到最新的下属员工日报
    def toEmpReportDetailByContent(self,content):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/rb_work_daily_subordinate'))).click()
        self.refresh()
        xpath='//android.widget.TextView[@text=\''+content+'\'][@resource-id=\'com.hecom.sales:id/tv_workdaily_item_mine_content\']'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
        return dailyReportDetailsPage(self._driver)

    def toEmpLatestReport(self):
        self.work_daily_subordinate.click()
        self.refresh()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, 'com.hecom.sales:id/rb_work_daily_mine')))
        return dailyReportDetailsPage(self._driver)


    def createReport(self):
        self.addreport.click()
        return  editDailyReportPage(self._driver)


class dailyReportDetailsPage(Page):
    def __init__(self,driver):
        super(dailyReportDetailsPage,self).__init__(driver)

    def getMyReportTime(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_time_mine'))).text

    def getMyReportDay(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_day_mine'))).text


    #下属员工日报详情专用
    def getEmpReportTitle(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/rl_title_sub'))).text
    def getEmpReportName(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_name_sub'))).text
    def getEmpRePortTime(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_time_sub'))).text


    def getContent(self):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/tv_content'))).text

    def goBack(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'返回\'][@resource-id=\'com.hecom.sales:id/top_left_text\']'))).click()
        return dailyReportPage(self._driver)


class editDailyReportPage(Page):
    def __init__(self,driver):
        super(editDailyReportPage,self).__init__(driver)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'新建日报\'][@resource-id=\'com.hecom.sales:id/top_activity_name\']')))
        #self.submit = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'提交\'][@resource-id=\'com.hecom.sales:id/top_right_text\']')))

    def addReport(self,content):
        #com.hecom.sales:id/workdaily_content
        contentEdit = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'com.hecom.sales:id/workdaily_content')))
        contentEdit.send_keys(content)
        #self._driver.set_value(reasonEdit,reason)
        self._driver.keyevent(66)  #enter
        self._driver.hide_keyboard()


    def submit(self):  
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text=\'提交\'][@resource-id=\'com.hecom.sales:id/top_right_text\']'))).click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text=\'确认\']'))).click()
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text=\'确定\']'))).click()

        return dailyReportPage(self._driver)








