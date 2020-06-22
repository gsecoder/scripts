"""多个参数"""
import pytest


@pytest.fixture()
def login(request):
    param = request.param
    print(f"账号是：{param['username']}, 密码是：{param['passwd']}")
    return param

data = [
    {"username": "crisimple1", "passwd": "123456"},
    {"username": "crisimple2", "passwd": "654321"},
]

@pytest.mark.parametrize("login", data, indirect=True)
def test_login(login):
    print(f"账号是：{login['username']}，密码是：{login['passwd']}")