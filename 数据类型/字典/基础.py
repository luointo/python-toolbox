# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
字典是另一种可变容器模型，且可存储任意类型对象

字典的每个键值(key=>value)对用冒号(:)分割

整个字典包括在花括号(**{})**中

每个对之间用逗号(,)分割

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行

键必须是唯一的，但值则不必

键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

"""

# 创建字典
d1 = {}
d2 = {'abc': 456}
d3 = dict()
d3["abc"] = 123
d3[98.6] = 37

# 访问字典里的值
d = {'Name': 'jack', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", d['Name'])
print("dict['Age']: ", d['Age'])

# 修改字典
d = dict()
d['age'] = 12
d['age'] = 18

# 删除字典元素
d = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del d['Name']  # 删除键 'Name'
d.clear()  # 清空字典
del d  # 删除字典

# 遍历字典
dic = {'Name': 'Jack', 'Age': 7, 'Class': 'First'}
# 1  直接遍历字典获取键，根据键取值
for key in dic:
    print(key, dic[key])

# 2  利用items方法获取键值，速度很慢，少用！
for key, value in dic.items():
    print(key, value)

# 3  利用keys方法获取键
for key in dic.keys():
    print(key, dic[key])

# 4  利用values方法获取值，但无法获取对应的键。
for value in dic.values():
    print(value)

# 字典推导
d = {x: x ** 2 for x in (2, 4, 6)}
