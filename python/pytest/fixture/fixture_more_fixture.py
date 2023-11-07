"""多个fixture"""
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

name = ["name1", "name2"]
passwd = ["pwd1", "pwd2"]

@pytest.mark.parametrize("input_user", name, indirect=True)
@pytest.mark.parametrize("input_pwd", passwd, indirect=True)
def test_more_fixture(input_user, input_pwd):
    print("fixture返回的内容:", input_user, input_pwd)
    