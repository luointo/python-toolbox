# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os
import os.path as op


def get_modify_time(file):
    return os.path.getmtime(file)  # 获取文件修改时间


p_dir = op.join(op.dirname(__file__), "data")
files = [op.join(p_dir, name) for name in os.listdir(p_dir)]

files.sort(key=get_modify_time)

for i, f in enumerate(files):
    i += 1
    new_name = f"{i}.{op.basename(f)}"
    new_path = op.join(p_dir, new_name)
    os.rename(f, new_path)
    print(new_path)
