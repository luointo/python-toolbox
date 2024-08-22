# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 字典推导式

# 注意x: x**2的写法，中间的冒号，表示左边的是key右边的是value
dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)
