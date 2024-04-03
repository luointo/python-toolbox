# -*- coding: utf-8 -*-
__author__ = 'luointo'

from functools import reduce

"""
reduce
函数会对参数序列中元素进行累积
函数将集合中的所有数据进行下列操作：用传给educe中的函数function先对集合中的第1、2个元素进行操作，
得到的结果再与第三个数据用function函数运算，最后得到一个结果

在Python3中，reduce函数已经被从全局名字空间里移除了，
它现在被放置在fucntools模块里，如果想要使用它，则需要通过引入functools模块来调用reduce函数

reduce(function, iterable[, initializer])
参数/返回值
    function – 函数, 序列中的每个元素需要执行的操作, 可以是匿名函数
    iterable – 需要执行操作的序列
    initializer – 可选，初始参数
    最后返回函数的计算结果, 和初始参数类型相同
"""


# 求元素的和
def f(x, y):
    return x + y


list1 = [1, 2, 3, 4]
red = reduce(f, list1)
print(red)

red2 = reduce(f, list1, 2)
print(red2)

# 匿名函数
red3 = reduce(lambda x, y: x * y, list1)
print(red3)

red4 = reduce(lambda x, y: x * y, list1, 3)
print(red4)

red5 = reduce(lambda x, y: x + y, ['1', '2', '3', '4'], '数字: ')
print(red5)
