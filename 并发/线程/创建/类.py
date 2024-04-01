# -*- coding: utf-8 -*-
__author__ = 'luointo'

import threading
import random
import time

"""
run()，需要重写，编写代码实现所需要的功能
getName()，获得线程对象名称
setName()，设置线程对象名称
start()，启动线程
join([timeout])，等待另一线程结束后再运行。
setDaemon(bool)，设置子线程是否随主线程一起结束，必须在start() 之前调用，默认为False。
isDaemon()，判断线程是否随主线程一起结束。
isAlive()，检查线程是否在运行中。
currentThread()　　获得当前线程对象
activeCount()　　获得当前活动的线程总个数
enumerate()　　获得所有活动线程的列表
settrace(func)　　设置一跟踪函数，在run执行前执行
setprofile(func)　　设置一跟踪函数，在run执行完毕之后执行
"""


class MyThread(threading.Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        # 或者
        # threading.Thread.__init__(self)
        self.num = num

    def run(self):
        time.sleep(random.random())
        print(self.num, threading.currentThread().name)


threads = []

for x in range(5):
    t = MyThread(x)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
