# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
实例化方法，通过类创建实例时，自动触发执行

__init__是用来初始化一个实例的(initializer)

__init__所接收的第一个参数是self
当我们调用__init__的时候，实例已经存在，因此__init__接受self作为第一个参数并对该实例进行必要的初始化操作。
这也意味着__init__是在__new__之后被调用的。

__init__不能有返回值
"""


class MyClass1:
    def __init__(self):
        """
        类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
        """
        print("init")


class MyClass2:
    def __init__(self, a, b):
        """
        带参数
        """
        self.a = a
        self.b = b

        print(self.a, self.b)


my1 = MyClass1()
my2 = MyClass2(1, 2)
my3 = MyClass2(a="a", b="b")
