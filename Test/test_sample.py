import sys
sys.path.append("..")
from UIAuto.AppPages.examinePages import *
from UIAuto.AppPages.workPage import *
from UIAuto.AppPages.Page import *
from UIAuto.AppPages.homeMainTab import *

from appium.webdriver.webdriver import WebDriver
import pytest

desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'5.0.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
http='http://localhost:4723/wd/hub'
employerdriver = WebDriver(http, desired_caps)


def test_accept_leave_examine():  
        #跑时修改
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'5.0.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    employerdriver = WebDriver(http, desired_caps)
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    employeedriver = WebDriver(http, desired_caps)

    add_leave_examine(employeedriver)
    



    workpage=homeMainTab(employerdriver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(employerdriver)
    examinedetailpage=examinepage.toLatestWaitAprroveExamineDetailPage()
    examinepage = examinedetailpage.agree('agree')






def test_add_leave_examine(driver):
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    driver = WebDriver(http, desired_caps)


    workpage=homeMainTab(driver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(driver)
    leaveexaminepage=examinepage.addLeaveExamine()

    leaveexaminepage.setReason('leaveReason1')
    approverlistpage=leaveexaminepage.toSetApproverPage()

    approverlistpage.selectPersons([['小潘','xiaopan'],])  #审批人

    leaveexaminepage=approverlistpage.confirm()

    examinepage = leaveexaminepage.submit()
    examinedetailpage = examinepage.toLatestCreatedExamineDetailPage('请假申请')
    
    details = examinedetailpage.getDetails()['approve_desc']
    assert 'leaveReason1' in details
    assert  '事假' in  details


def test_add_business_examine(driver):
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    driver = WebDriver(http, desired_caps)


    workpage=homeMainTab(driver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(driver)
    leaveexaminepage=examinepage.addBussinessOutExamine()

    leaveexaminepage.setReason('businessreason1')
    approverlistpage=leaveexaminepage.toSetApproverPage()

    approverlistpage.selectPersons([['小潘','xiaopan'],])  #审批人

    leaveexaminepage=approverlistpage.confirm()

    examinepage = leaveexaminepage.submit()
    examinedetailpage = examinepage.toLatestCreatedExamineDetailPage('请假申请')
    
    details = examinedetailpage.getDetails()['approve_desc']
    assert 'businessreason1' in details


def test_add_common_examine(driver):
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    driver = WebDriver(http, desired_caps)

    workpage=homeMainTab(driver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(driver)
    leaveexaminepage=examinepage.addLeaveExamine()

    leaveexaminepage.setReason('commonreason')
    approverlistpage=leaveexaminepage.toSetApproverPage()

    approverlistpage.selectPersons([['小潘','xiaopan'],])  #审批人

    leaveexaminepage=approverlistpage.confirm()

    examinepage = leaveexaminepage.submit()
    examinedetailpage = examinepage.toLatestCreatedExamineDetailPage('请假申请')
    
    details = examinedetailpage.getDetails()['approve_desc']
    assert 'commonreason' in details

def test_dd_out_examine(driver):
    desired_caps = {'deviceName':'9cd2876d','platformName':'Android','platformVersion':'4.4.2','appPackage':'com.hecom.sales','appActivity':'com.hecom.splash.SplashActivity'}
    http='http://localhost:4723/wd/hub'
    driver = WebDriver(http, desired_caps)

    workpage=homeMainTab(driver).toWorkPages()
    workpage.getWorkItem(name='审批').click()

    examinepage=examinePage(driver)
    leaveexaminepage=examinepage.addCommonOutExamine()

    leaveexaminepage.setReason('outreason')
    approverlistpage=leaveexaminepage.toSetApproverPage()

    approverlistpage.selectPersons([['小潘','xiaopan'],])  #审批人

    leaveexaminepage=approverlistpage.confirm()

    examinepage = leaveexaminepage.submit()
    examinedetailpage = examinepage.toLatestCreatedExamineDetailPage('请假申请')
    
    details = examinedetailpage.getDetails()['approve_desc']
    assert 'outreason' in details


