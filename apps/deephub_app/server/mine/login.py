#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   login.py
@Time    :   2020/5/9 14:49
@Author  :   jiangheng
@Desc    :   
"""

import flask
# 获取参数
from flask import request, jsonify
import re
import random

# 创建 flask 对象
app = flask.Flask(__name__)

def connect_sql(sql):
    pass

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        phone_number = request.form.get("phone_number")
        phone_code = request.form.get('phone_code')
        if phone_number == "177" and phone_code == "200":
            return jsonify(
                {
                    "phone_number": phone_number,
                    "phone_code": phone_code
                }
            )
        else:
            return jsonify("check your phone number or code")
    else:
        return jsonify("please input phone number and code")

def phone_validator(re_phone_number):
    if not re.match(r"^1[3|5|6|7|8|9]+\d{9}$", re_phone_number):
        return False
    return True


@app.route('/send_phone_code', methods=["GET"])
def send_phone_code():
    if request.method == "GET":
        # 获取手机号
        phone_number = request.args.get("phone_number")
        # print("[send_phone_code]phone_number: ", phone_number)
        # print(phone_validator(17729291319))
        # 手机号合法性正则校验
        # print(phone_validator(re_phone_number=phone_number))
        if phone_validator(re_phone_number=phone_number):
            return jsonify({
                "phone_number": phone_number
            })
        else:
            return jsonify("phone number is not valid.")
    else:
        return jsonify("please check your method")

    # 生成随机验证码
    random_code = random.randint(1000, 9999)
    print(random_code)

    # 使用腾讯云短信1400367199


if __name__ == "__main__":
    app.run(port=8000, debug=True)