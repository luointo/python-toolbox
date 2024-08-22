# -*- coding: utf-8 -*-
__author__ = 'luointo'

import json

data = {
    "a": 1,
    "b": ["s1", "s2", 33],
    "c": {
        "x": "x",
        "y": "y",
    }
}

filename = "data.json"
with open(filename, 'w') as f:
    f.write(json.dumps(data))
