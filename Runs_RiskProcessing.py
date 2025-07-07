#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *
from AppAutoBase3_0 import *
from BmsAutoTest_1_7 import *
from MysqlConnectDemo import data


# 创建对象
BaseRun = AppAutoBase()
BmsRun = BmsAutoTest()
TradeRun = AppAutoTrade()


# 1.基地端整合登录
BaseRun.Login_Base()
# 2.点击单据项
BaseRun.MainPageBelowBtn_Base(u"单据")
# 3.在单据列表选择风险单据列表
BaseRun.InvoicesList_Base(4)
# 4.新增风险单据进入按钮
BaseRun.AddBtn_Base()

# 5.新增风险单据内容编辑
# 5.1点击开单日期
BaseRun.SelectedDate_Base()
# 5.1.1选择日期和确定
BaseRun.ConfirmBtn_Base()
# 5.2点击新增菜品明细字段
BaseRun.CreateProductBtn_Base()
# 5.2.1编辑新增菜品明细页面内容（亩数、已采摘斤数、备注）
BaseRun.EditProductDetail_Base(14, 3000, u"autoTest")
# 连接数据库数据
# BaseRun.EditProductDetail_Base(data[0][0], data[0][1], data[0][2])

# 5.3选择图片-数字3~30
BaseRun.AddPictureBtn_Base()
BaseRun.Risk_SendPictures_Base(5)
# 5.4点击确定生成不采收情况备案书单据
BaseRun.Risk_SaveBtn_Base()
# 5.5回退至单据列表页面
BaseRun.BackToMainFuncs_Base()

# 6.提交风险单据至主管审批
# 6.1点击进入风险单据列表
BaseRun.InvoicesList_Base(4)
# 6.2列表点击提交至主管按钮
BaseRun.Risk_SubmitBtn()
# 6.3详情点击提交至主管按钮
BaseRun.Risk_detail_SubmitBtn()
# 6.4列表点击确认按钮
BaseRun.Risk_SubmitBtn()
# 6.5详情点击确认按钮
BaseRun.Risk_detail_SubmitBtn()
# 6.6回退至单据列表页面
BaseRun.BackToMainFuncs_Base()

# 7.点击进入风险单据列表
BaseRun.InvoicesList_Base(4)
# 7.1列表点击提交风险单据至平台审批按钮
BaseRun.SubmitBtn_Base()
# 7.2详情点击提交至平台按钮
BaseRun.Risk_detail_SubmitBtn()
# 7.3获取不采收风险单据列表申请人ID-运营后台
BmsRun.GetBills_Bms(u'v3沃农基地')
# 7.4受理不采收风险单据-运营后台
BmsRun.AcceptRiskApply_Bms()
# 7.5核实不采收风险单据-运营后台
BmsRun.ConfirmRiskApply_Bms()
# 7.6转账不采收风险单据-运营后台
BmsRun.PaymentRiskApply_Bms()

