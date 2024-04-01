# -*- coding: utf-8 -*-
__author__ = 'luointo'

import asyncio
import time

"""
asyncio.create_task() 函数用来并发运行作为asyncio任务的多个协程

并发 运行两个 say_after 协程
预期的输出显示代码段的运行时间比之前快了 1 秒
"""


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
