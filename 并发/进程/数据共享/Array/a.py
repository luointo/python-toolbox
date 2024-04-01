# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing import Process, Value, Array

"""
共享内存
可以给Value或者Array传递lock参数来决定是否带锁，如果不指定默认为RLock
"""


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
