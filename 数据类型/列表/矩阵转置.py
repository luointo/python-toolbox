# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 矩阵转置
A = [[1, 2, 3, 4],
     [5, 6, 7, 8]]

a = [[r[c] for r in A] for c in range(len(A[0]))]
print(a)

trans_mat = lambda A: map(list, zip(*A))
a = list(trans_mat(A))
print(a)
