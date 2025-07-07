#-*-coding:utf-8-*-

from appium import webdriver
from time import sleep
import re
import operator as op
from selenium.common.exceptions import NoSuchElementException
# app外网地址
Trade_Url = "trade.sale.onlty.com"
Base_Url = "base.sale.onlty.com"
# app执行环境
Trade_Evr3_Http = u"http://api.asc.dev.ad2o.com/v3/trade/"
Trade_Evr2_Http = u"http://api.demo-asc.ad2o.com/trade/"
Base_Evr3_Http = u"http://api.asc.dev.ad2o.com/v3/base/"
Base_Evr2_Http = u"http://api.demo-asc.ad2o.com/base/"
# 环境名称
Evr_name = "v2_test"
# android系统查看app是否已安装
sys_url = "com.android.packageinstaller"
# 登录的账户号码
accountNo = "13533885458"
# 登录的账号密码
accountPwd = "13533885458"
# 自定义基地名称
base_name = u"沃农基地"
# app包名称
appPackage = "base.sale.onlty.com"
# app活动包
appActivity = "base.sale.onlty.com.activity.SplashActivity"



# 链接设备和APP设置-------------------------------------------------
desired_caps = {
'platformName': 'Android',
'deviceName': 'e874797',
'platformVersion': '6.0.1',
'appPackage': 'trade.sale.onlty.com',
'appActivity': 'trade.sale.onlty.com.activity.SplashActivity',
'unicodeKeyboard':'True',
'resetKeyboard':'True'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 启动APP---------------------------------------------------------
driver.launch_app()
sleep(7)
# 登录APP---------------------------------------------------------
# BANNER首页“跳过”
driver.find_element_by_id(Trade_Url+":id/next_button").click()
# 勾选“我已经阅读并同意《绿田云服务协议》
driver.find_element_by_id(Trade_Url+":id/veriflcation_login_serve_image").click()
# 在“手机登录/注册”坐标-点击3次进入切换环境，每次间隔100毫秒
for num in range(1,4):
    driver.tap([(60,273),(368,338)],100)
    print num

# 输入创建新环境名称
driver.find_element_by_id(Trade_Url+":id/damain_name_tv").send_keys(Evr_name)
# 输入创建新环境地址
driver.find_element_by_id(Trade_Url+":id/damain_path_tv").send_keys(Evr_http)
# 点击-确认-按钮
driver.find_element_by_id(Trade_Url+":id/damain_add_tv").click()

# 选择测试环境地址ad2o:获取相同ID列表list后，匹配所选环境地址
# 获取list元素数量
el_len = driver.find_elements_by_id(Trade_Url+":id/market_list_number_2_02").__len__()
# print "elements list length:",el_len

# 遍历所有list元素并获取text文本内容用于比较新建的测试环境地址，匹配成功则点击字段切换环境
for i in range(el_len):
    Base_Evr_Http_Add = driver.find_elements_by_id(Trade_Url+":id/market_list_number_2_02")[i].text
    # print Evr_add
    # print Evr_http
    # print type(Evr_add)
    # print type(Evr_http)
    # print op.eq(Evr_http,Evr_add)
    # 字符串比较函数
    if op.eq(Base_Evr2_Http,Base_Evr_Http_Add):
        driver.find_elements_by_id(Trade_Url + ":id/market_list_number_2_02")[i].click()
        break
        # print "if"
    else:
        # print "else"
        continue


# Evr_url_1 = driver.find_elements_by_id(url+":id/market_list_number_2_02")
# print "Evr_url_1",Evr_url_1[1:]
# output: Evr_url_1 [<appium.webdriver.webelement.WebElement (session="4802a604-de09-4e71-9897-42e7e89307f1", element="7")>,
# <appium.webdriver.webelement.WebElement (session="4802a604-de09-4e71-9897-42e7e89307f1", element="8")>]

# Evr_url_size = driver.find_elements_by_id(url+":id/market_list_number_2_02")[2].size
# output: Evr_url_size {'width': 610, 'height': 63}

# Evr_url_text = driver.find_elements_by_id(url+":id/market_list_number_2_02")[2].text
# output: 输出改ID元素的第3项的文本信息，http://api.asc.dev2.ad2o.com/trade/

# Evr_url_is_selected = driver.find_elements_by_id(url+":id/market_list_number_2_02")[2].is_selected()
# output: false

# 点击-切换-按钮
driver.find_element_by_id(Trade_Url+":id/damain_cut_tv").click()

# 在“请输入手机号”框输入手机号
driver.find_element_by_id(Trade_Url+":id/veriflcation_login_mobile_edit").send_keys(accountNo)

# 点击-下一步-按钮
driver.find_element_by_id(Trade_Url+":id/veriflcation_login_btn").click()

# 点击以输入密码方式登录
driver.find_element_by_id(Trade_Url+":id/account_loginType_tv").click()

# 输入密码登录
driver.find_element_by_id(Trade_Url+":id/account_password_edit").send_keys(accountPwd)

# 点击-登录-按钮
driver.find_element_by_id(Trade_Url+":id/account_login_btn").click()
sleep(4)

# 授权使用电话
driver.find_element_by_id(sys_url+":id/permission_allow_button").click()

# 授权使用日历
driver.find_element_by_id(sys_url+":id/permission_allow_button").click()

# 授权使用拍摄和录制视频
driver.find_element_by_id(sys_url+":id/permission_allow_button").click()

# 授权可以读取照片和媒体内容
driver.find_element_by_id(sys_url+":id/permission_allow_button").click()

# 授权使用录制音频
driver.find_element_by_id(sys_url+":id/permission_allow_button").click()

# 点击-入驻基地-按钮
driver.find_element_by_id(Trade_Url+":id/home_superMode_ll").click()
sleep(4)

# text1 = driver.find_element_by_class_name("android.widget.TextView").text
# print "text1:",text1
# sleep(4)
#
# text2 = driver.find_element_by_class_name("android.widget.TextView").tag_name
# print "text2:",text2
# sleep(4)
#
# text3 = driver.find_element_by_id(url+":id/super_mode_list_supplierName_tv").get_attribute("resourceId")
# print "resourceId:",text3
# sleep(4)
#
# text4 = driver.find_element_by_id(url+":id/super_mode_list_supplierName_tv").get_attribute("className")
# print "className:",text4
# sleep(4)
#
# text5 = driver.find_element_by_id(url+":id/super_mode_list_supplierName_tv").get_attribute("text")
# print "text:",text5
# sleep(4)

# el_lenA = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv").__len__()
# print "el_lenA:",el_lenA
#
# el_len = []
# el_len = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv")[0].text
# print el_len
# el_len = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv")[1].text
# print el_len
# el_len = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv")[2].text
# print el_len
# el_len = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv")[3].text
# el_len = driver.find_elements_by_id(url+":id/super_mode_list_supplierName_tv")[4].text
# print el_len

# 入驻基地-产品一览（在入驻基地列表滑动查找目标基地名称，查找到后停止滑动）
flag = True
while(flag):
    # 获取当前列表list元素个数
    el_Nlen = driver.find_elements_by_id(Trade_Url+":id/super_mode_list_supplierName_tv").__len__()
    # 遍历列表list元素并获取基地名称的文本
    for n1 in range(el_Nlen):
        base_name1 = driver.find_elements_by_id(Trade_Url+":id/super_mode_list_supplierName_tv")[n1].get_attribute("text")
        # print "com_name"+bytes(n1)+":"+bytes(base_name1)
        print n1
        print base_name1
        print op.eq(base_name1,base_name)
        #对比每一列表的基地名称，找到后点击该列表的“产品一览”按钮，遇到找不到的元素、索引超范围则重新再下滑动
        if op.eq(base_name1,base_name):
            try:
                base_name_in = driver.find_elements_by_id(Trade_Url+":id/super_mode_list_supplierName_tv")[n1].get_attribute("text")
                print base_name_in
                base_name_position = driver.find_elements_by_id(Trade_Url+":id/super_mode_list_supplierName_tv")[n1].location
                print base_name_position
                driver.find_elements_by_id(Trade_Url + ":id/super_mode_list_centerBtn_tv")[n1].click()
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
        driver.swipe(430, 1700, 430, 1175, 1000)

# 点击-产品一览-按钮
# driver.find_elements_by_id(url+":id/super_mode_list_centerBtn_tv")[0].click()









































