# -*- coding: utf-8 -*-
__author__ = 'luointo'


def logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))


# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))


say('hello')
do("my work")
