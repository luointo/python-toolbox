# -*- coding: utf-8 -*-
__author__ = 'luointo'


import pymysql

cnn = pymysql.connect(host='127.0.0.1',  # IP
                      user='root',  # 用户名
                      password='root',  # 密码
                      port=3306,  # 端口号
                      charset='utf8')  # 注意是utf8不是utf-8
# 使用cursor()方法获取操作游标
cursor = cnn.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
result = cursor.fetchone()
print("Database version : %s " % result)
