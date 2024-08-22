# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
匿名函数
python 使用 lambda 来创建匿名函数

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    lambda 只是一个表达式，函数体比 def 简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

其形式通常是这样的：lambda 参数: 表达式
"""


def f(x):
    return x * x


res = f(6)
print(res)

f1 = lambda x: x * x
res = f1(6)
print(res)

res = (lambda x: x * x)(6)
print(res)
