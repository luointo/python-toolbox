# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
动态参数

动态参数就是传入的参数的个数是动态的，可以是1个、2个到任意个，还可以是0个。在不需要的时候，你完全可以忽略动态函数，不用给它传递任何值

Python的动态参数有两种，分别是*args和**kwargs，
这里面的关键是一个和两个星号的区别，而不是args和kwargs在名字上的区别，
实际上你可以使用*any或**whatever的方式。但就如self一样，默认大家都使用*args和**kwargs

注意：动态参数，必须放在所有的位置参数和默认参数后面！
"""


def func1(name, age, sex='male', *args, **kwargs):
    pass


"""
*args
可变参数
一个星号表示接收任意个参数。调用时，会将实际参数打包成一个元组传入形式参数。如果参数是个列表，会将整个列表当做一个参数传入
通过循环args，我们可以获得传递的每个参数。
但是li这个列表，我们本意是让它内部的1,2,3分别当做参数传递进去，但实际情况是列表本身被当做一个整体给传递进去了。
怎么办呢？使用一个星号！调用函数，传递实参时，在列表前面添加一个星号就可以达到目的了。
实际情况是，不光列表，任何序列类型数据对象，比如字符串、元组都可以通过这种方式将内部元素逐一作为参数，传递给函数。
而字典，则会将所有的key逐一传递进去。

*args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
"""


def func2(*args):
    for arg in args:
        print(arg)


func2('a', 'b', 'c')

li = [1, 2, 3]
func2(li)
func2(*li)

print("=" * 10)

"""
**kwargs
关键字参数
两个星表示接受键值对的动态参数，数量任意。调用的时候会将实际参数打包成字典
"""


def func3(**kwargs):
    for kwg in kwargs:
        print(kwg, type(kwg), kwargs[kwg])


func3(k1='v1', k2=[0, 1, 2])

dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func3(**dic)

print("=" * 10)

"""
万能参数
当*args和**kwargs组合起来使用，理论上能接受任何形式和任意数量的参数，在很多代码中我们都能见到这种定义方式。
需要注意的是，*args必须出现在**kwargs之前
"""


def func4(*args, **kwargs):
    for arg in args:
        print(arg)

    for kwg in kwargs:
        print(kwg, kwargs[kwg])


lis = [1, 2, 3]
dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func4(*lis, **dic)

print("=" * 10)

"""
命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
"""


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person('Jack', 24, 'Beijing', 'Engineer')  # 报错

# 命名关键字参数可以有缺省值，从而简化调用
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person3(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
