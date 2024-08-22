# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 推导式

# 列表推导式
# 列表推导式是一种快速生成列表的方式。其形式是用方括号括起来的一段语句
lis1 = [x * x for x in range(1, 10)]
print("列表推导式:", lis1)
lis1 = []
for x in range(1, 10):
    lis1.append(x * x)
print("列表推导式:", lis1)

# 增加条件语句
lis2 = [x * x for x in range(1, 11) if x % 2 == 0]
print("增加条件语句:", lis2)

lis2 = []
for x in range(1, 11):
    if x % 2 == 0:
        lis2.append(x * x)
print("增加条件语句:", lis2)

# 多重循环
lis3 = [a + b for a in '123' for b in 'abc']
print("多重循环:", lis3)

lis3 = []
for a in '123':
    for b in 'abc':
        lis3.append(a + b)
print("多重循环:", lis3)
