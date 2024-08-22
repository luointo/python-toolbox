# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
__call__
如果为一个类编写了该方法，那么在该类的实例后面加括号，可会调用这个方法。
注：构造方法的执行是由类加括号执行的，即：对象 = 类名()，而对于__call__() 方法，是由对象后加括号触发的，即：对象() 或者 类()()

怎么判断一个对象是否可以被执行呢？
能被执行的对象就是一个Callable对象，可以用Python内建的callable()函数进行测试
"""


class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__

print(callable(Foo()))
