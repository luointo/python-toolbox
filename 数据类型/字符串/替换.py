# -*- coding: utf-8 -*-
__author__ = 'luointo'

import re

"""
替换子串：replace()
替换多个不同的字符串：re.sub()，re.subn()
用正则表达式替换：re.sub()，re.subn()
根据位置来替换：slice()
"""

s = 'one two one two one'
# 第一个参数为替换前的参数，第二个为替换后的参数。默认会替换字符串中的所有符合条件的字符串
print(s.replace(' ', '-'))

# 指定一个最大替换次数值，一旦指定，只会替换前面匹配的n个字符串
print(s.replace('one', 'XXX', 2))

# 链式的多次调用实现同时替换多个字符串
print(s.replace('one', '1').replace('two', '2'))

# 替换多个不同的字符串： translate()
# maketrans 方法中是一个字典参数，第一个参数（key）为替换前的参数，第二个参数（value）为替换后的参数（为None表示移除替换前的参数）
print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
# 第一个和第二个参数的长度必须匹配。在两个参数的情况下，会将第一个参数的字符，依次的映射成第二个参数的字符（o-> X，w-> Y）
# 第三个参数表示在映射完的结果之后，需要移除的字符。
print(s.translate(str.maketrans('ow', 'XY')))
print(s.translate(str.maketrans('ow', 'XY', 'n')))

print("用正则表达式替换")
# 用正则表达式替换
"""
re.sub(`pattern`, `repl`, `string`, `count=0`, `flags=0`)

`pattern`, `repl`, `string` 为必选参数
`count`, `flags` 为可选参数
`pattern`正则表达式
`repl`被替换的内容，可以是字符串，也可以是函数
`string`正则表达式匹配的内容
`count`由于正则表达式匹配的结果是多个，使用count来限定替换的个数从左向右，默认值是0，替换所有的匹配到的结果
`flags`是匹配模式，
    `re.I`忽略大小写，
    `re.L`表示特殊字符集\w,\W,\b,\B,\s,\S，
    `re.M`表示多行模式，
    `re.S` ‘.’包括换行符在内的任意字符，
    `re.U`表示特殊字符集\w,\W,\b,\B,\d,\D,\s,\D
"""
s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'
# 在第一个参数中输入正则表达式，第二个参数表示需要替换的子字符串，第三个参数表示需要处理的字符串
print(re.sub(r'[a-z]*@', 'ABC@', s))
print(re.sub('[a-z]*@', 'ABC@', s, 2))  # 指定最大的替换次数为2次
print(re.sub('aaa|bbb|ccc', 'ABC', s))  # 使用同一个字符串，来替换多个子串

# 获得正则表达式匹配后的各个组合部分（分组后的）信息，可以使用 re.subn() 函数
t = re.subn('[a-z]*@', 'ABC@', s)
print(t)

print("通过位置来替换")
s = 'abcdefghij'
print(s[:4] + 'XXX' + s[7:])
s_replace = 'XXX'
i = 4
print(s[:i] + s_replace + s[i + len(s_replace):])
print(s[:4] + '-' + s[7:])
