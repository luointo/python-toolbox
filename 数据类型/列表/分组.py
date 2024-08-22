# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 每三个为一组分割list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(a), 3):
    b = a[i:i + 3]
    print(b)

res = [a[i:i + 3] for i in range(0, len(a), 3)]
print(res)
