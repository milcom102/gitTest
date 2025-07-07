import yagmail
from auto_test_log_demo import *
from time import sleep

class SendEmail(object):

    def send_email(self,username,to):
        # username = 'xieyexiang@ad2o.com'
        password = "Aa123456"

        mail_server = 'smtp.ad2o.com'

        m = yagmail.SMTP(user=username,password=password,host=mail_server)

        to = [to]
        cc = []
        m.send(to=to,cc=cc,subject='subject_test1',contents="contents_testing1",attachments=r'logging_test.log')
        sleep(5)
        logger.info("send Email completed")
