# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 列表推导式

vec = [2, 4, 6]
new_vec = [3 * x for x in vec]  # 将列表中每个数值乘三，获得一个新的列表
print(new_vec)

new_vec = [[x, x ** 2] for x in vec]
print(new_vec)

new_vec = [3 * x for x in vec if x > 3]
print(new_vec)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

print([str(round(355 / 113, i)) for i in range(1, 6)])

# 以下实例将3X4的矩阵列表转换为4X3列表
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# 列表推导式中使用if-else
q = [x if x % 3 == 0 else -x for x in range(1, 101)]
print(q)