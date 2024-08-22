# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
取值、赋值、删除这“三剑客”的套路，在Python中，我们已经见过很多次了，比如前面的@property装饰器。

Python中，标识符后面加圆括号，通常代表执行或调用方法的意思。
而在标识符后面加中括号[]，通常代表取值的意思。
Python设计了__getitem__()、__setitem__()、__delitem__()这三个特殊成员，用于执行与中括号有关的动作。它们分别表示取值、赋值、删除数据。

a = 标识符[]　： 　　执行__getitem__方法
标识符[] = a  ： 　　执行__setitem__方法
del 标识符[]　： 　　执行__delitem__方法
"""


class Foo:

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'jack'  # 自动触发执行 __setitem__
del obj['k1']  # 自动触发执行 __delitem__
