# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
使用字符串的str.ljust() str.rjust() str.center()进行左，右，居中对齐
使用format()方法，传递类似<20 >20 ^20参数
"""
s = "abc"

print(s.ljust(20))
print(s.ljust(20, "-"))
print(s.rjust(10, "+"))
print(s.center(18, ">"))

print(format(s, ">20"))
print(format(s, "<20"))
print(format(s, "^20"))
