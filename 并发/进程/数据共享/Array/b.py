# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_bool, c_double

lock = Lock()


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, b, s, arr, A):
    n.value **= 2
    b.value = True

    for k, v, in enumerate(s):
        s[k] = v + 10

    arr[0] = 10
    for a in A:
        a.x **= 2
        a.y **= 2


if __name__ == '__main__':
    n = Value('i', 7)
    b = Value(c_bool, False, lock=False)

    s = Array('i', range(5), lock=lock)

    arr = Array('i', range(5), lock=True)

    A = Array(Point, [(1.875, -6.25), (-5.75, 2.0)], lock=lock)

    p = Process(target=modify, args=(n, b, s, arr, A))
    p.start()
    p.join()

    print(n.value)
    print(b.value)
    print(list(s))
    print(arr[:])
    print([(a.x, a.y) for a in A])
