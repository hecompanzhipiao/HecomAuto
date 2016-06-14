import sys
sys.path.append("..")
from UIAuto.AppPages.examinePages import *
from UIAuto.AppPages.workPage import *
from UIAuto.AppPages.Page import *
from UIAuto.AppPages.homeMainTab import *

from appium.webdriver.webdriver import WebDriver
import pytests



def  testcase1():
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    driver = WebDriver(http, desired_caps)


    workpage=homeMainTab(driver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(driver)
    leaveexaminepage=examinepage.addLeaveExamine()

    leaveexaminepage.setReason('helloword')
    approverlistpage=leaveexaminepage.toSetApproverPage()

    approverlistpage.selectPersons([['小潘','xiaopan'],])

    leaveexaminepage=approverlistpage.confirm()

    examinepage=leaveexaminepage.submit()



testcase1()