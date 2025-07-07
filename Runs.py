#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *
from AppAutoBase3_0 import *
from BmsAutoTest_1_7 import *



# 创建对象
# BaseRun = AppAutoBase()
# BmsRun = BmsAutoTest()
TradeRun = AppAutoTrade()

# 1.基地端登录流程
# BaseRun.Driver_Base()
# BaseRun.Banner_Pass_Base()
# BaseRun.Evr_Selected_Base()
# BaseRun.Login_By_Pwd_Base()
# BaseRun.Authorization_Sys_Base()
# 1.1基地端整合登录
# BaseRun.Login_Base()
#
# # 2.1基地端发布定价产品流程
# BaseRun.Click_Product_Transaction_Btn_Base()
# BaseRun.Click_Floating_Btn_Base()
# BaseRun.Click_checkImage_Btn_Base()
# # sell_type,unit_price,rates,expires,quantities,packages,gross_weight,product_name
# BaseRun.Creating_OnePrice_Order_Base(u"定价",u"2",u"30",u"7",u"10000",u"500",u"11000",u"线椒A大2019031801")
# BaseRun.MyTranscation_List_SubmitBtn_Base()
# BaseRun.MyTranscation_Detail_SubmitBtn_Base()
# BaseRun.MyTranscation_List_ConfirmBtn_Base()
# BaseRun.MyTranscation_Detail_ConfirmBtn_Base()
# # 2.2运营后台审核通过
# BmsRun.confirmTradeApply_Bms()
# # 2.3基地端发布定价产品流程
# BaseRun.MyTranscation_List_OnSaleBtn_Base()
# BaseRun.MyTranscation_Detail_OnSaleBtn_Base()
#
# 2.4市场端登录流程
TradeRun.Driver_Trade()
TradeRun.Banner_Pass_Trade()
TradeRun.Evr_Selected_Trade()
TradeRun.Login_By_Pwd_Trade()
TradeRun.Authorization_Sys_Trade()
#
# # 2.4.1市场端登录流程
# TradeRun.Login_Trade()
#
# # 2.5市场端申请定价流程
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
#
#
#
# # 2.6基地端审核定价+生成发货单流程
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
# BaseRun.InvoicesList_Base(4)
# BaseRun.Invoices_ShipmentList_ConfirmBtn_Base()
# BaseRun.Invoices_ShipmentDetail_ConfirmBtn_Base()
#
# # 2.7市场端支付首款
# TradeRun.Login_Trade()
# TradeRun.Invoices_Trade()
# TradeRun.InvoicesList_ShipmentList_Trade()
# TradeRun.InvoicesList_ShipmentList_DownPaymentBtn_Trade()
# TradeRun.InvoicesList_ShipmentList_ShipmentDetail_DownPaymentBtn_Trade()
# TradeRun.CashierDesk_Outline_PaymentMode_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_PaymentMode_Trade()
# TradeRun.CashierDesk_Outline_PaymentBtn_SubmitBtn_Trade()
#
# # 2.8运营后台结款确认
# BmsRun.ReceiptPayment_Bms()
#
# # 2.9基地端-司机签名
# BaseRun.Invoices_ShipmentList_SignatureBtn_Base()
# BaseRun.Invoices_ShipmentDetail_SignatureBtn_Base()
# BaseRun.Invoices_ShipmentDetail_Signing_Base()
#
# # 2.10基地端-发车
# BaseRun.Invoices_ShipmentList_DepartBtn_Base()
# BaseRun.Invoices_ShipmentDetail_DepartBtn_Base()
#
#
# # 2.11市场端-接车验货
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


