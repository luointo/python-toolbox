# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。
对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。

可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、再使用属性名作为key检索属性值的细节。

全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
你可以把local_school看成是全局变量，但每个属性例如local_school.student都是线程的局部变量，可以任意读写而互不干扰，
也不用管理锁的问题，ThreadLocal内部会处理

可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其它变量，如local_school.teacher等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

"""

import threading

# 创建全局ThreadLocal对象：
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
