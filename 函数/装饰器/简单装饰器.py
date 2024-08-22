# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()

    return wrapper


@debug
def hello():
    print("hello")


hello()

# ================
print("=" * 10)


def log(func):
    def wrapper(*args, **kwargs):
        print('%s function start' % func.__name__)
        result = func(*args, **kwargs)
        print('%s function end' % func.__name__)
        return result

    return wrapper


@log
def say1(words):
    print(words)


@log
def say2(words):
    return words


say1('hello')  # 此时say1和say2指向的是wrapper函数（__name__为'wrapper'）

data = say2('hello')
print(data)

# ================
print("=" * 10)


# 计算函数用时
def custom_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("函数（{}）执行用时：{}".format(func.__name__, time.time() - start))
        return res

    return wrapper


@custom_timer
def f():
    time.sleep(1)
    print(1)
    return 123


a = f()
print(a)
