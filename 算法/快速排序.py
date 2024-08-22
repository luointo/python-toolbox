# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
快速排序
原理
快速排序使用分治法（Divide and conquer）策略来把一个序列（raw_list）分为两个子序列（sub-lists）。

步骤
    从数列中挑出一个元素，称为”基准”（pivot），
    重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
    递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""


# 普通版
def quick_sort(raw_list):
    less = []
    pivot_list = []
    more = []
    # 递归出口
    if len(raw_list) <= 1:
        return raw_list
    else:
        # 将第一个值做为基准
        pivot = raw_list[0]
        for i in raw_list:
            # 将比急转小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准打的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivot_list.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = quick_sort(data_test)
print(sorted_list)


# 下面这段代码出自《Python cookbook 第二版》传说中的三行实现python快速排序
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])


sorted_list = qsort(data_test)
print(sorted_list)

# 一行语法糖版本
qs = lambda xs: ((len(xs)<=1 and [xs]) or [qs([x for x in xs[1:] if x < xs[0]])+[xs[0]] + qs([x for x in xs[1:] if x >= xs[0]])])[0]
sorted_list = qs(data_test)
print(sorted_list)
