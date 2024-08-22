# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 读取
import pickle


class A:
    def __init__(self):
        self.name = ""

    def func(self):
        print(self.name)
        print("func")


# data = pickle.loads(open('data.pkl', 'rb').read())

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    # data = pickle.loads(f.read())
    print(data['obj'].name)
