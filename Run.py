#-*-coding:utf-8-*-
from appium import webdriver
import DriverProperties

#启动设备
#Run.Driver().launch_app()

class Banner:

    def Next_button(self):
        DDR = DeviceConConfig
        DDR.Driver().find_element_by_id(DriverProperties.url+":id/next_button").click()


class DeviceConConfig:

    def Driver(self):
        # 链接设备和APP设置-------------------------------------------------
        desired_caps = {}
        desired_caps['platformName'] = DriverProperties.platformName
        desired_caps['deviceName'] = DriverProperties.deviceName
        desired_caps['platformVersion'] = DriverProperties.platformVersion
        desired_caps['appPackage'] = DriverProperties.appPackage
        desired_caps['appActivity'] = DriverProperties.appActivity
        desired_caps['unicodeKeyboard'] = DriverProperties.unicodeKeyboard
        desired_caps['resetKeyboard'] = DriverProperties.resetKeyboard
        driver = webdriver.Remote(DriverProperties.remote, desired_caps)
        return driver


if __name__=='__main__':
    Run = DeviceConConfig()
    Run.Driver().launch_app()
    Banner_next = Banner()
    Banner_next.Next_button()


