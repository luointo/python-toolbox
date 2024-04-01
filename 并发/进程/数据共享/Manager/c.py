# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing import Process, Manager

"""
一个multiprocessing.Manager对象会控制一个服务器进程，其他进程可以通过代理的方式来访问这个服务器进程。 常见的共享方式有以下几种：

Namespace。创建一个可分享的命名空间。
Value/Array。和上面共享ctypes对象的方式一样。
dict/list。创建一个可分享的dict/list，支持对应数据结构的方法。
Condition/Event/Lock/Queue/Semaphore。创建一个可分享的对应同步原语的对象

通过Manager类也可以实现进程间数据的共享。
Manager()返回的manager对象提供一个服务进程，使得其他进程可以通过代理的方式操作Python对象。
manager对象支持 list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, 
Condition, Event, Barrier, Queue, Value ,Array等多种格式
"""


def f(d, l):
    d[1] = "1"
    d["2"] = 2
    d[0.25] = None

    l.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
