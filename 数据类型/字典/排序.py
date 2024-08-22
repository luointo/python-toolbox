# -*- coding: utf-8 -*-
__author__ = 'luointo'

from random import randint

d = {x: randint(60, 100) for x in "xyzabc"}

a = sorted(zip(d.values(), d.keys()))
print(a)  # 排序后的结果

a = sorted(d.items(), key=lambda x: x[1])
print(a)  # 排序后的结果
