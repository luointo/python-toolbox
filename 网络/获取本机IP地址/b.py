# -*- coding: utf-8 -*-
__author__ = 'luointo'

import socket

"""
亲测本方法在windows和Linux系统下均可正确获取IP地址
"""


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == '__main__':
    print(get_host_ip())
