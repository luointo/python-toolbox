# -*- coding: utf-8 -*-
__author__ = 'luointo'

import functools


def logging(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logging(level='INFO')
def say(something):
    """say doc"""
    print("say {}!".format(something))


@logging(level='DEBUG')
def do(something):
    """do doc"""
    print("do {}...".format(something))


say('hello')
do("my work")

print(say.__name__, say.__doc__)
