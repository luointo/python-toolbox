# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
选择排序
原理
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置。

步骤
    在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
"""


def selection_sort(raw_list):
    n = len(raw_list)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if raw_list[j] < raw_list[min_index]:
                min_index = j
        raw_list[min_index], raw_list[i] = raw_list[i], raw_list[min_index]
    return raw_list


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = selection_sort(data_test)
print(sorted_list)
