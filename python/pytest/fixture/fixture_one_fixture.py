"""多个fixture，只加一个装饰器"""
import pytest

@pytest.fixture(scope="function")
def input_user(request):
    user = request.param
    print("登录账号为：%s" % user)
    return user

@pytest.fixture(scope="function")
def input_pwd(request):
    pwd = request.param
    print("登录密码为：%s" % pwd)
    return pwd

data = [
    ("name1", "pwd1"),
    ("name2", "pwd2")
]

@pytest.mark.parametrize("input_user, input_pwd", data, indirect=True)
def test_more_fixture(input_user, input_pwd):
    print("fixture返回的内容:", input_user, input_pwd)