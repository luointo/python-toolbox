# -*- coding: utf-8 -*-
__author__ = 'luointo'

b = b''  # 创建一个空的bytes
print(b)

b = bytes()  # 创建一个空的bytes
print(b)

b = b'hello'  # 直接指定这个hello是bytes类型
print(b)

b = bytes('hello', encoding='utf-8')  # 利用内置bytes方法，将字符串转换为指定编码的bytes
print(b)

b = "hello".encode('utf-8')  # 利用字符串的encode方法编码成bytes，默认为utf-8类型
print(b)

a = b.decode('utf-8')  # 将bytes对象解码成字符串，默认使用utf-8
print(a)
