# -*- coding: utf-8 -*-
__author__ = 'luointo'

r"""
在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意backslash '' 。
例如，\n 在raw string中，是两个字符，\和n， 而不会转意为换行符。
由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。

表示原始字符串
"""

s = r"\n"
print(s)
