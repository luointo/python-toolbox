# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
递归函数

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
"""


def sum_number(n):
    # 高斯求和, 循环实现
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


res = sum_number(100)
print(res)


def sum_number_recursion(n):
    # 高斯求和, 递归
    if n <= 0:
        return 0
    return n + sum_number_recursion(n - 1)


res = sum_number_recursion(100)
print(res)
