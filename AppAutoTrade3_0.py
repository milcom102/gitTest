#-*-coding:utf-8-*-


from appium import webdriver
from time import sleep
import operator as op
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from auto_test_log_demo import *

class AppAutoTrade:

    # 初始化自动化常量------------------------------
    def __init__(self):

        # app外网地址
        self.URL_TRADE = "trade.sale.onlty.com"


        # app执行环境
        # self.HTTP_EVR3_TRADE = u"https://api.asc.dev.ad2o.com/v3/trade/"  # 市场3.0开发环境
        # self.HTTP_EVR3_TRADE = u"https://api-demo.onlty.com/v3/trade/" # 市场3.0演示环境
        self.HTTP_EVR3_TRADE = u"https://api.asc.dev.ad2o.com/v3/" # 市场3.6 开发环境

        # app环境命名输入
        self.EVR_NAME = u"AutoTest"
        # self.EVR_NAME = u"https演示环境"

        # 登录的账户号码
        # self.ACCOUNT_NO_TRADE = "13533880000"
        # self.ACCOUNT_NO_TRADE = "15218870000"  # 市场3.0演示环境
        self.ACCOUNT_NO_TRADE = "13533880000"  # 市场3.6 开发环境

        # 登录的账号密码
        # self.ACCOUNT_PWD_TRADE = "13533880000"
        # self.ACCOUNT_PWD_TRADE = "15218870000"  # 市场3.0演示环境
        self.ACCOUNT_PWD_TRADE = "13533880000"  # 市场3.6 开发环境

        # app包名称
        self.APP_PACKAGE_TRADE = "trade.sale.onlty.com"


        # app活动包
        self.APP_ACTIVITY_TRADE = "trade.sale.onlty.com.activity.SplashActivity"


        # 停顿秒数设置
        self.SECONDS_LONG = 7
        self.SECONDS_SHORT = 3

        # 驱动
        self.DRIVER_TRADE = None


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


    # 市场端-链接设备和APP设置-------------------------------------------------
    def Driver_Trade(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': self.DEVICE_NAME,
        'platformVersion': self.PLATFORM_VERSION,
        'appPackage': self.APP_PACKAGE_TRADE,
        'appActivity': self.APP_ACTIVITY_TRADE,
        'unicodeKeyboard':True,
        'resetKeyboard':True
        }
        self.DRIVER_TRADE = webdriver.Remote(self.REMOTE_ADDR, desired_caps)

    # 市场端-完整登录-------------------------------------------------
    def Login_Trade(self):
        self.Driver_Trade()
        logger.info('[trade]Driver loading completed')
        self.Banner_Pass_Trade()
        logger.info('[trade]Banner completed')
        self.Evr_Selected_Trade()
        logger.info('[trade]Environment: %s completed' % self.HTTP_EVR3_TRADE)
        self.Login_By_Pwd_Trade()
        logger.info('[trade]Input user & password completed')
        self.Authorization_Sys_Trade()
        logger.info('[trade]System accredit completed')
        logger.info('[trade]Login completed')

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
            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_home_meun_title_tv")[1].click()
            logger.info("[Trade]click transcation button")
            sleep(self.SECONDS_SHORT)
        except NoSuchElementException:
            logger.warn("[Trade]click transcation button exception...")
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
                    logger.info("[Trade]selected transaction product list")
                    break
                else:
                    continue
        except NoSuchElementException:
            logger.warn("[Trade]selected transaction product list exception...")
            self.TranscationProduce_List_Trade()
        # sleep(self.seconds_short)

    # 市场端-首页-交易大厅（按钮）-交易产品列表-申请下单按钮--------------------
    def TranscationProduce_List_ApplyBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/home_deal_deal_product_apply_sell_tv").click()
            logger.info("[Trade]click transaction product ApplyBtn")
        except NoSuchElementException:
            logger.warn("[Trade]click transaction product ApplyBtn exception...")
            self.TranscationProduce_List_ApplyBtn_Trade()

    # 市场端-首页-交易大厅（按钮）-交易产品列表-申请下单列表录入+确认订单按钮--------------------
    def Produce_CreateOrderApply_Trade(self,units,quantities):
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
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_content_edit")[i].send_keys(units)
                            flag_text[0] = False
                            # print "0=%s" % flag_text[0]

                        if op.eq(u"下单斤数", el_text_quantities) and flag_text[1]:
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/parameter_content_edit")[i].send_keys(quantities)
                            flag_text[1] = False
                            # print "1=%s" % flag_text[1]
                try:
                    el_text_addr = self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/purchase_shop_contast_tv").text
                    if op.eq(u"请选择收货人信息",el_text_addr) and flag_text[2]:
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/purchase_shop_contast_tv").click()
                        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shipping_address_tv").click()
                        flag_text[2] = False
                        # print "2=%s" % flag_text[1]
                        flag = False
                        # print "flag=%s" % flag
                        break
                except NoSuchElementException:
                    pass
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/amount_save_tv").click()
            logger.info("[Trade]input information of  transaction product completed")
        except NoSuchElementException:
            logger.warn("[Trade]input information of  transaction product exception...")
            self.Produce_CreateOrderApply_Trade(units,quantities)

    # 市场端-首页-交易大厅（按钮）-交易产品列表-点击代销规则说明“知道了”按钮--------------------
    def KnowBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_bottom_btn").click()
            logger.info("[Trade]view deputesale rule completed")
        except NoSuchElementException:
            logger.warn("[Trade]view deputesale rule exception...")
            self.KnowBtn_Trade()

    # 市场端-单据-采购订单-采购订单列表-提交按钮--------------------
    def OrderList_SubmitBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(
                self.URL_TRADE + ":id/documents_procurement_order_create_invoice_btn").click()
            logger.info("[Trade]click OrderList SubmitBtn completed")
        except NoSuchElementException:
            logger.warn("[Trade]click OrderList SubmitBtn exception...")
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
    def Invoices_Trade(self,name):
        try:
            bottom_tv_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv").__len__()
            for i in range(bottom_tv_len):
                bottom_tv_text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].text
                if op.eq(bottom_tv_text, name):
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
    def BelowItem_Trade(self,item_name):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].text
                if op.eq(text, item_name):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.BelowItem_Trade(item_name)

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
    def Mine_MyItemList_Departments_AddLabel_InputContents_Trade(self,unit,name,tel,email,local1,local2,local3,addr):
        try:
            flag = True
            text_value = [u'机构名称',u'联系人',u'手机',u'邮箱']
            content_value = [unit,name,tel,email]
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

            self.ThereLevelSelect_Trade(local1,local2,local3)
            self.DetailEdit_Addr_Trade(addr)
            self.SaveBtn_Trade()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_AddLabel_InputContents_Trade(unit,name,tel,email,local1,local2,local3,addr)

    # 市场端-我的列表-机构管理列表-修改机构信息-------------------------
    def Mine_MyItemList_Departments_EditLabel_InputContents_Trade(self,unit,name,tel,email,province,city,district,addr):
        try:
            flag = True
            text_value = [u'机构名称', u'联系人', u'手机', u'邮箱']
            content_value = [unit,name,tel,email]

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

            self.ThereLevelSelect_Trade(province,city,district)
            self.DetailEdit_Addr_Trade(addr)
            self.SaveBtn_Trade()
        except NoSuchElementException:
            self.Mine_MyItemList_Departments_EditLabel_InputContents_Trade(unit,name,tel,email,province,city,district,addr)

    # 市场端-我的列表-机构管理列表-查看选择机构信息详情-------------------------
    def Mine_MyItemList_DepartmentDetail_Trade(self,dept_name):
        try:
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
            logger.info("click ConfirmBtn")
        except NoSuchElementException:
            logger.warn("click ConfirmBtn exception...")
            self.ConfirmBtn_SmallWindow()


    # 市场端-列表三级选择和录入--------------------------------------
    def ThereLevelSelect_Trade(self,arg1,arg2,arg3):
        try:
            arg = [arg1,arg2,arg3]
            flag_arg_level = [True]*3
            try:
                self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_tv").click()
            except NoSuchElementException:
                pass
            for k in range(flag_arg_level.__len__()):
                # print k
                while (flag_arg_level[k]):
                    el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv").__len__()
                    for j in range(el_len):
                        text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv")[j].text
                        if op.eq(text, arg[k]):
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_city_name_tv")[j].click()
                            flag_arg_level[k] = False
                            break
                        else:
                            pass
                    if flag_arg_level[k]:
                        self.Swipe_Addr_Trade()
                    else:
                        pass
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/city_confirm_tv").click()
        except NoSuchElementException:
            self.ThereLevelSelect_Trade(arg1,arg2,arg3)

    # 市场端-地址选择滑动动作--------------------------------------
    def Swipe_Addr_Trade(self):
        self.DRIVER_TRADE.swipe(130, 1776, 130, 1476, 1000)

    # 市场端-地址详情输入--------------------------------------
    def DetailEdit_Addr_Trade(self,addr):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_edit").clear()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/shop_foot_address_edit").send_keys(addr)
        except NoSuchElementException:
            self.DetailEdit_Addr_Trade(addr)

    # 市场端-保存按钮--------------------------------------
    def SaveBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            pass


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

    # 市场端-返回到设置列表页面（物理返回键:返回键代码4）--------------------------------------
    def BackToSetting_Trade(self):
        flag = True
        while flag:
            try:
                self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_tv")
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
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
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
                    break
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
                content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text_value[0], content):
                    if op.eq(content, u'角色'):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                        self.Mine_MyItemList_StaffRole_Trade(position)
                        del text_value[0], content_value[0]
                    else:
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
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

    # 市场端-我的列表-菜品列表-新增菜品信息-------------------------
    def Mine_MyItemList_CreateProduct_Trade(self,pname,pclass1,pclass2,pclass3,province,city,district,supplier):
        try:

            fields = [u"菜品名称", u"菜品品种", u"菜品产地", u"供应商"]
            flag_fields = [True]*4
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text,fields[0]) and flag_fields[i]:
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(pname)
                    flag_fields[i] = False
                    continue
                elif op.eq(text,fields[1]) and flag_fields[i]:
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.ThereLevelSelect_Trade(pclass1,pclass2,pclass3)
                    flag_fields[i] = False
                    continue
                elif op.eq(text,fields[2]) and flag_fields[i]:
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.ThereLevelSelect_Trade(province,city,district)
                    flag_fields[i] = False
                    continue
                elif op.eq(text,fields[3]) and flag_fields[i]:
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.Mine_MyItemList_MySupplier_Trade(supplier)
                    flag_fields[i] = False
                    continue
        except NoSuchElementException:
            self.Mine_MyItemList_CreateProduct_Trade(pname,pclass1,pclass2,pclass3,province,city,district,supplier)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Trade:indexError"
            pass

    # 市场端-我的列表-选择我的供应商--------------------------
    def Mine_MyItemList_MySupplier_Trade(self,supplier):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE+":id/suppliers_name_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE+":id/suppliers_name_tv")[i].text
                if op.eq(text,supplier):
                    self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/suppliers_name_tv").click()
        except NoSuchElementException:
            self.Mine_MyItemList_MySupplier_Trade(supplier)

    # 市场端-我的列表-菜品列表-选择查看菜品信息页面-------------------------
    def Mine_MyItemList_SelectedEditProductInfo_Trade(self, produceName):
        try:
            flag = True
            while flag:
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/sale_produce_produceName_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/sale_produce_produceName_tv")[i].text
                    # print text
                    if op.eq(produceName, text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/sale_produce_produceName_tv")[i].click()
                        # print text
                        # print produceName
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_SelectedEditProductInfo_Trade(produceName)

    # 市场端-我的列表-菜品列表-编辑菜品信息-------------------------
    def Mine_MyItemList_EditProduct_Trade(self, pname, pclass1, pclass2, pclass3, province, city, district, supplier):
        try:
            fields = [u"菜品名称", u"菜品品种", u"菜品产地", u"供应商"]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text, fields[0]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(pname)
                if op.eq(text, fields[1]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.ThereLevelSelect_Trade(pclass1, pclass2, pclass3)
                if op.eq(text, fields[2]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.ThereLevelSelect_Trade(province, city, district)
                if op.eq(text, fields[3]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                    self.Mine_MyItemList_MySupplier_Trade(supplier)
        except NoSuchElementException:
            self.Mine_MyItemList_EditProduct_Trade(pname, pclass1, pclass2, pclass3, province, city, district,supplier)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Trade:indexError"
            pass

    # 市场端-我的列表-我的客户列表-新增客户信息-------------------------
    def Mine_MyItemList_CreateCustomer_Trade(self,cname,consignee,tel,email,receipt_addr):
        try:

            fields = [u"客户名称", u"联系人", u"手机号码", u"邮箱" , u"收货地址"]
            flag_fields = [True]*5
            value_fields = [cname,consignee,tel,email,receipt_addr]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text,fields[i]) and flag_fields[i]:
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(value_fields[i])
                    flag_fields[i] = False

        except NoSuchElementException:
            self.Mine_MyItemList_CreateCustomer_Trade(cname,consignee,tel,email,receipt_addr)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Trade:indexError"
            pass

    # 市场端-我的列表-我的客户列表-选择查看客户信息-------------------------
    def Mine_SelectedCustomer_Trade(self, name):
        try:
            text = name
            flag = True
            while flag:
                text_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv").__len__()
                for i in range(text_len):
                    content = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv")[i].text
                    if op.eq(content,text):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/employee_name_tv")[i].click()
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

    # 市场端-我的列表-我的供应商列表-编辑供应商信息-------------------------
    def Mine_MyItemList_EditSupplier_Trade(self, name, linkman, tel, province, city, district, addr):
        try:
            fields = [u"供应商名称", u"联系人", u"联系电话"]
            fields_value = [name, linkman, tel]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text, fields[0]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(fields_value[0])
                    del fields[0], fields_value[0]
                    if fields == [] and fields_value == []:
                        break
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/address_foot_address_tv").click()
            self.ThereLevelSelect_Trade(province, city, district)
            self.Mine_MyItemList_AddrDetail_Trade(addr)
        except NoSuchElementException:
            self.Mine_MyItemList_EditSupplier_Trade(name, linkman, tel, province, city, district, addr)
        except IndexError:
            print "Mine_MyItemList_EditSupplier_Trade:indexError"
            pass

    # 市场端-我的列表-我的供应商列表-编辑供应商按钮-------------------------
    def Mine_MyItemList_AddrDetail_Trade(self,addr):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/edit_address_content_edit").clear()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/edit_address_content_edit").send_keys(addr)
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/edit_address_default_tv").click()
        except NoSuchElementException:
            self.Mine_MyItemList_AddrDetail_Trade(addr)



    # 市场端-我的列表-我的供应商列表-编辑供应商按钮-------------------------
    def Mine_MyItemList_EditSupplierBtn_Trade(self,name):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_name_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_name_tv")[i].text
                if op.eq(text,name):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_edit_tv")[i].click()
                    break
        except NoSuchElementException:
            self.Mine_MyItemList_EditSupplierBtn_Trade(name)

    # 市场端-我的列表-我的供应商列表-删除供应商按钮-------------------------
    def Mine_MyItemList_DelSupplierBtn_Trade(self,name):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_name_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_name_tv")[i].text
                # print 1
                if op.eq(text,name):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/suppliers_delete_tv")[i].click()
                    # print 2
        except NoSuchElementException:
            self.Mine_MyItemList_DelSupplierBtn_Trade(name)

    # 市场端-我的列表-增加供应商按钮-------------------------
    def Mine_MyItemList_AddBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_AddBtn_Trade()

    # 市场端-我的列表-我的收货地址列表-新增收货地址信息-------------------------
    def Mine_MyItemList_CreateReceiptAddr_Trade(self,consignee,tel,province,city,district,addr):
        try:

            fields = [u"收货人", u"手机号码"]
            fields_value = [consignee,tel]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            # print el_len
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                # print text
                if op.eq(text,fields[0]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(fields_value[0])
                    del fields[0],fields_value[0]
                    # print 1
                if fields == [] and fields_value == []:
                    # print 2
                    break
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/address_foot_address_tv").click()
            self.ThereLevelSelect_Trade(province,city,district)
            self.Mine_MyItemList_AddrDetail_Trade(addr)
        except NoSuchElementException:
            self.Mine_MyItemList_CreateReceiptAddr_Trade(consignee, tel, province, city, district, addr)
            # print 3
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Trade:indexError"
            pass

    # 市场端-我的列表-我的供应商列表-编辑供应商按钮-------------------------
    def Mine_MyItemList_EditAddrBtn_Trade(self,name):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_contacts_tv").__len__()
            print el_len
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_contacts_tv")[i].text
                print text
                if op.eq(text,name):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_edit_tv")[i].click()
                    print 1
                    break
        except NoSuchElementException:
            print 2
            self.Mine_MyItemList_EditAddrBtn_Trade(name)

    # 市场端-我的列表-我的收货地址列表-删除我的收货地址按钮-------------------------
    def Mine_MyItemList_DelAddrBtn_Trade(self,name):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_contacts_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_contacts_tv")[i].text
                # print 1
                if op.eq(text,name):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/shipping_address_delete_tv")[i].click()
                    # print 2
        except NoSuchElementException:
            self.Mine_MyItemList_DelAddrBtn_Trade(name)

    # 市场端-我的列表-个人资料列表-------------------------
    def Mine_MyItemList_MineInfoList_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_personage_ll").click()
        except NoSuchElementException:
            self.Mine_MyItemList_MineInfoList_Trade()

    # 市场端-我的列表-个人资料列表-编辑信息-------------------------
    def Mine_MyItemList_MineInfoList_EditInfo_Trade(self,nickname):
        try:
            fields_value = [u"头像",u"昵称",u"微信账号"]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_key_tv").__len__()
            for j in range(2):
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_key_tv")[i].text
                    print text
                    if op.eq(text,fields_value[0]):
                        if j == 0:
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_skip_image")[i].click()
                            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_photograph_photo_tv").click()
                            self.DRIVER_TRADE.find_elements_by_class_name("android.widget.ImageView")[2].click()
                            print u"头像更改完成"
                            sleep(self.SECONDS_SHORT)
                            continue
                    if op.eq(text,fields_value[1]):
                        if j == 0:
                            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_skip_image")[i].click()
                            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_edit_nickname_edit").clear()
                            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_edit_nickname_edit").send_keys(nickname)
                            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_edit_nickname_confirom_btn").click()
                            print u"昵称更改完成"
                            sleep(self.SECONDS_SHORT)
                            continue
                    if op.eq(text,fields_value[2]):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_item_skip_image")[i].click()
                        if j == 1:
                            self.ConfirmBtn_SmallWindow()
                        print u"绑定微信完成"
        except NoSuchElementException:
            self.Mine_MyItemList_MineInfoList_EditInfo_Trade(nickname)
        except IndexError:
            print "IndexError"
            pass

    # 市场端-我的列表-个人资料列表-消息通知按钮-------------------------
    def Mine_MyItemList_MineMessageBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_inform_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_MineMessageBtn_Trade()

    # 市场端-我的列表-个人资料列表-消息通知列表-------------------------
    def Mine_MyItemList_MineMessages_Trade(self, message1, message2, message3):
        try:
            params = [message1, message2, message3]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meassage_inform_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meassage_inform_title_tv")[i].text
                if op.eq(text, params[0]):
                    # print i
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meassage_inform_title_tv")[i].click()
                    del params[0]
                    sleep(self.SECONDS_SHORT)
                    self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_tv").click()
                if params == []:
                   break
        except NoSuchElementException:
            self.Mine_MyItemList_MineMessages_Trade(message1,message2,message3)

    # 市场端-我的列表-个人资料列表-设置按钮-------------------------
    def Mine_MyItemList_SettingBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_setting_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_SettingBtn_Trade()

    # 市场端-我的列表-个人资料列表-设置按钮-------------------------
    def Mine_MyItemList_SettingList_Trade(self):
        try:
            # 查看术语/条款
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/setting_clause_ll").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看使用指南
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_account_instructions_ll").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看关于我们
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_account_regard_we_ll").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看联系客服
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/mine_account_onlineService_ll").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看蓝牙配置
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/setting_out_bluetooth_ll").click()
            self.DRIVER_TRADE.find_element_by_id(self.SYS_URL + ":id/permission_allow_button").click()
            sleep(self.SECONDS_SHORT)
            # 退出系统
            self.BackToSetting_Trade()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/setting_out_login_ll").click()
        except NoSuchElementException:
            self.Mine_MyItemList_SettingList_Trade()

    # 市场端-主页-首页功能按钮-------------------------
    def MainPageBtn_Trade(self, item):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_home_meun_title_tv").__len__()
            print el_len
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_home_meun_title_tv")[i].text
                if op.eq(text, item):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/item_home_meun_title_tv")[i].click()
                    sleep(self.SECONDS_SHORT)
                    break
        except NoSuchElementException:
            self.MainPageBtn_Trade(item)

    # 市场端-库存明细-查看按品种和按发货单-------------------------
    def Storage_Trade(self,name1,name2):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView").__len__()
            params = [name1,name2]
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(text,params[0]):
                    self.DRIVER_TRADE.find_elements_by_class_name("android.widget.TextView")[i].click()
                    del params[0]
                    if params == []:
                        print i
                        break
        except NoSuchElementException:
            self.Storage_Trade(name1,name2)

    # 市场端-主页-主页功能按钮-------------------------
    def MainPageBelowBtn_Trade(self, item):
        try:
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].text
                if op.eq(text, item):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/bottom_tv")[i].click()
        except NoSuchElementException:
            self.MainPageBelowBtn_Trade(item)

    # 市场端-主页-功能+按钮-------------------------
    def MainPageFuncsBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_elements_by_class_name("android.support.v7.app.ActionBar$Tab")[2].click()
        except NoSuchElementException:
            self.MainPageFuncsBtn_Trade()

    # 市场端-横向滑动动作ppi--------------------------------------
    def Swipe_Horizontal_Trade(self):
        self.DRIVER_TRADE.swipe(1000, 1351, 300, 1651, 1000)

    # 市场端-功能页面-功能按钮--------------------------------------
    def FuncBtn_Trade(self,item):
        try:
            flag = True
            while(flag):
                el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meun_title_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meun_title_tv")[i].text
                    if op.eq(text, item):
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/meun_title_tv")[i].click()
                        flag = False
                        break
                if flag:
                    self.Swipe_Horizontal_Trade()
                else:
                    pass
        except NoSuchElementException:
            self.FuncBtn_Trade(item)

    # 市场端-功能页面-新增行情信息--------------------------------------
    def Create_Quotation_Trade(self,openingPrice,closingPrice,highestPrice,lowestPrice,averagePrice):
        try:
            # 选择市场
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_tv").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/sell_couments_content_tv").click()
            # 选择产地
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_produceArea_tv").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/sell_couments_content_tv").click()
            # 选择品种
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_productName_tv").click()
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/sell_couments_content_tv").click()
            # 输入开盘价
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_opening_tv").send_keys(openingPrice)
            # 输入收盘价
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_closing_tv").send_keys(closingPrice)
            # 输入最高价
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_highest_tv").send_keys(highestPrice)
            self.DRIVER_TRADE.swipe(120, 1376, 130, 876, 1000)
            # 输入最低价
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_lowest_tv").send_keys(lowestPrice)
            # 输入平均价
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_average_tv").send_keys(averagePrice)

            # 输入备注
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/added_market_remark_edit").send_keys(u"AutoTest")

        except NoSuchElementException:
            self.Create_Quotation_Trade(openingPrice,closingPrice,highestPrice,lowestPrice,averagePrice)

    # 市场端-我的认证-输入认证申请编辑信息页面-文字-------------------------
    def Mine_MyItemList_CreateApplyMemberStr_Trade(self, cert_type,organization_type,unit, credit_code, name, id_no, tel, addr, bank,user,card_no):
        try:
            fields = [u"认证类型 ",u"机构类型 ",u"主体法定名称 ", u"统一社会信用代码 ", u"主体法人姓名 ",u"法人身份证号码 ",u"联系电话 ",u"联系地址 ",u"开户行 ",u"开户名 ",u"银行账号 "]
            # flag_fields = [True] * 11
            flag = True
            fields_value = [cert_type, organization_type, unit, credit_code, name, id_no, tel, addr, bank,user,card_no]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv").__len__()
            print el_len
            while flag:
                for i in range(el_len):
                    text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_title_tv")[i].text
                    if op.eq(text, u"认证类型 "):# and flag_fields[i]:
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/hot_tags_content_tv")[cert_type].click()
                        # flag_fields[i] = False
                        del fields[0],fields_value[0]
                        continue

                    if op.eq(text, u"机构类型 "):# and flag_fields[i]:
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].click()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/hot_tags_content_tv")[organization_type].click()
                        # flag_fields[i] = False
                        del fields[0],fields_value[0]
                        continue

                    if op.eq(text, fields[0]):# and flag_fields[i]:
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/mine_edit_personage_content_tv")[i].send_keys(fields_value[0])
                        # flag_fields[i] = False
                        del fields[0],fields_value[0]

                    if fields.__len__() > 0 and i+1 == el_len:
                        self.PageSwipe_Trade()

                    if fields == []:
                        flag = False
                        break

                    print fields
                    print text

        except NoSuchElementException:
            self.Mine_MyItemList_CreateApplyMemberStr_Trade(cert_type,organization_type,unit, credit_code, name, id_no, tel, addr, bank,user,card_no)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Trade:indexError"
            pass

    # 市场端-我的认证-输入认证申请编辑信息页面-图片-------------------------
    def Mine_MyItemList_CreateApplyMemberPicture_Trade(self):
        text_id = [u":id/idCardFrontPhoto_image",u":id/idCardBackPhoto_image",u":id/businessLicensePhoto_image",u":id/logo_image",u":id/issuesIv"]
        flag = True
        while flag:
            for i in range(text_id.__len__()):
                try:
                    if (text_id[0]==u":id/issuesIv"):
                        self.SendPictures_Trade(text_id[0])
                        del text_id[0]
                    else:
                        self.UploadPictures_Trade(text_id[0])
                        del text_id[0]
                    if text_id == []:
                        print "text_id"
                        flag = False
                        break
                    else:
                        print text_id
                        pass
                except NoSuchElementException:
                    self.PageSwipe_Trade()


    # 市场端-页面滑动-------------------------------------------
    def PageSwipe_Trade(self):
        try:
            self.DRIVER_TRADE.swipe(430, 1600, 430, 1175, 500)
        except WebDriverException:
            self.PageSwipe_Trade()

    # 市场端-上传图片-------------------------------------------
    def UploadPictures_Trade(self,param):

        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + param).click()
        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_photograph_photo_tv").click()
        self.DRIVER_TRADE.find_elements_by_class_name("android.widget.ImageView")[4].click()


    # 市场端-发送图片-------------------------------------------
    def SendPictures_Trade(self,param):

        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + param).click()
        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/picker_photofolder_info").click()
        self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/picker_photo_grid_item_select")[4].click()
        self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/picker_bottombar_select").click()


    # 市场端-进入详情页面按钮-------------------------------------------
    def VerifyDetailBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_list_bottom_left_btn").click()
        except NoSuchElementException:
            self.VerifyDetailBtn_Trade()

    # 市场端-编辑按钮-------------------------------------------
    def EditBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.EditBtn_Trade()

    # 市场端-提交按钮 - ------------------------------------------
    def SubmitBtn_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/item_list_bottom_right_btn").click()
        except NoSuchElementException:
            self.SubmitBtn_Trade()

    # 市场端-单据列表-风险单据列表 ------------------------------------------
    def RiskInvoicesList_Trade(self):
        try:
            self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/documents_list_image")[4].click()
        except NoSuchElementException:
            self.RiskInvoicesList_Trade()

    # 市场端-单据列表-新增风险单据菜品明细-点击条 ------------------------------------------
    def AddProductDetailLink_Trade(self):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reject_harvest_detail_addProduce_ll").click()
        except NoSuchElementException:
            self.AddProductDetailLink_Trade()

    # 市场端-单据列表-新增风险单据菜品明细-编辑菜品明细 ------------------------------------------
    def EditProductDetail_Trade(self,mu,nopicking_rate):
        try:
            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reject_harvest_detail_sheetNo_ll").click()

            self.DRIVER_TRADE.find_element_by_id(self.URL_TRADE + ":id/reject_harvest_edit_produce_productName_ll").click()

            params = [mu,nopicking_rate]
            el_len = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/reject_harvest_edit_produce_name_tv").click()
            text = self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/reject_harvest_edit_produce_name_tv").click()
            for i in range(el_len):
                if op.eq(text,params[0]):
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/reject_harvest_edit_produce_value_edit")[i].clear()
                    self.DRIVER_TRADE.find_elements_by_id(self.URL_TRADE + ":id/reject_harvest_edit_produce_value_edit")[i].send_keys(mu)
                    del params[0]

        except NoSuchElementException:
            self.EditProductDetail_Trade(mu,nopicking_rate)





