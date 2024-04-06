# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os
import time

db_host = '127.0.0.1'
db_user = 'root'
db_pwd = 'e&d#5u1%a7#1s/2k101'

# 要备份的数据库
db_names = [
    'huayu_sales_bj',
    'huayu_sales_cd',
    'huayu_sales_gz',
    'huayu_sales_heb',
    'huayu_sales_hs',
    'huayu_sales_hz',
    'huayu_sales_jn',
    'huayu_sales_sh',
    'huayu_sales_sy',
    'huayu_sales_sz',
    'huayu_sales_tj',
    'huayu_sales_xa',
    'huayu_sales_zb',
]

# 备份的路径
backup_path = '/home/zhangdayang/mysqlDataBackups/' + time.strftime("%Y%m%d_%H%M%S", time.localtime())
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

for db_name in db_names:
    db_name_path = db_name + '_' + time.strftime('%Y%m%d_%H%M%S', time.localtime())
    dumpcmd = "mysqldump -u" + db_user + " -p'" + db_pwd + "' " + db_name + " > " + backup_path + "/" + db_name_path + ".sql"
    os.system(dumpcmd)
