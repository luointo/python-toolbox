# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
zip
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
函数有一个参数, 接受一个或多个序列
函数利用*号操作符，可以将元组解压为列表
zip方法在Python 2.x中返回一个列表, 在Python 3.x中返回一个对象

zip([iterable, ...])
"""

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [4, 5, 6, 7]

zip1 = zip(a, b)
print(zip1)
print(list(zip1))

# 两个列表不同元素个数, 元素个数与最短的列表一致
zip2 = zip(a, c)
print(list(zip2))

# `*`号操作符，可以将元组解压为列表
a1, c1 = zip(*zip(a, c))
print(a1)
print(c1)
