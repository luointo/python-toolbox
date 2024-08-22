# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
插入排序
原理
插入排序（Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤
    从第一个元素开始，该元素可以认为已经被排序
    取出下一个元素，在已经排序的元素序列中从后向前扫描
    如果该元素（已排序）大于新元素，将该元素移到下一位置
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    将新元素插入到该位置后
    重复步骤2~5
"""


def insert_sort(raw_list):
    n = len(raw_list)
    for i in range(1, n):
        # 后一个元素和前一个元素比较
        # 如果比前一个小
        if raw_list[i] < raw_list[i - 1]:
            # 将这个数取出
            temp = raw_list[i]
            # 保存下标
            index = i
            # 从后往前依次比较每个元素
            for j in range(i - 1, -1, -1):
                # 和比取出元素大的元素交换
                if raw_list[j] > temp:
                    raw_list[j + 1] = raw_list[j]
                    index = j
                else:
                    break
            # 插入元素
            raw_list[index] = temp
    return raw_list


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = insert_sort(data_test)
print(sorted_list)
