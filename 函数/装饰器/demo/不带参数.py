# -*- coding: utf-8 -*-
__author__ = 'luointo'

import functools

"""
使用标准库里functools.wraps 保留原函数属性
"""


def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@logging
def say(something):
    """say something"""
    print("say {}!".format(something))


print(say.__name__)  # say
print(say.__doc__)  # say something
