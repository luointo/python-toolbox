# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
bytes和bytearray区别
bytes是不可变的，同str。bytearray是可变的，同list。
"""
b = bytearray()
b.append(10)
b.append(100)
b.remove(100)
b.insert(0, 150)
b.extend([1, 3, 5])
b.pop(2)
b.reverse()
b.clear()
print(b)

# bytes和 bytearray转换
b = b"abcdef"
bay = bytearray(b)
print(b)
print(bay)
b = bytes(bay)
print(b)

# bytearray和str转换
a = 'abcdef'
b = bytearray(a, encoding='utf-8')
a = b.decode(encoding='utf-8')
print(a)
