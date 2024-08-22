# -*- coding: utf-8 -*-
__author__ = 'luointo'

import requests
from collections.abc import Iterator, Iterable

"""
实现可迭代对象和迭代器对象

实现一个迭代器对象 WeatherIterator , __next__ 方法每次返回一次城市气温
实现一个可迭代对象 WeatherIterable, __iter__方法返回一个迭代器对象
"""


class WeatherIterator(Iterator):
    """
    创建一个天气的迭代器
    """

    def __init__(self, cities):
        self.cities = cities  # 城市
        self.index = 0

    @staticmethod
    def get_weather(city):
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + city)
        data = r.json()["data"]["forecast"][0]
        return "{}, {}, {}".format(city, data["low"], data["high"])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    """
    实现可迭代对象
    """

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable(["北京", "上海", "广州"]):
    print(x)
