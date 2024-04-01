# -*- coding: utf-8 -*-
__author__ = 'luointo'

import os
import time
import random
from multiprocessing import Pool

"""
使用进程池（非阻塞）

Pool 对象调用 join() 方法会等待所有子进程执行完毕，调用 join() 之前必须先调用 close() 
调用close() 之后就不能继续添加新的 Process 了。

注意输出的结果，task0，1，2，3是立刻执行的，而task4要等待前面某个task完成后才执行，
这是因为Pool的默认大小设置成了4(p = Pool(4))，代表着最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
如果改成: p = Pool(5) 就可以跑5个进程了, 由于Pool的默认大小是CPU的核数，如果你拥有8核CPU，提交至少9个子进程才能看到上面的等待效果
"""


def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))


if __name__ == '__main__':
    print('主进程的 PID：{0}'.format(os.getpid()))
    p = Pool(4)  # 同时跑4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    p.close()  # 调用 join() 之前必须先调用 close() ，调用close() 之后就不能继续添加新的 Process 了
    p.join()  # 等待所有子进程结束后在关闭主进程
    print('end')
