# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
__new__是用来创造一个类的实例的（constructor）

__new__所接收的第一个参数是cls，
这是因为当我们调用__new__的时候，该类的实例还并不存在（也就是self所引用的对象还不存在），所以需要接收一个类作为参数，从而产生一个实例。

__new__函数直接上可以返回别的类的实例
"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("new")
        return "new obj"


my = MyClass()
print(my)
