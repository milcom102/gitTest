#-*-coding:utf-8-*-

from BmsAutoTest_1_7 import *
from appium import webdriver
from time import sleep
import operator as op
from selenium.common.exceptions import NoSuchElementException

class AppAutoTrade:



    # 初始化自动化常量------------------------------
    def __init__(self):

        # app外网地址
        self.URL_TRADE = "trade.sale.onlty.com"
        self.URL_BASE = "base.sale.onlty.com"

        # app执行环境
        self.HTTP_EVR3_TRADE = u"http://api.asc.dev.ad2o.com/v3/trade/"  # 市场3.0开发环境
        self.HTTP_EVR3_BASE = u"http://api.asc.dev.ad2o.com/v3/base/"  # 基地3.0开发环境
        # self.HTTP_EVR3_TRADE = u"https://api-demo.onlty.com/v3/trade/" 市场3.1演示环境
        # self.HTTP_EVR3_TRADE = u"https://api-dev.onlty.com/v3/trade/"  # 基地3.1开发环境

        # app环境命名输入
        self.EVR_NAME = u"AutoTest"
        # self.EVR_NAME = u"https演示环境"

        # 登录的账户号码
        self.ACCOUNT_NO_BASE = "15218870000"
        self.ACCOUNT_NO_TRADE = "13533880000"
        # self.ACCOUNT_NO_TRADE = "15218870000"

        # 登录的账号密码
        self.ACCOUNT_PWD_BASE = "15218870000"
        self.ACCOUNT_PWD_TRADE = "13533880000"
        # self.ACCOUNT_PWD_TRADE = "15218870000"

        # app包名称
        self.APP_PACKAGE_TRADE = "trade.sale.onlty.com"
        self.APP_PACKAGE_BASE = "base.sale.onlty.com"

        # app活动包
        self.APP_ACTIVITY_TRADE = "trade.sale.onlty.com.activity.SplashActivity"
        self.APP_ACTIVITY_BASE = "base.sale.onlty.com.activity.SplashActivity"

        # 停顿秒数设置
        self.SECONDS_LONG = 7
        self.SECONDS_SHORT = 3

        # 驱动
        self.DRIVER_TRADE = None
        self.DRIVER_BASE = None

        # 移动设备端型号
        # coolpad c106
        self.DEVICE_NAME = 'e874797'
        self.PLATFORM_VERSION = '6.0.1'

        # Appium工具耦合地址
        self.REMOTE_ADDR = 'http://127.0.0.1:4723/wd/hub'

        # android系统查看app是否已安装
        self.SYS_URL = "com.android.packageinstaller"

        # 驱动
        self.DRIVER_TRADE = None
        self.DRIVER_BASE = None

    # 市场端-链接设备和APP设置-------------------------------------------------
    def Driver_Trade(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': self.DEVICE_NAME,
        'platformVersion': self.PLATFORM_VERSION,
        'appPackage': self.APP_PACKAGE_TRADE,
        'appActivity': self.APP_ACTIVITY_TRADE,
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }
        self.DRIVER_TRADE = webdriver.Remote(self.REMOTE_ADDR, desired_caps)

    # 市场端-完整登录-------------------------------------------------
    def Login_Trade(self):
        self.Driver_Trade()
        self.Banner_Pass_Trade()
        self.Evr_Selected_Trade()
        self.Login_By_Pwd_Trade()
        self.Authorization_Sys_Trade()

    # 快速启动商城
    def LaunchFast_Trade(self):
        # self.DRIVER_TRADE.start_activity(self.APP_PACKAGE_TRADE, self.APP_ACTIVITY_TRADE)
        # sleep(self.SECONDS_SHORT)
        self.DRIVER_TRADE.launch_app()

    # 市场端-BANNER首页“跳过”-------------------------------------------------
    def Banner_Pass_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/next_button").click()
        except NoSuchElementException:
            self.Banner_Pass_Trade()

    # 市场端-选择登录环境---------------------------------------------------------
    def Evr_Selected_Trade(self):
        try:
            # 勾选“我已经阅读并同意《绿田云服务协议》
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/veriflcation_login_serve_image").click()
            # 在“手机登录/注册”坐标-点击3次进入切换环境，每次间隔100毫秒
            # 获取“手机登录/注册”坐标位置
            bounds = self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/veriflcation_login_title_tv").location
            # print bounds
            # bounds2 = self.driver.find_element_by_class_name(self.trade_url + ":id/veriflcation_login_title_tv").location.items(
            # print bounds2
            # bounds = self.driver.find_element_by_id(self.trade_url+":id/veriflcation_login_title_tv").
            # print bounds
            for num in range(1,4):
                # 点击“手机登录/注册”的坐标位置
                self.DRIVER_TRADE.tap([(bounds['x'], bounds['y']), (bounds['x'], bounds['y'])], 100)
            #     self.driver.tap([(60,273),(368,338)],100)
            #     print num
            # 输入创建新环境名称
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/damain_name_tv").send_keys(self.EVR_NAME)
            # 清空输入框预录入的内容
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/damain_path_tv").clear()
            # 输入创建新环境地址
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/damain_path_tv").send_keys(self.HTTP_EVR3_TRADE)
            # 点击-确认-按钮
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/damain_add_tv").click()

            # 选择测试环境地址demo-asc:获取相同ID列表list后，匹配所选环境地址
            # 获取list元素数量
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/market_list_number_2_02").__len__()
            # print "elements list length:",el_len

            # 遍历所有list元素并获取text文本内容用于比较新建的测试环境地址，匹配成功则点击字段切换环境
            for i in range(el_len):
                evr_add = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/market_list_number_2_02")[i].text
                # 字符串比较函数
                if op.eq(self.HTTP_EVR3_TRADE, evr_add):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/market_list_number_2_02")[i].click()
                    # print "if"
                    break
                else:
                    # print "else"
                    continue
            # 点击-切换-按钮
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/damain_cut_tv").click()
        except NoSuchElementException:
            self.Evr_Selected_Trade()

    # 市场端-用户登录----------------------------------
    def Login_By_Pwd_Trade(self):
        try:
            # 在“请输入手机号”框输入手机号
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/veriflcation_login_mobile_edit").send_keys(self.ACCOUNT_NO_TRADE)

            # 点击-下一步-按钮
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/veriflcation_login_btn").click()

            # 点击以输入密码方式登录
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/account_loginType_tv").click()

            # 输入密码登录
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/account_password_edit").send_keys(self.ACCOUNT_PWD_TRADE)

            # 点击-登录-按钮
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/account_login_btn").click()
        except NoSuchElementException:
            self.Login_By_Pwd_Trade()

    # 市场端-首次登录系统设备授权--------------------------------
    def Authorization_Sys_Trade(self):
        try:
            sleep(self.SECONDS_SHORT)
            # 授权使用电话
            # 授权使用日历
            # 授权使用拍摄和录制视频
            # 授权允许访问照片和媒体内容
            # 授权使用录制音频
            for i in range(5):
                self.DRIVER_TRADE.find_element_by_id(self.SYS_URL + ":id/permission_allow_button").click()
        except NoSuchElementException:
            self.Authorization_Sys_Trade()

    # 市场端-首页-交易大厅（按钮）----------------------------
    def TranscationHallBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/home_presell_project_ll").click()
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            self.TranscationHallBtn_Trade()


    # 市场端-首页-交易大厅（按钮）-交易产品列表---------------------
    def TranscationProduce_List_Trade(self):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView").__len__()
            print el_len
            for i in range(el_len):
                title_bar_name = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].text
                print title_bar_name
                if op.eq(u"交易产品", title_bar_name):
                    self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].click()
                    break
                else:
                    continue
        except NoSuchElementException:
            self.TranscationProduce_List_Trade()
        # sleep(self.seconds_short)

    # 市场端-首页-交易大厅（按钮）-交易产品列表-申请下单按钮--------------------
    def TranscationProduce_List_ApplyBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/home_deal_deal_product_apply_sell_tv").click()
        except NoSuchElementException:
            self.TranscationProduce_List_ApplyBtn_Trade()

    # 市场端-首页-交易大厅（按钮）-交易产品列表-申请下单列表录入+确认订单按钮--------------------
    def Produce_CreateOrderApply_Trade(self):
        try:
            flag = True
            flag_text = [True]*3
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv").__len__()
            while(flag):
                self.DRIVER_TRADE.swipe(430, 1700, 430, 1175, 500)
                if flag_text[0] or flag_text[1]:
                    for i in range(el_len):
                        el_text_quantities = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv")[i].text
                        if op.eq(u"下单件数", el_text_quantities) and flag_text[0]:
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_content_edit")[i].send_keys(u'20')
                            flag_text[0] = False
                            print "0=%s" % flag_text[0]

                        if op.eq(u"下单斤数", el_text_quantities) and flag_text[1]:
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_content_edit")[i].send_keys(u'400')
                            flag_text[1] = False
                            print "1=%s" % flag_text[1]
                try:
                    el_text_addr = self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/purchase_shop_contast_tv").text
                    if op.eq(u"请选择收货人信息",el_text_addr) and flag_text[2]:
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/purchase_shop_contast_tv").click()
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shipping_address_tv").click()
                        flag_text[2] = False
                        print "2=%s" % flag_text[1]
                        flag = False
                        print "flag=%s" % flag
                        break
                except NoSuchElementException:
                    pass
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/amount_save_tv").click()
        except NoSuchElementException:
            self.Produce_CreateOrderApply_Trade()
