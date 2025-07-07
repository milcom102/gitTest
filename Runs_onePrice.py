#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *
from AppAutoBase3_0 import *
from BmsAutoTest_1_7 import *
from MysqlConnectDemos import *
from log_send_email_demo import *

# 创建对象
BaseRun = AppAutoBase()
BmsRun = BmsAutoTest()
TradeRun = AppAutoTrade()
SendEmail = SendEmail()
Msc = mysqlConn()

# # 1.基地端-完整登录
# BaseRun.Login_Base()
# # 2.基地端-选择进入产品交易页面按钮
# BaseRun.Click_Product_Transaction_Btn_Base()
# # 3.基地端-新增（设置）交易产品按钮
# BaseRun.Click_Floating_Btn_Base()
# # 4.基地端-点击选择交易产品项
# BaseRun.Click_checkImage_Btn_Base()
# # 5.基地端-新增（设置）交易产品信息
# params = []     # 定义一个数组装载数据库获取的数据
# order_params = Msc.one_price_order_params()  # 获取数据库定价销售的数据
# list1 = order_params.__len__()  # 获取数据库列数
# line1 = order_params[list1-1].__len__() # 获取数据库元素数
# for i in range(1):
#     for j in range(1, line1):
#         # print data[i][j]
#         params.append(order_params[i][j])
# # 删除第一个数据库ID数据
# # params.remove(data[0][0]) #j循环设置1，可去掉该语句
# BaseRun.Creating_OnePrice_Order_Base(params)
# # 6.基地端-在列表点击提交交易产品信息“提交”按钮
# BaseRun.MyTranscation_List_SubmitBtn_Base()
# # 7.基地端-弹出小框提交确认
# BaseRun.ConfirmBtn_SmallWindow()
# # 8.基地端-点击产品交易列表的“主管核准”按钮
# BaseRun.MyTranscation_List_SubmitBtn_Base()
# # 9.基地端-弹出小框提交确认
# BaseRun.ConfirmBtn_SmallWindow()
# # 10.运营后台-获取提交状态的交易上架申请，输入参数（搜索之后Id范围、申请单位）
# BmsRun.getTradeApplys_Bms(u'330',u"沃沃基地班")
# # 11.运营后台-交易上架申请审核通过
# BmsRun.confirmTradeApply_Bms()
#
# # 12.基地端-返回到首页主页
# BaseRun.BackToMainFuncs_Base()
# # 13.基地端-返回到首页主页选择进入产品交易页面按钮
# BaseRun.Click_Product_Transaction_Btn_Base()
# # 14.基地端-在产品列表点击“上架”按钮
# BaseRun.MyTranscation_List_SubmitBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()

# # 15.市场端-完整登录
# TradeRun.Login_Trade()
# # 16.市场端-首页点击“交易大厅”进入
# TradeRun.TranscationHallBtn_Trade()
# # 17.市场端-首页点击“交易大厅”进入-选择“交易产品”列表
# TradeRun.TranscationProduce_List_Trade()
# # 18.市场端-首页点击“交易大厅”进入-选择“交易产品”列表的“申请下单”按钮
# TradeRun.TranscationProduce_List_ApplyBtn_Trade()
# # 19.市场端-申请下单列表录入+确认订单按钮
# order_Apply = Msc.one_price_order_apply()  # 获取数据库定价销售的采购订单数据
# TradeRun.Produce_CreateOrderApply_Trade(order_Apply[0][1],order_Apply[0][2])
# # 20.市场端-采购订单-采购订单列表-提交按钮
# TradeRun.OrderList_SubmitBtn_Trade()
# TradeRun.ConfirmBtn_SmallWindow()
# # 21.市场端-采购订单-采购订单列表-验证按钮
# TradeRun.OrderList_VerifyBtn_Trade()
# TradeRun.ConfirmBtn_SmallWindow()

