# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time
import datetime

# 计算两个日期相差天数
d1 = datetime.datetime(2018, 9, 30)
d2 = datetime.datetime(2017, 9, 30)
a = (d1 - d2).days
print(a)

# 计算两个日期相差秒
start_time = datetime.datetime.now()
time.sleep(1)
end_time = datetime.datetime.now()
print((end_time - start_time).seconds)

# 延时多少时间后
d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(seconds=2)
time.sleep(3)
if datetime.datetime.now() >= d3:
    print("ok")

t1 = datetime.timedelta(seconds=60)
t2 = datetime.timedelta(seconds=30)
print(t1 + t2)
print(t1 - t2)
print(t1 * 2)
print(t1 / 3)

"""
两个timedelta对象可以直接进行比较操作，
而一个timedelta对象与一个非timedelta对象进行==或!=操作时总是返回False，而进行>或<操作则会抛出TypeError。
"""
print(t1 > t2)
t3 = datetime.timedelta(days=1, seconds=30)
print(t3.total_seconds())  # 用于计算秒数

dt = datetime.datetime.now()
print(dt + datetime.timedelta(3))  # 3天后
print(dt + datetime.timedelta(-3))  # 3天前
print(dt + datetime.timedelta(hours=3))  # 3小时后
print(dt + datetime.timedelta(hours=3, seconds=30))  # 3小时30秒后


# 时间差
t1 = "2021-10-27 14:37:24"
t2 = "2021-10-27 14:39:55"
tt1 = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
tt2 = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
print((tt2 - tt1).seconds)