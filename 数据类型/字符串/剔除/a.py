# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
字符串strip() lstrip() rstrip()去掉字符串两端字符
删除单个固定位置的字符，可以使用切片 + 拼接的方式
字符串的replace() 方法 或正则表达式 re.sub() 删除任意位置字符
字符串translate()方法，可以同时删除多种不同字符
"""

import re

s = "---abc+++"
print(s.strip("-+"))

s = "abc:123"
print(s[:3] + s[4:])

s = "\tabc\t123\txyz"
print(s.replace("\t", ""))

s = "\tabc\t123\txyz\r"
print(re.sub(r"[\t\r]", "", s))
