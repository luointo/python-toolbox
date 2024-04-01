# -*- coding: utf-8 -*-
__author__ = 'luointo'

import multiprocessing


def f(i, event):
    if not event.is_set():
        print(i)
    if i == 20:
        event.set()


if __name__ == "__main__":
    p = multiprocessing.Pool(10)
    m = multiprocessing.Manager()
    event = m.Event()
    for i in range(100):
        p.apply_async(f, (i, event))
    p.close()

    event.wait()  # 我们将在这里阻塞，直到一个worker调用 event.set()
    p.terminate()  # 终止池中的所有进程
