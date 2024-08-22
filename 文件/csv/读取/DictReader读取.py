# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
DictReader
使用DictReader可以像操作字典那样获取数据，把表的第一行（一般是标头）作为key。可访问每一行中那个某个key对应的数据
"""

import csv

filename = "test.csv"
with open(filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("行号：{}  内容：name={}, age={}".format(reader.line_num, row["name"], row["age"]))
