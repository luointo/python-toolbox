# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
map函数：map()函数接收俩个参数，一个是函数，一个是Iterable(可迭代对象)；
map将传入的函数依次作用到可迭代对象中的每个元素，并且把结果作为新的可迭代对象返回

根据提供的函数对指定序列做映射, 并返回映射后的序列

map(function, iterable, ...)
参数/返回值
    function – 函数, 序列中的每个元素需要执行的操作, 可以是匿名函数
    iterable – 一个或多个序列
    Python 2.x中返回列表, Python 3.x中返回map类

"""


# 调用外部函数
def square(x):
    return x ** 2


res = map(square, [1, 2, 3, 4])
print(res)
print(list(res))

# 使用匿名函数
res1 = map(lambda x: x * 3, [1, 2, 3, 4])
print(list(res1))

# 使用内置函数
res2 = map(str, [2, 3, 4, 5])
print(list(res2))

# 多个序列
res3 = map(lambda x, y: x * y, [1, 2, 3, 4], [3, 2, 4, 1])
print(list(res3))
