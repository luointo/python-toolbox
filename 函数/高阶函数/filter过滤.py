# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
filter过滤
用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

filter(function, iterable)
参数/返回值
    function – 过滤操作执行的函数
    iterable – 需要过滤的序列
    序列的每个元素作为参数传递给函数进行判，然后返回True或False，最后将返回True的元素放到新列表中
    Python 2.x中返回的是过滤后的列表, 而Python 3.x中返回到是一个filter类
"""


def is_odd(x):
    if x % 2 == 1:
        return True
    return False


list2 = [1, 2, 3, 4, 5, 6]
fil0 = filter(is_odd, list2)
print(fil0)
print(list(fil0))

# 匿名函数
fil = filter(lambda x: x % 2 == 0, list2)
print(list(fil))
