# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
高阶函数

一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（若返回值为该函数本身，则为递归），满足其一则为高阶函数

一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
"""


# 参数为函数
def bar1():
    print("in the bar..")


def foo1(func):
    # 函数foo1()为高阶函数, 函数bar1作为foo1的参数传入
    func()
    print("in the foo..")


foo1(bar1)


# 返回值为函数
def bar2():
    print("in the bar..")


def foo2(func):
    # 函数foo2()为高阶函数, 函数bar2作为foo2的返回值
    print("in the foo..")
    return bar2


res = foo2(bar2)
res()
