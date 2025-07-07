#-*-coding:utf-8-*-

from appium import webdriver
from time import sleep
import operator as op
from selenium.common.exceptions import NoSuchElementException

class AppRun:
    # app外网地址
    trade_url = "trade.sale.onlty.com"
    base_url = "base.sale.onlty.com"
    # app执行环境
    trade_evr3_http = u"http://api.asc.dev.ad2o.com/v3/trade/" #市场3.0开发环境
    trade_evr2_http = u"http://api.asc.dev.ad2o.com/v2/trade/" #市场2.0开发环境
    trade_evr1_http = u"http://api.demo-asc.ad2o.com/v2/trade/"   #市场演示环境
    base_evr3_http = u"http://api.asc.dev.ad2o.com/v3/base/"   #基地3.0开发环境
    base_evr2_http = u"http://api.asc.dev.ad2o.com/v2/base/"   #基地2.0开发环境
    base_evr1_http = u"http://api.demo-asc.ad2o.com/v2/base/"     #基地演示环境
    # 环境名称
    evr_name = "demo-asc_test"
    # android系统查看app是否已安装
    sys_url = "com.android.packageinstaller"
    # 登录的账户号码
    accountNo = "15218870000"
    base_accountNo = "13533880000"
    # 登录的账号密码
    accountPwd = "15218870011"
    base_accountPwd = "13533880011"
    # 自定义名称
    # 基地名称
    base_name = u"沃农基地"
    # 交易产品
    trade_produce =u"交易产品"
    # 预售产品名称
    # product_presell = u"甜线椒"
    product_presell = u"线椒A小"

    #申请代销信息录入
    # 件数
    proxy_quantities = "10"
    # 斤数
    proxy_weight = "200"
    # 对比字符串
    proxy_quantities_str = u"X 10件"


    # app包名称
    trade_appPackage = "trade.sale.onlty.com"
    base_appPackage = "base.sale.onlty.com"
    # app活动包
    trade_appActivity = "trade.sale.onlty.com.activity.SplashActivity"
    base_appActivity = "base.sale.onlty.com.activity.SplashActivity"

    # 秒数
    seconds_long = 8
    seconds_short = 4
    # 驱动
    driver = None
    base_driver = None

    # MIUI10属性
    # deviceName = '4e313e330210'
    # platformVersion = '8.1.0'

    # coolpad c106
    deviceName = 'e874797'
    platformVersion = '6.0.1'


    # 市场端链接设备和APP设置-------------------------------------------------
    def Driver(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': self.deviceName,
        'platformVersion': self.platformVersion,
        'appPackage': self.trade_appPackage,
        'appActivity': self.trade_appActivity,
        'unicodeKeyboard':'True',
        'resetKeyboard':'True'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print self.driver
        # return driver

    # 基地端链接设备和APP设置-------------------------------------------------
    def Base_Driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': self.deviceName,
            'platformVersion': self.platformVersion,
            'appPackage': self.base_appPackage,
            'appActivity': self.base_appActivity,
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        self.base_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print self.base_driver
        # return driver

    # 市场端启动APP---------------------------------------------------------
    def Launch_App(self):
        self.driver.launch_app()


    # 市场端关闭APP---------------------------------------------------------
    def Close_App(self):
        self.driver.close_app()


    # 市场端物理返回键（返回键代码4）---------------------------------------------------------
    def Back_PhysicsBtn(self):
        self.driver.press_keycode(4)
        print "press_keycode"


    # 市场端BANNER首页“跳过”-------------------------------------------------
    def Pass_Banner(self):
        try:
            self.driver.find_element_by_id(self.trade_url+":id/next_button").click()
        except NoSuchElementException:
            self.Pass_Banner()

    # 基地端启动APP---------------------------------------------------------
    def Base_Launch_App(self):
        self.base_driver.launch_app()


    # 基地端关闭APP---------------------------------------------------------
    def Base_Close_App(self):
        self.base_driver.close_app()


    # 基地端物理返回键（返回键代码4）---------------------------------------------------------
    def Base_Back_PhysicsBtn(self):
        self.base_driver.press_keycode(4)
        sleep(4)
        print "press_keycode"



    # 基地端BANNER首页“跳过”-------------------------------------------------
    def Base_Pass_Banner(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/next_button").click()

        except NoSuchElementException:
            self.Base_Pass_Banner()

    # 选择登录环境---------------------------------------------------------
    def Evr_Selected(self):
        try:
            # 勾选“我已经阅读并同意《绿田云服务协议》
            self.driver.find_element_by_id(self.trade_url+":id/veriflcation_login_serve_image").click()
            # 在“手机登录/注册”坐标-点击3次进入切换环境，每次间隔100毫秒
            # 获取“手机登录/注册”坐标位置
            bounds = self.driver.find_element_by_id(self.trade_url + ":id/veriflcation_login_title_tv").location
            print bounds
            # bounds2 = self.driver.find_element_by_class_name(self.trade_url + ":id/veriflcation_login_title_tv").location.items(
            # print bounds2
            # bounds = self.driver.find_element_by_id(self.trade_url+":id/veriflcation_login_title_tv").
            # print bounds
            for num in range(1,4):
                # 点击“手机登录/注册”的坐标位置
                self.driver.tap([(bounds['x'],bounds['y']),(bounds['x'],bounds['y'])],100)
            #     self.driver.tap([(60,273),(368,338)],100)
            #     print num
            # 输入创建新环境名称
            self.driver.find_element_by_id(self.trade_url+":id/damain_name_tv").send_keys(self.evr_name)
            # 清空输入框预录入的内容
            self.driver.find_element_by_id(self.trade_url + ":id/damain_path_tv").clear()
            # 输入创建新环境地址
            self.driver.find_element_by_id(self.trade_url+":id/damain_path_tv").send_keys(self.trade_evr1_http)
            # 点击-确认-按钮
            self.driver.find_element_by_id(self.trade_url+":id/damain_add_tv").click()

            # 选择测试环境地址demo-asc:获取相同ID列表list后，匹配所选环境地址
            # 获取list元素数量
            el_len = self.driver.find_elements_by_id(self.trade_url+":id/market_list_number_2_02").__len__()
            # print "elements list length:",el_len

            # 遍历所有list元素并获取text文本内容用于比较新建的测试环境地址，匹配成功则点击字段切换环境
            for i in range(el_len):
                Evr_add = self.driver.find_elements_by_id(self.trade_url+":id/market_list_number_2_02")[i].text
                # 字符串比较函数
                if op.eq(self.trade_evr1_http,Evr_add):
                    self.driver.find_elements_by_id(self.trade_url + ":id/market_list_number_2_02")[i].click()
                    print "if"
                    break
                else:
                    print "else"
                    continue
            # 点击-切换-按钮
            self.driver.find_element_by_id(self.trade_url + ":id/damain_cut_tv").click()
        except NoSuchElementException:
            self.Evr_Selected()

    # 基地选择登录环境---------------------------------------------------------
    def Base_Evr_Selected(self):
        try:
            # 勾选“我已经阅读并同意《绿田云服务协议》
            self.base_driver.find_element_by_id(self.base_url+":id/veriflcation_login_serve_image").click()
            # 在“手机登录/注册”坐标-点击3次进入切换环境，每次间隔100毫秒
            # 获取“手机登录/注册”坐标位置
            bounds = self.base_driver.find_element_by_id(self.base_url + ":id/veriflcation_login_title_tv").location
            print bounds
            # bounds2 = self.base_driver.find_element_by_class_name(self.base_url + ":id/veriflcation_login_title_tv").location.items(
            # print bounds2
            # bounds = self.base_driver.find_element_by_id(self.base_url+":id/veriflcation_login_title_tv").
            # print bounds
            for num in range(1,4):
                # 点击“手机登录/注册”的坐标位置
                self.base_driver.tap([(bounds['x'],bounds['y']),(bounds['x'],bounds['y'])],100)
            #     self.base_driver.tap([(60,273),(368,338)],100)
            #     print num
            # 输入创建新环境名称
            self.base_driver.find_element_by_id(self.base_url+":id/damain_name_tv").send_keys(self.evr_name)
            # 清空输入框预录入的内容
            self.base_driver.find_element_by_id(self.base_url + ":id/damain_path_tv").clear()
            # 输入创建新环境地址
            self.base_driver.find_element_by_id(self.base_url+":id/damain_path_tv").send_keys(self.base_evr1_http)
            # 点击-确认-按钮
            self.base_driver.find_element_by_id(self.base_url+":id/damain_add_tv").click()

            # 选择测试环境地址demo-asc:获取相同ID列表list后，匹配所选环境地址
            # 获取list元素数量
            el_len = self.base_driver.find_elements_by_id(self.base_url+":id/market_list_number_2_02").__len__()
            # print "elements list length:",el_len

            # 遍历所有list元素并获取text文本内容用于比较新建的测试环境地址，匹配成功则点击字段切换环境
            for i in range(el_len):
                evr_add = self.base_driver.find_elements_by_id(self.base_url+":id/market_list_number_2_02")[i].text
                # 字符串比较函数
                if op.eq(self.base_evr1_http,evr_add):
                    self.base_driver.find_elements_by_id(self.base_url + ":id/market_list_number_2_02")[i].click()
                    print "if"
                    break
                else:
                    print "else"
                    continue
            # 点击-切换-按钮
            self.base_driver.find_element_by_id(self.base_url + ":id/damain_cut_tv").click()

        except NoSuchElementException:
            self.Base_Evr_Selected()

    # 用户登录----------------------------------
    def Login_By_Pwd(self):
        try:
            # 在“请输入手机号”框输入手机号
            self.driver.find_element_by_id(self.trade_url + ":id/veriflcation_login_mobile_edit").send_keys(self.accountNo)

            # 点击-下一步-按钮
            self.driver.find_element_by_id(self.trade_url + ":id/veriflcation_login_btn").click()

            # 点击以输入密码方式登录
            self.driver.find_element_by_id(self.trade_url + ":id/account_loginType_tv").click()

            # 输入密码登录
            self.driver.find_element_by_id(self.trade_url + ":id/account_password_edit").send_keys(self.accountPwd)

            # 点击-登录-按钮
            self.driver.find_element_by_id(self.trade_url + ":id/account_login_btn").click()

        except NoSuchElementException:
            self.Login_By_Pwd()

    # 基地用户登录----------------------------------
    def Base_Login_By_Pwd(self):
        try:
            # 在“请输入手机号”框输入手机号
            self.base_driver.find_element_by_id(self.base_url + ":id/veriflcation_login_mobile_edit").send_keys(
                self.base_accountNo)

            # 点击-下一步-按钮
            self.base_driver.find_element_by_id(self.base_url + ":id/veriflcation_login_btn").click()

            # 点击以输入密码方式登录
            self.base_driver.find_element_by_id(self.base_url + ":id/account_loginType_tv").click()

            # 输入密码登录
            self.base_driver.find_element_by_id(self.base_url + ":id/account_password_edit").send_keys(self.base_accountPwd)

            # 点击-登录-按钮
            self.base_driver.find_element_by_id(self.base_url + ":id/account_login_btn").click()

        except NoSuchElementException:
            self.Base_Login_By_Pwd()

    # 首次登录系统设备授权--------------------------------
    def Authorization_Sys(self):
        try:
            # 授权使用电话
            self.driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用日历
            self.driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用拍摄和录制视频
            self.driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权允许访问照片和媒体内容
            self.driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用录制音频
            self.driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()
        except NoSuchElementException:
            self.Authorization_Sys()

    # 首页-接车查验
    def PickupInspect(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/home_product_transaction_ll").click()

        except NoSuchElementException:
            self.PickupInspect()

    # 首页-接车列表-已接车列表
    def PickupList_HadPickupList(self):
        try:
            text = u"已接车"
            el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                title_name = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
                print title_name
                if op.eq(title_name,text):
                    self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                    break
                else:
                    pass

        except NoSuchElementException:
            self.PickupList_HadPickupList()

    # 首页-待接车列表页面-接车-按钮
    def PickupList_PickupBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/reception_await_car_invoice_btn").click()

        except NoSuchElementException:
            self.PickupList_PickupBtn()

    # 首页-已接车列表页面-验货-按钮
    def PickupList_HadPickupList_InspectBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/reception_alread_car_invoice_btn").click()

        except NoSuchElementException:
            self.PickupList_HadPickupList_InspectBtn()

    # 首页-已接车列表页面-验货页面-新增货损明细
    def PickupList_HadPickupList_CreateDamageDetail(self):
        try:
            flag = True
            text = u"新增货损明细"
            while(flag):
                el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
                for i in range(el_len):
                    biz_name = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
                    if op.eq(biz_name,text):
                        self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                        # print "damageDetail"
                        self.driver.find_element_by_id(self.trade_url + ":id/sell_couments_content_tv").click()
                        # print "parkageOrder"
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
                        # print "save"
                        sleep(self.seconds_short)
                        flag = False
                        break
                    else:
                        pass
                self.driver.swipe(430, 1700, 430, 875, 200)
        except NoSuchElementException:
            self.PickupList_HadPickupList_CreateDamageDetail()

    # 首页-接车验货-已接车-验货-新增测温明细
    def PickupList_HadPickupList_CreateTemplature(self):
        try:
            flag = True
            text = u"新增测温明细"
            while (flag):
                el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
                for i in range(el_len):
                    biz_name = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
                    if op.eq(biz_name, text):
                        self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/examine_added_detail_difference_packages_edit").send_keys("3")
                        self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
                        sleep(self.seconds_short)
                        flag = False
                        break
                    else:
                        pass
                self.driver.swipe(430, 1700, 430, 1175, 200)
        except NoSuchElementException:
            self.PickupList_HadPickupList_CreateTemplature()

    # 首页-接车验货-已接车-验货-提交-按钮
    def PickupList_HadPickupList_InspectPage_Submit(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
            self.driver.find_element_by_id(self.trade_url + ":id/pupop_dialog_confirm").click()

        except NoSuchElementException:
            self.PickupList_HadPickupList_InspectPage_Submit()

    # 首页-接车验货-已接车-验货列表-确认-按钮
    def PickupList_HadPickupList_InspectPage_comfirmBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/reception_alread_car_invoice_btn").click()
        except NoSuchElementException:
            self.PickupList_HadPickupList_InspectPage_comfirmBtn()

    # 首页-接车验货-已接车-验货详情-确认-按钮
    def PickupList_HadPickupDetail_InspectPage_comfirmBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.PickupList_HadPickupDetail_InspectPage_comfirmBtn()



    # 基地-首次登录系统设备授权--------------------------------
    def Base_Authorization_Sys(self):
        try:
            # 授权使用电话
            self.base_driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用日历
            # self.base_driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用拍摄和录制视频
            self.base_driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权允许访问照片和媒体内容
            self.base_driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

            # 授权使用录制音频
            self.base_driver.find_element_by_id(self.sys_url + ":id/permission_allow_button").click()

        except NoSuchElementException:
            self.Base_Authorization_Sys()

    # 基地-首页-单据
    def Base_Invoices(self):
        try:
            text = u"单据"
            bottom_tv_len = self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv").__len__()
            for i in range(bottom_tv_len):
                bottom_tv_text = self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv")[i].text
                if op.eq(bottom_tv_text,text):
                    self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv")[i].click()
                    break
                else:
                    continue
        except NoSuchElementException:
            self.Base_Invoices()

    # 基地-首页-单据-采购订单
    def Base_Invoices_OrderList(self):
        try:
            self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[0].click()

        except NoSuchElementException:
            self.Base_Invoices_OrderList()

    # 基地-首页-单据-发货单据
    def Base_Invoices_ShipmentList(self):
        try:
            self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[1].click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentList()

    # 基地-首页-单据-结算单据
    def Base_Invoices_SettlementList(self):
        try:
            self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[2].click()
        except NoSuchElementException:
            self.Base_Invoices_SettlementList()

    # 基地-首页-单据-付款凭证
    def Base_Invoices_EvidenceOfPaymentList(self):
        try:
            self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[3].click()
        except NoSuchElementException:
            self.Base_Invoices_EvidenceOfPaymentList()

    # 基地-首页-单据-风险单据
    def Base_Invoices_RiskList(self):
        try:
            self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[4].click()
        except NoSuchElementException:
            self.Base_Invoices_RiskList()

    # 基地-首页-单据-采购订单-确认按钮(singleBtn)
    def Base_Invoices_OrderConfirm_Btn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_OrderConfirm_Btn()

    # # 基地-首页-单据-采购订单-确认按钮(multiBtn)
    # def Base_Invoices_OrderConfirm_Btn(self):
    #     try:
    #         flag = True
    #         # 获取当前列表list元素个数
    #         while (flag):
    #             el_len = self.base_driver.find_elements_by_id(
    #                 self.base_url + ":id/order_create_invoice_btn").__len__()
    #             print el_len
    #             # 遍历列表list元素并获取按钮名称的文本
    #             for i in range(el_len):
    #                 name_btn = u"确认订单"
    #                 text = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn")[
    #                     i].text
    #                 print text
    #                 product_quantities = self.base_driver.find_elements_by_id(self.base_url + ":id/order_count_tv")[
    #                     i].text
    #                 print product_quantities
    #                 # 对比每一列表的按钮名称，找到后点击该列表的“确认订单”按钮，遇到找不到的元素、索引超范围则重新再下滑动
    #                 if op.eq(name_btn, text):
    #                     print op.eq(name_btn, text)
    #                     if op.eq(self.proxy_quantities_str, product_quantities):
    #                         print op.eq(self.proxy_quantities_str, product_quantities)
    #                         try:
    #                             self.base_driver.find_elements_by_id(
    #                                 self.base_url + ":id/order_create_invoice_btn")[i].click()
    #                             flag = False
    #                             break
    #                         except NoSuchElementException:
    #                             pass
    #                         except IndexError:
    #                             pass
    #                     else:
    #                         pass
    #                 else:
    #                     continue
    #             if flag is True:
    #                 # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
    #                 self.base_driver.swipe(430, 1700, 430, 1175, 1000)
    #     except NoSuchElementException:
    #         self.Base_Invoices_OrderConfirm_Btn()

    # 基地-首页-单据-采购订单-订单信息页面-确认-按钮
    def Base_Invoices_OrderConfirm_MegBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url+":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_OrderConfirm_MegBtn()

    # 基地-首页-单据-采购订单-处理-按钮
    def Base_Invoices_ToProcess_Btn(self):
        try:
            flag = True
            # 获取当前列表list元素个数
            while (flag):
                el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn").__len__()
                print el_len
                # 遍历列表list元素并获取按钮名称的文本
                for i in range(el_len):
                    name_btn = u"处理"
                    text = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn")[i].text
                    print text
                    product_quantities = self.base_driver.find_elements_by_id(self.base_url + ":id/order_count_tv")[
                        i].text
                    print product_quantities
                    # 对比每一列表的按钮名称，找到后点击该列表的“处理”按钮，遇到找不到的元素、索引超范围则重新再下滑动
                    if op.eq(name_btn, text):
                        print op.eq(name_btn, text)
                        if op.eq(self.proxy_quantities_str, product_quantities):
                            print op.eq(self.proxy_quantities_str, product_quantities)
                            try:
                                self.base_driver.find_elements_by_id(
                                    self.base_url + ":id/order_create_invoice_btn")[i].click()
                                flag = False
                                break
                            except NoSuchElementException:
                                pass
                            except IndexError:
                                pass
                        else:
                            pass
                    else:
                        continue
                if flag is True:
                    # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
                    self.driver.swipe(430, 1700, 430, 1175, 1000)
        except NoSuchElementException:
            self.Base_Invoices_ToProcess_Btn()

    # 基地-首页-单据-采购订单-订单信息页面-处理-按钮
    def Base_Invoices_ToProcess_MegBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_ToProcess_MegBtn()

    # 基地-首页-单据-采购订单-处理完成-按钮
    def Base_Invoices_OrderCompleted_Btn(self):
        try:
            flag = True
            # 获取当前列表list元素个数
            while (flag):
                el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn").__len__()
                print el_len
                # 遍历列表list元素并获取按钮名称的文本
                for i in range(el_len):
                    name_btn = u"处理完成"
                    text = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn")[i].text
                    print text
                    product_quantities = self.base_driver.find_elements_by_id(self.base_url + ":id/order_count_tv")[
                        i].text
                    print product_quantities
                    # 对比每一列表的按钮名称，找到后点击该列表的“处理完成”按钮，遇到找不到的元素、索引超范围则重新再下滑动
                    if op.eq(name_btn, text):
                        print op.eq(name_btn, text)
                        if op.eq(self.proxy_quantities_str, product_quantities):
                            print op.eq(self.proxy_quantities_str, product_quantities)
                            try:
                                self.base_driver.find_elements_by_id(
                                    self.base_url + ":id/order_create_invoice_btn")[i].click()
                                flag = False
                                break
                            except NoSuchElementException:
                                pass
                            except IndexError:
                                pass
                        else:
                            pass
                    else:
                        continue
                if flag is True:
                    # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
                    self.base_driver.swipe(430, 1700, 430, 1175, 1000)
        except NoSuchElementException:
            self.Base_Invoices_OrderCompleted_Btn()

    # 基地-首页-单据-采购订单-订单信息页面-处理完成-按钮
    def Base_Invoices_OrderCompleted_MegBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_OrderCompleted_MegBtn()

    # 基地-首页-单据-采购订单-生成发货单-按钮
    def Base_Invoices_CreateShippingOrder_Btn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_CreateShippingOrder_Btn()


        # flag = True
        # # 获取当前列表“生成发货单”list元素个数
        # while (flag):
        #     el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn").__len__()
        #     print "el_len"
        #     print el_len
        #     # 遍历列表list元素并获取按钮名称的文本
        #     for i in range(el_len):
        #         name_btn = u"生成发货单"
        #         text = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn")[i].text
        #         print text
        #         product_quantities = self.base_driver.find_elements_by_id(self.base_url + ":id/order_count_tv")[
        #             i].text
        #         print product_quantities
        #         # 对比每一列表的按钮名称，找到后点击该列表的“生成发货单”按钮，遇到找不到的元素、索引超范围则重新再下滑动
        #         if op.eq(name_btn, text):
        #             print op.eq(name_btn, text)
        #             if op.eq(self.proxy_quantities_str, product_quantities):
        #                 print op.eq(self.proxy_quantities_str, product_quantities)
        #                 try:
        #                     self.base_driver.find_elements_by_id(
        #                         self.base_url + ":id/order_create_invoice_btn")[i].click()
        #                     flag = False
        #                     break
        #                 except NoSuchElementException:
        #                     pass
        #                 except IndexError:
        #                     pass
        #             else:
        #                 pass
        #         else:
        #             continue
        #     if flag is True:
        #         # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
        #         self.base_driver.swipe(430, 1700, 430, 1175, 1000)
        # sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-订单信息页面-生成发货单-按钮
    def Base_Invoices_CreateShippingOrder_MegBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_CreateShippingOrder_MegBtn()

    # 基地-首页-单据-采购订单-生成发货单页面输入内容
    def Base_Invoices_EditToShippingOrder(self):
        try:
            flag_text = True
            flag_selected = True
            el_content = [u"请输入物流公司", u"请输入拖头车牌号", u"请输入挂车牌号", u"请输入司机名称", u"请输入物流电话", u"请输入车厢温度", u"请输入运费金额"]
            write_content = [u"得意物流",u"粤A12345",u"粤B54321",u"来福","13588888888","3","100"]
            # logistics_company_name = u"请输入物流公司"
            # trailer_VIN = u"请输入拖头车牌号"
            # semi_VIN = u"请输入挂车牌号"
            # driver_name = u"请输入司机名称"
            # phone = u"请输入物流电话"
            # temperature = u"请输入车厢温度"
            # freight_fee = u"请输入运费金额"
            while(flag_text):
                try:
                    # 获取全部输入框元素，统计其数量
                    el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/list_value_edit").__len__()
                    # 遍历所有元素并获取文本内容
                    for i in range(el_len):
                        name_text = self.base_driver.find_elements_by_id(self.base_url + ":id/list_value_edit")[i].text
                        try:
                            #每段文本内容与所需输入框列表内容匹配，配对上的录入内容，并删除元素的对应列表内容
                            for j in range(el_content.__len__()):
                                if op.eq(el_content[j],name_text):
                                    self.base_driver.find_elements_by_id(self.base_url + ":id/list_value_edit")[i].click()
                                    # self.base_driver.find_elements_by_id(self.base_url + ":id/list_value_edit")[i].clear()
                                    self.base_driver.find_elements_by_id(self.base_url + ":id/list_value_edit")[i].send_keys(write_content[j])
                                    del write_content[j]
                                    del el_content[j]
                                else:
                                    continue
                            # 判断2个列表是否为空，为空就退出循环
                            if len(write_content) and len(el_content):
                                continue
                            else:
                                flag_text = False
                                break
                        except NoSuchElementException:
                            pass
                        except IndexError:
                            pass
                except NoSuchElementException:
                    pass
                except IndexError:
                    pass
                self.base_driver.swipe(430, 1700, 430, 1175, 1000)


            #循环选择输入框填写，默认选择第一项
            while(flag_selected):
                try:
                    el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/list_next_image").__len__()
                    for i in range(el_len):
                        self.base_driver.find_elements_by_id(self.base_url + ":id/list_next_image")[i].click()
                        self.base_driver.find_elements_by_id(self.base_url + ":id/hot_tags_content_tv")[0].click()
                    flag_selected = False
                except NoSuchElementException:
                    print "NoSuchElementException"
                except IndexError:
                    print "IndexError"

        except NoSuchElementException:
            self.Base_Invoices_EditToShippingOrder()

    # 基地-首页-单据-采购订单-生成发货单据-提交-按钮
    def Base_Invoices_SubmitShippingOrder(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
            sleep(self.seconds_short)
        except NoSuchElementException:
            self.Base_Invoices_SubmitShippingOrder()

    # 基地-首页-单据-发货单据-确认-按钮
    def Base_Invoices_ShipmentList_ConfirmBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentList_ConfirmBtn()

    # 基地-首页-单据-发货单据-发货单据详情-确认-按钮
    def Base_Invoices_ShipmentDetail_ConfirmBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentDetail_ConfirmBtn()

    # 基地-首页-单据-发货单据-司机签名-按钮
    def Base_Invoices_ShipmentList_DriverSignBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentList_DriverSignBtn()

    # 基地-首页-单据-发货单详情-司机签名-按钮
    def Base_Invoices_ShipmentDetail_DriverSignBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentDetail_DriverSignBtn()

    # 基地-首页-单据-发货单详情-司机签名画板
    def Base_Invoices_ShipmentPad_DriverSign(self):
        try:
            self.base_driver.swipe(430, 700, 430, 900, 1000)
            self.base_driver.find_element_by_id(self.base_url + ":id/signature_confirm_btn").click()
        except NoSuchElementException:
           self.Base_Invoices_ShipmentPad_DriverSign()

    # 基地-首页-单据-发货单单据-发车-按钮
    def Base_Invoices_ShipmentList_DepartBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentList_DepartBtn()

    # 基地-首页-单据-发货单详情-发车-按钮
    def Base_Invoices_ShipmentDetail_DepartBtn(self):
        try:
            self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Base_Invoices_ShipmentDetail_DepartBtn()









    # 首页-入驻档口（按钮）----------------------------
    def Settled_Button(self):
        # 点击-入驻基地-按钮
        self.driver.find_element_by_id(self.trade_url + ":id/home_superMode_ll").click()
        sleep(self.seconds_short)

    # 首页-交易大厅（按钮）----------------------------
    def Trade_Button(self):
        self.driver.find_element_by_id(self.trade_url+":id/home_presell_project_ll").click()
        sleep(self.seconds_short)

    # 首页-交易大厅（按钮）-交易产品---------------------
    def Market_Bar_TradeProduce(self):
        el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
        print el_len
        for i in range(el_len):
            title_bar_name = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
            print title_bar_name
            if op.eq(self.trade_produce,title_bar_name):
                self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                break
            else:
                continue
        sleep(self.seconds_short)

    # 首页-交易大厅（按钮）-交易产品-申请代销--------------
    # 在交易产品列表滑动查找目标基地名称，查找到后停止滑动
    def Deal_Product(self):
        try:
            flag = True
            # 获取当前列表list元素个数
            while (flag):
                el_len = self.driver.find_elements_by_id(self.trade_url+":id/home_deal_deal_product_name_tv").__len__()
                print el_len
                # 遍历列表list元素并获取产品名称的文本
                for i in range(el_len):
                    product_presell = self.driver.find_elements_by_id(self.trade_url+":id/home_deal_deal_product_name_tv")[i].text
                    print product_presell
                    # 对比每一列表的产品名称，找到后点击该列表的“申请代销”按钮，遇到找不到的元素、索引超范围则重新再下滑动
                    if op.eq(self.product_presell,product_presell):
                        try:
                            self.driver.find_elements_by_id(self.trade_url+":id/home_deal_deal_product_apply_sell_tv")[i].click()
                        except NoSuchElementException:
                            continue
                        except IndexError:
                            continue
                        flag = False
                        break
                    else:
                        continue
                if flag is True:
                    # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
                    self.driver.swipe(430, 1700, 430, 1175, 1000)
        except NoSuchElementException:
            self.Deal_Product()


    # 点击代销规则说明“知道了”按钮
    def Know_Button(self):
        try:
            self.driver.find_element_by_id(self.trade_url+":id/item_bottom_btn").click()
        except NoSuchElementException:
            self.Know_Button()

    # 录入申请代销信息和提交
    def Order_Input(self):
        try:
            # 输入件数
            self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_number_count_edit").send_keys(
                self.proxy_quantities)
            # 输入斤数
            self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_weight_edit").send_keys(
                self.proxy_weight)
            # 向上滑动525像素
            self.driver.swipe(430, 1700, 430, 1175, 1000)

            # 点击收货人地址
            self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_recriving_address_ll").click()

            flag = True
            while (flag):
                try:
                    # 进入收货地址选择页面点击收货地址
                    self.driver.find_element_by_id(self.trade_url + ":id/shipping_address_tv").click()
                    flag = False
                    break
                except NoSuchElementException:
                    pass

            # 点击-提交按钮
            self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_confirm_btn").click()


            # flag = True
            # while(flag):
            #     try:
            #         proxy_quantities = self.driver.find_element_by_id(self.trade_url+":id/consignment_sell_number_count_edit").text
            #         proxy_weight = self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_number_count_edit").text
            #         if op.eq(self.proxy_quantities,proxy_quantities):
            #             pass
            #         else:
            #             self.driver.find_element_by_id(self.trade_url+":id/consignment_sell_number_count_edit").send_keys(self.proxy_quantities)
            #
            #         if op.eq(self.proxy_weight,proxy_weight):
            #             pass
            #         else:
            #             self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_number_count_edit").send_keys(self.proxy_weight)
            #
            #         self.driver.find_element_by_id(self.trade_url +":id/consignment_sell_recriving_address_ll").click()
            #         self.driver.find_element_by_id(self.trade_url +":id/shipping_address_tv").click()
            #         sleep(self.seconds_short)
            #
            #         self.driver.find_element_by_id(self.trade_url +":id/consignment_sell_confirm_btn").click()
            #         sleep(self.seconds_short)
            #         break
            #     except NoSuchElementException:
            #         self.driver.swipe(430, 1700, 430, 1175, 1000)
            #         continue
        except NoSuchElementException:
            self.Order_Input()

    # 主管验证采购订单
    def Purchase_Order_Verify(self):
        try:
            flag = True
            # 获取当前列表list元素个数
            while (flag):
                el_len = self.driver.find_elements_by_id(self.trade_url+":id/documents_procurement_order_create_invoice_btn").__len__()
                print el_len
                # 遍历列表list元素并获取产品名称的文本
                for i in range(el_len):
                    product_name = self.driver.find_elements_by_id(self.trade_url+":id/documents_procurement_order_name_tv")[i].text
                    print product_name
                    product_quantities = self.driver.find_elements_by_id(self.trade_url + ":id/documents_procurement_order_count_tv")[i].text
                    print product_quantities
                    # 对比每一列表的产品名称，找到后点击该列表的“验证”按钮，遇到找不到的元素、索引超范围则重新再下滑动
                    if op.eq(self.product_presell,product_name):
                        print op.eq(self.product_presell,product_name)
                        if op.eq(self.proxy_quantities_str,product_quantities):
                            print op.eq(self.proxy_quantities_str,product_quantities)
                            try:
                                self.driver.find_elements_by_id(self.trade_url+":id/documents_procurement_order_create_invoice_btn")[i].click()
                                flag = False
                                break
                            except NoSuchElementException:
                                pass
                            except IndexError:
                                pass
                        else:
                            pass
                    else:
                        continue
                if flag is True:
                    # 屏幕滑动高度距离，1700-1175=525px的高度（1个列表+分隔杠的距离）
                    self.driver.swipe(430, 1700, 430, 1175, 1000)

        except NoSuchElementException:
            self.Purchase_Order_Verify()

    # 主管验证采购订单
    def Order_Verify(self):
        try:
            #点击-验证
            self.driver.find_element_by_id(self.trade_url+":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.Order_Verify()

    # # 启动基地
    # def base_launch(self):
    #     self.driver.start_activity(self.appPackage,self.appActivity)
    #     sleep(self.seconds_short)

    # 首页-我的
    def MyInfoList(self):
        try:
            # 点击-我的-按钮
            my_text = u"我的"
            el_len = self.driver.find_elements_by_id(self.trade_url+":id/bottom_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url+":id/bottom_tv")[i].text
                if op.eq(text,my_text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/bottom_tv")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.MyInfoList()

    # 首页-我的-我的菜品列表页面
    def MyInfoList_MyProductList(self):
        try:
            # 点击-我的菜品-按钮
            my_text = u"我的菜品"
            el_len = self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv")[i].text
                if op.eq(text, my_text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.MyInfoList_MyProductList()




    # 首页-我的-我的菜品列表-新增-按钮
    def MyInfoList_MyProductList_AddProductBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/title_switch_image").click()
        except NoSuchElementException:
            self.MyInfoList_MyProductList_AddProductBtn()

    # 首页-我的-我的菜品列表-新增-按钮-新增资料页面
    def MyInfoList_MyProductList_AddProductBtn_Info(self):

        products_info = u"菜品名称"
        products_info_chose = [u"菜品品种", u"菜品产地", u"供应商"]
        products_class = [u"蔬菜类", u"茄果类", u"线椒"]
        products_name = u"红线椒"
        products_origin = [u"广西", u"贺州", u"钟山"]
        try:
            el_len = self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_ll").__len__()
            for i in range(el_len):
                try:
                    if i==0:
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].send_keys(products_name)
                    else:
                        pass
                except NoSuchElementException:
                    pass
                try:
                    if i==1:
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/city_confirm_tv").click()
                        sleep(self.seconds_short)
                    else:
                        pass
                except NoSuchElementException:
                    pass
                try:
                    if i==2:
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                        sleep(self.seconds_short)

                        # 地址多项/列选择。方法三：代码少，回归执行思路清晰，容易理解
                        flag_origin_level = [True, True, True]
                        for k in range(3):
                            while(flag_origin_level[k]):
                                el_len_origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv").__len__()
                                for j in range(el_len_origin):
                                    origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].text
                                    if op.eq(origin,products_origin[k]):
                                        self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].click()
                                        flag_origin_level[k] = False
                                        break
                                    else:
                                        pass
                                self.driver.swipe(130,1776,130,1476,1000)
                        self.driver.find_element_by_id(self.trade_url + ":id/city_confirm_tv").click()

                        # -----------------------------------------------------------------------------------------------------
                        # 地址多项/列选择。方法二：直观筛选，（劣势：代码重复，量大）
                        # flag_origin_level_1 = True
                        # flag_origin_level_2 = True
                        # flag_origin_level_3 = True
                        # while(flag_origin_level_1):
                        #     el_len_origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv").__len__()
                        #     for j in range(el_len_origin):
                        #         origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].text
                        #         if op.eq(origin,u"广西"):
                        #             self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].click()
                        #             flag_origin_level_1 = False
                        #             break
                        #         else:
                        #             pass
                        #     self.driver.swipe(130,1776,130,1476,1000)
                        #
                        # while (flag_origin_level_2):
                        #     el_len_origin = self.driver.find_elements_by_id(
                        #         self.trade_url + ":id/item_city_name_tv").__len__()
                        #     for j in range(el_len_origin):
                        #         origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[
                        #             j].text
                        #         if op.eq(origin, u"贺州"):
                        #             self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].click()
                        #             flag_origin_level_2 = False
                        #             break
                        #         else:
                        #             pass
                        #     self.driver.swipe(130, 1776, 130, 1476, 1000)
                        #
                        # while (flag_origin_level_3):
                        #     el_len_origin = self.driver.find_elements_by_id(
                        #         self.trade_url + ":id/item_city_name_tv").__len__()
                        #     for j in range(el_len_origin):
                        #         origin = self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[
                        #             j].text
                        #         if op.eq(origin, u"钟山"):
                        #             self.driver.find_elements_by_id(self.trade_url + ":id/item_city_name_tv")[j].click()
                        #             flag_origin_level_3 = False
                        #             break
                        #         else:
                        #             pass
                        #     self.driver.swipe(130, 1776, 130, 1476, 1000)
                        # self.driver.find_element_by_id(self.trade_url + ":id/city_confirm_tv").click()
                        # -----------------------------------------------------------------------------------------------------

                        #---------------------------------------------------------------------------------
                        # 地址多项/列选择。方法一：固定选择第一项（劣势：缺少灵活度）
                        # self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        # sleep(self.seconds_short)
                        # self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        # sleep(self.seconds_short)
                        # self.driver.find_element_by_id(self.trade_url + ":id/item_city_name_tv").click()
                        # sleep(self.seconds_short)
                        # self.driver.find_element_by_id(self.trade_url + ":id/city_confirm_tv").click()
                        # sleep(self.seconds_short)
                        #----------------------------------------------------------------------------------
                    else:
                        pass
                except NoSuchElementException:
                    pass
                try:
                    if i==3:
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                        sleep(self.seconds_short)
                        self.driver.find_element_by_id(self.trade_url + ":id/suppliers_name_tv").click()
                        sleep(self.seconds_short)
                    else:
                        pass
                except NoSuchElementException:
                    pass
            self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyInfoList_MyProductList_AddProductBtn_Info()



    # 首页-我的-员工管理列表页面
    def MyInfoList_EmployeeList(self):
        try:
            # 点击-我的-按钮
            my_text = u"员工管理"
            el_len = self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv")[i].text
                if op.eq(text, my_text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.MyInfoList_EmployeeList()

    # 首页-我的-员工管理列表页面-添加员工
    def MyInfoList_EmpoyeeList_AddEmpoyee(self):
        try:
            # 点击-"+"-按钮
            self.driver.find_element_by_id(self.trade_url + ":id/title_switch_image").click()
            el_contents = [u"请输入被添加人姓名", u"请输入被添加人的手机号码", u"请输入邮箱地址"]
            employee_info = [u"蒙岛", "13455555588", "13455555588@qq.com"]
            el_len = self.driver.find_elements_by_id(
                self.trade_url + ":id/mine_edit_personage_content_tv").__len__()
            for i in range(el_len):
                el_text = self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].text
                for j in range((employee_info.__len__())):
                    if op.eq(el_text, el_contents[j]):
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].send_keys(employee_info[j])
                        del el_contents[j]
                        del employee_info[j]
                        break
                    else:
                        pass
                # 选择档口、角色
                if op.eq(el_text,u"请选择"):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                    flag = True
                    while(flag):
                        try:
                            # 选择第一个档口
                            self.driver.find_element_by_id(self.trade_url + ":id/stall_name_tv").click()
                            flag = False
                        except NoSuchElementException:
                            try:
                                # 选择第一个角色
                                self.driver.find_element_by_id(self.trade_url + ":id/role_list_roleName_tv").click()
                                flag = False
                            except NoSuchElementException:
                                pass
            self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyInfoList_EmpoyeeList_AddEmpoyee()

    # 首页-我的-我的信息页面
    def MyInfoList_CustomerList(self):
        try:
            # 点击-我的-按钮
            my_text = u"我的客户"
            el_len = self.driver.find_elements_by_id(self.trade_url+":id/mine_item_key_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url+":id/mine_item_key_tv")[i].text
                if op.eq(text,my_text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_key_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.MyInfoList_CustomerList()

    # 首页-我的-我的信息页面-添加我的客户
    def MyInfoList_CustomerList_AddCustomer(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/title_switch_image").click()
            el_contents =[u"请输入客户名称",u"请输入联系人名称",u"请输入手机号码",u"请输入邮箱地址",u"请输入收货地址",u"￥0.00"]
            customer_info = [u"black科技123",u"三丰like123","13455555511","13455555511@qq.com",u"硅谷路13号","0"]
            el_len = self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv").__len__()
            # 点击-"+"-按钮
            for i in range(el_len):
                el_text = self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].text
                for j in range((customer_info.__len__())):
                    if op.eq(el_text,el_contents[j]):
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                        self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].send_keys(customer_info[j])
                        del el_contents[j]
                        del customer_info[j]
                        break
                    else:
                        pass
            self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyInfoList_CustomerList_AddCustomer()

    # 功能+（功能列表）
    def FuncPlusMark(self):
        try:
            self.driver.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[2].click()
        except NoSuchElementException:
            self.FuncPlusMark()

    # 功能+（-功能列表）-正常销售-按钮
    def FuncPlusMark_SaleBtn(self):
        try:
            el_len = self.driver.find_elements_by_id(self.trade_url + ":id/meun_title_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url + ":id/meun_title_tv")[i].text
                if op.eq(text,u"正常销售"):
                    self.driver.find_elements_by_id(self.trade_url + ":id/meun_title_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn()

    # 功能+（-功能列表）-正常销售-按钮-客户信息-按钮
    def FuncPlusMark_SaleBtn_CustomerInfoBtn(self):
        try:
            customer_info_btn = u"客户信息"
            el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(customer_info_btn,text):
                    self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_CustomerInfoBtn()

    # 功能+（-功能列表）-正常销售-按钮-客户信息-按钮-散客-选择
    def FuncPlusMark_SaleBtn_CustomerInfoBtn_Customer(self):
        try:
            # 点击选择散客
            self.driver.find_element_by_id(self.trade_url + ":id/customer_message_scattered_radio").click()
            # 点击确认按钮
            self.driver.find_element_by_id(self.trade_url + ":id/customer_message_confirm_tv").click()
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_CustomerInfoBtn_Customer()

    # 功能+（-功能列表）-正常销售-按钮-客户信息-按钮-客户-选择
    def FuncPlusMark_SaleBtn_CustomerInfoBtn_client(self):
        try:
            # 点击选择客户
            self.driver.find_element_by_id(self.trade_url + ":id/customer_message_customer_radio").click()
            client_name = u"饼盛"
            flag = True
            while(flag):
                try:
                    self.driver.find_element_by_id(self.trade_url + ":id/customer_message_add_customer_tv").click()
                    el_len = self.driver.find_elements_by_id(self.trade_url + ":id/filter_dialog_list_content_tv").__len__()
                    for i in range(el_len):
                        text = self.driver.find_elements_by_id(self.trade_url + ":id/filter_dialog_list_content_tv")[i].text
                        if op.eq(client_name,text):
                            self.driver.find_elements_by_id(self.trade_url + ":id/filter_dialog_list_content_tv")[i].click()
                            #在客户列表点击“确定”按钮
                            self.driver.find_element_by_id(self.trade_url + ":id/filter_dialog_confirm_tv").click()
                            flag = False
                            break
                        else:
                            pass
                except NoSuchElementException:
                    pass
            # 点击确认按钮
            self.driver.find_element_by_id(self.trade_url + ":id/customer_message_confirm_tv").click()
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_CustomerInfoBtn_client()




    # 功能+（-功能列表）-正常销售-按钮-选择菜品-按钮
    def FuncPlusMark_SaleBtn_SelectProductBtn(self):
        try:
            select_product_btn = u"选择菜品"
            el_len = self.driver.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(select_product_btn, text):
                    self.driver.find_elements_by_class_name("android.widget.TextView")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_SelectProductBtn()

    # 功能+（-功能列表）-正常销售-按钮-选择菜品-按钮-选择菜品页面输入信息
    def FuncPlusMark_SaleBtn_SelectProductBtn_SaveInfo(self):
        try:
            product_text = u"菜品"
            product_name = u"线椒A小"
            quantity_text = u"件数"
            weight_text = u"斤数"
            unit_price = u"参考单价"
            el_len = self.driver.find_elements_by_id(self.trade_url +":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(product_text,text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].click()
                    flag = True
                    while(flag):
                        try:
                            productsList_len = self.driver.find_elements_by_id(self.trade_url + ":id/role_list_roleName_tv").__len__()
                            for j in range(productsList_len):
                                text_name = self.driver.find_elements_by_id(self.trade_url + ":id/role_list_roleName_tv")[j].text
                                if op.eq(text_name,product_name):
                                    self.driver.find_elements_by_id(self.trade_url + ":id/role_list_roleName_tv")[j].click()
                                    flag = False
                                    break
                                else:
                                    pass
                        except NoSuchElementException:
                            continue
                if op.eq(quantity_text,text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[i].send_keys("2")
                if op.eq(weight_text, text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[
                        i].clear()
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[
                        i].send_keys("40")
                if op.eq(unit_price, text):
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[
                        i].clear()
                    self.driver.find_elements_by_id(self.trade_url + ":id/mine_edit_personage_content_tv")[
                        i].send_keys("30")
            self.driver.find_element_by_id(self.trade_url + ":id/amount_save_tv").click()
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_SelectProductBtn_SaveInfo()

    # 功能+（-功能列表）-正常销售-按钮-保存-按钮
    def FuncPlusMark_SaleBtn_SaveBtn(self):
        try:
            self.driver.find_element_by_id(self.trade_url + ":id/amount_save_tv").click()
        except NoSuchElementException:
            self.FuncPlusMark_SaleBtn_SaveBtn()

    # 我的-设置
    def SettingView(self):
        # 设置按钮
        self.driver.find_element_by_id(self.trade_url + ":id/mine_setting_image").click()
        sleep(self.seconds_short)
        # 术语/条款
        self.driver.find_element_by_id(self.trade_url + ":id/setting_clause_ll").click()
        sleep(self.seconds_short)
        self.driver.find_element_by_id(self.trade_url + ":id/title_left_image").click()
        sleep(self.seconds_short)
        # 使用指南
        self.driver.find_element_by_id(self.trade_url + ":id/mine_account_instructions_ll").click()
        sleep(self.seconds_short)
        self.driver.find_element_by_id(self.trade_url + ":id/title_left_image").click()
        sleep(self.seconds_short)
        # 关于我们
        self.driver.find_element_by_id(self.trade_url + ":id/mine_account_regard_we_ll").click()
        sleep(self.seconds_short)
        self.driver.find_element_by_id(self.trade_url + ":id/title_left_image").click()
        sleep(self.seconds_short)
        # 联系客服
        self.driver.find_element_by_id(self.trade_url + ":id/mine_account_onlineService_ll").click()
        sleep(self.seconds_short)
        # 电话客服
        self.driver.find_element_by_id(self.trade_url + ":id/tel_service_ll").click()
        sleep(self.seconds_short)
        self.Back_PhysicsBtn()
        sleep(self.seconds_short)
        # 在线客服
        self.driver.find_element_by_id(self.trade_url + ":id/online_service_ll").click()
        sleep(self.seconds_short)
        # 选择客服组
        flag = True
        while(flag):
            try:
                self.driver.find_elements_by_id(self.trade_url + ":id/mine_item_ll")[0].click()
                sleep(self.seconds_short)
                self.driver.find_element_by_id(self.trade_url + ":id/udesk_confirm_pop_positive").click()
                sleep(self.seconds_short)
                self.driver.find_element_by_id(self.trade_url + ":id/udesk_back_linear").click()
                sleep(self.seconds_short)
                self.driver.find_element_by_id(self.trade_url + ":id/title_left_image").click()
                flag = False
            except IndexError:
                pass
        # 在线留言
        self.driver.find_element_by_id(self.trade_url + ":id/online_guestbook_ll").click()
        sleep(self.seconds_short)
        # 留言页面后退
        self.driver.find_element_by_id(self.trade_url + ":id/udesk_back_img").click()
        sleep(self.seconds_short)
        self.Back_PhysicsBtn()
        self.Back_PhysicsBtn()

        # 蓝牙配置
        self.driver.find_element_by_id(self.trade_url + ":id/setting_out_bluetooth_ll").click()
        sleep(self.seconds_short)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        sleep(self.seconds_short)
        self.Back_PhysicsBtn()

        # 退出系统
        self.driver.find_element_by_id(self.trade_url + ":id/setting_out_login_ll").click()
        sleep(self.seconds_short)
        self.driver.find_element_by_id(self.trade_url + ":id/pupop_dialog_confirm").click()

# 快速启动基地
    def base_launch(self):
        self.driver.start_activity(self.base_appPackage,self.base_appActivity)
        sleep(self.seconds_short)

# 快速启动商城
    def Trade_Launch(self):
        self.driver.start_activity(self.trade_appPackage,self.trade_appActivity)
        sleep(self.seconds_short)







if __name__ == '__main__':

    # # 申请代销订单
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    # tradeRun.Trade_Button()
    # tradeRun.Market_Bar_TradeProduce()
    # tradeRun.Deal_Product()
    # tradeRun.Know_Button()
    # tradeRun.Deal_Product()
    # tradeRun.Order_Input()
    # tradeRun.Purchase_Order_Verify()
    # tradeRun.Order_Verify()
    # tradeRun.Close_App()

    # # 基地订单确认、生成发货单、发车
    # baseRun = AppRun()
    # baseRun.Base_Driver()
    # baseRun.Base_Launch_App()
    # baseRun.Base_Pass_Banner()
    # baseRun.Base_Evr_Selected()
    # baseRun.Base_Login_By_Pwd()
    # baseRun.Base_Authorization_Sys()
    # baseRun.Base_Invoices()
    # baseRun.Base_Invoices_OrderList()
    # baseRun.Base_Invoices_OrderConfirm_Btn()
    # baseRun.Base_Invoices_OrderConfirm_MegBtn()
    # baseRun.Base_Invoices_ToProcess_Btn()
    # baseRun.Base_Invoices_ToProcess_MegBtn()
    # baseRun.Base_Invoices_OrderCompleted_Btn()
    # baseRun.Base_Invoices_OrderCompleted_MegBtn()
    # baseRun.Base_Invoices_CreateShippingOrder_Btn()
    # baseRun.Base_Invoices_CreateShippingOrder_MegBtn()
    # baseRun.Base_Invoices_EditToShippingOrder()
    # baseRun.Base_Invoices_SubmitShippingOrder()
    # baseRun.Base_Back_PhysicsBtn()
    # baseRun.Base_Back_PhysicsBtn()
    # baseRun.Base_Invoices_ShipmentList()
    # baseRun.Base_Invoices_ShipmentList_ConfirmBtn()
    # baseRun.Base_Invoices_ShipmentDetail_ConfirmBtn()
    # baseRun.Base_Invoices_ShipmentList_DriverSignBtn()
    # baseRun.Base_Invoices_ShipmentDetail_DriverSignBtn()
    # baseRun.Base_Invoices_ShipmentPad_DriverSign()
    # baseRun.Base_Invoices_ShipmentList_DepartBtn()
    # baseRun.Base_Invoices_ShipmentDetail_DepartBtn()
    # baseRun.Base_Close_App()

    # # 接车验货
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    # tradeRun.PickupInspect()
    # tradeRun.PickupList_PickupBtn()
    # # tradeRun.PickupList_HadPickupList()
    # tradeRun.PickupList_HadPickupList_InspectBtn()
    # tradeRun.PickupList_HadPickupList_CreateDamageDetail()
    # tradeRun.PickupList_HadPickupList_CreateTemplature()
    # tradeRun.PickupList_HadPickupList_InspectPage_Submit()
    # tradeRun.PickupList_HadPickupList_InspectPage_comfirmBtn()
    # tradeRun.PickupList_HadPickupDetail_InspectPage_comfirmBtn()

    # # 正常销售
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    # tradeRun.FuncPlusMark()
    # tradeRun.FuncPlusMark_SaleBtn()
    # tradeRun.FuncPlusMark_SaleBtn_CustomerInfoBtn()
    # tradeRun.FuncPlusMark_SaleBtn_CustomerInfoBtn_client()
    # tradeRun.FuncPlusMark_SaleBtn_SelectProductBtn()
    # tradeRun.FuncPlusMark_SaleBtn_SelectProductBtn_SaveInfo()
    # tradeRun.FuncPlusMark_SaleBtn_SaveBtn()






    # # 我的-我的客户-添加客户
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    #
    # tradeRun.MyInfoList()
    # tradeRun.MyInfoList_CustomerList()
    # tradeRun.MyInfoList_CustomerList_AddCustomer()

    # # 我的-我的客户-添加客户
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    #
    # tradeRun.MyInfoList()
    # tradeRun.MyInfoList_EmployeeList()
    # tradeRun.MyInfoList_EmpoyeeList_AddEmpoyee()

    # 我的-我的菜品-添加菜品
    tradeRun = AppRun()
    tradeRun.Driver()
    tradeRun.Launch_App()
    tradeRun.Pass_Banner()
    tradeRun.Evr_Selected()
    tradeRun.Login_By_Pwd()
    tradeRun.Authorization_Sys()
    # tradeRun.Trade_Launch()

    tradeRun.MyInfoList()
    tradeRun.MyInfoList_MyProductList()
    tradeRun.MyInfoList_MyProductList_AddProductBtn()
    tradeRun.MyInfoList_MyProductList_AddProductBtn_Info()


    # # 我的-设置(所有操作）
    # tradeRun = AppRun()
    # tradeRun.Driver()
    # tradeRun.Launch_App()
    # tradeRun.Pass_Banner()
    # tradeRun.Evr_Selected()
    # tradeRun.Login_By_Pwd()
    # tradeRun.Authorization_Sys()
    #
    # tradeRun.MyInfoList()
    # tradeRun.SettingView()







    # driver.start_activity("base.sale.onlty.com","base.sale.onlty.com.activity.SplashActivity")
    # sleep(4)
    # driver.start_activity("trade.sale.onlty.com","trade.sale.onlty.com.activity.SplashActivity")