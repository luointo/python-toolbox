# -*- coding: utf-8 -*-
__author__ = 'luointo'

import threading
import random
import time


# 在函数中使用多线程
def run(num, **kwargs):
    time.sleep(random.random())
    print(num, kwargs)


threads = []

for x in range(5):
    """
    target - 线程函数
    args - 传递给线程函数的参数,必须是个tuple类型
    kwargs - 可选参数
    """
    t = threading.Thread(target=run, args=(x,), kwargs={"name": "可选参数"})
    threads.append(t)
    t.start()

"""
join方法的作用是阻塞主进程（无法执行join以后的语句），主线程等待这个线程结束后，才可以执行下一条指令。
多线程多join的情况下，依次执行各线程的join方法，前头一个结束了才能执行后面一个。
无参数，则等待到该线程结束，才开始执行下一个线程的join。
设置参数后，则等待该线程这么长时间就不管它了（而该线程并没有结束）。不管的意思就是可以执行后面的主进程了
"""
for t in threads:
    t.join()

# 使用join后， 等线程结束后才执行后面的语句
print("多线程结束")
