# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
列出类或对象中的所有成员！非常重要和有用的一个属性，Python自建，无需用户自己定义
"""


class Province:
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    @staticmethod
    def func():
        print('func')


# 获取类的成员
print(Province.__dict__)

# 获取 对象obj1 的成员
obj1 = Province('HeBei', 10000)
print(obj1.__dict__)

# 获取 对象obj2 的成员
obj2 = Province('HeNan', 3888)
print(obj2.__dict__)
