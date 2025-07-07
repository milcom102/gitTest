#-*-coding:utf-8-*-

import mysql.connector
# import mysql.connector



# 方法一：连接数据库（简约法）
# buffered游标适用于多个小结果集的查询，且多个结果集之间的数据需要一起使用，查询时取方法(fetchone(),fetchall())返回的是缓存区中的行
cnn = mysql.connector.connect(user='root', passwd='Aa123456', database='john', buffered=True)
# 方法二：连接数据库（用使用关键字方法，如果出现游标异常问题添加buffered=True参数）
# cnn = mysql.connector.connect(host='127.0.0.1',port=3306,user='root', passwd='root', database='ORDER',charset='utf8')
# cnn = mysql.connector.connect(user='root', passwd='root', database='ORDER',buffered = True)
# 方法三：连接数据库（使用字典进行连接参数的管理）
# 普通的操作无论是fetchall()还是fetchone()都是先将数据载入到本地再进行计算，大量的数据会导致内存资源消耗光。解决办法是使用SSCurosr光标来处理。
# config = {
#           'host':'127.0.0.1',
#           'port':3306,
#           'user':'root',
#           'password':'root',
#           'database':'onlty',
#           'charset':'utf8'
#          'cursorclass':'mysql.connector.cursor.SSCursor'
#           }
# conn = mysql.connect(**config)

# 使用cursor()方法获取操作游标,
cursor = cnn.cursor()

# 执行mysql语句
# cursor.execute("select version()") #查看数据库版本号
cursor.execute("SELECT * FROM john.student;")

# sql = """CREATE TABLE EMPLOYEE(
#          FIRST_NAME CHAR(20) NOT NULL,
#          LAST_NAME CHAR(20),
#          AGE INT,
#          SEX CHAR(1)
#          INCOME FLOAT)
#         """
# cursor.execute(sql)

# 如果没有设置自动提交事务，则这里需要手动提交一次
# cnn.commit()
# 设置自动提交事务
# cnn.autocommit(1)
# cnn.autocommit(True)

# 使用fetchone()方法获取一条数据
# data = cursor.fetchone()

# 使用fetchall()方法获取所有数据
data = cursor.fetchall()

# 使用fetchmany(2)方法获取2条数据,使用该方法时，头connect()方法参数必须带有buffered=True参数
# 原因是nonbuffered游标不从服务器获取数据，而是直接调用了某个获取数据行的方法，在使用nonbuffered游标时，
# 必须确保取出的结果是结果集中的所有才行，才能再用同一连接指向性其他语句，否则报错InternalError(Unread result found)
# data = cursor.fetchmany(2)

# 使用eval()方法把unicode变为中文输出
# data = eval("u"+"\'"+data[0][2]+"\'")
# print isinstance(data[0][2],int)
# 使用fetchmany(self, size=None) 接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据


# 获取数据表条数
el_len = data.__len__()


print(el_len)
# str1.append(data[0][1])
# tip = data[0][2]
print("Database information : %s" % data)
# print tip
# 发送错误时会滚
# cnn.rollback()
# 关闭游标连接
cursor.close()
# 关闭数据库连接
cnn.close()