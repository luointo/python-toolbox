# -*- coding: utf-8 -*-
__author__ = 'luointo'

import re

val = "-13084, -8019"

r = r"[,| |,\s+]"

pos = re.split(r, val)

print(pos)
