# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
进程启动的开销比较大，过多的创建新进程会消耗大量的内存空间。仿照线程池的做法，我们可以使用进程池控制内存开销。

比较幸运的是，Python给我们内置了一个进程池，不需要像线程池那样要自己写，你只需要简单的from multiprocessing import Pool导入就行。
进程池内部维护了一个进程序列，需要时就去进程池中拿取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中常用的方法：
    apply() 同步执行（串行）
    apply_async() 异步执行（并行）
    terminate() 立刻关闭进程池
    join() 主进程等待所有子进程执行完毕。必须在close或terminate()之后。
    close() 等待所有进程结束后，才关闭进程池。

"""

from multiprocessing import Pool
import time


def func(args):
    time.sleep(1)
    print("正在执行进程 ", args)


if __name__ == '__main__':

    p = Pool(5)  # 创建一个包含5个进程的进程池

    for i in range(30):
        p.apply_async(func=func, args=(i,))

    p.close()  # 等子进程执行完毕后关闭进程池
    # time.sleep(2)
    # p.terminate()     # 立刻关闭进程池
    p.join()
