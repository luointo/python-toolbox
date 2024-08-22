# -*- coding: utf-8 -*-
__author__ = 'luointo'

s = "19"
print(f"{s:0<5}")  # 后面补零
print(f"{s:1>7}")  # 前面补1

real_time = str('{:0>2d}'.format(2))
print(real_time)
