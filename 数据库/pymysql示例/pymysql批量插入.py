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

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES (%s,%s,%s,%s,%s)"
# 区别与单条插入数据，VALUES ('%s', '%s',  %s,  '%s', %s) 里面不用引号

val = (('li', 'si', 16, 'F', 1000),
       ('Bruse', 'Jerry', 30, 'F', 3000),
       ('Lee', 'Tomcat', 40, 'M', 4000),
       ('zhang', 'san', 18, 'M', 1500))
try:
    # 执行sql语句
    cursor.executemany(sql, val)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
