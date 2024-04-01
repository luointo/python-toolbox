# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing.pool import ThreadPool

pool = ThreadPool(5)

print(pool.map(lambda x: x ** 2, range(5)))
