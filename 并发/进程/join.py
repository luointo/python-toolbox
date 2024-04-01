# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing
import time

"""
join 方法的主要作用是：阻塞当前进程，直到调用 join 方法的那个进程执行完，再继续执行当前进程
"""


def worker(interval):
    print('工作开始时间：{0}'.format(time.time()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.time()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    # p.daemon = True
    p.start()
    p.join()

    print('end')
