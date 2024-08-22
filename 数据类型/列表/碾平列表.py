# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 碾平列表（flatten list ），即当列表里面嵌套列表，如何将这些子列表给取出来，得到一个不包含子列表的列表

# 支持任意层次的捋平，或全部捋平
lst = [1, 2, [3, 4], [[5, 6], [8, 9, [19, 29, 39], 900], 10], 10, [8], 11, 12, 13, [14, 15]]

flatten = (lambda lst, lv=None:
           [elem2 for elem1 in lst for elem2 in flatten(elem1, lv if lv is None else lv - 1)]
           if type(lst) is list and (lambda lv: 0 if lv is None else lv)(lv) >= 0 else [lst])

a = flatten(lst)
print(a)

b = flatten(lst, 1)
print(b)


# 碾平列表
# 1. 利用递归的思想
def f(lis_data):
    res = []

    def _lis(data):
        for x in data:
            if isinstance(x, list):
                _lis(x)
            else:
                res.append(x)

    _lis(lis_data)
    return res


print(f(lst))

list1 = [1, [2, [3, 4]], 5]
res = []


def fun(s):
    for i in s:
        if isinstance(i, list):
            fun(i)
        else:
            res.append(i)


fun(list1)
print(res)

# 2. 用 lambda 实现一个匿名函数
flat = lambda L: sum(map(flat, L), []) if isinstance(L, list) else [L]
print(flat(list1))

# 3
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
print(flatten(a))
