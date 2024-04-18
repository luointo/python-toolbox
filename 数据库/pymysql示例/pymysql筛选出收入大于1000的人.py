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
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % 1000
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
