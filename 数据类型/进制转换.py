# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
↓	2进制	8进制	10进制	16进制
2进制	-	bin(int(x, 8))	bin(int(x, 10))	bin(int(x, 16))
8进制	oct(int(x, 2))	-	oct(int(x, 10))	oct(int(x, 16))
10进制	int(x, 2)	int(x, 8)	-	int(x, 16)
16进制	hex(int(x, 2))	hex(int(x, 8))	hex(int(x, 10))	-
"""

# 2 to 16 (去掉0x)
a = format(int("01000001", 2), "x")
b = f"{a:0>2}"
print(b)

# 16 to 2 (去掉0b 最前面补零 八位)
c = format(int("7F", 16), "b")
d = f"{c:0>8}"
print(d)

# Byte 2-7 XOR
a = bytearray(b'\x85\x01\x7f\x00\x7f\x06\x28\x2f')
e = 0
for x in a[1:7]:
    e = e ^ x
a[7] = e
print("e:", e)
print("a:", a)

# 十六进制字符串转byte
a = bytes.fromhex("85 01 7F 00 7F 06 28 2F")
print(a)

# 二进制字符串转byte
a = bytes().fromhex("01000001")
print(a)

print("=" * 10)
# 整数之间的进制转换
# 10进制转16进制: hex(16) ==> 0x10
# 16进制转10进制: int('0x10', 16) ==> 16

# 字符串转整数
# 10进制字符串: int('10') ==> 10
# 16进制字符串: int('10', 16) ==> 16
# 16进制字符串: int('0x10', 16) ==> 16

# 字节串转整数
# 转义为short型整数: struct.unpack('<hh', bytes(b'\x01\x00\x00\x00')) ==> (1, 0)
# 转义为long型整数: struct.unpack('<L', bytes(b'\x01\x00\x00\x00')) ==> (1,)

# 整数转字节串
# 转为两个字节: struct.pack('<HH', 1,2) ==> b'\x01\x00\x02\x00'
# 转为四个字节: struct.pack('<LL', 1,2) ==> b'# \x01\x00\x00\x00\x02\x00\x00\x00'

# 字符串转字节串
"""
字符串编码为字节码: '12abc'.encode('ascii') ==> b'12abc'
数字或字符数组: bytes([1,2, ord('1'),ord('2')]) ==> b'\x01\x0212'
16进制字符串: bytes().fromhex('010210') ==> b'\x01\x02\x10'
16进制字符串: bytes(map(ord, '\x01\x02\x31\x32')) ==> b'\x01\x0212'
16进制数组: bytes([0x01,0x02,0x31,0x32]) ==> b'\x01\x0212'
"""

# 字节串转字符串
"""
字节码解码为字符串: bytes(b'\x31\x32\x61\x62').decode('ascii') ==> 12ab
字节串转16进制表示,夹带ascii: str(bytes(b'\x01\x0212'))[2:-1] ==> \x01\x0212
字节串转16进制表示,固定两个字符表示: str(binascii.b2a_hex(b'\x01\x0212'))[2:-1] ==> 01023132
字节串转16进制数组: [hex(x) for x in bytes(b'\x01\x0212')] ==> ['0x1', '0x2', '0x31', '0x32']
"""

# str->bytes
a = "你好".encode("utf-8")  # encode()
print(a)
a = bytes("你好", encoding="utf-8")  # bytes()
print(a)

print("=" * 10)
# bytes->str
b = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode("utf-8")
print(b)
b = str(b'\xe4\xbd\xa0\xe5\xa5\xbd', encoding="utf-8")
print(b)
