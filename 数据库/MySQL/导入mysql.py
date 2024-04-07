# -*- coding: utf-8 -*-
__author__ = 'luointo'

import pymysql
import os
from time import time

start = time()

dir_path = r'/vagrant/mysqlData/'
list_dirs = os.walk(dir_path)
dic_sql = {}
for root, dirs, files in list_dirs:
    for d in dirs:
        # print(os.path.join(root, d))
        continue
    for f in files:
        f_len = f.find('_', 13)
        dic_sql[f[0:f_len]] = os.path.join(root, f)

# 建立和数据库系统的连接
conn = pymysql.connect(
    host='192.168.1.77',
    user='root',
    passwd='root',
    charset='UTF8')
# 获取操作游标
cur = conn.cursor()

for db, sql_path in dic_sql.items():
    drop_sql = r'drop database if exists {}'.format(db)
    create_sql = r'create database if not exists {} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'.format(db)
    cur.execute(drop_sql)
    cur.execute(create_sql)
    dumpcmd = "mysql -uroot -proot {0} < {1}".format(db, sql_path)
    os.system(dumpcmd)

# 关闭游标
cur.close()
# 向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
conn.commit()
# 关闭到数据库的连接，释放数据库资源
conn.close()

stop = time()

print(str(stop - start) + "秒")
