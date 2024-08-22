# -*- coding: utf-8 -*-
__author__ = 'luointo'

# break 语句可以跳出 for 和 while 的循环体
for letter in 'name':
    if letter == 'm':
        break
    print('当前字母为 :', letter)

var = 10
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("=" * 10)
# continue语句被用来跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for letter in 'name':
    if letter == 'm':
        continue
    print('当前字母 :', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)

print("=" * 10)
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
