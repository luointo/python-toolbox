# -*- coding: utf-8 -*-
__author__ = 'luointo'

import wrapt

"""
pip install wrapt

wrapt是一个功能非常完善的包，用于实现各种你想到或者你没想到的装饰器。
使用wrapt实现的装饰器你不需要担心之前inspect中遇到的所有问题，因为它都帮你处理了，甚至inspect.getsource(func)也准确无误。
"""


# 无参数
@wrapt.decorator
def logging(wrapped, instance, args, kwargs):  # instance is must
    print("[DEBUG]: enter {}()".format(wrapped.__name__))
    return wrapped(*args, **kwargs)


@logging
def f():
    print("hello world")


f()


# 带参数
def logging_with_arguments(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print("[{}]: enter {}()".format(level, wrapped.__name__))
        return wrapped(*args, **kwargs)

    return wrapper


@logging_with_arguments(level="INFO")
def do():
    print("hello world")


do()
