# -*- coding: utf-8 -*-
__author__ = 'luointo'

import asyncio
import sys

file_name = "copy_python-3.9.6-docs-text.zip"
file_size = 0


async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    data = await reader.read(4096)
    print(f'{data.decode()}')

    with open(file=file_name, mode="wb") as f:
        while not reader.at_eof():
            data = await reader.read(4096)

            global file_size
            file_size += sys.getsizeof(data) / 1024 / 1024

            print(f"已下载: {round(file_size, 2)}M")

            f.write(data)

    writer.write("下载完成".encode())
    writer.close()  # 关闭连接
    await writer.wait_closed()


asyncio.run(tcp_client())
