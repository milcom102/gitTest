#-*-coding:utf-8-*-
from appium import webdriver
from time import sleep
import re
import operator as op

class EvrConfig():


# app的http地址
url = "trade.sale.onlty.com"

# 测试环境地址，前面的加u字母，代表是Unicode型字符串，默认输入的是bytes型字符串
Evr_http = u"http://api.asc.dev.ad2o.com/v3/trade/"

# 自动化设置的环境名称
Evr_name = "v3_test"

# 物理android设备系统的包名
sys_url = "com.android.packageinstaller"


driver.find_element_by_id(url+":id/damain_name_tv").send_keys(Evr_name)
driver.find_element_by_id(url+":id/damain_path_tv").send_keys(Evr_http)
driver.find_element_by_id(url+":id/damain_add_tv").click()

# 选择测试环境地址ad2o:获取相同ID列表list后，匹配列表是否设置环境地址，选择对应的列表项（如[0]）
el_len = driver.find_elements_by_id(url+":id/market_list_number_2_02").__len__()
print "elements list length:",el_len
flag = True
for i in range(el_len):
    Evr_add = driver.find_elements_by_id(url+":id/market_list_number_2_02")[i].text
    print Evr_add
    print Evr_http
    print type(Evr_add)
    print type(Evr_http)
    print op.eq(Evr_http,Evr_add)

    if re.match(Evr_http,Evr_add):
        driver.find_elements_by_id(url + ":id/market_list_number_2_02")[i].click()
        break
        print "if"
    else:
        print "else"
        continue