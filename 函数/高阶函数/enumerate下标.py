# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
enumerate
用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
Python 2.3以上版本可用，2.6添加start参数

enumerate(sequence, [start=0])
参数/返回值
    sequence – 一个序列、迭代器或其他支持迭代对象
    start – 下标起始位置
    函数返回enumerate(枚举) 对象
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
sea1 = enumerate(seasons)
print(sea1)
print(list(sea1))

# 自定义起始索引
sea2 = list(enumerate(seasons, start=1))
print(sea2)

# 普通的 for 循环
i = 0
for element in seasons:
    print(i, seasons[i])
    i += 1

# for 循环使用 enumerate
for i, ele in enumerate(seasons):
    print(i, ele)
