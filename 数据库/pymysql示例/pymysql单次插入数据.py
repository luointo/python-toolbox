# -*- coding: utf-8 -*-
__author__ = 'luointo'


import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',  # IP
                     user='root',  # 用户名
                     password='root',  # 密码
                     port=3306,  # 端口号
                     charset='utf8',
                     database="demo")  # 注意是utf8不是utf-8

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql_1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
        ('Mac', 'Mohan', 20, 'M', 2000)

sql_2 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
        ('Johon', 'Snow', 28, 'M', 9000)
try:
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
