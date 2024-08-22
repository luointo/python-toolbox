# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
生成器
    创建一个生成器
    只要把一个列表生成式的[]改成()，就创建了一个generator
    使用yield关键字

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

生成器自动实现了迭代器协议，而且将输出状态挂起，有延时输出效果。
还有值得注意细节：生成器只能遍历一次，因为遍历完一次后，最终输出状态已经没了   
"""

# 创建generator，第一种方法，只要把一个列表生成式的[]改成()，就创建了一个generator
list_data = [x * x for x in range(10)]
print(type(list_data), list_data)
g = (x * x for x in range(10))
print(type(g), g)
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# generator也是可迭代对象
for x in g:
    print(x)

print("=" * 10)


def create_counter(n):
    print("create_counter")
    while True:
        yield n
        print("增加 n")
        n += 1


gen = create_counter(2)
print(gen)
print(next(gen))
print(next(gen))


# 生成器函数yeild
def gen_squares(n):
    for i in range(n):
        print('当前的元素为', i)
        yield i * i


for item in gen_squares(5):
    print(item)
