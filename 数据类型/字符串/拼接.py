# -*- coding: utf-8 -*-
__author__ = 'luointo'

name = "Tom"
age = 25

# 加号拼接
s = name + "'s age is " + str(age)
print(s)

# 字符串格式化
s = "%s's age is %d" % (name, age)
print(s)
