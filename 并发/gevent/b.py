# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time
import gevent
from gevent import monkey

monkey.patch_all()


def get(val):
    time.sleep(1)
    return val ** 2


g_list = []
for x in range(5):
    g = gevent.spawn(get, x)
    g_list.append(g)

gevent.joinall(g_list)
for g in g_list:
    print(g.value)
