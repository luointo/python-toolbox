# -*- coding: utf-8 -*-
__author__ = 'luointo'


# 字典的Key与Value对调
d = m = {'A': 1, 'B': 2, 'C': 3}
res = {v: k for k, v in m.items()}
print(res)

res = (lambda x: dict(zip(x.values(), x.keys())))
print(res(d))
