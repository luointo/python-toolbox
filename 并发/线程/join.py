# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
join(timeout)方法将会等待直到线程结束。这将阻塞正在调用的线程，直到被调用join()方法的线程结束。

主线程或者某个函数如果创建了子线程，只要调用了子线程的join方法，那么主线程就会被子线程所阻塞，直到子线程执行完毕再轮到主线程执行。
其结果就是所有子线程执行完毕

join方法的作用是阻塞主进程（挡住，无法执行join以后的语句），专注执行多线程。
多线程多join的情况下，依次执行各线程的join方法，前头一个结束了才能执行后面一个。
无参数，则等待到该线程结束，才开始执行下一个线程的join。
设置参数后，则等待该线程这么长时间就不管它了（而该线程并没有结束）。不管的意思就是可以执行后面的主进程了
"""

import threading
import time


def context(tJoin):
    print('in threadContext.')
    tJoin.start()

    # 将阻塞tContext直到threadJoin终止。
    tJoin.join()

    # tJoin终止后继续执行。
    print('out threadContext.')


def join():
    print('in threadJoin.')
    time.sleep(1)
    print('out threadJoin.')


tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()
