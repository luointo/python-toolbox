# -*- coding: utf-8 -*-
__author__ = 'luointo'

# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
res = bytes(s, encoding="utf8")
print("str to bytes:", res)

# bytes to str
res = str(b, encoding="utf-8")
print("bytes to str:", res)

# an alternative method
# str to bytes
res = str.encode(s)
print(res)

# bytes to str
res = bytes.decode(b)
print(res)
