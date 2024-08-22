# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os
import stat
import time

s = os.stat("a.txt")

print(stat.S_ISDIR(s.st_mode))  # 判断是否是文件夹

print(time.localtime(s.st_atime))  # 文件的访问时间

print(s.st_size)  # 文件的大小

a = "a.txt"
print(os.path.isdir(a))

print(os.path.islink(a))

print(os.path.isfile(a))

print(os.path.getatime(a))

print(os.path.getsize(a))