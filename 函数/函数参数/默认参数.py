# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
默认参数

在函数定义时，如果给某个参数提供一个默认值，这个参数就变成了默认参数，不再是位置参数了。
在调用函数的时候，我们可以给默认参数传递一个自定义的值，也可以使用默认值
"""


def power(x, n=2):
    return x ** n


ret1 = power(10)  # 使用默认的参数值n=2
ret2 = power(10, 4)  # 将4传给n，实际计算10**4的值


# 默认参数必须在位置参数后面
# 这是一个错误的例子
# def power(n = 2,x):
#     return x**n

# 当有多个默认参数的时候，通常将更常用的放在前面，变化较少的放后面
def student1(name, sex, age, classroom="101", tel="88880000", address="..."):
    pass


# 在调用函数的时候，尽量给实际参数提供默认参数名
def student(name, sex, age, classroom="101", tel="88880000", address="..."):
    pass


student('jack', 'male', 17)  # 其它全部使用默认值
student('tom', 'male', 18, '102', '666666', 'beijing')  # 全部指定默认参数的值
student('mary', 'female', 18, '102', tel='666666')  # 挑着来

# 这是错误的参数传递方式,因为一切没有提供参数名的实际参数，都会当做位置参数按顺序从参数列表的左边开头往右匹配
# student('mary', 'female', 18, tel='666666', 'beijing')

student("mary", "female", 18, tel="666666", address="beijing")


# 使用参数名传递参数
def student2(name, age, classroom, tel, address="..."):
    pass


student2(classroom=101, name="Jack", tel=66666666, age=20)
