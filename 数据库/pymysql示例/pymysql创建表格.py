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

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
result1 = cursor.fetchall()
sql_2 = "SHOW TABLES"
cursor.execute(sql_2)
result2 = cursor.fetchall()
print('result1:', result1)
print('result2:', result2)
# 关闭数据库连接
db.close()
