# -*- coding: utf-8 -*-
__author__ = 'luointo'

# DictWriter
# 使用DictWriter类，可以写入字典形式的数据，同样键也是标头（表格第一行）

import csv

headers = ['name', 'age']

data = [
    {'name': 'Bob', 'age': 23},
    {'name': 'Jerry', 'age': 44},
    {'name': 'Tom', 'age': 15}
]

filename = "test.csv"
with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)  # 标头在这里传入，作为第一行数据
    writer.writeheader()
    for row in data:
        writer.writerow(row)
