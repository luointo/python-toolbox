# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
采用super()方式时，会自动找到第一个多继承中的第一个父类，但是如果还想强制调用其他父类的init()函数或两个父类的同名函数时，就要用老办法了。
"""


class Person:
    name = ""
    sex = ""

    def __init__(self, name, sex='U'):
        print('Person')
        self.name = name
        self.sex = sex


class Consumer:
    def __init__(self):
        print('Consumer')


class Student(Person, Consumer):
    def __init__(self, score, name):
        # print(Student.__bases__)
        super(Student, self).__init__(name, sex='F')
        Consumer.__init__(self)
        self.score = score


s1 = Student(90, 'abc')
print(s1.name, s1.score, s1.sex)
