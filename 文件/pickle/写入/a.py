# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 写入
import pickle


class A:
    def __init__(self):
        self.name = ""

    def func(self):
        print(self.name)
        print("func")


obj = A()
obj.name = "test name"

data = {
    "a": 1,
    "b": 2,
    "obj": obj
}

with open("data.pkl", "wb") as f:
    # f.write(pickle.dumps(data))
    pickle.dump(data, f)
