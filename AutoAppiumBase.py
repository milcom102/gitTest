#-*-coding:utf-8-*-

from appium import webdriver


desired_caps = {
    'platformName':'Android',
    'deviceName':'e874797',
    'platformVersion':'6.0.1',
    'appPackage':'trade.sale.onlty.com',
    'appActivity':'trade.sale.onlty.com.activity.SplashActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.launch_app()