# 3.市场端-我的列表
# TradeRun.BelowItem_Trade(u"我的")
# 3.1.1市场端-我的机构-新增机构
# TradeRun.Mine_MyItemList_Trade(u"我的机构")
# TradeRun.Mine_MyItemList_Departments_AddLabel_Trade()
# TradeRun.Mine_MyItemList_Departments_AddLabel_InputContents_Trade(u'捣蛋星',u'哈士奇',u'13677777777',u'1367@qq.com',u"广西",u"贺州",u"钟山",u"春风路18号")
# TradeRun.BackToMainFuncs_Trade()
# # 3.1.2市场端-我的机构-修改机构
# TradeRun.Mine_MyItemList_Trade(u"我的机构")
# TradeRun.Mine_MyItemList_DepartmentDetail_Trade(u"捣蛋星")
# TradeRun.Mine_MyItemList_DepartmentDetail_EditBtn_Trade()
# TradeRun.Mine_MyItemList_Departments_EditLabel_InputContents_Trade(u'捣蛋星改', u'哈士奇改', u'13677777888', u'13688@qq.com',u"广西",u"贺州",u"钟山",u"春风路20号")
# TradeRun.BackToMainFuncs_Trade()
# # 3.1.3市场端-我的机构-设置机构
# TradeRun.Mine_MyItemList_Trade(u"我的机构")
# TradeRun.Mine_MyItemList_DepartmentDetail_Trade(u"捣蛋星")
# TradeRun.Mine_MyItemList_DepartmentDetail_Setting_Trade()
# TradeRun.BackToMainFuncs_Trade()
# # 3.1.4市场端-我的机构-设置机构
# TradeRun.Mine_MyItemList_Trade(u"我的机构")
# TradeRun.Mine_MyItemList_DepartmentDetail_Trade(u"v3贰档口")
# TradeRun.Mine_MyItemList_DepartmentDetail_Setting_Trade()
# TradeRun.BackToMainFuncs_Trade()
# # 3.1.5市场端-我的机构-删除机构
# TradeRun.Mine_MyItemList_Trade(u"我的机构")
# TradeRun.Mine_MyItemList_DepartmentDetail_Trade(u"捣蛋星改")
# TradeRun.Mine_MyItemList_DepartmentDetail_EditBtn_Trade()
# TradeRun.Mine_MyItemList_DepartmentDetail_DelBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()

# 3.2.1市场端-员工管理列表
# TradeRun.Mine_MyItemList_Trade(u"员工管理")
# # 3.2.2市场端-员工管理-新增员工
# # TradeRun.Mine_MyItemList_Trade(u"员工管理")
# # TradeRun.Mine_MyItemList_CreateBtn_Trade()
# TradeRun.Mine_MyItemList_CreateStaffInfo_Trade(u'哈士奇', u'13677777777', u'136@qq.com',u'员工')
# # TradeRun.SaveBtn_Trade()
# # TradeRun.BackToMainFuncs_Trade()
# # # 3.2.3市场端-员工管理-修改员工
# # TradeRun.Mine_MyItemList_Trade(u"员工管理")
# # TradeRun.Mine_MyItemList_SelectedEditStaffInfo_Trade(u'哈士奇')
# # TradeRun.Mine_MyItemList_EditBtn_Trade()
# TradeRun.Mine_MyItemList_EditStaffInfo_Trade(u'w哈士奇',u'13677777788', u'1368@qq.com',u'主管')
# # TradeRun.SaveBtn_Trade()
# # TradeRun.BackToMainFuncs_Trade()
# # # 3.2.4市场端-员工管理-删除员工
# # TradeRun.Mine_MyItemList_Trade(u"员工管理")
# # TradeRun.Mine_MyItemList_SelectedEditStaffInfo_Trade(u'w哈士奇')
# # TradeRun.Mine_MyItemList_EditBtn_Trade()
# # TradeRun.Mine_MyItemList_DelBtn_Trade()
# # TradeRun.ConfirmBtn_SmallWindow()
# # TradeRun.BackToMainFuncs_Trade()


