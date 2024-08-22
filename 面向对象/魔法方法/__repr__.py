# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
__repr__

这个方法的作用和__str__()很像，两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。通常两者代码一样
"""


class Foo:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "this is %s" % self.name

    # __repr__ = __str__


obj = Foo("a")
s = obj.__str__()
print(s)