# 22.基地端-完整登录
BaseRun.Login_Base()
# 23.基地端-点击单据进入单据列表页面
BaseRun.Invoices_Base()
# 24.基地端-点击单据进入单据列表页面-选择采购订单列表
BaseRun.Invoices_OrderList_Base()
# # 25.基地端-点击单据进入单据列表页面-选择采购订单列表-列表项选择“确认订单”
# BaseRun.Invoices_OrderList_ConfirmBtn_Base()
# # 26.基地端-弹出小框提交确认
# BaseRun.ConfirmBtn_SmallWindow()
# 27.基地端-首页-单据列表-采购订单列表-生成发货单按钮
BaseRun.Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base()
# 28.基地端-生成发货单和提交按钮
examine_cargo = Msc.one_price_examine_cargo()  # 获取数据发货单数据
# 第几行数据
num = 0
BaseRun.Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base(num,examine_cargo)

# 29.基地端-返回到首页主页
BaseRun.BackToMainFuncs_Base()
# 30.基地端-选择点击进入发货单据
BaseRun.InvoicesList_Base(1)
# 31.基地端-在发货单据列表点击“提交审核”按钮
BaseRun.Invoices_ShipmentList_ConfirmBtn_Base()
# 32.基地端-弹出小框提交确认
BaseRun.ConfirmBtn_SmallWindow()
# 33.基地端-主管点击“确认”按钮
BaseRun.Invoices_ShipmentList_ConfirmBtn_Base()
# 34.基地端-弹出小框提交确认
BaseRun.ConfirmBtn_SmallWindow()

# 35.市场端-完整登录
TradeRun.Login_Trade()
# 36.市场端-点击底端“单据”
TradeRun.Invoices_Trade(u"单据")
# 37.市场端-在“单据”列表点击“发货单据”
TradeRun.InvoicesList_ShipmentList_Trade()
# 38.市场端-在“发货单据”列表点击“支付首款”按钮
TradeRun.InvoicesList_ShipmentList_DownPaymentBtn_Trade()
# 39.市场端-选择“线下支付”
TradeRun.CashierDesk_Outline_PaymentMode_Trade()
# 40.市场端-点击“确认支付”按钮
TradeRun.CashierDesk_Outline_PaymentBtn_Trade()
# 41.市场端-点击“支付方式”列-选择“支票”支付
TradeRun.CashierDesk_Outline_PaymentBtn_PaymentMode_Trade()
# 42.市场端-在“线下支付”页面点击“提交”按钮
TradeRun.CashierDesk_Outline_PaymentBtn_SubmitBtn_Trade()

# 43.运营后台-获取首付款档口名称和付款凭证号码
BmsRun.getVouchers_Bms(u"企业档口法定名")
# 44.运营后台-根据付款凭证号码点击“结款”按钮
BmsRun.ReceiptPayment_Bms()

# 2.9基地端-司机签名
# BaseRun.Invoices_ShipmentList_SignatureBtn_Base()
# BaseRun.Invoices_ShipmentDetail_SignatureBtn_Base()
# BaseRun.Invoices_ShipmentDetail_Signing_Base()

# 2.10基地端-发车
# BaseRun.Invoices_ShipmentList_DepartBtn_Base()
# BaseRun.Invoices_ShipmentDetail_DepartBtn_Base()


# 2.11市场端-接车验货
# TradeRun.Login_Trade()
# TradeRun.PickupExamineBtn_Trade()
# TradeRun.PickupBtn_Trade()
# TradeRun.HadPickupList_Trade()
# TradeRun.SignatureBtn_Trade()
# TradeRun.ExamineStatus_CreateDamageDetail_Trade()
# TradeRun.ExamineStatus_CreateTemplature_Trade()
# TradeRun.ExamineStatus_SignatureBtn_Trade()
# TradeRun.ExamineStatus_Signing_Trade()
# TradeRun.ExamineStatus_DirectorConfirm_Trade()
# TradeRun.ExamineStatusList_DirectorConfirm_Trade()


