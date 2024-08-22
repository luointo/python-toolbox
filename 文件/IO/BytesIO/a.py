# -*- coding: utf-8 -*-
__author__ = 'luointo'

from io import BytesIO

"""
使用BytesIO操作二进制数据
BytesIO实现了在内存中读写bytes
"""

# 写入
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 读取
f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f2.read())
