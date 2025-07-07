#-*-coding:utf-8-*-
from AppAutoTrade3_0 import *

# 1.实例化对象
TradeRun = AppAutoTrade()

# 2.市场端登陆
TradeRun.Driver_Trade()
TradeRun.Authorization_Sys_Trade()
TradeRun.Banner_Pass_Trade()
TradeRun.Evr_Selected_Trade()
TradeRun.Login_By_Pwd_Trade()

# 3.市场端-我的列表
TradeRun.BelowItem_Trade(u"我的")
# 3.1市场端-我的机构-新增机构
TradeRun.Mine_MyItemList_Trade(u"我的机构")
TradeRun.Mine_MyItemList_Departments_AddLabel_Trade()
TradeRun.Mine_MyItemList_Departments_AddLabel_InputContents_Trade(u'捣蛋星',u'哈士奇',u'13677777777',u'1367@qq.com',u"广西",u"贺州",u"钟山",u"春风路18号")
TradeRun.BackToMainFuncs_Trade()
