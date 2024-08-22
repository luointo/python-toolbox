# -*- coding: utf-8 -*-

"""
@author: luointo
@time: 2021/7/25 14:56
"""

import requests

url = "http://192.168.134.106:30879/v2/config/feature/base_features/30001"

payload = ""
headers = {
  'X-User-Id': 'admin',
  'X-Auth-Token': '111111',
  'X-Is-Admin': 'True'
}

for x in range(100):
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
