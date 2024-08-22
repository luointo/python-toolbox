# -*- coding: utf-8 -*-
__author__ = 'luointo'

from collections import defaultdict
from collections import Counter


# 定义多维字典

# 迭代器创建，推荐
def nested_dict():
    return defaultdict(nested_dict)


d = nested_dict()
d['key1']['key2']['key3'] = 10
d['a'][1]['b'] = 'test'
print(d['key1']['key2']['key3'])
print(d['a'][1]['b'])

# 利用元组来充当多维字典的key,即将多维key按照规则放入元组中，使用该元组作为字典的key并赋值，以达到多维key的效果
d = dict()
set_data1 = ('a', 'b', 'c')
set_data2 = ('a', 'b')
d[set_data1] = '多维数组1'
d[set_data2] = '多维数组2'
print(d[set_data1])
print(d[set_data2])


# 迭代创建
def multi_dimensions(n, types):
    if n <= 1:
        return types()
    return defaultdict(lambda: multi_dimensions(n - 1, types))


m = multi_dimensions(5, Counter)
m['d1']['d2']['d3']['d4']['d5'] = 1
m['a1']['a2'] = 2
print(m['d1']['d2']['d3']['d4']['d5'])
print(m['a1']['a2'])


# 利用collections模块defaultdict方法的特性,利用外部函数来实现
def site_struct():
    return defaultdict(board_struct)


def board_struct():
    return defaultdict(user_struct)


def user_struct():
    return dict(pageviews=0, username='', comments=0)


d = defaultdict(site_struct)

d['site']['board']['username'] = 1
d['par']['chl']['username'] = 'a'
print(d['site']['board']['username'])
print(d['par']['chl']['username'])
