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
        sleep(self.seconds_long)

    # 市场端关闭APP---------------------------------------------------------
    def Close_App(self):
        self.driver.close_app()
        sleep(self.seconds_long)

    # 市场端物理返回键（返回键代码4）---------------------------------------------------------
    def Back_PhysicsBtn(self):
        self.driver.press_keycode(4)
        print "press_keycode"
        sleep(self.seconds_long)

    # 市场端BANNER首页“跳过”-------------------------------------------------
    def Pass_Banner(self):
        self.driver.find_element_by_id(self.trade_url+":id/next_button").click()
        sleep(self.seconds_short)

    # 基地端启动APP---------------------------------------------------------
    def Base_Launch_App(self):
        self.base_driver.launch_app()
        sleep(self.seconds_long)

    # 基地端关闭APP---------------------------------------------------------
    def Base_Close_App(self):
        self.base_driver.close_app()
        sleep(self.seconds_long)

    # 基地端物理返回键（返回键代码4）---------------------------------------------------------
    def Base_Back_PhysicsBtn(self):
        self.base_driver.press_keycode(4)
        print "press_keycode"
        sleep(self.seconds_long)

    # 基地端BANNER首页“跳过”-------------------------------------------------
    def Base_Pass_Banner(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/next_button").click()
        sleep(self.seconds_short)

    # 选择登录环境---------------------------------------------------------
    def Evr_Selected(self):
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

    # 基地选择登录环境---------------------------------------------------------
    def Base_Evr_Selected(self):
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
        sleep(self.seconds_short)

    # 用户登录----------------------------------
    def Login_By_Pwd(self):
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
        sleep(self.seconds_short)

    # 基地用户登录----------------------------------
    def Base_Login_By_Pwd(self):
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
        sleep(self.seconds_long)

    # 首次登录系统设备授权--------------------------------
    def Authorization_Sys(self):
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

        sleep(self.seconds_short)

    # 首页-接车查验
    def PickupInspect(self):
        self.driver.find_element_by_id(self.trade_url + ":id/home_product_transaction_ll").click()
        sleep(self.seconds_short)

    # 首页-接车列表-已接车列表
    def PickupList_HadPickupList(self):
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
        sleep(self.seconds_short)

    # 首页-待接车列表页面-接车-按钮
    def PickupList_PickupBtn(self):
        self.driver.find_element_by_id(self.trade_url + ":id/reception_await_car_invoice_btn").click()
        sleep(self.seconds_short)

    # 首页-已接车列表页面-验货-按钮
    def PickupList_HadPickupList_InspectBtn(self):
        self.driver.find_element_by_id(self.trade_url + ":id/reception_alread_car_invoice_btn").click()
        sleep(self.seconds_short)

    # 首页-已接车列表页面-验货页面-新增货损明细
    def PickupList_HadPickupList_CreateDamageDetail(self):
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
            self.driver.swipe(430, 1700, 430, 875, 1000)
        sleep(self.seconds_short)

    # 首页-接车验货-已接车-验货-新增测温明细
    def PickupList_HadPickupList_CreateTemplature(self):
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
            self.driver.swipe(430, 1700, 430, 1175, 1000)

    # 首页-接车验货-已接车-验货-提交-按钮
    def PickupList_HadPickupList_InspectPage_Submit(self):
        self.driver.find_element_by_id(self.trade_url + ":id/bottom_right_btn").click()
        self.driver.find_element_by_id(self.trade_url + ":id/pupop_dialog_confirm").click()
        sleep(self.seconds_long)

    # 基地-首次登录系统设备授权--------------------------------
    def Base_Authorization_Sys(self):
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
        sleep(self.seconds_short)

    # 基地-首页-单据
    def Base_Invoices(self):
        text = u"单据"
        bottom_tv_len = self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv").__len__()
        for i in range(bottom_tv_len):
            bottom_tv_text = self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv")[i].text
            if op.eq(bottom_tv_text,text):
                self.base_driver.find_elements_by_id(self.base_url + ":id/bottom_tv")[i].click()
                sleep(self.seconds_short)
                break
            else:
                continue
    # 基地-首页-单据-采购订单
    def Base_Invoices_OrderList(self):
        self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[0].click()
        sleep(self.seconds_short)

    # 基地-首页-单据-发货单据
    def Base_Invoices_ShipmentList(self):
        self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[1].click()
        sleep(self.seconds_short)

    # 基地-首页-单据-结算单据
    def Base_Invoices_SettlementList(self):
        self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[2].click()
        sleep(self.seconds_short)

    # 基地-首页-单据-付款凭证
    def Base_Invoices_EvidenceOfPaymentList(self):
        self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[3].click()
        sleep(self.seconds_short)

    # 基地-首页-单据-风险单据
    def Base_Invoices_RiskList(self):
        self.base_driver.find_elements_by_id(self.base_url + ":id/documents_list_image")[4].click()
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-确认按钮
    def Base_Invoices_OrderConfirm_Btn(self):
        flag = True
        # 获取当前列表list元素个数
        while (flag):
            el_len = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn").__len__()
            print el_len
            # 遍历列表list元素并获取按钮名称的文本
            for i in range(el_len):
                name_btn = u"确认订单"
                text = self.base_driver.find_elements_by_id(self.base_url + ":id/order_create_invoice_btn")[i].text
                print text
                product_quantities = self.base_driver.find_elements_by_id(self.base_url + ":id/order_count_tv")[i].text
                print product_quantities
                # 对比每一列表的按钮名称，找到后点击该列表的“确认订单”按钮，遇到找不到的元素、索引超范围则重新再下滑动
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
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-订单信息页面-确认-按钮
    def Base_Invoices_OrderConfirm_MegBtn(self):
        self.base_driver.find_element_by_id(self.base_url+":id/order_meassage_commit_btn").click()
        sleep(self.seconds_long)

    # 基地-首页-单据-采购订单-处理-按钮
    def Base_Invoices_ToProcess_Btn(self):
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
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-订单信息页面-处理-按钮
    def Base_Invoices_ToProcess_MegBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        sleep(self.seconds_long)

    # 基地-首页-单据-采购订单-处理完成-按钮
    def Base_Invoices_OrderCompleted_Btn(self):
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
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-订单信息页面-处理完成-按钮
    def Base_Invoices_OrderCompleted_MegBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-生成发货单-按钮
    def Base_Invoices_CreateShippingOrder_Btn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/order_create_invoice_btn").click()
        sleep(self.seconds_short)


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
        self.base_driver.find_element_by_id(self.base_url + ":id/order_meassage_commit_btn").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-生成发货单页面输入内容
    def Base_Invoices_EditToShippingOrder(self):
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
        sleep(self.seconds_short)

    # 基地-首页-单据-采购订单-生成发货单据-提交-按钮
    def Base_Invoices_SubmitShippingOrder(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-发货单据-确认-按钮
    def Base_Invoices_ShipmentList_ConfirmBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        sleep(self.seconds_long)

    # 基地-首页-单据-发货单据-发货单据详情-确认-按钮
    def Base_Invoices_ShipmentDetail_ConfirmBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-发货单据-司机签名-按钮
    def Base_Invoices_ShipmentList_DriverSignBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        sleep(self.seconds_long)

    # 基地-首页-单据-发货单详情-司机签名-按钮
    def Base_Invoices_ShipmentDetail_DriverSignBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-发货单详情-司机签名画板
    def Base_Invoices_ShipmentPad_DriverSign(self):
        self.base_driver.swipe(430, 700, 430, 900, 1000)
        self.base_driver.find_element_by_id(self.base_url + ":id/signature_confirm_btn").click()
        sleep(self.seconds_long)

    # 基地-首页-单据-发货单单据-发车-按钮
    def Base_Invoices_ShipmentList_DepartBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/shipments_contact_driver_btn").click()
        sleep(self.seconds_short)

    # 基地-首页-单据-发货单详情-发车-按钮
    def Base_Invoices_ShipmentDetail_DepartBtn(self):
        self.base_driver.find_element_by_id(self.base_url + ":id/bottom_btn_right").click()
        sleep(self.seconds_short)









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
        sleep(self.seconds_short)

    # 点击代销规则说明“知道了”按钮
    def Know_Button(self):
        self.driver.find_element_by_id(self.trade_url+":id/item_bottom_btn").click()
        sleep(self.seconds_short)

    # 录入申请代销信息和提交
    def Order_Input(self):
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
        sleep(self.seconds_short)
        # 进入收货地址选择页面点击收货地址
        self.driver.find_element_by_id(self.trade_url + ":id/shipping_address_tv").click()
        sleep(self.seconds_short)
        # 点击-提交按钮
        self.driver.find_element_by_id(self.trade_url + ":id/consignment_sell_confirm_btn").click()
        sleep(self.seconds_short)

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

    # 主管验证采购订单
    def Purchase_Order_Verify(self):
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
        sleep(self.seconds_short)

    # 主管验证采购订单
    def Order_Verify(self):
        #点击-验证
        self.driver.find_element_by_id(self.trade_url+":id/bottom_right_btn").click()
        sleep(self.seconds_short)

    # # 启动基地
    # def base_launch(self):
    #     self.driver.start_activity(self.appPackage,self.appActivity)
    #     sleep(self.seconds_short)






if __name__ == '__main__':
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

    tradeRun = AppRun()
    tradeRun.Driver()
    tradeRun.Launch_App()
    tradeRun.Pass_Banner()
    tradeRun.Evr_Selected()
    tradeRun.Login_By_Pwd()
    tradeRun.Authorization_Sys()
    tradeRun.PickupInspect()
    # tradeRun.PickupList_PickupBtn()
    tradeRun.PickupList_HadPickupList()
    tradeRun.PickupList_HadPickupList_InspectBtn()
    tradeRun.PickupList_HadPickupList_CreateDamageDetail()
    tradeRun.PickupList_HadPickupList_CreateTemplature()
    tradeRun.PickupList_HadPickupList_InspectPage_Submit()












    # driver.start_activity("base.sale.onlty.com","base.sale.onlty.com.activity.SplashActivity")
    # sleep(4)
    # driver.start_activity("trade.sale.onlty.com","trade.sale.onlty.com.activity.SplashActivity")