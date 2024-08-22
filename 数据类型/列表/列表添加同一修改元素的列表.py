# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 列表添加同一修改元素的列表

"""
正确方法
使用copy后会把列表复制一份
"""
a = [1, 2, 3]
b = [4, 5]

c = b.copy()
c[1] = 6
a.append(c)

c = b.copy()
c[1] = 7
a.append(c)

print(a)
print(b)

"""
错误做法
直接修改原列表，多次修改的会是内存同一个地址
a = [1, 2, 3]
b = [4, 5]

b[1] = 6
a.append(b)

b[1] = 7
a.append(b)

print(a)
print(b)
"""
