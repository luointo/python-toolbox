# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
使用 threading.Event() 实现线程的暂停, 恢复和停止的功能

但是这里有一个缺点: 无论是暂停还是停止, 都不是瞬时的, 必须等待run函数内部的运行到达标志位判断时才有效.
也就是说操作会滞后一次.

但是这有时也不一定是坏事. 如果run函数中涉及了文件操作或数据库操作等, 完整地运行一次后再退出, 反而能够执行剩余的资源释放操作的代码(例如各种close)
不会出现程序的文件操作符超出上限, 数据库连接未释放等尴尬的情况.
"""

import threading
import time
import datetime


class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print(datetime.datetime.now())

    def pause(self):
        # 暂停
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        # 恢复
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        # 停止
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


job = Job()
job.start()

job.pause()  # 暂停3秒
time.sleep(3)

job.resume()  # 恢复

job.pause()  # 暂停2秒
time.sleep(2)

job.stop()
