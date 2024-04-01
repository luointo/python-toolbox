# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os
import multiprocessing


def foo(num):
    print("这里是 ", multiprocessing.current_process().name)
    print('模块名称:', __name__)
    print('父进程 id:', os.getppid())  # 获取父进程id
    print('当前子进程 id:', os.getpid())  # 获取自己的进程id
    print(num)
    print('------------------------')


if __name__ == '__main__':

    for i in range(2):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
        p.join()
