#-*-coding:utf-8-*-
from appium import webdriver
# from selenium import webdriver as swbd
from time import sleep
import operator as op
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

desired_caps = {
        'automationName':'XCUITest',
        'platformName': 'iOS',

        # 'deviceName': 'iPhone',
        # 'platformVersion': '9.3',
        # 'bundleId':'com.xie.wda.lib',
        # 'udid':'901130617b3b2e1347beaba150fdf33871430c21', #iphone 6Plus

        'deviceName': 'iPhone X',
        'platformVersion': '12.1',
        'udid':'421c3dc31fac5f1f375998bcc7801064e91d5245', #iphone X
        # 'browserName': 'safari'
        'app':'com.lvtainyuan.MallApp'

        }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(2)
# driver.get('https://www.baidu.com')
try:

    # driver.find_element_by_name(u"农场基地").click()
    # sleep(4)
    driver.find_element_by_accessibility_id('home_btn_trade').click()
    # length1 = driver.find_elements_by_ios_predicate(u'value=="预售产品"').__len__()
    # length2 = driver.find_elements_by_ios_predicate('type=="XCUIElementTypeStaticText"').__len__()
    # index = driver.find_elements_by_ios_predicate('type=="XCUIElementTypeStaticText"').index(1)
    # print "value:%s" % length1
    # print "count:%s" % length2
    # print "index:%s" % index
except Exception:
    print Exception



