# -*- coding: utf-8 -*-
__author__ = 'luointo'

from xlrd import open_workbook
from xlutils.copy import copy

"""
excel文件追加内容
"""

r_xls = open_workbook("test.xls")  # 读取excel文件
row = r_xls.sheets()[0].nrows  # 获取已有的行数
excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
table = excel.get_sheet(0)  # 获取要操作的sheet
# 对excel表追加一行内容
table.write(row, 0, '内容1')  # 括号内分别为行数、列数、内容
table.write(row, 1, '内容2')
table.write(row, 2, '内容3')
excel.save("test.xls")  # 保存并覆盖文件
