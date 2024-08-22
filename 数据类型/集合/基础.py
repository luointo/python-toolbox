# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
set集合是一个无序不重复元素的集，基本功能包括关系测试和消除重复元素。
集合使用大括号{}框定元素，并以逗号进行分隔。
但是注意：如果要创建一个空集合，必须用 set() 而不是 {} ，因为后者创建的是一个空字典。
集合除了在形式上最外层用的也是花括号外，其它的和字典没有一毛钱关系

集合数据类型的核心在于自动去重
集合既不支持下标索引也不支持字典那样的通过键获取值
"""

list_data = [1, 1, 2, 3, 3, 4]
print(set(list_data))  # 自动去重

str_data = "it is a nice day"
print(set(str_data))  # 对于字符串，集合会把它一个一个拆开，然后去重

s = {1, 2, 3, 4}
# add
s.add(5)  # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s)
# update
s.update("hello")  # 可以通过update()方法，将另一个对象更新到已有的集合中，这一过程同样会进行去重
print(s)
# del
s.remove("l")  # 通过remove(key)方法删除指定元素，或者使用pop()方法。注意，集合的pop方法无法设置参数，删除指定的元素
s.pop()
print(s)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 删除重复的
print('orange' in basket)  # 检测成员

# 两个集合的交、并、差操作
a = set('abracadabra')
b = set('alacazam')
print(a - b)  # 在 a 中的字母，但不在 b 中
print(a | b)  # 在 a 或 b 中的字母
print(a & b)  # 在 a 和 b 中都有的字母
print(a ^ b)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中


# 集合也支持推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)