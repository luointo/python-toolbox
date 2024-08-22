# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 拆分含有多种分隔符的字符串

import re


def my_split(s, ds):
    # 连续使用str.split()方法，每次处理一种分割符号
    res = [s]
    for d in ds:
        t = []
        for x in res:
            t.extend(x.split(d))
        res = t
    return [x for x in res if x]


s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
a = my_split(s, ";,|\t")
print(a)

# 使用正则表达式的re.split()方法，一次性拆分字符串
res = re.split(r"[;,|\t]+", s)
print(res)
