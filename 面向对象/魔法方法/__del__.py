# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
析构方法，当对象在内存中被释放时，自动触发此方法。

注：此方法一般无须自定义，因为Python自带内存分配和释放机制，除非你需要在释放的时候指定做一些动作。
析构函数的调用是由解释器在进行垃圾回收时自动触发执行的

"""


class Foo:

    def __del__(self):
        print("我被回收了！")


obj = Foo()
del obj
