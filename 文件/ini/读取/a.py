# -*- coding: utf-8 -*-
__author__ = 'luointo'

import configparser

cfg = configparser.ConfigParser()

cfg.read("config.ini", encoding="utf-8")  # 用config对象读取配置文件

sections = cfg.sections()  # 以列表形式返回所有的section
print(sections)

options = cfg.options("server")  # 得到指定section的所有option
print(options)

items = cfg.items("server")  # 得到指定section的所有键值对
print(items)

get_val = cfg.get("server", "port")  # 指定section，option读取值, str
print(get_val, type(get_val))

get_int_val = cfg.getint("server", "port")  # 指定section，option读取值, int
print(get_int_val, type(get_int_val))
