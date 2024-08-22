# -*- coding: utf-8 -*-
__author__ = 'luointo'



with open(file="test.txt", mode="r", encoding="utf-8") as f:
    # data = f.read(1024)
    # print(data)

    data = f.readline()
    print(data)
