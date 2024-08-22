# -*- coding: utf-8 -*-
__author__ = 'luointo'

import csv

# 使用数字和字符串的数字都可以
data = [['name', 'age'],
        ['Bob', 14],
        ['Tom', 23],
        ['Jerry', '18']]

filename = "test.csv"
# 如果不指定newline='',则每写入一行将有一空行被写入
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)  # 一行行的写入数据
        # writer.writerows(data)  # 一次写入多行

"""
# 简写一行
import csv
info = []
writer = csv.writer(open('ret.csv', 'w', newline='', encoding='utf-8'))
writer = csv.writer(open('ret.csv', 'w', newline='', encoding='utf_8_sig'))  # BOM utf-8, 这样excel不乱码
writer.writerows(info)
"""