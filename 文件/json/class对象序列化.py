# -*- coding: utf-8 -*-
__author__ = 'luointo'

import json

"""
class对象序列化
"""


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)

# 方法一
print(json.dumps(s, default=student2dict))

# 方法二
print(json.dumps(s, default=lambda obj: obj.__dict__))

print("=" * 10)

"""
把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
"""


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
data = json.loads(json_str, object_hook=dict2student)
print(data)
print(data.name)
