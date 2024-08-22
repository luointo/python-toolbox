# -*- coding: utf-8 -*-
__author__ = 'luointo'

# reader只能被遍历一次。由于reader是可迭代对象，可以使用next方法一次获取一行

import csv

# reader
filename = "test.csv"
with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("行号：{}  内容：{}".format(reader.line_num, row))

"""
import csv
reader = csv.reader(open('test.csv', 'r', encoding='utf-8'))
print(reader.__next__())

reader = csv.reader(open('test.csv', 'r', encoding='cp936'))  # for excel
"""
