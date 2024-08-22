# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 遍历列表时删除元素

"""
# 错误示范, Python的for可以遍历一个List，但是在遍历的过程中删除元素常常会得到意想不到的结果甚至程序出现异常
# 1.遍历时直接移除元素
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
for item in lst:
    if item == 0:
        lst.remove(item)
print(lst)
# 2. 利用索引来遍历删除列表中的元素
# 这时候就报错了，抛出了数组下标越界的异常。
# 原因是用for发起任何形式的遍历时，它的遍历顺序都是从最初就确定的，而在遍历中删除了元素会导致当前索引的变化，这样一是会导致漏删元素，
# 二是会导致遍历超过链表的长度
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
for item in range(len(lst)):
    if lst[item] == 0:
        del lst[item]
print(lst)
"""

# 使用filter过滤返回新的List
# filter包括两个参数，分别是function和list，filter把传入的函数依次作用于每个元素，然后根据返回值是True还是False来决定是保留还是丢弃该元素
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
lst = list(filter(lambda x: x != 0, lst))
print(lst)

# 列表解析
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
lst = [x for x in lst if x != 0]
print(lst)

# 遍历拷贝的List，操作原始的List
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
for item in lst[:]:
    if item == 0:
        lst.remove(item)
print(lst)

# while循环，每次循环都先会判断 0 是否在列表中
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
while 0 in lst:
    lst.remove(0)
print(lst)

# 倒序循环遍历
lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
for item in range(len(lst) - 1, -1, -1):
    if lst[item] == 0:
        del lst[item]
print(lst)
