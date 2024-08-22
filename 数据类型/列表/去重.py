# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 列表去重

# 去重，但改变顺序
# 方法1 就是利用 set 进行去重
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))
print(l2)

# 方法2 是利用字典的键不重复的特性，将列表的元素作为一个字典的键
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = {}.fromkeys(l1).keys()
print(list(l2))

# 去重，不改变顺序
# 利用 sorted 和 set 方法实现去重并保留原始顺序，这里 sorted 指定排序的规则就是按照原列表的索引顺序
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = sorted(set(l1), key=l1.index)
print(l2)
