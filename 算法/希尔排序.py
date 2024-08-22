# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
希尔排序
原理
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。

步骤
    每次以一定步长(就是跳过等距的数)进行排序，直至步长为1.
"""


def shell_sort(raw_list):
    n = len(raw_list)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = raw_list[i]
            j = i
            # 插入排序
            while j >= gap and raw_list[j - gap] > temp:
                raw_list[j] = raw_list[j - gap]
                j -= gap
            raw_list[j] = temp
        # 得到新的步长
        gap = gap // 2
    return raw_list


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = shell_sort(data_test)
print(sorted_list)
