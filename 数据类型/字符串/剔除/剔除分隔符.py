# -*- coding: utf-8 -*-
__author__ = 'luointo'

import itertools

# 剔除分隔符
s = ''.join('A|B|C|D|E|F|G'.split('|'))
print(s)

s = ''.join(itertools.islice('A|B|C|D|E|F|G', 6, None, 2))
print(s)

s = ''.join(itertools.islice('A|B|C|D|E|F|G', 0, None, 2))
print(s)
