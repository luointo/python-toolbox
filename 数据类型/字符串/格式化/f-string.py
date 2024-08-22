# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
f-string

前缀f的字符串中向{}内直接填入要嵌入的值、变量或计算表达式
"""
import math
import datetime

print(f'1 + 1 = {2}')
a = 1 + 1
print(f'1 + 1 = {a}')
print(f'1 + 1 = {1 + 1}')

# 控制浮点数精度
pi = math.pi
print(f'输出π：{pi}')  # 输出π
print(f'输出π小数点后2位：{pi:.2f}')  # 截取π的小数点后2位并输出
print(f'输出π小数点后9位：{pi:.9f}')  # 截取π的小数点后9位并输出

# 设置科学计算法格式
# pix100后以科学计算法输出
print(f'输出πx100后科学计算法显示：{pi * 100:.10e}')

# 自记录表达式
# 从python3.8开始，f-string就引入了自记录表达式，
# 好处：快速的输出计算表达式。
a = 8
print(f'math.log(a) = {math.log(a)}')  # 输出math.log(a)的值

# 多行 f-string
a = 1
b = 2
c = 3
# f-string 编写多行，需要使用()
result = (f'a = {a} \n'
          f'b = {b} \n'
          f'c = {c} \n'
          )
print(f'result输出结果是：\n{result}')

# 在f-string格式化日期
now = datetime.datetime.now()
print(f'当前输出日期时间是：{now:%Y-%m-%d %H:%M:%S}')  # 输出日期时间

print("=" * 10)
# 控制有效数字位数
# 显示从左往右第一个不为0的12位数字
a = 123.4567890123456
print(f'从左往右剔除第一个为0的12个数字 ：{a:.12g}')
# 同样显示10个数字，当位数小于整数部分时，自动变成科学计数法
a = 12345678.90123456
print(f'从左往右刨除第一个为0的5个数字 ：{a:.5g}')

print("=" * 10)
# 修改为左对齐
# f-string默认为右对齐
# 使用来"<"修改显示模式为左对齐
for j in range(1, 11):
    print(f'{j:<2}|{j ** 3:<4}|{j ** 6:<7}')  # 修改显示模式为左对齐
    # print(f'{j:2}|{j ** 3:4}|{j ** 6:7}') # 默认显示为右对齐

print("=" * 10)
# 标准化显示宽度
for j in range(1, 11):
    print(f'{j:02}|{j ** 3:4}|{j ** 5:6}')  # 第一列都占两个字符
    # print(f'{j:02}|{j ** 3:0004}|{j ** 5:00006}')  # 第二列都占用4个字符，第三列都占用6个字符

# 懒得再敲一遍变量名
str_value = "hello，python coders"
print(f"{ str_value = }")
# str_value = 'hello，python coders'

# 直接改变输出结果
num_value = 123
print(f"{num_value % 2 = }")
# num_value % 2 = 1


# 直接格式化日期
today = datetime.date.today()
print(f"{today: %Y%m%d}")
# 20211019
print(f"{today =: %Y%m%d}")
# today = 20211019

# 2/8/16 进制输出真的太简单
"""
>>> a = 42
>>> f"{a:b}" # 2进制
'101010'
>>> f"{a:o}" # 8进制
'52'
>>> f"{a:x}" # 16进制，小写字母
'2a'
>>> f"{a:X}" # 16进制，大写字母
'2A'
>>> f"{a:c}" # ascii 码
'*'
"""

# 格式化浮点数
"""
>>> num_value = 123.456
>>> f'{num_value = :.2f}' #保留 2 位小数
'num_value = 123.46'
>>> nested_format = ".2f" #可以作为变量
>>> print(f'{num_value:{nested_format}}')
123.46
"""

# 字符串对齐
"""
>>> x = 'test'
>>> f'{x:>10}'   # 右对齐，左边补空格
'      test'
>>> f'{x:*<10}'  # 左对齐，右边补*
'test******'
>>> f'{x:=^10}'  # 居中，左右补=
'===test==='
>>> x, n = 'test', 10
>>> f'{x:~^{n}}' # 可以传入变量 n
'~~~test~~~'
>>>
"""

# 使用 !s，!r
"""
>>> x = '中'
>>> f"{x!s}" # 相当于 str(x)
'中'
>>> f"{x!r}" # 相当于 repr(x)
"'中'"
"""


# 自定义格式
class MyClass:
    def __format__(self, format_spec) -> str:
        print(f'MyClass __format__ called with {format_spec=!r}')
        return "MyClass()"


print(f'{MyClass():bala bala  %%MYFORMAT%%}')
