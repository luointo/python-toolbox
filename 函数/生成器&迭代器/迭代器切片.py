# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
使用标准库中的 itertools.islice，它能返回一个迭代对象切片的生成器
"""

from itertools import islice

with open("test.log", "r") as f:
    for line in islice(f, 100, 300):
        print(line.strip())

    # data = islice(f, 500)  # 0到500行
    # print(data)

    # islice(f, 100, None)  # 100到末尾
