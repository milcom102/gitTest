#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *
from AppAutoBase3_0 import *
from BmsAutoTest_1_7 import *

# 创建对象
BaseRun = AppAutoBase()
BmsRun = BmsAutoTest()
TradeRun = AppAutoTrade()

# 1.1基地端整合登录
BaseRun.Login_Base()
# 2.1基地端发布定价产品流程
BaseRun.Click_Product_Transaction_Btn_Base()
BaseRun.Click_Floating_Btn_Base()
BaseRun.Click_checkImage_Btn_Base()
# 对应参数sell_type（0代销-1定价）,unit_price,rates,expires,quantities,packages,gross_weight,grade(0A,1B,2C),size(0大1中2小),product_name
BaseRun.Creating_OnePrice_Order_Base(1,u"2",u"30",u"7",u"10000",u"500",u"11000",0,0,u"线椒A大2019031801")
BaseRun.MyTranscation_List_SubmitBtn_Base()
# BaseRun.MyTranscation_Detail_SubmitBtn_Base()
# BaseRun.MyTranscation_List_ConfirmBtn_Base()
# BaseRun.MyTranscation_Detail_ConfirmBtn_Base()
# 2.2运营后台审核通过
# BmsRun.confirmTradeApply_Bms()
# 2.3基地端发布定价产品流程
# BaseRun.MyTranscation_List_OnSaleBtn_Base()
# BaseRun.MyTranscation_Detail_OnSaleBtn_Base()

# 2.4.1市场端登录流程
# TradeRun.Login_Trade()

# 2.5市场端申请定价流程
# TradeRun.TranscationHallBtn_Trade()
# TradeRun.TranscationProduce_List_Trade()
# TradeRun.TranscationProduce_List_ApplyBtn_Trade()
# TradeRun.KnowBtn_Trade()
# TradeRun.TranscationProduce_List_ApplyBtn_Trade()
# TradeRun.Produce_CreateOrderApply_Trade()
# TradeRun.OrderList_SubmitBtn_Trade()
# TradeRun.OrderList_Detail_SubmitBtn_Trade()
# TradeRun.OrderList_VerifyBtn_Trade()
# TradeRun.OrderList_Detail_VerifyBtn_Trade()



# 2.6基地端审核定价+生成发货单流程
# BaseRun.Login_Base()
# BaseRun.Invoices_Base()
# BaseRun.Invoices_OrderList_Base()
# BaseRun.Invoices_OrderList_ConfirmBtn_Base()
# BaseRun.Invoices_OrderDetail_ConfirmBtn_Base()
# BaseRun.Invoices_OrderList_ToProcessBtn_Base()
# BaseRun.Invoices_OrderList_OrderMsg_ToProcessBtn_Base()
# BaseRun.Invoices_OrderList_OrderList_DoneBtn_Base()
# BaseRun.Invoices_OrderList_OrderMsg_DoneBtn_Base()
# BaseRun.Invoices_OrderList_OrderList_CreateShippingPackageBtn_Base()
# BaseRun.Invoices_OrderList_OrderMsg_CreateShippingPackageBtn_Base()
# BaseRun.Invoices_OrderList_OrderMsg_CreateShippingPackageAndSubmitBtn_Base()
# BaseRun.Back_PhysicsBtn_Base()
# BaseRun.Back_PhysicsBtn_Base()
# BaseRun.Invoices_ShipmentList_Base()
# BaseRun.Invoices_ShipmentList_ConfirmBtn_Base()
# BaseRun.Invoices_ShipmentDetail_ConfirmBtn_Base()

# 2.7市场端支付首款
# TradeRun.Login_Trade()
# TradeRun.Invoices_Trade()
# TradeRun.InvoicesList_ShipmentList_Trade()
# TradeRun.InvoicesList_ShipmentList_DownPaymentBtn_Trade()
# TradeRun.InvoicesList_ShipmentList_ShipmentDetail_DownPaymentBtn_Trade()
# TradeRun.CashierDesk_Outline_PaymentMode_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_PaymentMode_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_SubmitBtn_Trade()

# 2.8运营后台结款确认
# BmsRun.ReceiptPayment_Bms()

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