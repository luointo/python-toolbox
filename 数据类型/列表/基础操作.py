# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
list是一种有序的集合
可以随时添加和删除其中的元素
索引从零开始
"""
# 列表创建
lis1 = []  # 创建一个空列表
lis2 = list()
lis3 = [1, 2, 3]
lis4 = [1, 'a', [11, 22], {'k1': 'v1'}]
lis5 = [1, 2, [3, 4, 5]]
str_list = ['a', 'b', 'c']
# str_list = list(['a', 'b', 'c'])

# 索引（访问列表中某一个值）
# 最后一个元素的索引是len(list)-1
print("第一个元素:", str_list[0])
print("最后一个元素:", str_list[len(str_list) - 1])

# 修改元素的值
str_list[1] = 'bb'
print("修改后列表:", str_list)

# 追加（增加元素到末尾）
str_list.append('d')
print("追加:", str_list)

# 插入（在指定位置加入元素）
str_list.insert(1, 'e')
print("插入:", str_list)

# 删除（删除指定元素）
# 使用del语句或者remove(),pop()方法删除指定的元素
del str_list[0]
print("del:", str_list)
str_list.remove('c')
print("remove:", str_list)
str_list.pop(1)
print("pop:", str_list)
