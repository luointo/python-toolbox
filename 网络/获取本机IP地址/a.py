# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
获取本机IP地址
"""

# 通常使用socket.gethostbyname()方法即可获取本机IP地址，但有时候获取不到(比如没有正确设置主机名称)
import socket

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)
