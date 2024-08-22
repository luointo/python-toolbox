# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
堆排序
原理
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

步骤
    创建最大堆:将堆所有数据重新排序，使其成为最大堆
    最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
    堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算
"""


def heap_sort(raw_list):
    # 创建最大堆
    for start in range((len(raw_list) - 2) // 2, -1, -1):
        sift_down(raw_list, start, len(raw_list) - 1)

    # 堆排序
    for end in range(len(raw_list) - 1, 0, -1):
        raw_list[0], raw_list[end] = raw_list[end], raw_list[0]
        sift_down(raw_list, 0, end - 1)
    return raw_list


# 最大堆调整
def sift_down(lst, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = heap_sort(data_test)
print(sorted_list)
