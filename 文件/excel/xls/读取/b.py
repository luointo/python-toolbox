# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 全部读取
import xlrd

xls = xlrd.open_workbook('test.xls')
sheet = xls.sheet_by_name('Sheet1')
data = [sheet.row_values(x) for x in range(sheet.nrows)]

print(data)
