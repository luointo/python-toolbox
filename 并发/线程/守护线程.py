# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
后台线程

使用多线程默认情况下，当主线程退出之后，即使子线程没有 join，子线程也依然会继续执行。
如果希望主线程退出后，其子线程也退出而不再执行，则需要设置子线程为后台线程。
python提供了setDaemon方法，将子线程与主线程进行绑定，当主线程退出时子线程的生命也随之结束
"""

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    def run(self):
        while True:
            print(self.num)
            time.sleep(3)


for x in range(5):
    t = MyThread(num=x)
    t.setDaemon(True)
    t.start()