# 3.3.1市场端-我的菜品列表-新增菜品
# TradeRun.Mine_MyItemList_Trade(u"我的菜品")
# TradeRun.Mine_MyItemList_CreateBtn_Trade()
# TradeRun.Mine_MyItemList_CreateProduct_Trade(u"线椒1", u"蔬菜类", u"茄果类", u"线椒", u"宁夏", u"中卫", u"中宁", u"v3沃沃基地")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
# # 3.3.2市场端-我的菜品列表-编辑菜品
# TradeRun.Mine_MyItemList_Trade(u"我的菜品")
# TradeRun.Mine_MyItemList_SelectedEditProductInfo_Trade(u"线椒1")
# TradeRun.Mine_MyItemList_EditBtn_Trade()
# TradeRun.Mine_MyItemList_EditProduct_Trade(u"黄线椒", u"蔬菜类", u"茄果类", u"线椒", u"广西", u"柳州", u"柳南", u"v3沃沃基地")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
# # 3.3.3市场端-我的菜品列表-删除菜品
# TradeRun.Mine_MyItemList_Trade(u"我的菜品")
# TradeRun.Mine_MyItemList_SelectedEditProductInfo_Trade(u"黄线椒")
# TradeRun.Mine_MyItemList_EditBtn_Trade()
# TradeRun.Mine_MyItemList_DelBtn_Trade()
# TradeRun.ConfirmBtn_SmallWindow()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.4.1市场端-我的超利列表
# TradeRun.Mine_MyItemList_Trade(u"我的超利")
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.5.1市场端-我的收藏列表
# TradeRun.Mine_MyItemList_Trade(u"我的收藏")
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.6.1市场端-我的客户列表-新增客户信息
# TradeRun.Mine_MyItemList_Trade(u"我的客户")
# TradeRun.Mine_MyItemList_CreateBtn_Trade()
# TradeRun.Mine_MyItemList_CreateCustomer_Trade(u"鹿鼎记1",u"君临",u"13678789923",u"1234@qq.com",u"广州天河兴盛路13号",)
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.6.2市场端-我的客户列表-修改客户信息
# TradeRun.Mine_MyItemList_Trade(u"我的客户")
# TradeRun.Mine_SelectedCustomer_Trade(u"鹿鼎记1")
# TradeRun.Mine_MyItemList_EditBtn_Trade()
# TradeRun.Mine_MyItemList_CreateCustomer_Trade(u"bei北",u"贾玲",u"13678789999",u"123@qq.com",u"广州天河冼村北88号",)
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.6.3市场端-我的客户列表-删除客户信息
# TradeRun.Mine_MyItemList_Trade(u"我的客户")
# TradeRun.Mine_SelectedCustomer_Trade(u"bei北")
# TradeRun.Mine_MyItemList_EditBtn_Trade()
# TradeRun.Mine_MyItemList_DelBtn_Trade()
# TradeRun.ConfirmBtn_SmallWindow()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.7.1市场端-我的供应商列表-新增供应商信息
# TradeRun.Mine_MyItemList_Trade(u"我的供应商")
# TradeRun.Mine_MyItemList_AddBtn_Trade()
# TradeRun.Mine_MyItemList_EditSupplier_Trade(u"沃沃基地2",u"小强",u"13800998877",u"福建",u"南平",u"延平",u"采集路138号")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.7.2市场端-我的供应商列表-修改供应商信息
# TradeRun.Mine_MyItemList_Trade(u"我的供应商")
# TradeRun.Mine_MyItemList_EditSupplierBtn_Trade(u"沃沃基地2")
# TradeRun.Mine_MyItemList_EditSupplier_Trade(u"沃沃基地改",u"小强子",u"13844998877",u"广东",u"广州",u"白云",u"采集路256号")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.7.3市场端-我的供应商列表-删除供应商信息
# TradeRun.Mine_MyItemList_Trade(u"我的供应商")
# TradeRun.Mine_MyItemList_DelSupplierBtn_Trade(u"沃沃基地改")
# TradeRun.ConfirmBtn_SmallWindow()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.8.1市场端-我的收货地址列表-新增我的收货地址信息
# TradeRun.Mine_MyItemList_Trade(u"我的收货地址")
# TradeRun.Mine_MyItemList_AddBtn_Trade()
# TradeRun.Mine_MyItemList_CreateReceiptAddr_Trade(u"爵溪2",u"13477889900",u"广东",u"广州",u"白云",u"采集路256号")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.8.2市场端-我的收货地址列表-编辑我的收货地址信息
# TradeRun.Mine_MyItemList_Trade(u"我的收货地址")
# TradeRun.Mine_MyItemList_EditAddrBtn_Trade(u"鱼缸11")
# TradeRun.Mine_MyItemList_CreateReceiptAddr_Trade(u"鱼缸",u"13477889911",u"广东",u"广州",u"白云",u"采集路256号")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.8.3市场端-我的收货地址列表-删除我的收货地址信息
# TradeRun.Mine_MyItemList_Trade(u"我的收货地址")
# TradeRun.Mine_MyItemList_DelAddrBtn_Trade(u"爵溪2")
# TradeRun.ConfirmBtn_SmallWindow()
# TradeRun.BackToMainFuncs_Trade()
#
# 3.9.1市场端-我的个人资料列表
# TradeRun.Mine_MyItemList_MineInfoList_Trade()
# # 3.9.2市场端-编辑我的个人资料列表
# TradeRun.Mine_MyItemList_MineInfoList_EditInfo_Trade(u"鹧鸪菜1")
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.10.1市场端-我的消息提醒
# TradeRun.Mine_MyItemList_MineMessageBtn_Trade()
# TradeRun.Mine_MyItemList_MineMessages_Trade(u"公告", u"提醒", u"私信")
# TradeRun.BackToMainFuncs_Trade()
#
# # 3.11.1市场端-我的设置列表
# TradeRun.Mine_MyItemList_SettingBtn_Trade()
# TradeRun.Mine_MyItemList_SettingList_Trade()
# TradeRun.ConfirmBtn_SmallWindow()

