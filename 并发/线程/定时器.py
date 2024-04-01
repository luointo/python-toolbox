# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法

构造方法：
    Timer(interval, function, args=[], kwargs={})
    interval: 指定的时间
    function: 要执行的方法
    args/kwargs: 方法的参数
"""

import threading


def f():
    print("等待2s")


timer = threading.Timer(2, f)
timer.start()
