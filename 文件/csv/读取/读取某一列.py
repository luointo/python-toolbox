# -*- coding: utf-8 -*-
__author__ = 'luointo'

import csv

# test.csv
"""
No.,Name,Age,Score
1,Apple,12,98
2,Ben,13,97
3,Celia,14,96
4,Dave,15,95
"""

filename = "test.csv"
with open(filename, "r") as f:
    reader = csv.reader(f)
    column = [row[1] for row in reader]  # 读取第三列
    print(column)


# 用列名来读取
"""
import csv

filename = "test.csv"
with open(filename, "r") as f:
    reader = csv.DictReader(f)
    column = [row["Age"] for row in reader]
    print(column)
"""