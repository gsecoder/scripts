import pytest, allure


@allure.title("前置操作：登录")
@pytest.fixture
def test_loginss(request):
    params = request.param
    name = params["username"]
    pwd = params["pwd"]
    allure.attach(f"这是测试用例传的参数{params}")
    print(name, pwd, params)
    yield name, pwd


@allure.title("成功登录，测试数据是：{test_loginss}")
@pytest.mark.parametrize("test_loginss", [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f"账号{name},密码{pwd}")
    
@allure.title("多个参数{name},{phone},{age}")
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)