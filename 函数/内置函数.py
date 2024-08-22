# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
你会不会有些好奇Python为什么可以直接使用一些内建函数，而不用显式的导入它们？
比如 str()、int()、dir()、id()、type()，max()，min()，len()等，许多许多非常好用，快捷方便的函数。
因为这些函数都是一个叫做builtins模块中定义的函数，而builtins模块默认在Python环境启动的时候就自动导入，所以你可以直接使用这些函数。

builtins模块里有接近80个内置函数，60多个内置异常，还有几个内置常数，特殊名称以及模块相关的属性
"""

print(globals())

print(dir(__builtins__))
