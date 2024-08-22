# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 单列读取
import xlrd

xls = xlrd.open_workbook('test.xls')
sheet = xls.sheet_by_name('Sheet1')
rowA = sheet.row_values(0)  # 第一行
colA = sheet.col_values(0)  # 第一列

print(rowA)
print(colA)
