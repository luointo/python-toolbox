# -*- coding: utf-8 -*-
__author__ = 'luointo'

# Flask HttpResponse 响应体中返回 openpyxl 生成的 Excel 文档
# https://www.thetopsites.net/article/58920327.shtml

import time
from openpyxl import Workbook
from io import BytesIO
from tempfile import NamedTemporaryFile, TemporaryFile
# from openpyxl.writer.excel import save_virtual_workbook

from flask import make_response


wb = Workbook()
sheet = wb.active

sheet['A1'] = 56
sheet['A2'] = 43

now = time.strftime("%x")
sheet['A3'] = now

# content = save_virtual_workbook(wb)

with NamedTemporaryFile() as tmp:
    print(tmp.name)
    wb.save(tmp.name)
    print(123)
    a = BytesIO(tmp.read())
    print(a.getvalue())


# with NamedTemporaryFile() as tmp:
#     wb.save(tmp.name)
#     output = BytesIO(tmp.read())
#     print(output)

def save_virtual_workbook(workbook):
    with NamedTemporaryFile() as tf:
        workbook.save(tf.name)
        in_memory = BytesIO(tf.read())
        return in_memory.getvalue()


# print(save_virtual_workbook(wb))

# resp = make_response(content)
# resp.headers["Content-Disposition"] = 'attachment; filename=finance_info.xlsx'
# resp.headers['Content-Type'] = 'application/x-xlsx'

# print(resp)

# wb.save("sample.xlsx")
