# -*- coding: utf-8 -*-
__author__ = 'luointo'

from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import time

"""
wait方法可以让主线程阻塞，直到满足设定的要求

wait方法接收3个参数，等待的任务序列、超时时间以及等待条件。
等待条件return_when默认为ALL_COMPLETED，表明要等待所有的任务都结束。
可以看到运行结果中，确实是所有任务都完成了，主线程才打印出main。等待条件还可以设置为FIRST_COMPLETED，表示第一个任务完成就停止等待

"""


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]  # 并不是真的url
all_task = [executor.submit(get_html, url) for url in urls]
# wait(all_task, return_when=ALL_COMPLETED)
wait(all_task, return_when=FIRST_COMPLETED)
print("main")

# 执行结果
# get page 2s finished
# get page 3s finished
# get page 4s finished
# main
