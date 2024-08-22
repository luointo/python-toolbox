# -*- coding: utf-8 -*-
__author__ = 'luointo'

from collections.abc import Iterable

"""
迭代器
可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str, bytes等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
"""

# 使用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('string data', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))  # False

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

