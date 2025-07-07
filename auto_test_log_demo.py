#-*-coding:utf-8-*-
import logging
from logging import handlers

# 设置logging日志
# 注意：使用其他的中间设备的运行log也都记录下来。如：appium
logging.basicConfig(
    format='%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s',
    level=logging.WARN,
    filemode='a',
    filename='logging_test.log'
)

# logging.debug('debug information')
# logging.warning(u'警告日志')
# logging.info(u'info信息')
# logging.error(u'error信息')
# logging.critical(u'critial信息')
# filemode = 'a'
# filename = 'logging_test1.log'
fmt = '%(asctime)s-%(levelname)s:%(message)s'
format_str = logging.Formatter(fmt)
sh = logging.StreamHandler()
sh.setFormatter(format_str)

logger = logging.getLogger(__name__)
# 定义输出logo级别
logger.setLevel(logging.WARN)
logger.addHandler(sh)
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')