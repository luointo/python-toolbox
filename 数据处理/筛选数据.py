# -*- coding: utf-8 -*-
__author__ = 'luointo'


"""
如何在列表，字典，集合中根据条件筛选数据？
"""

# 过滤掉列表[1, 5, -3, -2, 6, 0, 9]中的负数
# 传统方法
data = [1, 5, -3, -2, 6, 0, 9]
res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)

# 使用filter函数
data = [1, 5, -3, -2, 6, 0, 9]
res = list(filter(lambda x: x >= 0, data))
print(res)

# 列表解析
data = [1, 5, -3, -2, 6, 0, 9]
res = [x for x in data if x >= 0]
print(res)

