# -*- coding: utf-8 -*-
__author__ = 'luointo'

import time

last_time = time.time()

while True:
    if time.time() - last_time > 2:
        last_time = time.time()
        print(last_time)


# from datetime import datetime, timedelta
#
# last_time = None
#
# print(last_time)
# print(datetime.now())
# print("===")
# while True:
#     if last_time is None or last_time + timedelta(seconds=2) < datetime.now():
#         last_time = datetime.now()
#
#         print(last_time)

