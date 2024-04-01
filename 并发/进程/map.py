# -*- coding: utf-8 -*-
__author__ = 'luointo'

from multiprocessing import Pool

"""
Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。 
注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
"""


def f(num):
    print(num)
    return num * 10


if __name__ == '__main__':
    p = Pool(4)  # 同时跑4个进程

    data_list = [3, 4, 2, 1, 6]

    res = p.map(f, data_list)

    p.close()  # 调用 join() 之前必须先调用 close() ，调用close() 之后就不能继续添加新的 Process 了
    p.join()  # 等待所有子进程结束后在关闭主进程

    print(res)
