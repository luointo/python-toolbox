# -*- coding: utf-8 -*-
__author__ = 'luointo'

# python3
s = '\\u751F\\u5316\\u5371\\u673A'
print(s.encode('utf-8').decode('unicode_escape'))

# python2
# s = '\u4e2d\u6587\u6d4b\u8bd5'
# print s.decode('unicode_escape')

# 如果想转成json:json.dumos(s).decode("unicode-escape")
