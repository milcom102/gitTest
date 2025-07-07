#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *
from AppAutoBase3_0 import *
from BmsAutoTest_1_7 import *
from MysqlConnectDemo import *
from auto_test_log_demo import *
from log_send_email_demo import *



# 创建对象
BaseRun = AppAutoBase()
BmsRun = BmsAutoTest()
TradeRun = AppAutoTrade()
SendEmail = SendEmail()

# 1.基地端整合登录
BaseRun.Login_Base()
# 2.点击单据项
BaseRun.MainPageBelowBtn_Base(u"单据")
# 3.在单据列表选择风险单据列表
BaseRun.InvoicesList_Base(4)
# 4.新增风险单据进入按钮
BaseRun.AddBtn_Base()
try:
    # 5.新增风险单据
    # 5.1点击开单日期
    BaseRun.SelectedDate_Base()
    # 5.1.1选择日期和确定
    BaseRun.ConfirmBtn_Base()
    # 5.2点击新增菜品明细字段
    BaseRun.CreateProductBtn_Base()
    # 5.2.1编辑新增菜品明细页面内容（亩数、已采摘斤数、备注）
    BaseRun.EditProductDetail_Base(13, 2000, u"autoTest")
    # 5.3选择图片-数字3~30
    BaseRun.AddPictureBtn_Base()
    BaseRun.Risk_SendPictures_Base(5)
    # 5.4点击确定生成不采收情况备案书单据
    BaseRun.Risk_SaveBtn_Base()
    # 5.5回退至单据列表页面
    BaseRun.BackToMainFuncs_Base()

    for i in range(el_len):
        # 6.编辑风险单据内容
        # 6.1点击进入风险单据列表
        BaseRun.InvoicesList_Base(4)
        # 6.2点击单号进入详情
        BaseRun.Risk_ClickNo()
        # 6.3点击编辑不采收备案书内容按钮
        BaseRun.Risk_EditBtn()
        # 6.4点击编辑不采收备案书内容编辑按钮
        BaseRun.Risk_EditDataBtn()
        # 6.5编辑不采收备案书内容（亩数、已采摘斤数、备注）
        # BaseRun.EditProductDetail_Base(11, 2300, u"autoTestAgain")
        BaseRun.EditProductDetail_Base(data[i][0], data[i][1], data[i][2])
        # 6.6点击更新按钮
        BaseRun.Risk_SaveBtn_Base()
        # 6.7回退至单据列表页面
        BaseRun.BackToMainFuncs_Base()

    # 7.删除风险单据
    # 7.1点击进入风险单据列表
    BaseRun.InvoicesList_Base(4)
    # 7.2点击删除风险单据按钮-列表
    BaseRun.Risk_DeletionBtn()
    # # 7.3点击删除风险单据按钮-详情
    # BaseRun.Risk_Detail_DeletionBtn()
    # 7.4弹框确认删除
    BaseRun.ConfirmBtn_SmallWindow()
    # 7.5回退至单据列表页面
    BaseRun.BackToMainFuncs_Base()

finally:
    # 8.发送log至xieyexiang@ad20.com邮箱
    # 需要加finally最后必须执行
    SendEmail.send_email('xieyexiang@ad2o.com','milcom102@163.com')
