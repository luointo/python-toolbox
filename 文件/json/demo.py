# -*- coding: utf-8 -*-
__author__ = 'luointo'

import json

# dumps 把python对象转换为json字符串
j = [1, 2, "abc", {"name": "Bob", "age": 18}]
res = json.dumps(j)
print(res)

# indent是缩进的意思一般写为4或者2
# separators 是(‘元素之间用逗号隔开’ ， ‘key和内容之间’ 用冒号隔开)
res = json.dumps(j, indent=2, separators=(',', ': '))
print(res)

d = {"b": None, "a": 5, "c": "abc"}
res = json.dumps(d, sort_keys=True)  # 排序
print(res)

# loads 把json字符串转换为python对象
res = json.loads('[1,2,"abc",{"name":"Bob","age":18}]')
print(res)
# # dump 把python对象存入到json文件中
# with open("demo.json", "w") as f:
#     json.dump(j, f)
#
# with open("demo.json", "r") as f:
#     res = json.load(f)
#     print(res)
