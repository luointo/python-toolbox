# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing


def work(num):
    print(num)


if __name__ == '__main__':
    p = multiprocessing.Process(target=work, args=(1,))

    print("进程开始")
    p.start()
    p.join()
    print("进程结束")
