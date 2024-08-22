# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os

# 获取指定目录下的文件列表包括文件和目录
file_list = os.listdir(".")

print(file_list)

# # 获取文件创建时间
# file_time = os.path.getmtime("file.py")
#
# # 判断文件是否是目录
# file_is_dir = os.path.isdir()
#
# # 获取文件大小
# file_size = os.path.getsize("file.py")
