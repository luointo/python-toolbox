# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
Queue 队列
Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。
如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。

get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。
如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。
如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。

"""

from multiprocessing import Process, Queue
import os
import time
import random


# 写数据进程执行的代码
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程pw，写入：
    pr.start()  # 启动子进程pr，读取：
    pw.join()  # 等待pw结束
    pr.terminate()  # pr进程里的死循环，无法等待结束，只能强制终止
