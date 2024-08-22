# -*- coding: utf-8 -*-
__author__ = 'luointo'

import queue
import collections

"""
Python提供的所有队列类型
先进先出队列 queue.Queue
后进先出队列 queue.LifoQueue (Queue的基础上进行的封装)
优先级队列 queue.PriorityQueue (Queue的基础上进行的封装)
双向队列 collections.deque()
"""

# 先进先出队列
q = queue.Queue()
a = q.empty()  # empty如果队列为空，返回True
print(a)
q = queue.Queue(1)  # 指定队列大小
q.put("a")
a = q.full()  # full如果队列满了，返回True
print(a)
print(q.qsize())  # 获取当前队列长度
# q = queue.Queue()
# q.put("b", timeout=2)  # 超时时间为2秒
# q.get(timeout=1) # 超时时间为1秒
# q.put_nowait(1) # put_nowait（立即放入一个元素，不等待）
# q.get_nowait()  # get_nowait（立即取出一个元素，不等待）
# q.put('PolarSnow', block=False)  # 设置队列不阻塞(当队列满的时候再插入数据,直接报错)
# q.get(block=False) # 设置不阻塞（get）
print(q.get())

# 后进先出队列
q = queue.LifoQueue()
q.put('a')
q.put('b')
print(q.get())

# 优先级队列
# 数字越小优先级越高，数字相同，先进先出
q = queue.PriorityQueue()
q.put((1, 'a'))
q.put((0, 'b'))
print("优先级队列:", q.get())

# 双向队列
q = collections.deque()
q.append('a')  # 在右侧追加
q.append('b')
print(q)
q.appendleft('c')  # 在左侧追加
print(q)
print(q.pop())  # 从右侧取
print(q.popleft())  # 从左侧取
q.clear()  # clear(清空队列)
print(q)
q.append(1)
q.append(2)
q.append(1)
print(q.count(1))  # count(返回指定元素的出现次数)
q.extend([3, 4, 5])  # extend(从队列右边扩展一个列表的元素)
q.extendleft([7, 8])  # extendleft(从队列左边扩展一个列表的元素)
print(q)
print(q.index(3))  # index（查找某个元素的索引位置）
print(q.index(7, 0, 3))  # 指定查找区间
q.insert(3, "a")  # insert（在指定位置插入元素）
print(q)
a = q.pop()  # pop（获取最右边一个元素，并在队列中删除）
print(a, q)
a = q.popleft()  # popleft（获取最左边一个元素，并在队列中删除）
print(a, q)
q.remove("a")  # remove（删除指定元素）
print(q)
q.reverse()  # reverse（队列反转）
print(q)
q.rotate(2)  # rotate（把右边元素放到左边）指定次数，默认1次
print(q)

if __name__ == '__main__':
    q = queue.Queue()
    try:
        a = q.get(timeout=1)
    except queue.Empty:
        print("empty")
