# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing
import time

"""
如果在子进程中添加了 daemon 属性，那么当主进程结束的时候，子进程也会跟着结束
"""


def worker(interval):
    print('工作开始时间：{0}'.format(time.time()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.time()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    print('end')
