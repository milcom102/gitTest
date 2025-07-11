#-*-coding:utf-8-*-
import logging
from logging import handlers

# 设置logging日志
# logging.basicConfig(
#     format='%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s',
#     level=logging.DEBUG,
#     filemode='a',
#     filename='logging_test.log'
# )
#
# logging.debug('debug information')
# logging.warning(u'警告日志')
# logging.info(u'info信息')
# logging.error(u'error信息')
# logging.critical(u'critial信息')


class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)# 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()# 创建往屏幕上输出
        sh.setFormatter(format_str)# 设置屏幕上显示的格式

        # 往文件里写入
        # 指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh)#把对象加到logger里
        self.logger.addHandler(th)

if __name__ == '__main__':
    log = Logger('all.log',level='warning')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning(u'警告')
    log.logger.error(u'报错')
    log.logger.critical(u'严重')
    Logger('error.log',level='error').logger.error('error')






















