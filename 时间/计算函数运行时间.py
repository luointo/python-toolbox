# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time
import datetime
import timeit


# 计算代码块或程序的运行时间

def func():
    time.sleep(0.01)


start = time.time()
func()
end = time.time()
total_time = end - start
print(total_time)

start = datetime.datetime.now()
func()
end = datetime.datetime.now()
total_time = end - start
print(total_time.microseconds)

start = timeit.default_timer()
func()
end = timeit.default_timer()
total_time = end - start
print(total_time)
