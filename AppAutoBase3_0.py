#-*-coding:utf-8-*-

from BmsAutoTest_1_7 import *
from appium import webdriver
from time import sleep
import operator as op
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from auto_test_log_demo import *

class AppAutoBase:



    # 初始化自动化常量------------------------------
    def __init__(self):

        # app外网地址

        self.URL_BASE = "base.sale.onlty.com"

        # app执行环境
        # self.HTTP_EVR3_BASE = u"https://api.asc.dev.ad2o.com/v3/base/"  # 基地3.0开发环境
        # self.HTTP_EVR3_BASE = u"https://api-dev.onlty.com/v3/base/"  # 基地3.1开发环境
        # self.HTTP_EVR3_BASE = u"https://api-demo.onlty.com/v3/base/"  # 基地3.0演示环境
        # self.HTTP_EVR3_BASE = u"https://api-demo.onlty.com/v3/"  # 基地3.6演示环境
        self.HTTP_EVR3_BASE = u"https://api.asc.dev.ad2o.com/v3/"  # 基地3.6测试环境

        # app环境命名输入
        self.EVR_NAME = u"AutoTest1"
        # self.EVR_NAME = u"https演示环境"

        # 登录的账户号码
        # self.ACCOUNT_NO_BASE = "15218870000"   # 测试3.0演示环境
        self.ACCOUNT_NO_BASE = "13533880000" # 基地3.0演示环境

        # 登录的账号密码
        # self.ACCOUNT_PWD_BASE = "15218870000"   # 测试3.0演示环境
        self.ACCOUNT_PWD_BASE = "13533880000" # 基地3.0演示环境

        # app包名称
        self.APP_PACKAGE_BASE = "base.sale.onlty.com"

        # app活动包
        self.APP_ACTIVITY_BASE = "base.sale.onlty.com.activity.SplashActivity"

        # 停顿秒数设置
        self.SECONDS_LONG = 7
        self.SECONDS_SHORT = 3

        # 驱动

        self.DRIVER_BASE = None

        # 移动设备端型号
        # coolpad c106
        self.DEVICE_NAME = 'e874797'
        self.PLATFORM_VERSION = '6.0.1'

        # Appium工具耦合地址
        self.REMOTE_ADDR = 'http://127.0.0.1:4723/wd/hub'
        # 远程地址连接
        # self.REMOTE_ADDR = 'http://192.168.1.7:4723/wd/hub'


        # android系统查看app是否已安装
        self.SYS_URL = "com.android.packageinstaller"

        # 驱动
        self.DRIVER_BASE = None

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
        logger.info('Driver loading completed')
        self.Banner_Pass_Base()
        logger.info('Banner completed')
        self.Evr_Selected_Base()
        logger.info('Environment: %s completed' % self.HTTP_EVR3_BASE)
        self.Login_By_Pwd_Base()
        logger.info('Input user & password completed')
        self.Authorization_Sys_Base()
        logger.info('System accredit completed')
        logger.info('Login completed')


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
            logger.info('Choose productTransactionBtn')
        except NoSuchElementException:
            logger.info('ProductTransactionBtn exception...')
            self.Click_Product_Transaction_Btn_Base()


    # 基地端-产品交易页面点击“+”进入“设置交易产品”页面
    def Click_Floating_Btn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/floating_cut_btn").click()
            logger.info('Increase a new transaction information')
        except NoSuchElementException:
            logger.info('FloatingBtn exception...')
            self.Click_Floating_Btn_Base()


    # 基地端-创建交易产品申请（暂存状态）
    def Click_checkImage_Btn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_transaction_list_checkImage").click()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_transaction_confirm_btn").click()
            logger.info('Create a apply of transaction')
        except NoSuchElementException:
            logger.info('Create a apply of transaction exception...')
            self.Click_checkImage_Btn_Base()

    # 基地端-设置交易产品输入页面-定价录入
    def Creating_OnePrice_Order_Base(self,args):
        # title_text = [u"销售方式",
        #               u"产品单价",
        #               u"首款比例",
        #               u"尾款账期",
        #               u"发货地址",
        #               u"发货时间",
        #               u"产量",
        #               u"件数",
        #               u"毛重",
        #               u"品级",
        #               u"品相",
        #               u"产品标题定义",
        #               u"设置包装方式"]
        # tup参数排列内容:
        # sell_type(0),unit_price(1),rates(2),expires(3),quantities(4),packages(5),gross_weight(6),grade(7),size(8),product_name(9)
        tup = args
        flag_value = [True]*13
        flag = True
        try:
            while flag:
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv").__len__()
                try:
                    for i in range(el_len):
                        el_text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].text
                        if op.eq(el_text, u"销售方式") and flag_value[0]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            self.SelectedSellType_Base(tup[0])
                            flag_value[0] = False
                            continue
                        if op.eq(el_text, u"产品单价") and flag_value[1]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[1])
                            flag_value[1] = False
                            continue
                        if op.eq(el_text, u"首款比例") and flag_value[2]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[2])
                            flag_value[2] = False
                            continue
                        if op.eq(el_text, u"尾款账期") and flag_value[3]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[3])
                            flag_value[3] = False
                            continue
                        if op.eq(el_text, u"发货地址") and flag_value[4]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            self.SelectedAddr_Base()
                            flag_value[4] = False
                            continue
                        if op.eq(el_text, u"发货时间") and flag_value[5]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/btnSubmit").click()
                            flag_value[5] = False
                            continue
                        if op.eq(el_text, u"产量") and flag_value[6]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[4])
                            flag_value[6] = False
                            continue
                        if op.eq(el_text, u"件数") and flag_value[7]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[5])
                            flag_value[7] = False
                            continue
                        if op.eq(el_text, u"毛重") and flag_value[8]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].clear()
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(tup[6])
                            flag_value[8] = False
                            continue
                        if op.eq(el_text, u"品级") and flag_value[9]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            self.Product_Grade_Base(tup[7])
                            flag_value[9] = False
                            continue
                        if op.eq(el_text, u"品相") and flag_value[10]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            self.Product_Size_Base(tup[8])
                            flag_value[10] = False
                            continue
                        if flag_value[11]:
                            try:
                                self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/input_content_edit").send_keys(tup[9])
                                flag_value[11] = False
                            except NoSuchElementException:
                                pass
                        if op.eq(el_text, u"设置包装方式") and flag_value[12]:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_title_tv")[i].click()
                            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_title_tv").__len__()
                            for j in range(el_len):
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_title_tv")[j].click()
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/filter_title_tv")[0].click()
                                self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_btn_right")[0].click()
                                continue
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
                            flag_value[12] = False
                            break
                except IndexError:
                    self.PageSwipe_Base()
                try:
                    self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_tansaction_trading_confirm_btn").click()
                    flag = False
                except NoSuchElementException:
                    self.PageSwipe_Base()
            logger.info('Transaction information input over')
        except NoSuchElementException:
            logger.info('Transaction information input exception...')
            self.Creating_OnePrice_Order_Base(args)
            print "NoSuchElementException"

    # 基地端-“我的交易”列表页面-提交按钮
    def MyTranscation_List_SubmitBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/invoice_details_list_confirm_tv").click()
            logger.info('Submit Transaction information to director')
        except NoSuchElementException:
            logger.info('Submit Transaction information exception...')
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
            logger.info("[base]click Invoices")
        except NoSuchElementException:
            logger.warn("[base]click Invoices exception...")
            self.Invoices_Base()

    # 基地端-首页-单据列表-采购订单列表
    def Invoices_OrderList_Base(self):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/documents_list_image")[0].click()
            logger.info("[base]click OrderList")
        except NoSuchElementException:
            logger.info("[base]click OrderList exception...")
            self.Invoices_OrderList_Base()

    # 基地端-首页-单据列表-采购订单列表-确认订单按钮(singleBtn)
    def Invoices_OrderList_ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/documents_procurement_order_create_invoice_btn").click()
            logger.info("[base]click OrderList ConfirmBtn")
        except NoSuchElementException:
            logger.warn("[base]click OrderList ConfirmBtn exception...")
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
            logger.info("[base]click CreateShippingPackageBtn")
        except NoSuchElementException:
            logger.warn("[base]click CreateShippingPackageBtn exception...")
            self.Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-生成发货单按钮
    def Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(
                self.URL_BASE + ":id/order_meassage_commit_btn").click()
        except NoSuchElementException:
            self.Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base()

    # 基地端-首页-单据列表-采购订单信息-生成发货单和提交按钮
    def Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base(self,num,examine_cargo):
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
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][1])
                        flag_text[0] = False

                    if op.eq(u"拖头牌号", el_text) and flag_text[1]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][2])
                        flag_text[1] = False

                    if op.eq(u"挂车牌号", el_text) and flag_text[2]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][3])
                        flag_text[2] = False

                    if op.eq(u"司机姓名", el_text) and flag_text[3]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][4])
                        flag_text[3] = False

                    if op.eq(u"手机号码", el_text) and flag_text[4]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][5])
                        flag_text[4] = False

                    if op.eq(u"车厢温度", el_text) and flag_text[5]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][6])
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
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/parameter_content_edit")[i].send_keys(examine_cargo[num][7])
                        flag_text[9] = False
                        flag = False
            logger.info("CreateShippingPackage completed")
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            logger.warn("CreateShippingPackage exception...")
            self.Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base(num,examine_cargo)

    # 基地端-物理返回键（返回键代码4）---------------------------------------------------------
    def Back_PhysicsBtn_Base(self):
        self.DRIVER_BASE.press_keycode(4)
        print "press_keycode"

    # 基地端-首页-单据列表-发货单据列表,采购订单-0，发货单据-1，结算单据-2，付款凭证-3，风险单据-4
    def InvoicesList_Base(self,invoice_title):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/documents_list_image")[invoice_title].click()
        except NoSuchElementException:
            self.InvoicesList_Base(invoice_title)

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

    # 基地端-主页-主页功能按钮-------------------------
    def MainPageBelowBtn_Base(self, item):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv")[i].text
                if op.eq(text, item):
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/bottom_tv")[i].click()
        except NoSuchElementException:
            self.MainPageBelowBtn_Base(item)

    # 基地端-我的列表-个人资料列表-------------------------
    def Mine_MyItemList_MineInfoList_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/account_user_name_tv").click()
        except NoSuchElementException:
            self.Mine_MyItemList_MineInfoList_Base()

    # 市场端-我的列表-个人资料列表-编辑信息-------------------------
    def Mine_MyItemList_MineInfoList_EditInfo_Base(self,nickname):
        try:
            fields_value = [u"头像",u"昵称",u"微信账号"]
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_key_tv").__len__()
            print el_len
            for j in range(2):
                for i in range(el_len):
                    text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_key_tv")[i].text
                    print text
                    if op.eq(text,fields_value[0]):
                        if j == 0:
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_skip_image")[i].click()
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_photograph_photo_tv").click()
                            self.DRIVER_BASE.find_elements_by_class_name("android.widget.ImageView")[2].click()
                            print u"头像更改完成"
                            sleep(self.SECONDS_SHORT)
                            continue
                    if op.eq(text,fields_value[1]):
                        if j == 0:
                            print u"昵称更改中"
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_skip_image")[i].click()
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_edit_nickname_edit").clear()
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_edit_nickname_edit").send_keys(nickname)
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_edit_nickname_confirom_btn").click()
                            print u"昵称更改完成"
                            sleep(self.SECONDS_SHORT)
                            continue
                    if op.eq(text,fields_value[2]):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_skip_image")[i].click()
                        if j == 1:
                            self.ConfirmBtn_SmallWindow()
                        print u"绑定微信完成"
        except NoSuchElementException:
            self.Mine_MyItemList_MineInfoList_EditInfo_Base(nickname)
        except IndexError:
            self.Mine_MyItemList_MineInfoList_EditInfo_Base(nickname)
        #     pass

    # 基地端-弹框确认-----------------------
    def ConfirmBtn_SmallWindow(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/pupop_dialog_confirm").click()
            logger.info('ConfirmBtn Transaction information')
        except NoSuchElementException:
            logger.info('ConfirmBtn Transaction information exception...')
            self.ConfirmBtn_SmallWindow()

    # 基地端-返回主模块页面（物理返回键:返回键代码4）--------------------------------------
    def BackToMainFuncs_Base(self):
        flag = True
        while flag:
            try:
                self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_tv")
                flag = False
                break
            except NoSuchElementException:
                self.DRIVER_BASE.press_keycode(4)

    # 基地端-我的列表-查看各个我的列表--------------------------
    # name = u"我的基地"/"员工管理"/"我的菜品"/"我的产品"/"我的认证"/"消息通知"/"设置"
    def Mine_MyItemList_Base(self, item):
        try:
            text = item
            flag = True
            while flag:
                text_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_key_tv").__len__()
                for i in range(text_len):
                    content = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_key_tv")[i].text
                    if op.eq(content,text):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_item_key_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
                if flag:
                    self.DRIVER_BASE.swipe(430, 1400, 430, 900, 1000)
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_Base(item)

    # 基地端-我的列表-我的基地-新增基地按钮-------------------------
    def Mine_MyItemList_MyBases_AddLabel_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_MyBases_AddLabel_Base()

    # 基地端-新增单据按钮-------------------------
    def AddBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.AddBtn_Base()

    # 基地端-我的列表-我的基地-新增基地信息-------------------------
    def Mine_MyItemList_Bases_AddLabel_InputContents_Base(self,unit,area,products,linkman,tel,local1,local2,local3,addr):
        try:
            flag = True
            text_value = [u'基地名称',u'基地面积',u'主营',u'联系人',u"联系电话"]
            content_value = [unit, area, products, linkman, tel]
            while flag:
                flag = False
                texts_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv").__len__()
                for i in range(texts_len):
                    content = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv")[i].text
                    if op.eq(text_value[0],content):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0],content_value[0]
                        continue
                    else:
                        pass
                if text_value == [] and content_value == []:
                    flag = False
                else:
                    pass
            self.ThereLevelSelect_Base(local1,local2,local3)
            self.DetailEdit_Addr_Base(addr)
            self.SaveBtn_Base()
        except NoSuchElementException:
            self.Mine_MyItemList_Bases_AddLabel_InputContents_Base(unit,area,products,linkman,tel,local1,local2,local3,addr)

    # 基地端-列表三级选择和录入--------------------------------------
    def ThereLevelSelect_Base(self,arg1,arg2,arg3):
        try:
            arg = [arg1,arg2,arg3]
            flag_arg_level = [True]*3
            try:
                self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/address_tv").click()
            except NoSuchElementException:
                pass
            for k in range(flag_arg_level.__len__()):
                # print k
                while (flag_arg_level[k]):
                    el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/item_city_name_tv").__len__()
                    for j in range(el_len):
                        text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/item_city_name_tv")[j].text
                        if op.eq(text, arg[k]):
                            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/item_city_name_tv")[j].click()
                            flag_arg_level[k] = False
                            break
                        else:
                            pass
                    if flag_arg_level[k]:
                        self.Swipe_Addr_Base()
                    else:
                        pass
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/city_confirm_tv").click()
        except NoSuchElementException:
            self.ThereLevelSelect_Base(arg1,arg2,arg3)

    # 基地端-地址选择滑动动作--------------------------------------
    def Swipe_Addr_Base(self):
        try:
            self.DRIVER_BASE.swipe(130, 1776, 130, 1476, 1000)
        except WebDriverException:
            self.Swipe_Addr_Base()

    # 基地端-地址详情输入--------------------------------------
    def DetailEdit_Addr_Base(self,addr):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/address_edit").clear()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/address_edit").send_keys(addr)
        except NoSuchElementException:
            self.DetailEdit_Addr_Base(addr)

    # 基地端-保存按钮--------------------------------------
    def SaveBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_right_btn").click()
        except NoSuchElementException:
            self.SaveBtn_Base()

    # 基地端-我的列表-基地列表-查看选择基地信息详情-------------------------
    def Mine_MyItemList_BaseDetail_Base(self,base_name):
        try:
            flag = True
            while flag:
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv")[i].text
                    if op.eq(base_name,text):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_BaseDetail_Base(base_name)

    # 基地端-我的列表-基地列表-查看选择基地信息详情-编辑按钮-------------------------
    def Mine_MyItemList_BaseDetail_EditBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_BaseDetail_EditBtn_Base()

    # 基地端-我的列表-基地列表-查看选择基地信息详情-设置当前/默认按钮-------------------------
    def Mine_MyItemList_BaseDetail_Setting_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/switchBase_tv").click()
            self.ConfirmBtn_SmallWindow()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/default_tv").click()
            self.ConfirmBtn_SmallWindow()
        except NoSuchElementException:
            self.Mine_MyItemList_BaseDetail_Setting_Base()

    # 基地端-我的列表-员工列表-新增员工信息-------------------------
    def Mine_MyItemList_CreateStaffInfo_Base(self,name,tel,email,unit,position):
        try:
            text_value = [u'员工姓名', u'手机号码', u'邮箱', u'基地', u'角色']
            content_value = [name, tel, email, unit, position]
            texts_len = self.DRIVER_BASE.find_elements_by_id(
                self.URL_BASE + ":id/mine_edit_personage_title_tv").__len__()
            print texts_len
            for i in range(texts_len):
                content = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv")[
                    i].text
                print content
                print i
                if op.eq(text_value[0], content):
                    if op.eq(content, u'角色'):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                            i].click()
                        self.Mine_MyItemList_StaffRole_Base(position)
                        del text_value[0], content_value[0]
                    elif op.eq(content, u'基地'):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                            i].click()
                        self.Mine_MyItemList_BelongBase_Base(unit)
                        del text_value[0], content_value[0]

                    else:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                            i].clear()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                            i].send_keys(content_value[0])
                        del text_value[0], content_value[0]
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_CreateStaffInfo_Base(name, tel, email,unit, position)
        except IndexError:
            print "Mine_MyItemList_CreateStaffInfo_Trade:indexError"
            pass

    # 基地端-我的列表-员工列表-员工信息-角色选择-------------------------
    def Mine_MyItemList_StaffRole_Base(self,position):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[i].text
                if op.eq(text,position):
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_StaffRole_Base(position)
        except IndexError:
            pass

    # 基地端-我的列表-员工列表-员工信息-基地选择-------------------------
    def Mine_MyItemList_BelongBase_Base(self,unit):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv")[i].text
                if op.eq(text,unit):
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/base_name_tv")[i].click()
                    break
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_BelongBase_Base(unit)
        except IndexError:
            pass

    # 基地端-我的列表-员工列表-员工信息详情-------------------------
    def Mine_MyItemList_EmployeeDetail_Base(self,name):
        try:
            flag = True
            while flag:
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/employee_name_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/employee_name_tv")[i].text
                    if op.eq(name,text):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/employee_name_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_BaseDetail_Base(name)

    # 基地端-我的产品-查看我的预售和我的交易-------------------------
    def MyProducts_Base(self,name1,name2):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView").__len__()
            params = [name1,name2]
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(text,params[0]):
                    self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].click()
                    del params[0]
                    if params == []:
                        print i
                        break
        except NoSuchElementException:
            self.MyProducts_Base(name1,name2)

    # 基地端-我的列表-员工列表-修改员工信息-------------------------
    def Mine_MyItemList_EditStaffInfo_Base(self,name,tel,email,unit,position):
        try:
            text_value = [u'员工姓名', u'手机号码', u'邮箱',u'基地', u'角色']
            content_value = [name, tel, email, unit,position]
            texts_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv").__len__()
            print texts_len
            del_btn_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_left_image").__len__()
            print del_btn_len
            for j in range(del_btn_len):
                try:
                    self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/mine_edit_left_image").click()
                except IndexError:
                    pass
            for i in range(texts_len):
                content = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv")[i].text
                print content
                print i
                if op.eq(text_value[0], content):
                    if op.eq(content, u'角色'):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].click()
                        self.Mine_MyItemList_StaffRole_Base(position)
                        del text_value[0], content_value[0]
                    elif op.eq(content, u'基地'):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].click()
                        self.Mine_MyItemList_BelongBase_Base(unit)
                        del text_value[0], content_value[0]

                    else:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].clear()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].send_keys(content_value[0])
                        del text_value[0], content_value[0]
                else:
                    pass
        except NoSuchElementException:
            self.Mine_MyItemList_CreateStaffInfo_Base(name, tel, email,unit, position)
        except IndexError:
            pass

    # 基地端-我的列表-我的菜品-新增菜品按钮-------------------------
    def Mine_MyItemList_AddBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Mine_MyItemList_AddBtn_Base()

    # 基地端-我的列表-菜品列表-新增菜品信息-------------------------
    def Mine_MyItemList_CreateProduct_Base(self, pname, pclass1, pclass2, pclass3, province, city, district):
        try:

            fields = [u"菜品名称", u"菜品品种", u"菜品产地"]
            flag_fields = [True] * 3
            el_len = self.DRIVER_BASE.find_elements_by_id(
                self.URL_BASE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv")[
                    i].text
                if op.eq(text, fields[0]) and flag_fields[i]:
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                        i].send_keys(pname)
                    flag_fields[i] = False
                    continue
                elif op.eq(text, fields[1]) and flag_fields[i]:
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                        i].click()
                    self.ThereLevelSelect_Base(pclass1, pclass2, pclass3)
                    flag_fields[i] = False
                    continue
                elif op.eq(text, fields[2]) and flag_fields[i]:
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[
                        i].click()
                    self.ThereLevelSelect_Base(province, city, district)
                    flag_fields[i] = False
                    continue
        except NoSuchElementException:
            self.Mine_MyItemList_CreateProduct_Base(pname, pclass1, pclass2, pclass3, province, city, district)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Base:indexError"
            pass
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/product_UpProduceThumb_image").click()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_photograph_photo_tv").click()
            self.DRIVER_BASE.find_elements_by_class_name("android.widget.ImageView")[4].click()
        except NoSuchElementException:
            pass

    # 基地端-我的列表-我的菜品列表-菜品信息详情-------------------------
    def Mine_MyItemList_ProductDetail_Base(self,name):
        try:
            flag = True
            while flag:
                el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/sale_produce_produceName_tv").__len__()
                for i in range(el_len):
                    text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/sale_produce_produceName_tv")[i].text
                    if op.eq(name,text):
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/sale_produce_produceName_tv")[i].click()
                        flag = False
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_ProductDetail_Base(name)

    # 基地端-我的列表-个人资料列表-设置列表查看-------------------------
    def Mine_MyItemList_SettingList_Base(self):
        try:
            # 查看使用指南
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/mine_account_instructions_ll").click()
            sleep(self.SECONDS_SHORT)
            print u"完成查看使用指南"
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看关于我们
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/mine_account_regard_we_ll").click()
            sleep(self.SECONDS_SHORT)
            print u"完成查看关于我们"
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看联系客服
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/mine_account_onlineService_ll").click()
            sleep(self.SECONDS_SHORT)
            print u"完成查看联系客服"
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看术语/条款
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_clause_ll").click()
            sleep(self.SECONDS_SHORT)
            print u"完成查看术语/条款"
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_image").click()
            sleep(self.SECONDS_SHORT)
            # 查看蓝牙配置
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_out_bluetooth_ll").click()
            sleep(self.SECONDS_SHORT)
            print u"完成查看蓝牙配置"
            self.DRIVER_BASE.find_element_by_id(self.SYS_URL + ":id/permission_allow_button").click()
            sleep(self.SECONDS_SHORT)
            self.BackToSetting_Base()
            # 退出系统
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/setting_out_login_ll").click()
        except NoSuchElementException:
            self.Mine_MyItemList_SettingList_Base()

    # 基地端-返回到设置列表页面（物理返回键:返回键代码4）--------------------------------------
    def BackToSetting_Base(self):
        flag = True
        while flag:
            try:
                self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_tv")
                flag = False
                break
            except NoSuchElementException:
                self.DRIVER_BASE.press_keycode(4)

    # 基地端-我的列表-查看消息通知列表-------------------------
    def Mine_MyItemList_MineMessages_Base(self, message1, message2, message3):
        try:
            params = [message1, message2, message3]
            print params
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/meassage_inform_title_tv").__len__()
            print el_len
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/meassage_inform_title_tv")[i].text
                print text
                if op.eq(text, params[0]):
                    print i
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/meassage_inform_title_tv")[i].click()
                    del params[0]
                    sleep(self.SECONDS_SHORT)
                    self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_left_tv").click()
                if params == []:
                   break
            self.BackToMainFuncs_Base()
        except NoSuchElementException:
            self.Mine_MyItemList_MineMessages_Base(message1,message2,message3)

    # 基地端-我的列表-查看专家咨询页面-------------------------
    def MainPage_consult_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/home_consult_ll").click()
        except NoSuchElementException:
            self.MainPage_consult_Base()

    # 基地端-我的列表-查看市场行情页面-------------------------
    def MainPage_market_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/home_market_ll").click()
        except NoSuchElementException:
            self.MainPage_market_Base()

    # 基地端-我的认证-输入认证申请编辑信息页面-文字-------------------------
    def Mine_MyItemList_CreateApplyMemberStr_Base(self, unit, credit_code, name, id_no, tel, addr, bank,user,card_no):
        try:
            fields = [u"主体法定名称 ", u"统一社会信用代码 ", u"主体法人姓名 ",u"法人身份证号码 ",u"联系电话 ",u"联系地址 ",u"开户行 ",u"开户名 ",u"银行账号 "]
            flag_fields = [True] * 9
            fields_value = [unit, credit_code, name, id_no, tel, addr, bank,user,card_no]
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_title_tv")[i].text
                if op.eq(text, fields[0]) and flag_fields[i]:
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].clear()
                    self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/mine_edit_personage_content_tv")[i].send_keys(fields_value[i])
                    flag_fields[i] = False
                    del fields[0]
                    if fields ==[]:
                        self.PageSwipe_Base()
                        break
                    else:
                        pass
        except NoSuchElementException:
            self.Mine_MyItemList_CreateApplyMemberStr_Base(unit, credit_code, name, id_no, tel, addr, bank,user,card_no)
        except IndexError:
            print "Mine_MyItemList_CreateProduct_Base:indexError"
            pass

    # 基地端-我的认证-输入认证申请编辑信息页面-图片-------------------------
    def Mine_MyItemList_CreateApplyMemberPicture_Base(self):
        text_id = [u":id/idCardFrontPhoto_image",u":id/idCardBackPhoto_image",u":id/businessLicensePhoto_image",u":id/logo_image",u":id/issuesIv"]
        flag = True
        while flag:
            for i in range(text_id.__len__()):
                try:
                    if (text_id[0]==u":id/issuesIv"):
                        self.SendPictures_Base(text_id[0])
                        del text_id[0]
                    else:
                        self.UploadPictures_Base(text_id[0])
                        del text_id[0]
                    if text_id == []:
                        print "text_id == []"
                        flag = False
                        break
                    else:
                        print text_id
                        pass
                except NoSuchElementException:
                    self.PageSwipe_Base()


    # 基地端-页面滑动-------------------------------------------
    def PageSwipe_Base(self):
        try:
            self.DRIVER_BASE.swipe(430, 1600, 430, 1175, 500)
        except WebDriverException:
            self.PageSwipe_Base()

    # 基地端-上传图片-------------------------------------------
    def UploadPictures_Base(self,param):
        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + param).click()
        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_photograph_photo_tv").click()
        self.DRIVER_BASE.find_elements_by_class_name("android.widget.ImageView")[4].click()


    # 基地端-发送图片-------------------------------------------
    def SendPictures_Base(self,param):
        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + param).click()
        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/picker_photofolder_info").click()
        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/picker_photo_grid_item_select")[4].click()
        self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/picker_bottombar_select").click()


    # 基地端-进入详情页面按钮-------------------------------------------
    def VerifyDetailBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_list_bottom_left_btn").click()
        except NoSuchElementException:
            self.VerifyDetailBtn_Base()

    # 基地端-编辑按钮-------------------------------------------
    def EditBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.EditBtn_Base()

    # 基地端-提交按钮 - ------------------------------------------
    def SubmitBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_list_bottom_right_btn").click()
        except NoSuchElementException:
            self.SubmitBtn_Base()

    # 基地端-选择发货地址---------------------------------------------
    def SelectedAddr_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/shipping_address_contacts_tv").click()
        except NoSuchElementException:
            self.SelectedAddr_Base()

    # 基地端-选择销售方式---------------------------------------------
    def SelectedSellType_Base(self,sell_type):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[sell_type].click()
        except NoSuchElementException:
            self.SelectedSellType_Base(sell_type)

    # 基地端-选择产品品级---------------------------------------------
    def Product_Grade_Base(self,grade):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[grade].click()
            # print grade
        except NoSuchElementException:
            self.Product_Grade_Base(grade)
        except IndexError:
            self.Product_Grade_Base(grade)

    # 基地端-选择产品品相---------------------------------------------
    def Product_Size_Base(self, size):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[size].click()
            # print size
        except NoSuchElementException:
            self.Product_Size_Base(size)
        except IndexError:
            self.Product_Size_Base(size)

    # 基地端-选择日期---------------------------------------------------
    def SelectedDate_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/reject_harvest_detail_sheetDate_tv").click()
            logger.info('SelectedData completed')
        except NoSuchElementException:
            self.SelectedDate_Base()

    # 基地端-风险单据-新增菜品明细按钮------------------------------------
    def CreateProductBtn_Base(self):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(text,u"新增菜品明细"):
                    self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.CreateProductBtn_Base()

    # 基地端-风险单据-添加图片按钮------------------------------------
    def AddPictureBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/issuesIv").click()
        except NoSuchElementException:
            self.PageSwipe_Base()
            self.AddPictureBtn_Base()

    # 基地端-风险单据-选择时间确认按钮------------------------------------
    def ConfirmBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/btnSubmit").click()
        except NoSuchElementException:
            self.ConfirmBtn_Base()

    # 基地端-风险单据-保存按钮-生成单据------------------------------------
    def Risk_SaveBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Risk_SaveBtn_Base()

    # 基地端-风险单据-合同按钮------------------------------------
    def SelectContractBtn_Base(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/reject_harvest_detail_sheetNo_tv").click()
        except NoSuchElementException:
            self.SelectContractBtn_Base()

    # 基地端-风险单据-选择合同/菜品项------------------------------------
    def SelectItem_Base(self):
        try:
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/role_list_roleName_tv")[0].click()
        except NoSuchElementException:
            self.SelectItem_Base()

    # 基地端-风险单据-选择合同菜品按钮------------------------------------
    def SelectContractProductBtn_Base(self):
        try:
            el_len = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView").__len__()
            for i in range(el_len):
                text = self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].text
                if op.eq(text, u"菜品"):
                    self.DRIVER_BASE.find_elements_by_class_name("android.widget.TextView")[i].click()
                else:
                    pass
        except NoSuchElementException:
            self.SelectContractProductBtn_Base()
        except IndexError:
            pass

    # 基地端-风险单据-新增菜品明细编辑页面（亩数、已采摘斤数、备注）------------------------------------
    def EditProductDetail_Base(self,mou,drop_off_qty,remark):
        # 点击合同字段
        self.SelectContractBtn_Base()
        # 选择合同项
        self.SelectItem_Base()
        # 点击菜品字段
        self.SelectContractProductBtn_Base()
        # 选择菜品项
        self.SelectItem_Base()
        flag = True
        flag_text = [True]*3
        try:
            el_len = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_name_tv").__len__()
            while flag:
                for i in range(el_len):
                    text = self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_name_tv")[i].text
                    if op.eq(text,u"亩数") and flag_text[0]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_value_edit")[i].clear()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_value_edit")[i].send_keys(mou)
                        flag_text[0] = False
                        continue
                    if op.eq(text,u"已采摘斤数") and flag_text[1]:
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_value_edit")[i].clear()
                        self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/reject_harvest_edit_produce_value_edit")[i].send_keys(drop_off_qty)
                        flag_text[1] = False
                        continue
                    if flag_text[2]:
                        try:
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/edit_remark").clear()
                            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/edit_remark").send_keys(remark)
                            flag = False
                            flag_text[2] = False
                        except NoSuchElementException:
                            self.PageSwipe_Base()
            sleep(self.SECONDS_SHORT)
            self.SaveBtn_Base()
        except NoSuchElementException:
            self.EditProductDetail_Base(mou,drop_off_qty,remark)

    # 基地端-风险单据-在图片分类列表选择图片发送-------------------------------------------
    def Risk_SendPictures_Base(self, param):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/picker_photofolder_info").click()
            self.DRIVER_BASE.find_elements_by_id(self.URL_BASE + ":id/picker_photo_grid_item_select")[param].click()
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/picker_bottombar_select").click()
        except NoSuchElementException:
            self.Risk_SendPictures_Base(param)

    # 基地端-风险单据-不采收情况备案书列表-提交至主管/确认按钮
    def Risk_SubmitBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_list_bottom_right_btn").click()
        except NoSuchElementException:
            self.Risk_SubmitBtn()



    # 基地端-风险单据-不采收情况备案书列表-点击单号进入详情
    def Risk_ClickNo(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/reject_harvest_sheetNo_tv").click()
        except NoSuchElementException:
            self.Risk_ClickNo()

    # 基地端-风险单据-不采收情况备案书详情-提交至主管按钮
    def Risk_detail_SubmitBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Risk_detail_SubmitBtn()

    # 基地端-风险单据-不采收情况备案书详情-编辑按钮
    def Risk_EditBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/title_right_image").click()
        except NoSuchElementException:
            self.Risk_EditBtn()

    # 基地端-风险单据-不采收情况备案书详情-内容编辑按钮
    def Risk_EditDataBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/reject_harvest_detail_produce_edit_image").click()
        except NoSuchElementException:
            self.Risk_EditDataBtn()

    # 基地端-风险单据-不采收情况备案书列表-删除按钮
    def Risk_DeletionBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_list_bottom_left_btn").click()
        except NoSuchElementException:
            self.Risk_DeletionBtn()

    # 基地端-风险单据-不采收情况备案书列表-拒绝按钮
    def Risk_RejectionBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/item_list_bottom_left_btn").click()
        except NoSuchElementException:
            self.Risk_RejectionBtn()

    # 基地端-风险单据-不采收情况备案书详情-删除按钮
    def Risk_Detail_DeletionBtn(self):
        try:
            self.DRIVER_BASE.find_element_by_id(self.URL_BASE + ":id/bottom_btn_right").click()
        except NoSuchElementException:
            self.Risk_Detail_DeletionBtn()

if __name__ == '__main__':
#
#     # 创建对象
    BaseRun = AppAutoBase()
    # BmsRun = BmsAutoTest()
#     TradeRun = AppAutoTest()
#
#     # 1.基地端登录流程
    BaseRun.Driver_Base()
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
#     # TradeRun.DRIVER_BASE()
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









