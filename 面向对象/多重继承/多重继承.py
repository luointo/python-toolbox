# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
总之前人留下的经验就是：保持一致性。要不全部用类名调用父类，要不就全部用 super，不要一半一半。

Python类分为两种，一种叫经典类，一种叫新式类。两种都支持多继承。

考虑一种情形，B继承于A，C继承于A和B, 但C需要调用父类的init()函数时，前者会导致父类A的init()函数被调用2次，这是不希望看到的。
而且子类要显式地指定父类，不符合DRY原则。

采用新式类，要求最顶层的父类一定要继承于object，这样就可以利用super()函数来调用父类的init()等函数，
每个父类都执行且执行一次，并不会出现重复调用的情况。而且在子类的实现中，不用到处写出所有的父类名字，符合DRY原则。
"""


# 经典类
class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')


class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C')


# 新式类
class NewA:
    def __init__(self):
        print('NewA')


class NewB(NewA):
    def __init__(self):
        super(NewB, self).__init__()
        print('NewB')


class NewC(NewB, NewA):
    def __init__(self):
        super(NewC, self).__init__()
        print('NewC')


if __name__ == '__main__':
    # c = C()
    newC = NewC()
