# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 字典
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)

print("=" * 10)
# 列表遍历得到索引和对应值
list_data = [1, 2, 3]
for i, v in enumerate(list_data):
    print(i, v)

print("=" * 10)
# 同时遍历两个或更多的序列，可以使用 zip() 组合
list_data1 = ['a', 'b', 'c']
list_data2 = [1, 2, 3, 4]
for a, b in zip(list_data1, list_data2):
    print(a, b)

print("=" * 10)
# 反向遍历一个序列，然后调用 reversed() 函数
list_data = [1, 2, 3]
for i in reversed(list_data):
    print(i)

print("=" * 10)
# 按顺序遍历一个序列，使用 sorted() 函数, 并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

print("=" * 10)
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
