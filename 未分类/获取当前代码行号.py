# -*- coding: utf-8 -*-
__author__ = 'luointo'

import inspect

frame = inspect.currentframe()

print("行号: ", frame.f_lineno)

print("文件名: ", frame.f_code.co_filename)