# 4.1.1市场端-库存信息查看
# TradeRun.MainPageBtn_Trade(u"商品库存")
# TradeRun.Storage_Trade(u"按发货单", u"按品种")
# TradeRun.BackToMainFuncs_Trade()
#
# 5.1.1市场端-市场行情查看
# TradeRun.MainPageBtn_Trade(u"市场行情")
# TradeRun.BackToMainFuncs_Trade()

# 6.1.1市场端-新增行情
# TradeRun.MainPageFuncsBtn_Trade()
# TradeRun.FuncBtn_Trade(u"新增行情")
# TradeRun.Create_Quotation_Trade(u'2',u'3',u'4',u'1',u'3.3')
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()

# 6.1.2市场端-查看行情数据
# TradeRun.MainPageFuncsBtn_Trade()
# TradeRun.FuncBtn_Trade(u"行情数据")
# TradeRun.BackToMainFuncs_Trade()


# 7.1.1基地端-我的列表
# BaseRun.MainPageBelowBtn_Base(u"我的")
# 7.2.1基地端-我的个人资料列表
# BaseRun.Mine_MyItemList_MineInfoList_Base()
# # 7.2.2基地端-编辑我的个人资料列表
# BaseRun.Mine_MyItemList_MineInfoList_EditInfo_Base(u"沃农基地Auto")
# BaseRun.BackToMainFuncs_Base()
#
# 7.3.1基地端-我的基地列表
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# 7.3.2基地端-我的基地-新增基地
# BaseRun.Mine_MyItemList_MyBases_AddLabel_Base()
# BaseRun.Mine_MyItemList_Bases_AddLabel_InputContents_Base(u"基地AUTO2019031801",u"1001",u"线椒、白菜",u"追梦",u"13466887878",u"内蒙古",u"包头",u"固阳",u"阳光大道118号")
# BaseRun.BackToMainFuncs_Base()
# 7.3.3基地端-我的基地-修改基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"基地AUTO2019031801")
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.Mine_MyItemList_Bases_AddLabel_InputContents_Base(u"基地AUTO2019031801改",u"1111",u"线椒",u"追梦人",u"13466887899",u"内蒙古",u"包头",u"固阳",u"阳光大道111号")
# BaseRun.BackToMainFuncs_Base()
# 7.3.4基地端-我的基地-设置当前/默认基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"基地AUTO2019031801改")
# BaseRun.Mine_MyItemList_BaseDetail_Setting_Base()
# BaseRun.BackToMainFuncs_Base()
# # 7.3.5基地端-我的基地-设置当前/默认基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"v3沃农基地")
# BaseRun.Mine_MyItemList_BaseDetail_Setting_Base()
# BaseRun.BackToMainFuncs_Base()
# 7.3.6基地端-我的基地-删除基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"基地AUTO2019031801改")
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()

