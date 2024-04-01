# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing import Process
from multiprocessing import Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import time

"""
进程锁
为了防止和多线程一样的出现数据抢夺和脏数据的问题，同样需要设置进程锁。
与threading类似，在multiprocessing里也有同名的锁类RLock，Lock，Event，Condition和 Semaphore，
"""


def func(i, lis, lc):
    lc.acquire()
    lis[0] = lis[0] - 1
    time.sleep(1)
    print('say hi', lis[0])
    lc.release()


if __name__ == "__main__":
    array = Array('i', 1)
    array[0] = 10
    lock = RLock()
    for i in range(10):
        p = Process(target=func, args=(i, array, lock))
        p.start()
