# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
这是迭代器方法！列表、字典、元组之所以可以进行for循环，是因为其内部定义了 __iter__()这个方法。
如果用户想让自定义的类的对象可以被迭代，那么就需要在类中定义这个方法，并且让该方法的返回值是一个可迭代的对象。
当在代码中利用for循环遍历对象时，就会调用类的这个__iter__()方法。
"""

"""
class Foo:
    pass


obj = Foo()

for i in obj:
    print(i)

# 报错：TypeError: 'Foo' object is not iterable<br># 原因是Foo对象不可迭代
"""

"""
添加一个__iter__()，但什么都不返回：

class Foo:
    def __iter__(self):
        pass

obj = Foo()

for i in obj:
    print(i)

# 报错：TypeError: iter() returned non-iterator of type 'NoneType'
#原因是 __iter__方法没有返回一个可迭代的对象
"""


# 返回一个个迭代对象
class Foo:

    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)


obj = Foo([11, 22, 33, 44])

for i in obj:
    print(i)


# 使用生成器
class Foo2:
    def __init__(self):
        pass

    def __iter__(self):
        for x in range(5):
            yield x


obj = Foo2()
for i in obj:
    print(i)
