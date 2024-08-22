# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 读取
import json

data = json.loads(open('data.json', 'r').read())

print(data)
