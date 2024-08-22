# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
冒泡排序
原理
冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一
次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

步骤
冒泡排序算法的运作如下：
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubble_sort(raw_list):
    length = len(raw_list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            if raw_list[j - 1] > raw_list[j]:
                # 交换两者数据，这里没用temp是因为python 特性元组。
                raw_list[j - 1], raw_list[j] = raw_list[j], raw_list[j - 1]
    return raw_list


def bubble_sort_flag(raw_list):
    length = len(raw_list)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if raw_list[j - 1] > raw_list[j]:
                raw_list[j - 1], raw_list[j] = raw_list[j], raw_list[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return raw_list
    return raw_list


# 测试
data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = bubble_sort(data_test)
print(sorted_list)

sorted_list = bubble_sort_flag(data_test)
print(sorted_list)
