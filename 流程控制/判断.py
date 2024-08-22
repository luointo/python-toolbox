# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False

if x is not None是最好的写法，清晰，不会出现错误，以后坚持使用这种写法

使用if not x这种写法的前提是：必须清楚x等于None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()时对你的判断没有影响才行

(ob1 is ob2) 等价于 (id(ob1) == id(ob2))
"""

x = None
if x is None:
    print("x is None")
