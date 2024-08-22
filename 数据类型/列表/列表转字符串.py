# -*- coding: utf-8 -*-
__author__ = 'luointo'

s = ["i", "love", "pytonh"]
res = " ".join(s)
print(res)

s = ["abc", 123, 33, "xy"]
a = " ".join(str(x) for x in s)
print(a)
