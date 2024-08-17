import requests
from flask import jsonify
import re

def test_login(test_url, method, test_data):
    if method == "POST":
        res = requests.post(
            url=test_url,
            data=test_data
        )
        print(res.text)
    elif method == "GET":
        res = requests.get(
            url=test_url,
            data=test_data
        )
        print(res.text)
    else:
        return jsonify("developing")

def test_send_phone_code(test_url, method, test_data):
    if method == "GET":
        res = requests.get(
            url=test_url,
            params=test_data
        )
        print(res.text)
    else:
        return jsonify("developing")

def phone_validator(re_phone_number):
    if not re.match(r"^1[3|5|6|7|8|9]\d{9}$", re_phone_number):
        return False
    return True


if __name__ == "__main__":
    # print(phone_validator("17729291319"))
    params = {
        "phone_number": 177,
        "phone_code": 200
    }
    login_url = "http://127.0.0.1:8000/login"
    # test_login(login_url, "POST", params)

    params_1 = {
        "phone_number": 13729291319
    }
    send_phone_code_url = "http://127.0.0.1:8000/send_phone_code"
    test_send_phone_code(send_phone_code_url, "GET", params_1)


