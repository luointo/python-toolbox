# -*- coding: utf-8 -*-
__author__ = 'luointo'


class MyClass:

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = "c"

    def test(self):
        for i, j in vars(self).items():
            print(i, j)


obj = MyClass()
obj.test()
