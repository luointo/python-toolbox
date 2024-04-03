# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
sorted排序
在列表中有一个内置的排序函数sort(), 对列表的对象进行排序, 没有返回值
sorted()函数对所有可迭代的对象进行排序操作
sort与sorted区别：
    sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作。
    list的sort方法返回的是对已经存在的列表进行操作，而内建函数sorted方法返回的是一个新的list，而不是在原来的基础上进行的操作

list.sort(cmp=None, key=None, reverse=False)
sorted(iterable[, cmp[, key[, reverse]]])
参数/返回值
    iterable – 可迭代对象
    cmp – 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse – 排序规则，reverse = True降序，reverse = False升序(默认）
    sort没有返回值, sorted返回重新排序的列表
"""

# 使用sort()排序
# 用sort
list3 = [3, 7, 2, 5, 0, 4]
list3.sort()
print(list3)

aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort(reverse=True)  # 降序
print(aList)


def take_second(elem):
    return elem[1]


random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=take_second)
print(random)

# ==============================================
print("=" * 10)

# 使用sorted()函数排序时
res = sorted([0, 2, 3, 4, 5, 7])
print(res)

# 按绝对值大小排序
list_data = [4, -7, 2, 6, -3]
res = sorted(list_data, key=abs)  # key接受函数来实现自定义排序规则
print(res)
print(sorted(list_data, key=abs, reverse=True))  # 将序排列


# 函数可以自己写
def my_len(str):
    return len(str)


list_data = ['b333', 'a1111111', 'c22', 'd5554']
res = sorted(list_data, key=my_len)  # 默认升序排序
print(res)

# 匿名函数
list9 = sorted(list_data, key=lambda x: len(x), reverse=True)
print(list9)
