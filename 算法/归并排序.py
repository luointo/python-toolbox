# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
归并排序
原理
归并操作(归并算法)，指的是将两个已经排序的序列合并成一个序列的操作。归并排序算法依赖归并操作。

步骤
    迭代法
    申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
    设定两个指针，最初位置分别为两个已经排序序列的起始位置
    比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
    重复步骤3直到某一指针到达序列尾
    将另一序列剩下的所有元素直接复制到合并序列尾
"""


# 递归法
def merge_sort(raw_list):
    # 认为长度不大于1的数列是有序的
    if len(raw_list) <= 1:
        return raw_list
    # 二分列表
    middle = len(raw_list) // 2
    left = merge_sort(raw_list[:middle])
    right = merge_sort(raw_list[middle:])
    # 最后一次合并
    return merge(left, right)


# 合并
def merge(left, right):
    l_index, r_index = 0, 0
    result = []
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result += left[l_index:]
    result += right[r_index:]
    return result


data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
sorted_list = merge_sort(data_test)
print(sorted_list)

print("=" * 10)


# 归并排序，就是把两个已经排列好的序列合并为一个序列
# 算法逻辑比较简单，以第一个list为基准，第二个向第一个插空
def merge_sort(list1, list2):
    length_list1 = len(list1)
    length_list2 = len(list2)
    list3 = []
    j = 0
    for i in range(length_list1):
        while j < length_list2 and list2[j] < list1[i]:
            list3.append(list2[j])
            j = j + 1
        list3.append(list1[i])
    if j < (length_list2 - 1):
        for k in range(j, length_list2):
            list3.append(list2[k])
    return list3


# 测试
list1_data = [1, 3, 5, 10]
list2_data = [2, 4, 6, 8, 9, 11, 12, 13, 14]
print(merge_sort(list1_data, list2_data))