# 7.4.1基地端-我的员工管理列表
# BaseRun.Mine_MyItemList_Base(u"员工管理")
# 7.4.2基地端-我的员工管理列表-新增员工信息
# BaseRun.Mine_MyItemList_Base(u"员工管理")
# BaseRun.Mine_MyItemList_MyBases_AddLabel_Base()
# BaseRun.Mine_MyItemList_CreateStaffInfo_Base(u"佛系fox2",u"13788990088",u"123@139.com",u"v3沃农基地", u"主管")
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# # # 7.4.3基地端-我的员工管理列表-修改员工信息
# BaseRun.Mine_MyItemList_Base(u"员工管理")
# BaseRun.Mine_MyItemList_EmployeeDetail_Base(u"佛系fox2")
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.Mine_MyItemList_EditStaffInfo_Base(u"佛系fox",u"13788990055",u"123@139.com",u"v3沃农基地", u"员工")
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# # # 7.4.4基地端-我的员工管理列表-删除员工信息
# # BaseRun.Mine_MyItemList_Base(u"员工管理")
# # BaseRun.Mine_MyItemList_EmployeeDetail_Base(u"佛系fox")
# # BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# # BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# # BaseRun.ConfirmBtn_SmallWindow()
# # BaseRun.BackToMainFuncs_Base()
#
# # 7.5.1基地端-我的产品列表-查看我的预售/交易列表
# BaseRun.Mine_MyItemList_Base(u"我的产品")
# BaseRun.MyProducts_Base(u"我的预售",u"我的交易")
# BaseRun.BackToMainFuncs_Base()
#
# # 7.6.1基地端-我的菜品列表-新增菜品
# BaseRun.Mine_MyItemList_Base(u"我的菜品")
# BaseRun.Mine_MyItemList_AddBtn_Base()
# BaseRun.Mine_MyItemList_CreateProduct_Base(u"线椒1", u"蔬菜类", u"茄果类", u"线椒", u"宁夏", u"中卫", u"中宁")
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# # # 7.6.2基地端-我的菜品列表-编辑菜品
# BaseRun.Mine_MyItemList_Base(u"我的菜品")
# BaseRun.Mine_MyItemList_ProductDetail_Base(u"线椒1")
# BaseRun.Mine_MyItemList_AddBtn_Base()
# BaseRun.Mine_MyItemList_CreateProduct_Base(u"线椒改", u"蔬菜类", u"茄果类", u"线椒", u"广东",u"广州",u"白云")
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# # # 7.6.3基地端-我的菜品列表-删除菜品
# BaseRun.Mine_MyItemList_Base(u"我的菜品")
# BaseRun.Mine_MyItemList_ProductDetail_Base(u"线椒改")
# BaseRun.Mine_MyItemList_AddBtn_Base()
# BaseRun.Mine_MyItemList_AddBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()

# 7.7.1基地端-设置列表-查看所有列表
# BaseRun.Mine_MyItemList_Base(u"设置")
# BaseRun.Mine_MyItemList_SettingList_Base()
# # BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()

# 7.8.1基地端-消息通知-查看所有通知列表
# BaseRun.Mine_MyItemList_Base(u"消息通知")
# BaseRun.Mine_MyItemList_MineMessages_Base(u"公告", u"提醒", u"私信")

# 7.9.1基地端-消息通知-查看市场行情页面
# BaseRun.MainPageBelowBtn_Base(u"首页")
# BaseRun.MainPage_market_Base()
# BaseRun.BackToMainFuncs_Base()
# 7.9.2基地端-消息通知-查看专家咨询页面
# BaseRun.MainPage_consult_Base()
# BaseRun.BackToMainFuncs_Base()
# 7.9.3基地端-消息通知-查看统计页面
# BaseRun.MainPageBelowBtn_Base(u"统计")


