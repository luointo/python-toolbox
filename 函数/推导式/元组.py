# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 圆括号在Python中被用作生成器的语法了
# 要通过类似方法生成元组，需要显式调用元组的类型转换函数tuple()

tup = tuple(x for x in range(9))
print(tup)
print(type(tup))
