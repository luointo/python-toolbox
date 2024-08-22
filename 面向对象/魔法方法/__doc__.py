# -*- coding: utf-8 -*-
__author__ = 'luointo'

"""
__doc__
说明性文档和信息。Python自建，无需自定义
"""


class Foo:
    """ 描述类信息，可被自动收集 """

    def func(self):
        pass


# 打印类的说明文档
print(Foo.__doc__)
