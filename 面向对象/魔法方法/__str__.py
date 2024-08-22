# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
如果一个类中定义了__str__()方法，那么在打印对象时，默认输出该方法的返回值。这也是一个非常重要的方法，需要用户自己定义。

下面的类，没有定义__str__()方法，打印结果是：<__main__.Foo object at 0x000000000210A358>
"""


class Foo:
    pass

    def __str__(self):
        return 'jack'


obj = Foo()
print(obj)
