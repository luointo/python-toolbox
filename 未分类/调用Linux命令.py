# -*- coding: utf-8 -*-
__author__ = 'luointo'

# 执行Linux Bash命令

import os
import subprocess

# system()调用
# 仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息
os.system('ls')

# popen()函数
# 不仅执行命令而且返回执行后的信息对象(常用于需要获取执行命令后的返回信息)
os.popen('ls').readlines()  # 这个返回值是一个list
now_time = os.popen('date')
print(now_time.read())

# 使用模块 subprocess
subprocess.call('ls')  # 可以直接call()调用

'''
#也可以使用subprocess.Popen
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line)

'''

# commands模块
"""
pip install commands

方法	说明
getoutput	获取执行命令后的返回信息
getstatus	获取执行命令的状态值(执行命令成功返回数值0，否则返回非0)
getstatusoutput	获取执行命令的状态值以及返回信息

import commonds
status, output = commands.getstatusoutput('date')
print(status)    # 0
print(output)    # 2016年 06月 30日 星期四 19:26:21 CST
"""
