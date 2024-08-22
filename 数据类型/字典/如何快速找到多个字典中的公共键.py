# -*- coding: utf-8 -*-
__author__ = 'luointo'


# 如何快速找到多个字典中的公共键

from random import randint, sample
from functools import reduce

s1 = {x: randint(1, 4) for x in sample("abcdeg", randint(3, 6))}
print("s1:", s1)
s2 = {x: randint(1, 4) for x in sample("abcdeg", randint(3, 6))}
print("s2:", s2)
s3 = {x: randint(1, 4) for x in sample("abcdeg", randint(3, 6))}
print("s3:", s3)

# 使用字典的keys()方法，得到一个字典keys的集合
r1 = s1.keys() & s2.keys() & s3.keys()
print(r1)

# 使用map函数，得到所有字典keys的集合
# 使用reduce函数，取所有字典的keys的集合的交集
r2 = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))
print(r2)
