# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print("多进程")


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    p.join()
