# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
"""


class Student:
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.name = '小明'  # 动态给实例绑定一个属性
# print(s.name)

"""
给实例绑定一个方法
from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果

但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student() # 创建新的实例
s2.set_age(25) # 尝试调用方法
"""


# 给所有实例都绑定方法，可以给class绑定方法, 给class绑定方法后，所有实例均可调用
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s2 = Student()
s2.set_score(60)
print(s2.score)
