# -*- coding: utf-8 -*-
__author__ = 'luointo'

import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/Home/PickerApi/catUpdatePicker', methods=["POST"])
def index():
    if request.method == "POST":
        data = request.get_data()
        # print("data:", data)
        json_data = json.loads(data.decode("utf-8"))
        print(json_data)

    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

