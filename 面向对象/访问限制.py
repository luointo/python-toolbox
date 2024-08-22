# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
成员保护和访问限制

在Python中，如果要让内部成员不被外部访问，可以在成员的名字前加上两个下划线__，这个成员就变成了一个私有成员（private）。
私有成员只能在类的内部访问，外部无法访问

外部如果要对__age进行访问和修改呢？在类的内部创建外部可以访问的get和set方法

那么，以双下划线开头的数据成员是不是一定就无法从外部访问呢？
其实也不是！本质上，从内部机制原理讲，外部不能直接访问__age是因为Python解释器对外把__age变量改成了_People__age，
也就是_类名__age（类名前是一个下划线）。因此，投机取巧的话，你可以通过_People__age在类的外部访问__age变量
也就是说：Python的私有成员和访问限制机制是“假”的，没有从语法层面彻底限制对私有成员的访问。这一点和常量的尴尬地位很相似

类的成员与下划线总结：
_name、_name_、_name__:建议性的私有成员，不要在外部访问。
__name、 __name_ :强制的私有成员，但是你依然可以蛮横地在外部危险访问。
__name__:特殊成员，与私有性质无关，例如__doc__。
name_、name__:没有任何特殊性，普通的标识符，但最好不要这么起名
"""


class People:
    title = "人类"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def set_age_check(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            # raise ValueError
            return ValueError

    def print_age(self):
        print('%s: %s' % (self.name, self.__age))


obj = People("小明", 12)
# obj.print_age()
print(obj.get_age())
print(obj.set_age_check("a"))
print(obj._People__age)
