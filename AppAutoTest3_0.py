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

    # 市场端-首页-交易大厅（按钮）-交易产品列表-点击代销规则说明“知道了”按钮--------------------
    def KnowBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_bottom_btn").click()
        except NoSuchElementException:
            self.KnowBtn_Trade()

    # 市场端-单据-采购订单-采购订单列表-提交按钮--------------------
    def OrderList_SubmitBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(
                self.URL_TRADE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.OrderList_SubmitBtn_Trade()

    # 市场端-单据-采购订单-采购订单详情-提交按钮--------------------
    def OrderList_Detail_SubmitBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(
                self.URL_TRADE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.OrderList_Detail_SubmitBtn_Trade()

    # 市场端-单据-采购订单-采购订单列表-验证按钮--------------------
    def OrderList_VerifyBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(
                self.URL_TRADE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.OrderList_VerifyBtn_Trade()

    # 市场端-单据-采购订单-采购订单详情-验证按钮--------------------
    def OrderList_Detail_VerifyBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(
                self.URL_TRADE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.OrderList_Detail_VerifyBtn_Trade()

    # 市场端-首页-单据列表----------------------------
    def Invoices_Trade(self):
        try:
            bottom_tv_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv").__len__()
            for i in range(bottom_tv_len):
                bottom_tv_text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].text
                if op.eq(bottom_tv_text, u"单据"):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].click()
                    break
                else:
                    continue
        except NoSuchElementException:
            self.Invoices_Trade()

    # 市场端-首页-单据列表-发货单据列表----------------------------
    def InvoicesList_ShipmentList_Trade(self):
        try:
            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/documents_list_image")[1].click()
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            self.InvoicesList_ShipmentList_Trade()

    # 市场端-首页-单据列表-发货单据列表-支付首款按钮----------------------------
    def InvoicesList_ShipmentList_DownPaymentBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/clearing_train_more_btn").click()
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            self.InvoicesList_ShipmentList_DownPaymentBtn_Trade()

    # 市场端-首页-单据列表-发货单据列表-发货单据详情-支付首款按钮----------------------------
    def InvoicesList_ShipmentList_ShipmentDetail_DownPaymentBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            self.InvoicesList_ShipmentList_ShipmentDetail_DownPaymentBtn_Trade()

    # 市场端-收银台-线下支付--------------------------------------------------------
    def CashierDesk_Outline_PaymentMode_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/pay_type_balance").click()
        except NoSuchElementException:
            self.CashierDesk_Outline_PaymentMode_Trade()

    # 市场端-收银台-确认支付按钮--------------------------------------------------------
    def CashierDesk_Outline_PaymentBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/amount_confirm_tv").click()
        except NoSuchElementException:
            self.CashierDesk_Outline_PaymentBtn_Trade()

    # 市场端-收银台-线下支付页面-支付方式--------------------------------------------------------
    def CashierDesk_Outline_PaymentBtn_PaymentMode_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/parameter_title_tv").click()
            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/role_list_roleName_tv")[1].click()
        except NoSuchElementException:
            self.CashierDesk_Outline_PaymentBtn_PaymentMode_Trade()


    # 市场端-收银台-线下支付页面-提交按钮--------------------------------------------------------
    def CashierDesk_Outline_PaymentBtn_SubmitBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.CashierDesk_Outline_PaymentBtn_SubmitBtn_Trade()

    # 市场端-首页-接车验货按钮--------------------------------------------------------
    def PickupExamineBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/home_product_transaction_ll").click()
        except NoSuchElementException:
            self.PickupExamineBtn_Trade()

    # 市场端-接车-待接车列表-接车按钮--------------------------------------------------------
    def PickupBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reception_await_car_invoice_btn").click()
        except NoSuchElementException:
            self.PickupBtn_Trade()

    # 市场端-接车-已接车列表-----------------------------------------------------------------
    def HadPickupList_Trade(self):
        try:
            text = u"已接车"
            el_len = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                title_name = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].text
                print title_name
                if op.eq(title_name, text):
                    self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.HadPickupList_Trade()

    # 市场端-接车-已接车列表-接车按钮--------------------------------------------------------
    def SignatureBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reception_alread_car_invoice_btn").click()
        except NoSuchElementException:
            self.SignatureBtn_Trade()

    # 市场端-接车-已接车列表-验货页面-司机签名--------------------------------------------------------
    def ExamineStatus_SignatureBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
            sleep((self.SECONDS_SHORT))
        except NoSuchElementException:
            self.ExamineStatus_SignatureBtn_Trade()

    # 市场端-首页-已接车列表页面-验货页面-新增货损明细
    def ExamineStatus_CreateDamageDetail_Trade(self):
        try:
            flag = True
            text = u"新增货损明细"
            while (flag):
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv").__len__()
                for i in range(el_len):
                    biz_name = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv")[i].text
                    if op.eq(biz_name, text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE +":id/parameter_title_tv")[i].click()
                        # print "damageDetail"
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/sell_couments_content_tv").click()
                        # print "parkageOrder"
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
                        # print "save"
                        flag = False
                        # sleep((self.SECONDS_SHORT))
                        break
                    else:
                        pass
                if flag:
                    self.DRIVER_TRADE.swipe(430, 1000, 430, 575, 1000)
        except NoSuchElementException:
            self.ExamineStatus_CreateDamageDetail_Trade()
        except IndexError:
            self.ExamineStatus_CreateDamageDetail_Trade()

    # 市场端-首页-已接车列表页面-验货页面-新增测温明细
    def ExamineStatus_CreateTemplature_Trade(self):
        try:
            flag = True
            text = u"新增测温明细"
            while (flag):
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv").__len__()
                for i in range(el_len):
                    biz_name = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv")[i].text
                    if op.eq(biz_name, text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_title_tv")[i].click()
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/parameter_content_edit").send_keys(u"3")
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
                        flag = False
                        # sleep((self.SECONDS_SHORT))
                        break
                    else:
                        pass
                if flag:
                    self.DRIVER_TRADE.swipe(430, 1000, 430, 575, 1000)
        except NoSuchElementException:
            self.ExamineStatus_CreateTemplature_Trade()
        except IndexError:
            self.ExamineStatus_CreateTemplature_Trade()

    # 市场端-首页-已接车列表页面-验货页面-司机签名面板
    def ExamineStatus_Signing_Trade(self):
        try:
            self.DRIVER_TRADE.swipe(1300, 430, 800, 230, 1000)
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/signature_confirm_btn").click()
        except NoSuchElementException:
            self.ExamineStatus_Signing_Trade()

    # 市场端-首页-已接车列表页面-主管核准按钮
    def ExamineStatus_DirectorConfirm_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reception_alread_car_invoice_btn").click()
        except NoSuchElementException:
            self.ExamineStatus_DirectorConfirm_Trade()

    # 市场端-首页-已接车列表页面-验货页面-主管核准按钮
    def ExamineStatusList_DirectorConfirm_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.ExamineStatusList_DirectorConfirm_Trade()

    # 市场端-我的列表--------------------------
    def Mine_Trade(self):
        try:
            my_text = u"我的"
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].text
                if op.eq(text, my_text):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.Mine_Trade()

    # 市场端-我的列表-查看各个我的列表--------------------------
    # name = u"我的机构"/"员工管理"/"我的超利"/"我的菜品"/"我的收藏"/"我的客户"/"我的供应商"/"我的收货地址"/
    def Mine_MyItemList_Trade(self, name):
        try:
            text = name
            flag = True
            while flag:
                text_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_key_tv").__len__()
                for i in range(text_len):
                    content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_key_tv")[i].text
                    if op.eq(content,text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_key_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
                if flag:
                    self.DRIVER_TRADE.swipe(430, 1400, 430, 900, 1000)
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_Trade(name)

    # 市场端-我的列表-新增机构按钮-------------------------
    def Mine_MyItemList_Departments_AddLabel_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_AddLabel_Trade()

    # 市场端-我的列表-编辑按钮-------------------------
    def Mine_MyItemList_EditBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_AddLabel_Trade()

    # 市场端-我的列表-机构管理列表-新增机构信息-------------------------
    def Mine_MyItemList_Departments_AddLabel_InputContents_Trade(self):
        try:
            flag = True
            text_value = [u'机构名称',u'联系人',u'手机',u'邮箱']
            content_value=[u'捣蛋星',u'哈士奇',u'13677777777',u'13677777777@qq.com']
            while flag:
                flag = False
                texts_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
                for i in range(texts_len):
                    content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                    if op.eq(text_value[0],content):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0],content_value[0]
                        continue
                    else:
                        pass
                if text_value == [] and content_value == []:
                    flag = False
                else:
                    pass

            self.Create_Addr_Trade()
            self.DetailEdit_Addr_Trade()
            self.SaveBtn_Trade()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_AddLabel_InputContents_Trade()

    # 市场端-我的列表-机构管理列表-修改机构信息-------------------------
    def Mine_MyItemList_Departments_EditLabel_InputContents_Trade(self):
        try:
            flag = True
            text_value = [u'机构名称', u'联系人', u'手机', u'邮箱']
            content_value = [u'捣蛋星改', u'哈士奇改', u'13677777888', u'13677777888@qq.com']
            while flag:
                flag = False
                texts_len = self.DRIVER_TRADE.find_elements_by_id(
                    self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
                for i in range(texts_len):
                    content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                    if op.eq(text_value[0], content):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0], content_value[0]
                        continue
                    else:
                        pass
                if text_value == [] and content_value == []:
                    flag = False
                else:
                    pass

            self.Create_Addr_Trade()
            self.DetailEdit_Addr_Trade()
            self.SaveBtn_Trade()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_AddLabel_InputContents_Trade()

    # 市场端-我的列表-机构管理列表-查看选择机构信息详情-------------------------
    def Mine_MyItemList_DepartmentDetail_Trade(self,dept_name):
        try:
            # dept_name = u"捣蛋星"
            flag = True
            while flag:
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/stall_name_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/stall_name_tv")[i].text
                    if op.eq(dept_name,text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/stall_name_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_DepartmentDetail_Trade(dept_name)

    # 市场端-我的列表-机构管理列表-机构详情-编辑按钮-------------------------
    def Mine_MyItemList_DepartmentDetail_EditBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_switch_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_DepartmentDetail_EditBtn_Trade()

    # 市场端-我的列表-机构管理列表-机构详情-删除按钮-------------------------
    def Mine_MyItemList_DepartmentDetail_DelBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_switch_image").click()
            self.ConfirmBtn_SmallWindow()
        except NoSuchElementException:
            self.Mine_MyItemList_DepartmentDetail_EditBtn_Trade()



    # 市场端-我的列表-机构管理列表-机构详情-设置当前/默认机构-------------------------
    def Mine_MyItemList_DepartmentDetail_Setting_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_switchStall_tv").click()
            self.ConfirmBtn_SmallWindow()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_default_tv").click()
            self.ConfirmBtn_SmallWindow()
        except NoSuchElementException:
            self.Mine_MyItemList_DepartmentDetail_Setting_Trade()

    # 市场端-设置当前/默认机构/删除弹框确认-----------------------
    def ConfirmBtn_SmallWindow(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/pupop_dialog_confirm").click()
        except NoSuchElementException:
            self.ConfirmBtn_SmallWindow()


    # 市场端-地址区域三级选择和录入--------------------------------------
    def Create_Addr_Trade(self):
        try:
            addr = [u"广西", u"贺州", u"钟山"]
            flag_addr_level = [True]*3
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_tv").click()
            for k in range(flag_addr_level.__len__()):
                # print k
                while (flag_addr_level[k]):
                    el_len_addr = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv").__len__()
                    for j in range(el_len_addr):
                        el_addr = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv")[j].text
                        if op.eq(el_addr, addr[k]):
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv")[j].click()
                            flag_addr_level[k] = False
                            break
                        else:
                            pass
                    if flag_addr_level[k]:
                        self.Swipe_Addr_Trade()
                    else:
                        pass
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/city_confirm_tv").click()
        except NoSuchElementException:
            self.Create_Addr_Trade()

    # 市场端-地址选择滑动动作--------------------------------------
    def Swipe_Addr_Trade(self):
        self.DRIVER_TRADE.swipe(130, 1776, 130, 1476, 1000)

    # 市场端-地址详情输入--------------------------------------
    def DetailEdit_Addr_Trade(self):
        try:
            addr_detail = u"春风路18号"
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_edit").clear()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_edit").send_keys(addr_detail)
        except NoSuchElementException:
            self.DetailEdit_Addr_Trade()

    # 市场端-保存按钮--------------------------------------
    def SaveBtn_Trade(self):
        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()

    # 市场端-返回主模块页面（物理返回键:返回键代码4）--------------------------------------
    def BackToMainFuncs_Trade(self):
        flag = True
        while flag:
            try:
                self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_tv")
                flag = False
                break
            except NoSuchElementException:
                self.DRIVER_TRADE.press_keycode(4)

    # 市场端-我的列表-新增按钮-------------------------
    def Mine_MyItemList_CreateBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_switch_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_CreateBtn_Trade()

    # 市场端-我的列表-员工列表-新增员工信息-------------------------
    def Mine_MyItemList_CreateStaffInfo_Trade(self,name,tel,email,position):
        try:
            text_value = [u'员工名称', u'手机号码', u'邮箱',u'角色']
            content_value = [name, tel, email, position]
            texts_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(texts_len):
                content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text_value[0], content):
                    if op.eq(content,u'角色'):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[
                            i].click()
                        self.Mine_MyItemList_StaffRole_Trade(position)
                        del text_value[0], content_value[0]
                    else:
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0], content_value[0]
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_CreateStaffInfo_Trade(name, tel, email, position)
        except IndexError:
            print "Mine_MyItemList_CreateStaffInfo_Trade:indexError"
            pass

    # 市场端-我的列表-员工列表-员工信息-角色选择-------------------------
    def Mine_MyItemList_StaffRole_Trade(self,position):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/role_list_roleName_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/role_list_roleName_tv")[i].text
                if op.eq(text,position):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/role_list_roleName_tv")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_StaffRole_Trade(position)

    # 市场端-我的列表-员工管理列表-选择查看员工信息页面-------------------------
    def Mine_MyItemList_SelectedEditStaffInfo_Trade(self, staff):
        try:
            flag = True
            while flag:
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv")[i].text
                    if op.eq(staff, text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_SelectedEditStaffInfo_Trade(staff)

    # 市场端-我的列表-员工列表-编辑员工信息-------------------------
    def Mine_MyItemList_EditStaffInfo_Trade(self, name, tel, email, position):
        try:
            text_value = [u'员工名称', u'手机号码', u'邮箱', u'角色']
            content_value = [name, tel, email, position]
            texts_len = self.DRIVER_TRADE.find_elements_by_id(
                self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            del_btn_len = self.DRIVER_TRADE.find_elements_by_id(
                self.URL_TRADE + ":id/mine_edit_left_image").__len__()
            for j in range(del_btn_len):
                self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_edit_left_image").click()
            for i in range(texts_len):
                content = \
                self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text_value[0], content):
                    if op.eq(content, u'角色'):
                        self.DRIVER_TRADE.find_elements_by_id(
                            self.URL_TRADE + ":id/mine_edit_personage_content_tv")[
                            i].click()
                        self.Mine_MyItemList_StaffRole_Trade(position)
                        del text_value[0], content_value[0]
                    else:
                        self.DRIVER_TRADE.find_elements_by_id(
                            self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(
                            self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0], content_value[0]
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_EditStaffInfo_Trade(name, tel, email, position)
        except IndexError:
            print "Mine_MyItemList_EditStaffInfo_Trade:indexError"
            pass

    # 市场端-我的列表-删除按钮--------------------------------------------------
    def Mine_MyItemList_DelBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_DelBtn_Trade()

    # 基地端-链接设备和APP设置-------------------------------------------------
    def Driver_Base(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': self.DEVICE_NAME,
            'platformVersion': self.PLATFORM_VERSION,
            'appPackage': self.APP_PACKAGE_BASE,
            'appActivity': self.APP_ACTIVITY_BASE,
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        self.DRIVER_BASE = webdriver.Remote(self.REMOTE_ADDR, desired_caps)

    # 基地端-完整登录-------------------------------------------
    def Login_Base(self):
        self.Driver_Base()
        self.Banner_Pass_Base()
        self.Evr_Selected_Base()
        self.Login_By_Pwd_Base()
        self.Authorization_Sys_Base()
        print self.DRIVER_BASE

    # 快速启动基地
    def LaunchFast_Base(self):
        # self.DRIVER_BASE.start_activity(self.APP_PACKAGE_BASE, self.APP_ACTIVITY_BASE)
        # sleep(self.SECONDS_SHORT)
        self.DRIVER_BASE.launch_app()

    # 基地端-BANNER首页“跳过”-------------------------------------------------
    def Banner_Pass_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/next_button").click()
        except NoSuchElementException:
            self.Banner_Pass_Base()

    # 基地端-选择登录环境---------------------------------------------------------
    def Evr_Selected_Base(self):
        try:
            # 在“手机登录/注册”坐标-点击3次进入切换环境，每次间隔100毫秒
            # 获取“手机登录/注册”坐标位置
            bounds = self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/veriflcation_login_title_tv").location
            # bounds2 = self.base_driver.find_element_by_class_name(self.base_url + ":id/veriflcation_login_title_tv").location.items(
            # print bounds2
            # bounds = self.base_driver.find_element_by_id(self.base_url+":id/veriflcation_login_title_tv").
            # print bounds
            for num in range(1,4):
                # 点击“手机登录/注册”的坐标位置
                self.DRIVER_BASE.tap([(bounds['x'],bounds['y']),(bounds['x'],bounds['y'])],100)
            #     self.base_driver.tap([(60,273),(368,338)],100)
            #     print num
            # 输入创建新环境名称
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE+":id/damain_name_tv").send_keys(self.EVR_NAME)
            # 清空地址输入框预录入的内容
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/damain_path_tv").clear()
            # 输入创建新环境地址
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE+":id/damain_path_tv").send_keys(self.HTTP_EVR3_BASE)
            # 点击-确认-按钮
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE+":id/damain_add_tv").click()

            # 选择测试环境地址AutoTest:获取相同ID列表list后，匹配所选环境地址
            # 获取list元素数量
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE+":id/market_list_number_2_02").__len__()
            # print "elements list length:",el_len

            # 遍历所有list元素并获取text文本内容用于比较新建的测试环境地址，匹配成功则点击字段切换环境
            for i in range(el_len):
                EVR_ADDR = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE+":id/market_list_number_2_02")[i].text
                # 字符串比较函数
                if op.eq(self.HTTP_EVR3_BASE,EVR_ADDR):
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/market_list_number_2_02")[i].click()
                    break
                else:
                    continue
            # 点击-切换-按钮
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/damain_cut_tv").click()
        except NoSuchElementException:
            self.Evr_Selected_Base()

    # 基地端-用户登录----------------------------------------------------------
    def Login_By_Pwd_Base(self):
        try:
            # 勾选“我已经阅读并同意《绿田云服务协议》
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/veriflcation_login_serve_image").click()
            # 在“请输入手机号”框输入手机号
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/veriflcation_login_mobile_edit").send_keys(self.ACCOUNT_NO_BASE)
            # 点击-下一步-按钮
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/veriflcation_login_btn").click()
            # 点击以输入密码方式登录
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/account_loginType_tv").click()
            # 输入密码登录
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/account_password_edit").send_keys(self.ACCOUNT_PWD_BASE)
            # 点击-登录-按钮
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/account_login_btn").click()
        except NoSuchElementException:
            self.Login_By_Pwd_Base()

    # 基地端-首次登录系统设备授权APP运用--------------------------------
    def Authorization_Sys_Base(self):
        try:
            sleep(self.SECONDS_SHORT)
            # 授权使用电话
            # 授权使用拍摄和录制视频
            # 授权允许访问照片和媒体内容
            # 授权使用录制音频
            num = 4
            for i in range(num):
                self.DRIVER_BASE.find_element_by_id(self.SYS_URL + ":id/permission_allow_button").click()
        except NoSuchElementException:
            self.Authorization_Sys_Base()

    # 基地端-在首页点击“产品交易”按钮,进入产品交易页面
    def Click_Product_Transaction_Btn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/home_product_transaction_ll").click()
        except NoSuchElementException:
            self.Click_Product_Transaction_Btn_Base()

    # 基地端-产品交易页面点击“+”进入“设置交易产品”页面
    def Click_Floating_Btn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/floating_cut_btn").click()
        except NoSuchElementException:
            self.Click_Floating_Btn_Base()

    # 基地端-创建交易产品申请（暂存状态）
    def Click_checkImage_Btn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_transaction_list_checkImage").click()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_transaction_confirm_btn").click()
        except NoSuchElementException:
            self.Click_checkImage_Btn_Base()

    # 基地端-设置交易产品输入页面-定价录入
    def Creating_OnePrice_Order_Base(self):
        title_text = [u"销售方式",
                      u"产品单价",
                      u"首款比例",
                      u"尾款账期",
                      u"发货地址",
                      u"发货时间",
                      u"产量",
                      u"件数",
                      u"品级",
                      u"品相",
                      u"设置包装方式"]
        products_origin = [u"浙江", u"嘉兴", u"海盐"]
        try:
            flag = True
            flag_title = True
            flag_apply_btn = False
            flag_text = [True]*12
            while(flag):
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv").__len__()
                for i in range(el_len):
                    el_text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].text
                    if op.eq(el_text,u"销售方式") and flag_text[0]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[1].click()
                        del title_text[0]
                        flag_text[0] = False
                        continue
                    if op.eq(el_text,u"产品单价") and flag_text[1]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'2')
                        del title_text[0]
                        flag_text[1] = False
                        continue
                    if op.eq(el_text,u"首款比例") and flag_text[2]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'30')
                        del title_text[0]
                        flag_text[2] = False
                        continue
                    if op.eq(el_text,u"尾款账期") and flag_text[3]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'7')
                        del title_text[0]
                        flag_text[3] = False
                        continue
                    if op.eq(el_text,u"发货地址") and flag_text[4]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        flag_origin_level = [True, True, True]
                        for k in range(3):
                            while (flag_origin_level[k]):
                                el_len_origin = self.DRIVER_BASE.find_elements_by_id(
                                    self.URL_BASE + ":id/item_city_name_tv").__len__()
                                for j in range(el_len_origin):
                                    origin = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/item_city_name_tv")[j].text
                                    if op.eq(origin, products_origin[k]):
                                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/item_city_name_tv")[j].click()
                                        flag_origin_level[k] = False
                                        break
                                    else:
                                        pass
                                self.DRIVER_BASE.swipe(130, 1776, 130, 1476, 1000)
                        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/city_confirm_tv").click()
                        del title_text[0]
                        flag_text[4] = False
                        continue
                    if op.eq(el_text,u"发货时间") and flag_text[5]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/btnSubmit").click()
                        del title_text[0]
                        flag_text[5] = False
                        continue
                    if op.eq(el_text,u"产量") and flag_text[6]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'2000')
                        del title_text[0]
                        flag_text[6] = False
                        continue
                    if op.eq(el_text,u"件数") and flag_text[7]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'100')
                        del title_text[0]
                        flag_text[7] = False
                        continue
                    if op.eq(el_text,u"品级") and flag_text[8]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
                        del title_text[0]
                        flag_text[8] = False
                        continue
                    if op.eq(el_text,u"品相") and flag_text[9]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
                        del title_text[0]
                        flag_text[9] = False
                        continue
                    if op.eq(el_text,u"设置包装方式") and flag_text[10]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                        el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_image").__len__()
                        for i in range(el_len):
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_image")[i].click()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_title_tv")[0].click()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_btn_right")[0].click()
                            continue
                        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
                        del title_text[0]
                        flag_text[10] = False
                        continue
                    if flag_title:
                        try:
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/input_content_edit").send_keys(
                                u"线椒A大20190225")
                            flag_title = False
                        except NoSuchElementException:
                            pass
                if title_text==[] and flag_apply_btn:
                    flag = False
                    print flag
                    # print flag_apply_btn
                    break
                else:
                    try:
                        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_tansaction_trading_confirm_btn").click()
                        flag_apply_btn = True
                        # break
                    except NoSuchElementException:
                        pass
                    self.DRIVER_BASE.swipe(130, 1776, 130, 1476, 600)
                    # print title_text
                    # print flag
        except NoSuchElementException:
            self.Creating_OnePrice_Order_Base()

    # 基地端-“我的交易”列表页面-提交按钮
    def MyTranscation_List_SubmitBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/invoice_details_list_confirm_tv").click()
        except NoSuchElementException:
            self.MyTranscation_List_SubmitBtn_Base()

    # 基地端-“我的交易”-“交易申请”详情页面-提交按钮
    def MyTranscation_Detail_SubmitBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyTranscation_Detail_SubmitBtn_Base()

    # 基地端-“我的交易”-列表页面-主管核准按钮
    def MyTranscation_List_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/invoice_details_list_confirm_tv").click()
        except NoSuchElementException:
            self.MyTranscation_List_ConfirmBtn_Base()

    # 基地端-“我的交易”-“交易申请”详情页面-主管核准按钮
    def MyTranscation_Detail_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyTranscation_Detail_ConfirmBtn_Base()

    # 基地端-“我的交易”-列表页面-上架按钮
    def MyTranscation_List_OnSaleBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/invoice_details_list_confirm_tv").click()
        except NoSuchElementException:
            self.MyTranscation_List_OnSaleBtn_Base()

    # 基地端-“我的交易”-“交易申请”详情页面-上架按钮
    def MyTranscation_Detail_OnSaleBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.MyTranscation_Detail_OnSaleBtn_Base()

    # 基地端-首页-单据
    def Invoices_Base(self):
        try:
            bottom_tv_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv").__len__()
            for i in range(bottom_tv_len):
                bottom_tv_text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv")[i].text
                if op.eq(bottom_tv_text,u"单据"):
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv")[i].click()
                    break
                else:
                    continue
        except NoSuchElementException:
            self.Invoices_Base()

    # 基地端-首页-单据列表-采购订单列表
    def Invoices_OrderList_Base(self):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/documents_list_image")[0].click()
        except NoSuchElementException:
            self.Invoices_OrderList_Base()

    # 基地端-首页-单据列表-采购订单列表-确认订单按钮(singleBtn)
    def Invoices_OrderList_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_ConfirmBtn_Base()

    # 基地端-首页-单据列表-采购订单列表-订单信息页面-确认订单按钮
    def Invoices_OrderDetail_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderDetail_ConfirmBtn_Base()

    # 基地端-首页-单据列表-采购订单列表-处理按钮
    def Invoices_OrderList_ToProcessBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_ToProcessBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-处理按钮
    def Invoices_OrderList_OrderMsg_ToProcessBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderMsg_ToProcessBtn_Base()

    # 基地端-首页-单据列表-采购订单列表-处理完成按钮
    def Invoices_OrderList_OrderList_DoneBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderList_DoneBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-处理完成按钮
    def Invoices_OrderList_OrderMsg_DoneBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(
                self.URL_BASE + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderMsg_DoneBtn_Base()

    # 基地端-首页-单据列表-采购订单列表-生成发货单按钮
    def Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(
                self.URL_BASE + ":id/documents_procurement_order_create_invoice_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-生成发货单按钮
    def Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(
                self.URL_BASE + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-生成发货单和提交按钮
    def Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base(self):
        try:
            sleep(self.SECONDS_SHORT)
            flag = True
            flag_text = [True]*10
            while(flag):
                self.DRIVER_BASE.swipe(430, 1700, 430, 1175, 500)
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv").__len__()
                for i in range(el_len):
                    el_text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].text
                    if op.eq(u"物流公司", el_text) and flag_text[0]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'顺捷物流')
                        flag_text[0] = False

                    if op.eq(u"拖头牌号", el_text) and flag_text[1]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'粤A12345')
                        flag_text[1] = False

                    if op.eq(u"挂车牌号", el_text) and flag_text[2]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'粤A54321')
                        flag_text[2] = False

                    if op.eq(u"司机姓名", el_text) and flag_text[3]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'高彤')
                        flag_text[3] = False

                    if op.eq(u"手机号码", el_text) and flag_text[4]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'13588888888')
                        flag_text[4] = False

                    if op.eq(u"车厢温度", el_text) and flag_text[5]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'5')
                        flag_text[5] = False

                    if op.eq(u"运输类型", el_text) and flag_text[6]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].click()
                        while (True):
                            try:
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
                                break
                            except NoSuchElementException:
                                continue
                            except IndexError:
                                print u"运输类型IndexError"
                                continue

                        flag_text[6] = False

                    if op.eq(u"支付方式", el_text) and flag_text[7]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].click()
                        while (True):
                            try:
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
                                break
                            except NoSuchElementException:
                                continue
                            except IndexError:
                                print u"支付方式IndexError"
                                continue
                        flag_text[7] = False

                    if op.eq(u"运费定价", el_text) and flag_text[8]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].click()
                        while (True):
                            try:
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
                                break
                            except NoSuchElementException:
                                continue
                            except IndexError:
                                print u"运费定价IndexError"
                                continue
                        flag_text[8] = False

                    if op.eq(u"运费金额", el_text) and flag_text[9]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(u'100')
                        flag_text[9] = False
                        flag = False

            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base()

    # 基地端-物理返回键（返回键代码4）---------------------------------------------------------
    def Back_PhysicsBtn_Base(self):
        self.DRIVER_BASE.press_keycode(4)
        print "press_keycode"

    # 基地端-首页-单据列表-发货单据列表
    def Invoices_ShipmentList_Base(self):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/documents_list_image")[1].click()
        except NoSuchElementException:
            self.Invoices_OrderList_Base()

    # 基地端-首页-单据列表-发货单据列表-确认按钮
    def Invoices_ShipmentList_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Invoices_ShipmentList_ConfirmBtn_Base()

    # 基地端-首页-单据列表-发货单据详情-确认按钮
    def Invoices_ShipmentDetail_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Invoices_ShipmentDetail_ConfirmBtn_Base()

    # 基地端-首页-单据列表-发货单据列表-司机签名按钮
    def Invoices_ShipmentList_SignatureBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Invoices_ShipmentList_SignatureBtn_Base()

    # 基地端-首页-单据列表-发货单据详情-司机签名按钮
    def Invoices_ShipmentDetail_SignatureBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            self.Invoices_ShipmentList_SignatureBtn_Base()

    # 基地端-首页-单据列表-发货单据详情-司机签名面板
    def Invoices_ShipmentDetail_Signing_Base(self):
        try:
            self.DRIVER_BASE.swipe(1300, 430, 800, 430, 1000)
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/signature_confirm_btn").click()
        except NoSuchElementException:
            self.Invoices_ShipmentList_SignatureBtn_Base()

    # 基地端-首页-单据列表-发货单据列表-发车按钮
    def Invoices_ShipmentList_DepartBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/shipments_contact_driver_btn").click()
        except NoSuchElementException:
            self.Invoices_ShipmentList_DepartBtn_Base()

    # 基地端-首页-单据列表-发货单据详情-发车按钮
    def Invoices_ShipmentDetail_DepartBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Invoices_ShipmentDetail_DepartBtn_Base()






