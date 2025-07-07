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

    def confirmTradeApply_Bms(self):
        print u"----------确认交易产品上架申请-运营后台-----------"
        data_confirmTradeApply_Bms = '{"id":%s}' % self.getTradeApply_id
        url_confirmTradeApply = self.Evr + "bms/shop/product/trade/confirmTradeApply"
        data_confirmTradeApply_Bms_json = json.loads(data_confirmTradeApply_Bms)
        data_confirmTradeApply_Bms_response = requests.post(url=url_confirmTradeApply, json=data_confirmTradeApply_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        logger.info(data_confirmTradeApply_Bms_response.text)
        logger.info('confirmTradeApply done')

    def getVoucher_Bms(self):
        print u"----------查看付款凭证-运营后台-----------"
        data_getVoucher_Bms = u'{"id":"%s"}' % self.voucher_id
        print data_getVoucher_Bms
        url_getVoucher = self.Evr + "bms/finance/voucher/getVoucher"
        data_getVoucher_Bms_json = json.loads(data_getVoucher_Bms)
        data_getVoucher_Bms_response = requests.post(url=url_getVoucher, json=data_getVoucher_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        print data_getVoucher_Bms_response.text


    def getVouchers_Bms(self,stall_name):
        print u"----------查看和获取付款凭证列表-运营后台-----------"
        data_getVouchers_Bms = '{"draw": 1,"start": 590,"length": -1}'
        url_getVouchers = self.Evr + "bms/finance/voucher/getVouchers"
        data_getVouchers_Bms_json = json.loads(data_getVouchers_Bms)
        data_getVouchers_Bms_response = requests.post(url=url_getVouchers, json=data_getVouchers_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        print data_getVouchers_Bms_response.text
        data_getVouchers_Bms_response_json = json.loads(data_getVouchers_Bms_response.text)
        flag = True
        num = 0
        while flag:
            member_name = data_getVouchers_Bms_response_json['data']['data'][num]['member']['name']
            status = data_getVouchers_Bms_response_json['data']['data'][num]['status']
            if op.eq(member_name, stall_name) and status == 15:
                self.voucher_id = data_getVouchers_Bms_response_json['data']['data'][num]['id']
                self.voucher_no = data_getVouchers_Bms_response_json['data']['data'][num]['voucher_no']
                order_shipping_no = data_getVouchers_Bms_response_json['data']['data'][num]['source_bill_no']
                print "{voucher_id:%s;voucher_no:%s;order_shipping_no:%s;status:%s}" % (self.voucher_id, self.voucher_no, order_shipping_no, status)
                flag = False
            else:
                num += 1

    def ReceiptPayment_Bms(self):
        print u"----------付款凭证-结款-运营后台-----------"
        data_ReceiptPayment_Bms = u'{"voucherNo":"%s"}' % self.voucher_no
        print data_ReceiptPayment_Bms
        url_ReceiptPayment = self.Evr + "bms/finance/voucher/receipt"
        data_ReceiptPayment_Bms_json = json.loads(data_ReceiptPayment_Bms)
        data_ReceiptPayment_Bms_response = requests.post(url=url_ReceiptPayment, json=data_ReceiptPayment_Bms_json,verify = False,
                                                  headers=autoriz_headers)
        print data_ReceiptPayment_Bms_response.text

    #proposer
    def GetMemberCertId_Bms(self,proposer):
        print u"----------获取会员认证申请人ID-运营后台-----------"
        data_AcceptanceList_Bms = '{"draw": 1,"start": 34,"length": -1}'
        url_AcceptanceList = self.Evr + "bms/member/certificate/getCerts"
        data_AcceptanceList_Bms_json = json.loads(data_AcceptanceList_Bms)
        data_AcceptanceList_Bms_response = requests.post(url=url_AcceptanceList, json=data_AcceptanceList_Bms_json,headers=autoriz_headers)
        print data_AcceptanceList_Bms_response.text
        data_AcceptanceList_Bms_response_json = json.loads(data_AcceptanceList_Bms_response.text)
        flag = True
        num = 0
        while flag:
            proposer_text = data_AcceptanceList_Bms_response_json['data']['data'][num]['name']
            if proposer_text == proposer:
                self.MemberCertId = data_AcceptanceList_Bms_response_json['data']['data'][num]['id']
                print "{get_id:%s;proposer_text:%s;proposer:%s}" % (self.MemberCertId, proposer_text, proposer)
                flag = False
            else:
                num += 1

    def AcceptCert_Bms(self):
        print u"----------受理会员认证申请-运营后台-----------"
        data_AAcceptCert_Bms = '{"id":%s}' % self.MemberCertId
        url_AcceptCert = self.Evr + "bms/member/certificate/acceptCert"
        data_AcceptCert_Bms_json = json.loads(data_AAcceptCert_Bms)
        data_AcceptCert_Bms_response = requests.post(url=url_AcceptCert, json=data_AcceptCert_Bms_json,
                                                         headers=autoriz_headers)
        print data_AcceptCert_Bms_response.text
        sleep(self.SECONDS_SHORT)

    def SignCert_Bms(self):
        print u"----------确认会员认证申请-运营后台-----------"
        data_SignCert_Bms = '{"id":%s}' % self.MemberCertId
        url_SignCert = self.Evr + "bms/member/certificate/SignCert"
        data_SignCert_Bms_json = json.loads(data_SignCert_Bms)
        data_SignCert_Bms_response = requests.post(url=url_SignCert, json=data_SignCert_Bms_json,
                                                         headers=autoriz_headers)
        print data_SignCert_Bms_response.text
        sleep(self.SECONDS_SHORT)

    def StopCert_Bms(self):
        print u"----------终止会员认证-运营后台-----------"
        data_SignCert_Bms = '{"id":%s}' % self.MemberCertId
        url_SignCert = self.Evr + "bms/member/certificate/stopCert"
        data_SignCert_Bms_json = json.loads(data_SignCert_Bms)
        data_SignCert_Bms_response = requests.post(url=url_SignCert, json=data_SignCert_Bms_json,
                                                         headers=autoriz_headers)
        print data_SignCert_Bms_response.text
        sleep(self.SECONDS_SHORT)

    def GetBills_Bms(self, proposer):
        print u"----------获取不采收风险单据列表申请人ID-运营后台-----------"
        data_GetBills_Bms = '{"draw": 1,"start": 3,"length": -1}'
        url_GetBills = self.Evr + "bms/finance/unharvest/getBills"
        data_GetBills_Bms_json = json.loads(data_GetBills_Bms)
        data_GetBills_Bms_response = requests.post(url=url_GetBills, json=data_GetBills_Bms_json, headers=autoriz_headers)
        print data_GetBills_Bms_response.text
        data_GetBills_Bms_response_json = json.loads(data_GetBills_Bms_response.text)
        flag = True
        num = 0
        try:
            while flag:
                self.risk_apply_id = data_GetBills_Bms_response_json['data']['data'][num]['id']
                risk_name = data_GetBills_Bms_response_json['data']['data'][num]['baseMember']['name']
                risk_status = data_GetBills_Bms_response_json['data']['data'][num]['status']
                risk_sheet_no = data_GetBills_Bms_response_json['data']['data'][num]['sheet_no']
                # 20为待平台受理状态
                if op.eq(risk_name,proposer) and risk_status == 20:
                    print '{%s, %s, %s, %s}' % (risk_name,risk_status,self.risk_apply_id,risk_sheet_no)
                    self.risk_apply_id = data_GetBills_Bms_response_json['data']['data'][num]['id']
                    print "{get_id:%s;risk_name:%s;risk_status:%s;risk_sheet_no:%s}" % (self.risk_apply_id, risk_name, risk_status,risk_sheet_no)
                    flag = False
                else:
                    num += 1
        except IndexError:
            print "NoSuchElement"

    def AcceptRiskApply_Bms(self):
        print u"----------受理不采收风险单据列表申请人ID-运营后台-----------"
        data_AcceptRiskApply_Bms = '{"id":%s}' % self.risk_apply_id
        url_AcceptRiskApply = self.Evr + "bms/finance/unharvest/accept"
        data_AcceptRiskApply_Bms_json = json.loads(data_AcceptRiskApply_Bms)
        data_AcceptRiskApply_Bms_response = requests.post(url=url_AcceptRiskApply, json=data_AcceptRiskApply_Bms_json,
                                                         headers=autoriz_headers)
        print data_AcceptRiskApply_Bms_response.text
        sleep(self.SECONDS_SHORT)

    def ConfirmRiskApply_Bms(self):
        print u"----------核实不采收风险单据列表申请人ID-运营后台-----------"
        data_ConfirmRiskApply_Bms = '{"id":%s}' % self.risk_apply_id
        url_ConfirmRiskApply = self.Evr + "bms/finance/unharvest/confirm"
        data_ConfirmRiskApply_Bms_json = json.loads(data_ConfirmRiskApply_Bms)
        data_ConfirmRiskApply_Bms_response = requests.post(url=url_ConfirmRiskApply, json=data_ConfirmRiskApply_Bms_json,
                                                         headers=autoriz_headers)
        print data_ConfirmRiskApply_Bms_response.text
        sleep(self.SECONDS_SHORT)

    def PaymentRiskApply_Bms(self):
        print u"----------转账不采收风险单据列表申请人ID-运营后台-----------"
        data_PaymentRiskApply_Bms = '{"id":%s}' % self.risk_apply_id
        url_PaymentRiskApply = self.Evr + "bms/finance/unharvest/transfer"
        data_PaymentRiskApply_Bms_json = json.loads(data_PaymentRiskApply_Bms)
        data_PaymentRiskApply_Bms_response = requests.post(url=url_PaymentRiskApply, json=data_PaymentRiskApply_Bms_json,
                                                         headers=autoriz_headers)
        print data_PaymentRiskApply_Bms_response.text
        sleep(self.SECONDS_SHORT)

    # def GetBills_Bms(self, proposer):
    #     print u"----------获取不采收风险单据列表申请人ID-运营后台-----------"
    #     data_GetBills_Bms = '{"draw": 1,"start": 3,"length": -1}'
    #     url_GetBills = "http://api.asc.dev.ad2o.com/bms/finance/unharvest/getBills"
    #     data_GetBills_Bms_json = json.loads(data_GetBills_Bms)
    #     data_GetBills_Bms_response = requests.post(url=url_GetBills, json=data_GetBills_Bms_json, headers=autoriz_headers)
    #     print data_GetBills_Bms_response.text
    #     data_GetBills_Bms_response_json = json.loads(data_GetBills_Bms_response.text)
    #     # flag = True
    #     num = 0
    #     proposer_status = data_GetBills_Bms_response_json['data']['data'][num]['id']
    #     print proposer_status
    #     proposer_name = data_GetBills_Bms_response_json['data']['data'][num]['baseMember']['name']
    #     print proposer_name
    #     # proposer_apply_id = data_GetBills_Bms_response_json['data']['data'][num]['status']
    #     # proposer_sheet_no = data_GetBills_Bms_response_json['data']['data'][num]['sheet_no']



if __name__=='__main__':
    Run = BmsAutoTest()

    # Run.getTrade_Detail_Bms()
    # Run.confirmTradeApply_Bms()
    # Run.ReceiptPayment_Bms()
    # Run.GetMemberCertId_Bms(u"无良印品")
    # Run.GetBills_Bms(u'v3沃农基地')
    # Run.AcceptRiskApply_Bms()
    # Run.ConfirmRiskApply_Bms()
    # Run.PaymentRiskApply_Bms()
    # Run.getTradeApplys_Bms(u'330',u"沃沃基地班")
    # Run.confirmTradeApply_Bms()
    # Run.getVouchers_Bms(u"企业档口法定名")
    # Run.ReceiptPayment_Bms()

    Run.wwwtest()