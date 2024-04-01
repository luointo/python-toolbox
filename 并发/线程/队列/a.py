# -*- coding: utf-8 -*-
__author__ = 'luointo'

import queue
import threading
from random import randint
from queue import PriorityQueue

"""
队列在并发开发中最常用的。我们借助「生产者/消费者」模式来理解：生产者把生产的「消息」放入队列，消费者从这个队列中对去对应的消息执行。
主要关心如下4个方法就好了：
    put: 向队列中添加一个项。
    get: 从队列中删除并返回一个项。
    task_done: 当某一项任务完成时调用。
    join: 阻塞直到所有的项目都被处理完。
"""

q = PriorityQueue()  # 优先级队列,数字越小优先级越高，数字相同，先进先出


def double(n):
    return n * 2


def producer():
    # 生产者
    count = 0
    while count < 5:
        pri = randint(0, 100)
        print('put:{}'.format(pri))
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    # 消费者
    while True:
        try:
            pri, task, arg = q.get(timeout=1)
        except queue.Empty:
            print("队列已经空了")
            return
        print('get:{} {} * 2 = {}'.format(pri, arg, task(arg)))
        q.task_done()


for target in (producer, consumer):
    t = threading.Thread(target=target)
    t.start()