# if __name__ == '__main__':
#
#     # 创建对象
#     BaseRun = AppAutoTest()
#     BmsRun = BmsAutoTest()
#     TradeRun = AppAutoTest()
#
#     # 1.基地端登录流程
#     BaseRun.Driver_Base()
#     BaseRun.Banner_Pass_Base()
#     BaseRun.Evr_Selected_Base()
#     BaseRun.Login_By_Pwd_Base()
#     BaseRun.Authorization_Sys_Base()
#
#     # # 2.1基地端发布定价产品流程
#     # BaseRun.Click_Product_Transaction_Btn_Base()
#     # BaseRun.Click_Floating_Btn_Base()
#     # BaseRun.Click_checkImage_Btn_Base()
#     # BaseRun.Creating_OnePrice_Order_Base()
#     # BaseRun.MyTranscation_List_SubmitBtn_Base()
#     # BaseRun.MyTranscation_Detail_SubmitBtn_Base()
#     # BaseRun.MyTranscation_List_ConfirmBtn_Base()
#     # BaseRun.MyTranscation_Detail_ConfirmBtn_Base()
#     # # 2.2运营后台审核通过
#     # BmsRun.confirmTradeApply_Bms()
#     # # 2.3基地端发布定价产品流程
#     # BaseRun.MyTranscation_List_OnSaleBtn_Base()
#     # BaseRun.MyTranscation_Detail_OnSaleBtn_Base()
#
#     # # 2.4市场端登录流程
#     # TradeRun.Driver_Trade()
#     # TradeRun.Banner_Pass_Trade()
#     # TradeRun.Evr_Selected_Trade()
#     # TradeRun.Login_By_Pwd_Trade()
#     # TradeRun.Authorization_Sys_Trade()
#
#     # # 2.5市场端申请定价流程
#     # TradeRun.TranscationHallBtn_Trade()
#     # TradeRun.TranscationProduce_List_Trade()
#     # TradeRun.TranscationProduce_List_ApplyBtn_Trade()
#     # TradeRun.KnowBtn_Trade()
#     # TradeRun.TranscationProduce_List_ApplyBtn_Trade()
#     # TradeRun.Produce_CreateOrderApply_Trade()
#     # TradeRun.OrderList_SubmitBtn_Trade()
#     # TradeRun.OrderList_Detail_SubmitBtn_Trade()
#     # TradeRun.OrderList_VerifyBtn_Trade()
#     # TradeRun.OrderList_Detail_VerifyBtn_Trade()
#
#     #
#
#     # 2.6基地端审核定价+生成发货单流程
#
#     BaseRun.Invoices_Base()
#     # BaseRun.Invoices_OrderList_Base()
#     # BaseRun.Invoices_OrderList_ConfirmBtn_Base()
#     # BaseRun.Invoices_OrderDetail_ConfirmBtn_Base()
#     # BaseRun.Invoices_OrderList_ToProcessBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderMsg_ToProcessBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderList_DoneBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderMsg_DoneBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base()
#     # BaseRun.Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base()
#     # BaseRun.Back_PhysicsBtn_Base()
#     # BaseRun.Back_PhysicsBtn_Base()
#     BaseRun.Invoices_ShipmentList_Base()
#     BaseRun.Invoices_ShipmentList_ConfirmBtn_Base()
#     BaseRun.Invoices_ShipmentDetail_ConfirmBtn_Base()
#
#     # 2.7市场端支付首款
#
#     TradeRun.Invoices_Trade()
#     TradeRun.InvoicesList_ShipmentList_Trade()
#     TradeRun.InvoicesList_ShipmentList_DownPaymentBtn_Trade()
#









