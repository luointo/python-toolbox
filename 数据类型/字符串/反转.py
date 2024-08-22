# -*- coding: utf-8 -*-
__author__ = 'luointo'

from functools import reduce

s = "python"

# 方法一
s1 = s[::-1]
print(s1)

# 方法二
s2 = reduce(lambda x, y: y + x, s)
print(s2)
