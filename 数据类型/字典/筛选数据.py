# -*- coding: utf-8 -*-
__author__ = 'luointo'

from random import randint

d = {x: randint(60, 100) for x in range(1, 21)}

res = {k: v for k, v in d.items() if v > 90}

print(res)
