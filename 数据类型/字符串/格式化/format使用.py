# -*- coding: utf-8 -*-
__author__ = 'luointo'

from datetime import datetime

"""
format 格式转换

数字	        格式	       输出	        描述
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	3.14	带符号保留小数点后两位
-1	{:+.2f}	-1	带符号保留小数点后两位
2.71828	{:.0f}	3	不带小数
1000000	{:,}	1,000,000	以逗号分隔的数字格式
0.25	{:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00E+09	指数记法
25	{0:b}	11001	转换成二进制
25	{0:d}	25	转换成十进制
25	{0:o}	31	转换成八进制
25	{0:x}	19	转换成十六进制
5	{:0>2}	05	数字补零(填充左边, 宽度为2)
5	{:x<4}	5xxx	数字补x (填充右边, 宽度为4)
10	{:x^4}	x10x	数字补x (填充两边,优先左边, 宽度为4)
13	{:10}	13	右对齐 (默认, 宽度为10)
13	{:<10}	13	左对齐 (宽度为10)
13	{:^10}	13	中间对齐 (宽度为10)

b、d、o、x分别是二进制、十进制、八进制、十六进制
"""

# 通过位置来填充字符串
print('hello {0} i am {1}'.format('world', 'python'))
print('hello {} i am {}'.format('world', 'python'))
print('hello {0} i am {1} . a now language-- {1}'.format('world', 'python'))

# 通过key来填充
obj = 'world'
name = 'python'
print('hello, {obj} ,i am {name}'.format(obj=obj, name=name))

# 通过列表填充
list_data = ['world', 'python']
print('hello {names[0]}  i am {names[1]}'.format(names=list_data))
print('hello {0[0]}  i am {0[1]}'.format(list_data))

# 通过字典填充
dict_data = {'obj': 'world', 'name': 'python'}
print('hello {names[obj]} i am {names[name]}'.format(names=dict_data))


# 通过类的属性填充
class Names:
    obj = 'world'
    name = 'python'


print('hello {names.obj} i am {names.name}'.format(names=Names))

# 使用魔法参数
args = [',', 'inx']
kwargs = {'obj': 'world', 'name': 'python'}
print('hello {obj} {} i am {name}, {}'.format(*args, **kwargs))
print('hello {obj} {0} i am {name}, {1}'.format(*args, **kwargs))

# 转义“{}”
# 跟%中%%转义%一样，format中用 { 来转义{ ，用 } 来转义 }
print('{{hello}} {{{0}}}'.format('world'))  # 输出结果：{hello} {world}

# format作为函数变量
name = 'InX'
hello = 'hello,{} welcome to python world!!!'.format  # 定义一个问候函数
print(hello(name))

# 格式化datetime
now = datetime.now()
print('{:%Y-%m-%d %X}'.format(now))

# {}内嵌{}
print('hello {0:>{1}} '.format('world', 10))
