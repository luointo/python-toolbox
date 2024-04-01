# -*- coding: utf-8 -*-
__author__ = 'luointo'

import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        # 使用全局Event对象
        global event
        # 判断Event对象内部信号标志
        if event.is_set():
            event.clear()
            event.wait()
            print(111, self.getName())
        else:
            print(222, self.getName())
            # 设置Event对象内部信号标志
            event.set()


# 生成Event对象
event = threading.Event()
# 设置Event对象内部信号标志
event.set()
t1 = []
for i in range(4):
    t = MyThread(str(i))
    # 生成线程列表
    t1.append(t)

for i in t1:
    # 运行线程
    i.start()
