# -*- coding: utf-8 -*-
__author__ = 'luointo'

import asyncio

file_name = "python-3.9.6-docs-text.zip"


async def handle_echo(reader, writer):
    writer.write(f"下载文件名为:{file_name}".encode())
    await writer.drain()

    with open(file=file_name, mode="rb") as f:
        while True:
            data = f.read(4096)
            if data:
                writer.write(data)
                await writer.drain()
            else:
                writer.write_eof()
                break

    data = await reader.read(4096)
    message = data.decode()
    print(message)

    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
