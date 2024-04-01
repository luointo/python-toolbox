# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
进程通信

Pipe 管道
Pipe方法返回(conn1, conn2)代表一个管道的两个端。
Pipe方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发。
duplex为False，conn1只负责接受消息，conn2只负责发送消息。

send和recv方法分别是发送和接受消息的方法。
例如，在全双工模式下，可以调用conn1.send发送消息，conn1.recv接收消息。
如果没有消息可接收，recv方法会一直阻塞。如果管道已经被关闭，那么recv方法会抛出EOFError。
"""

import multiprocessing
import time


def proc_send(p):
    for i in range(5):
        print("发送:{}".format(i))
        p.send(i)
        time.sleep(1)


def proc_recv(p):
    while True:
        print("接收:{}".format(p.recv()))
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个管道　这个管道是双向的
    pipe = multiprocessing.Pipe()
    # pipe[0]　表示管道的一端，pipe[1] 表示管道的另外一端
    # 对pipe的某一端调用send方法来传送对象，在另外一端使用recv来接收
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p1.join()
