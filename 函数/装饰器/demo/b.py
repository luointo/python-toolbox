# -*- coding: utf-8 -*-
__author__ = 'luointo'

from decorator import decorator

"""
pip install decorator

decorator实现的装饰器能完整保留原函数的name，doc和args，
唯一有问题的就是inspect.getsource(func)返回的还是装饰器的源代码，你需要改成inspect.getsource(func.__wrapped__)
"""


@decorator
def logging(func, *args, **kwargs):
    print("[DEBUG]: enter {}()".format(func.__name__))
    return func(*args, **kwargs)


@logging
def f():
    """hello world"""
    print("hello world")


# f()

print(f.__name__)
print(f.__doc__)
