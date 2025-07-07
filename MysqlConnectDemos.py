#-*-coding:utf-8-*-

import mysql.connector
from auto_test_log_demo import *


class mysqlConn(object):

    def __init__(self):
        # 方法一：连接数据库（简约法）
        self.cnn = mysql.connector.connect(user='root', passwd='root', database='onlty')
        logger.debug('mysql online completed!')
        self.cursor = self.cnn.cursor()
        logger.debug('get cursor completed!')


    def deputesale(self):
        # 执行mysql语句
        self.cursor.execute("select mou,drop_off,text from risk_invoice;")
        logger.debug('execute mysql database completed!')
        # 使用fetchall()方法获取所有数据
        data = self.cursor.fetchall()
        logger.debug("Database information : %s" % bytes(data))
        # 获取数据表条数
        el_len = data.__len__()
        logger.debug('There are : %s data' % el_len)

    def one_price_order_params(self):
        # 执行mysql语句
        self.cursor.execute("select * from order_params;")
        logger.info('execute mysql database order_params completed!')
        # 使用fetchall()方法获取所有数据
        order_params = self.cursor.fetchall()
        logger.info("Database information : %s" % order_params)
        # 获取数据表条数
        el_len_list = order_params.__len__()
        el_len_line = order_params[el_len_list-1].__len__()
        logger.info('There are : %s data list' % el_len_list)
        logger.info('There are : %s data line' % el_len_line)
        return order_params

    def one_price_order_apply(self):
        # 执行mysql语句
        self.cursor.execute("select * from order_apply;")
        logger.info('execute mysql database order_apply completed!')
        # 使用fetchall()方法获取所有数据
        order_apply_data = self.cursor.fetchall()
        logger.info("Database information : %s" % order_apply_data)
        # 获取数据表条数
        el_len_list = order_apply_data.__len__()
        el_len_line = order_apply_data[el_len_list-1].__len__()
        logger.info('There are : %s data list' % el_len_list)
        logger.info('There are : %s data line' % el_len_line)
        return order_apply_data

    def one_price_examine_cargo(self):
        # 执行mysql语句
        self.cursor.execute("select * from examine_cargo_info;")
        logger.info('execute mysql database examine_cargo_info completed!')
        # 使用fetchall()方法获取所有数据
        examine_cargo_data = self.cursor.fetchall()
        logger.info("Database information : %s" % examine_cargo_data)
        # 获取数据表条数
        el_len_list = examine_cargo_data.__len__()
        el_len_line = examine_cargo_data[el_len_list-1].__len__()
        logger.info('There are : %s data list' % el_len_list)
        logger.info('There are : %s data line' % el_len_line)
        return examine_cargo_data

    def close_door(self):
        # 关闭游标连接
        self.cursor.close()
        # 关闭数据库连接
        self.cnn.close()

if __name__=='__main__':
    run = mysqlConn()
    # run.one_price_order_params()
    # run.one_price_order_apply()
    # run.one_price_examine_cargo()