# 8.1.1基地端-新增我的认证申请
# BaseRun.Mine_MyItemList_Base(u"我的认证")
# BaseRun.Mine_MyItemList_AddBtn_Base()
# BaseRun.Mine_MyItemList_CreateApplyMemberStr_Base(u"印品1",u"qwer1234",u"六道真人",u"110101199003074450",u"13522778833",u"北京天安门",u"北京银行",u"六道吖",u"12345678")
# BaseRun.Mine_MyItemList_CreateApplyMemberPicture_Base()
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# 8.1.2基地端-编辑我的认证申请
# BaseRun.Mine_MyItemList_Base(u"我的认证")
# BaseRun.VerifyDetailBtn_Base()
# BaseRun.EditBtn_Base()
# BaseRun.Mine_MyItemList_CreateApplyMemberStr_Base(u"印品1",u"qwer12341",u"八道1",u"110101199003074450",u"13522778833",u"北京天安门1",u"北京银行1",u"八道吖1",u"123456781")
# BaseRun.Mine_MyItemList_CreateApplyMemberPicture_Base()
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()
# 8.1.3基地端-删除我的认证申请
# BaseRun.Mine_MyItemList_Base(u"我的认证")
# BaseRun.VerifyDetailBtn_Base()
# BaseRun.SaveBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()
# 8.1.4基地端-提交我的认证申请
# BaseRun.Mine_MyItemList_Base(u"我的认证")
# BaseRun.SubmitBtn_Base()
# BaseRun.SaveBtn_Base()
# BaseRun.BackToMainFuncs_Base()

# 8.1.4.1运营后台-受理/确认我的认证申请
# BmsRun.GetMemberCertId_Bms(u"印品1")
# BmsRun.AcceptCert_Bms()
# BmsRun.SignCert_Bms()


# 9.1.1市场端-新增我的认证申请-第一位（0个人-未实现、1企业），第二位（0加工厂、1档口）
# TradeRun.Mine_MyItemList_Trade(u"我的认证")
# TradeRun.EditBtn_Trade()
# TradeRun.Mine_MyItemList_CreateApplyMemberStr_Trade(1, 1, u"档口捣蛋星",u"qwer1234",u"哈士奇",u"110101199003074450",u"13522778833",u"北京天安门",u"北京银行",u"哈士奇1",u"12345678")
# TradeRun.Mine_MyItemList_CreateApplyMemberPicture_Trade()
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()

# 9.1.2市场端-提交我的认证申请
# TradeRun.Mine_MyItemList_Trade(u"我的认证")
# TradeRun.SubmitBtn_Trade()
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()

# 9.1.3市场端-编辑我的认证申请-第一位（0个人-未实现、1企业），第二位（0加工厂、1档口）
# TradeRun.Mine_MyItemList_Trade(u"我的认证")
# TradeRun.VerifyDetailBtn_Trade()
# TradeRun.EditBtn_Trade()
# TradeRun.Mine_MyItemList_CreateApplyMemberStr_Trade(1, 1, u"档口捣蛋星",u"qwer1234",u"哈士奇",u"110101199003074450",u"13522778833",u"北京天安门",u"北京银行",u"哈士奇1",u"12345678")
# TradeRun.SaveBtn_Trade()
# TradeRun.BackToMainFuncs_Trade()

# 9.1.4市场端-删除我的认证申请
# TradeRun.Mine_MyItemList_Trade(u"我的认证")
# TradeRun.VerifyDetailBtn_Trade()
# TradeRun.SaveBtn_Trade()
# TradeRun.ConfirmBtn_SmallWindow()
# TradeRun.BackToMainFuncs_Trade()

# 10.市场端-单据列表
# TradeRun.BelowItem_Trade(u"单据")
# 10.1市场端-单据列表-风险单据列表
# TradeRun.RiskInvoicesList_Trade()
# 10.1.1市场端-单据列表-新增风险单据
# TradeRun.EditBtn_Trade()
# TradeRun.AddProductDetailLink_Trade()


# 临时
# 7.4.4基地端-我的员工管理列表-删除员工信息
# BaseRun.Mine_MyItemList_Base(u"员工管理")
# BaseRun.Mine_MyItemList_EmployeeDetail_Base(u"佛系fox")
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()
# 7.3.5基地端-我的基地-设置当前/默认基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"v3沃农基地")
# BaseRun.Mine_MyItemList_BaseDetail_Setting_Base()
# BaseRun.BackToMainFuncs_Base()
# 7.3.6基地端-我的基地-删除基地
# BaseRun.Mine_MyItemList_Base(u"我的基地")
# BaseRun.Mine_MyItemList_BaseDetail_Base(u"基地AUTO2019031801改")
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.Mine_MyItemList_BaseDetail_EditBtn_Base()
# BaseRun.ConfirmBtn_SmallWindow()
# BaseRun.BackToMainFuncs_Base()