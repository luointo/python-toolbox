# -*- coding: utf-8 -*-
__author__ = 'luointo'

with open(file="test.txt", mode="w", encoding="utf-8") as f:
    f.write("123\n")
    f.writelines([
        "a\n",
        'b\n'
    ])
