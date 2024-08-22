# -*- coding: utf-8 -*-
__author__ = 'luointo'

import json
from collections import OrderedDict

s = '{"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6"}'
data = json.loads(s, object_pairs_hook=OrderedDict);
print(data)
