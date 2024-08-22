# -*- coding: utf-8 -*-
__author__ = 'luointo'

import configparser

cfg = configparser.ConfigParser()

# 添加一个select
cfg.add_section("server")

cfg.set("server", "ip", "127.0.0.1")
cfg.set("server", "port", "8080")

# 保存
with open("config.ini", "w") as f:
    cfg.write(f)
