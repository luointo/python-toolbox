# -*- coding: utf-8 -*-
__author__ = 'luointo'

# unicode字符转成中文显示

a = '\u8fd9\u4e09\u4e2a\u5b69\u5b50\u90fd\u6b20\u6536\u62fe\uff0c\u4e0d\u4f1a\u505a\u4eba\u3002","abstract:'

# 方法1：使用eval
b = eval("u" + "\'" + a + "\'")
print(b)

# python2
# 方法2：使用decode将a解码 即解码成对应的汉字 但是abstract不是unicode编码 故不能按此解码 会报错
# c = a.decode('unicode_escape')
# print(c)

# 方法3（最佳）：先将a编码成utf-8,再按utf-8解码 就能得到对应的中文字符串（原始字符串）
d = a.encode('utf-8').decode('utf-8')
print(d)


# python2
# s = u'中文'
# s1 = s.encode('utf-8')  # unicode to str
# print s, type(s)
# print s1, type(s1)