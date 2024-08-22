# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time
from datetime import datetime

"""
python中时间日期格式化符号：
字符	描述
%a	星期的简写，如星期三为Wed
%A	星期的全写，如星期三为Wednesday
%b	月份的简写，如4月为Apr
%B	月份的全写，如4月为April
%c	日期时间的字符串表示，如： 04/07/10 10:43:39
%d	日在这个月中的天数
%f	微秒（范围：0至999999）
%H	小时（24小时制，范围：0至 23）
%I	小时（12小时制，范围：0至 11）
%j	日在年中的天数，范围：001至366
%m	月份，范围：01至12
%M	分钟，范围：00至59
%p	AM或者PM
%S	秒，范围：00至61
%U	周在当年的周数，星期天为周的第一天
%w	今天在这周的天数，范围：0至6，6表示星期天
%W	周在当年的周数，星期一作为周的第一天
%x	日期字符串，如：04/07/10
%X	时间字符串，如：10:43:39
%y	2位数表示的年份
%Y	4位数表示的年份
%z	与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z	时区名称（如果是本地时间，返回空字符串）
%%	转义，%不变
"""

"""
从	到	方法
时间戳	UTC结构化时间	gmtime()
时间戳	本地结构化时间	localtime()
UTC结构化时间	时间戳	calendar.timegm()
本地结构化时间	时间戳	mktime()
结构化时间	格式化字符串	strftime()
格式化字符串	结构化时间	strptime()
"""

# 从本地结构化时间转换为时间字符串
t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t2 = time.strftime("%Y-%m-%d %H:%M:%S")
print(t1)
print(t2)

# 字符串转换为日期
# strptime()方法从一个给定的字符串(表示日期和时间)创建一个datetime对象
print(datetime.strptime('2012-09-20', '%Y-%m-%d'))
print(datetime.strptime('20091031', '%Y%m%d'))
print(datetime.strptime("1 October, 2020", "%d %B, %Y"))
t = time.strptime("2020-09-26 06:50:36", "%Y-%m-%d %H:%M:%S")  # 从时间字符串转换为结构化时间
print(t)

# 时间戳到日期时间
timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)

# 日期时间到时间戳
now = datetime.now()
timestamp = datetime.timestamp(now)
print("时间戳 =", timestamp)
