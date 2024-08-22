# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 幂运算

这些都是算术运算方法，需要你自己为类设计具体运算代码。有些Python内置数据类型，比如int就带有这些方法。Python支持运算符的重载，也就是重写。
"""


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1)
print(v2)
print(v1 + v2)
