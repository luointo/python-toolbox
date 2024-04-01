# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
生成器（generator）

yield和send理解为挂起
send（n）理解为：挂起，然后把n传递为上次挂起yield表达式的返回值，继续yield后面的语句运行
再次循环到yield r，理解为：挂起，刚刚挂起的send（n）恢复，此时，把r传递为send（n）的返回值，继续send（n）之后的语句运行 4.循环往下....

一句话总结：send的参数为上次挂起的yield表达式的返回值，send的返回值为当前yiled的表达式的值。
"""


def consumer():  # 定义消费者，由于有yeild关键词，此消费者为一个生成器
    # 2. 然后，一旦生产了东西，通过c.send(n)切换到consumer执行
    r = ""  # 初始化返回结果，并在启动消费者时，返回给生产者
    while True:
        n = yield r  # 3. consumer通过yield拿到消息，处理，又通过yield把结果传回
        if not n:
            return
        print("消费者 %s" % n)
        r = "200 ok"  # 消费者消费结果，下个循环返回给生产者


def producer(c):  # 定义生产者，此时的 c 为一个生成器
    c.send(None)  # 1.首先调用c.send(None)启动生成器 4. producer拿到consumer处理的结果，继续生产下一条消息
    n = 0
    while n < 5:
        n += 1
        print("生产者 %s" % n)
        r = c.send(n)  # 向消费者发送消息并准备接收结果。此时会切换到消费者执行
        print("消费者返回 %s" % r)

    c.close()  # 5. producer决定不生产了，通过c.close()关闭consumer，整个过程结束


c = consumer()
producer(c)
