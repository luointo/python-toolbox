# -*- coding: utf-8 -*-
__author__ = 'luointo'

import datetime

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)

# 获取当前日期
d2 = datetime.date.today()
print(d2)
# # 打印今天的年，月和日
print(d2.year, d2.month, d2.day)

# 从date类示例化date对象
d3 = datetime.date(2020, 10, 1)
print(d3)

# 从时间戳获取日期
d4 = datetime.date.fromtimestamp(1576244364)
print(d4)

# 从time类示例化的时间对象表示本地时间
# time(hour, minute, second, microsecond)
d6 = datetime.time(12, 23, 50, 123)
print(d6)
print("小时=", d6.hour)
print("分钟=", d6.minute)
print("秒=", d6.second)
print("微秒=", d6.microsecond)

# datetime(year, month, day)
d7 = datetime.datetime(2019, 11, 28)
print(d7)

# datetime(year, month, day, hour, minute, second, microsecond)
a = datetime.datetime(2019, 11, 28, 23, 55, 59, 342380)
print(a)
print("年 =", a.year)
print("月 =", a.month)
print("日 =", a.day)
print("时 =", a.hour)
print("份 =", a.minute)
print("时间戳 =", a.timestamp())

# 两个timedelta对象之间的时间差
t1 = datetime.timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = datetime.timedelta(days=4, hours=11, minutes=4, seconds=54)
print(t1 - t2)
