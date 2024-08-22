# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time

# time()函数返回自纪元以来经过的秒数
t = time.time()
print(t)

# time.ctime()以历元以来的秒为参数，返回一个表示本地时间的字符串
# 自纪元以来经过的秒数
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

# localtime()函数将自epoch以来经过的秒数作为参数，并以localtime返回struct_time
result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# gmtime()函数将自epoch以来经过的秒数作为参数，并struct_time以UTC返回
result = time.gmtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# mktime()函数将struct_time（或包含9个元素的元组对应于struct_time）作为参数，并返回自当地时间的纪元以来经过的秒数。基本上，它是localtime()的反函数
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time = time.mktime(t)
print("Local time:", local_time)

# 该asctime()函数将struct_time（或包含9个元素的元组对应于struct_time）作为参数，并返回表示它的字符串
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
result = time.asctime(t)
print("Result:", result)

# sleep()函数在给定的秒数内暂停（延迟）当前线程的执行
print("这是立即打印输出。", time.time())
time.sleep(4)
print("这是4秒后打印的。", time.time())

