# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
读取文件的指定行
"""

import linecache

line = linecache.getline("demo.txt", 3)  # 读取第3行
print(line)
