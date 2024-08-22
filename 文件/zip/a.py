# -*- coding: utf-8 -*-
__author__ = 'luointo'

import zipfile

z = zipfile.ZipFile("test.zip", "r")
for filename in z.namelist():
    bys = z.read(filename)
    print(f"文件名:{filename} 内容:{str(bys)}")
