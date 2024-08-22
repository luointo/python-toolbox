# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
@property装饰器

Python内置的@property装饰器可以把类的方法伪装成属性调用的方式。
也就是本来是Foo.func()的调用方法，变成Foo.func的方式。在很多场合下，这是一种非常有用的机制

将一个方法伪装成为属性后，就不再使用圆括号的调用方式了。而是类似变量的赋值、获取和删除方法了。
当然，每个动作内部的代码细节还是需要你自己根据需求去实现的

首先，在普通方法的基础上添加@property装饰器，例如下面的age()方法。
这相当于一个get方法，用于获取值,决定类似"result = obj.age"执行什么代码。该方法仅有一个self参数。
写一个同名的方法，添加@xxx.setter装饰器（xxx表示和上面方法一样的名字），
比如例子中的第二个方法。这相当于编写了一个set方法，提供赋值功能，决定类似"obj.age = ...."的语句执行什么代码。
再写一个同名的方法，并添加@xxx.delete装饰器，比如例子中的第三个方法。用于删除功能，决定"del obj.age "这样的语句具体执行什么代码

简而言之，就是分别将三个方法定义为对同一个属性的获取、修改和删除。还可以定义只读属性，也就是只定义getter方法，不定义setter方法就是一个只读属性
"""


class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age.deleter
    def age(self):
        print("删除年龄数据！")


obj = People("jack", 18)
print(obj.age)
obj.age = 19
print("obj.age:  ", obj.age)
del obj.age
