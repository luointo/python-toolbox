# -*- coding: utf-8 -*-
__author__ = 'luointo'

import random
import string


def make_passwd(passwd_len):
    # 传入参数a，表示要生成几位数密码
    # 创建一个包含4个字符串的列表，4个字符串分别是：数字0~9，小写字母a~z，大写字母A~Z，自定义特殊符号
    char = [
        string.digits.replace("0", "").replace("1", ""),
        string.ascii_lowercase.replace("o", "").replace("i", "").replace("l", ""),
        string.ascii_uppercase.replace("O", "").replace("I", "").replace("L", ""),
        """!#$%&*().?+"""
    ]
    passwd = []  # 创建一个空列表
    for i in range(0, 4):  # 循环4次,确保每种类型字符至少有1个
        passwd.append(str(random.choice(char[i])))
    for i in range(0, passwd_len - 1 - 4):  # 循环剩余位数,确保接下来获取到每种字符概率相同
        passwd.append(str(random.choice(random.choice(char))))

    random.shuffle(passwd)  # 随机打乱列表passwd中元素的次序
    passwd.insert(0, str(random.choice(char[1])))
    passwd = ''.join(passwd)
    return passwd


if __name__ == '__main__':
    print(make_passwd(16))
