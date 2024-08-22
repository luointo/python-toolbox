# -*- coding: utf-8 -*-
__author__ = 'luointo'

from io import StringIO

"""
StringIO顾名思义就是在内存中读写str。
要把str写入StringIO，我们需要先创建一个StringIO

getvalue()方法用于获得写入后的str
"""

# 写入
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 读取
f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())
