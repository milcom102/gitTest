#-*-coding:utf-8-*-


import sys
import requests
import json
import operator as op
from time import sleep
from auto_test_log_demo import *
import ssl

# 编码类型
type = sys.getfilesystemencoding()
# 文件头参数设置-运营后台
# 演示权限
autoriz = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTQ3MTI2OTcsImRhdGEiOnsidXNlciI6IjEifSwiaWF0IjoxNTU0MTA3ODk3fQ.StgUE6oVrIkj4gOAEBhmkWHDbADLubzEH0n-AV1r1tU"
# 开发权限
# autoriz ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTM3Mzc3OTcsImRhdGEiOnsidXNlciI6IjEifSwiaWF0IjoxNTUzMTMyOTk3fQ.YBvFTo_A_72qi3krc0ZKy86BybirK6jS04zBP1YkSfE"

autoriz_headers = {"Content-Type": "application/json", "Authorization": autoriz}

# 文件头参数设置-商城与基地
header = {"Content-Type": "application/json"}



class BmsAutoTest:

    #初始化常量---------------------------------
    def __init__(self):

        # 会员认证申请生成的ID值
        self.MemberCertId = None
        # 风险单据申请ID值
        self.risk_apply_id = None
        # 交易产品上架申请ID
        self.getTradeApply_id = None

        # 停顿秒数设置
        self.SECONDS_LONG = 7
        self.SECONDS_SHORT = 3

        # 使用环境
        self.Evr = "https://api-demo.onlty.com/"  # 演示环境
        # self.Evr = "https://api.asc.dev.ad2o.com/"  # 测试环境

    def wwwtest(self):
        wwwtest_response = requests.get(url="https://api.onlty.com/",verify=False)
        print wwwtest_response.text

    # 演示环境https协议测试样板
    def getTrade_Detail_Bms(self):
        print u"----------获取交易详情-运营后台-----------"
        data_getTrade_Detail_Bms = '{"id":322}'
        url_getTrade_Detail = self.Evr + "bms/shop/product/trade/getTradeApply"
        data_getTrade_Detail_Bms_json = json.loads(data_getTrade_Detail_Bms)
        data_getTrade_Detail_Bms_response = requests.post(url=url_getTrade_Detail, json=data_getTrade_Detail_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        print data_getTrade_Detail_Bms_response.text

    def getTradeApplys_Bms(self,id,supplier):
        print u"----------获取交易产品上架申请列表和ID-运营后台-----------"
        data_getTrade_Detail_Bms = '{"draw": 1,"start": '+id+',"length": -1}'
        url_getTrade_Detail = self.Evr + "bms/shop/product/trade/getTradeApplys"
        data_getTrade_Detail_Bms_json = json.loads(data_getTrade_Detail_Bms)
        data_getTrade_Detail_Bms_response = requests.post(url=url_getTrade_Detail, json=data_getTrade_Detail_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        # print data_getTrade_Detail_Bms_response.text
        data_getTrade_Detail_Bms_response_json = json.loads(data_getTrade_Detail_Bms_response.text)
        flag = True
        num = 0
        try:
            while flag:
                getTradeApply_id = data_getTrade_Detail_Bms_response_json['data']['data'][num]['id']
                getTradeApply_status = data_getTrade_Detail_Bms_response_json['data']['data'][num]['trade']['status']
                getTradeApply_name = data_getTrade_Detail_Bms_response_json['data']['data'][num]['trade']['member']['name']
                # 5为提交状态
                if op.eq(getTradeApply_name, supplier) and getTradeApply_status == 5:
                    print '{%s, %s, %s}' % (getTradeApply_name, getTradeApply_status, getTradeApply_id)
                    self.getTradeApply_id = getTradeApply_id
                    flag = False
                else:
                    num += 1
            logger.info('getTradeApplys done')
        except IndexError:
            logger.info('getTradeApplys exception...')
            print "NoSuchElement"
