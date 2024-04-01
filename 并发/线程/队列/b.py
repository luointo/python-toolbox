# -*- coding: utf-8 -*-
__author__ = 'luointo'

from queue import Queue
from threading import Thread


def write(q):
    # 写数据进程
    for value in ['a', 'b', 'c']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)


def read(q):
    # 读取数据进程
    while True:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    qe = Queue()
    t1 = Thread(target=write, args=(qe,))
    t2 = Thread(target=read, args=(qe,))
    t1.start()
    t2.start()
