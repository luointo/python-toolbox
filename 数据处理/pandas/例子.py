# -*- coding: utf-8 -*-
__author__ = 'luointo'

# pandas 秒天秒地
# 条件有限的时候再考虑别的
# import pandas as pd
# import numpy as np
#
# df = pd.read_clipboard()
# df = pd.read_csv(data_or_path)
# df = pd.read_html(data_or_path)
# df = pd.read_json(data_or_path)
# df = pd.read_msgpack(data_or_path)
# df = pd.read_pickle(data_or_path)
#
# df.to_clipboard()
# df.to_csv()
# df.to_csv(fn)
# df.to_excel(fn)
# df.to_html()
# df.to_html(fn)
# df.to_json()
# df.to_json(fn)
# df.to_msgpack()
# df.to_msgpack(fn)
# df.to_pickle(fn)

# 转 dict 时 orient
# orient : str {‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’}
# Determines the type of the values of the dictionary.
#    dict (default) : dict like {column -> {index -> value}}
#    list : dict like {column -> [values]}
#    series : dict like {column -> Series(values)}
#    split : dict like {index -> [index], columns -> [columns], data -> [values]}
#    records : list like [{column -> value}, ... , {column -> value}]
#    index : dict like {index -> {column -> value}}


# 转 json 时 orient
# orient : string
# The format of the JSON string
#    split : dict like {index -> [index], columns -> [columns], data -> [values]}
#    records : list like [{column -> value}, ... , {column -> value}]
#    index : dict like {index -> {column -> value}}
#    columns : dict like {column -> {index -> value}}
#    values : just the values array
#    table : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data,
#            and the data component is like orient='records'.
