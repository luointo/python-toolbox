# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
相比函数装饰器，类式装饰器具有灵活度大、高内聚、封装性等优点。
使用类式装饰器可以依靠内部的__call__方法，当使用@形式将装饰器附加到函数上时，就会调用此方法。

__call__只会在装饰阶段被调用一次
"""


# 不带参数的类式装饰器
# 在装饰阶段，__init__函数执行，在被装饰的方法被调用的时候，__call__ 执行
class Log:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("start function {func}()".format(func=self._func.__name__))
        return self._func(*args, **kwargs)


@Log
def say(words):
    return words


res = say('hello')
print(res)

res = say('world')
print(res)

# ============
print("=" * 10)


# 带参数的类式装饰器
class Log2:

    def __init__(self, level):
        self._level = level

    def __call__(self, func):
        print('__call__()方法执行')

        def decorator(*args, **kwargs):
            if self._level == 'warning':
                print('warning! function was called')
            elif self._level == 'error':
                print('error! function was called')
            return func(*args, **kwargs)

        return decorator


@Log2('error')
def say2(words):
    return words


res = say2('hello')
print(res)

res = say2('world')
print(res)


# 带参数的类式装饰器2
class Logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper  # 返回函数


@Logging(level='INFO')
def say(something):
    print("say {}!".format(something))
    return 1


res = say(something=123)
print(res)
