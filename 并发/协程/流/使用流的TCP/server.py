# -*- coding: utf-8 -*-
__author__ = 'luointo'

import asyncio


async def handle(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"收到 {message!r} from {addr!r}")

    print(f"发送: {message!r}")
    writer.write(data)
    await writer.drain()

    print("关闭连接")
    writer.close()


async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'服务于 {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
