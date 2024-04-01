# -*- coding: utf-8 -*-
__author__ = 'luointo'

import asyncio

"""
使用流的 TCP 回显客户端
"""


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'发送: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'收到: {data.decode()!r}')

    print('关闭连接')
    writer.close()


asyncio.run(tcp_echo_client('Hello World!'))
