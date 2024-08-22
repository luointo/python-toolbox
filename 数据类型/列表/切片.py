# -*- coding: utf-8 -*-
__author__ = 'luointo'

str_list = [3, 4, 5, 6, 7, 8, 9]
new_1 = str_list[1:3]  # 从索引1开始取，取到索引3
new_2 = str_list[0:6:2]  # 从索引0开始取，每两位一取，到第6位为止
new_3 = str_list[-2:]  # 取后面2个数
new_4 = str_list[:3]  # 取前面3个数
new_5 = str_list[::3]  # 所有数，每3个取一个

print(new_1, new_2, new_3, new_4, new_5)
