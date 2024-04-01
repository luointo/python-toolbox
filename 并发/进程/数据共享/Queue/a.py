# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing
from multiprocessing import Process
from multiprocessing import queues

"""
multiprocessing是一个包，它内部又一个queues模块，提供了一个Queue队列类，可以实现进程间的数据共享

关于queue和Queue，在Python库中非常频繁的出现，很容易就搞混淆了。
甚至是multiprocessing自己还有一个Queue类(大写的Q)，一样能实现queues.Queue的功能，导入方式是from multiprocessing import Queue
"""


def func(i, q):
    ret = q.get()
    print("进程%s从队列里获取了一个%s，然后又向队列里放入了一个%s" % (i, ret, i))
    q.put(i)


if __name__ == "__main__":
    lis = queues.Queue(20, ctx=multiprocessing)
    lis.put(0)
    for i in range(10):
        p = Process(target=func, args=(i, lis,))
        p.start()
