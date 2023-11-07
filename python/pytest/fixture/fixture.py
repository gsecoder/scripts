import pytest

@pytest.fixture
def login():
    print("请输入帐号和密码")
    
def test_s1(login):
    print("用例1,登录后进行的，操作 111")
    
"""不穿login"""
def test_s2():
    print("用例2，不需要登录，操作 222")
    
    
"""方法二"""
@pytest.fixture
def login2():
    print("please输入账号，密码先登录")


@pytest.mark.usefixtures("login2", "login")
def test_s11():
    print("用例 11：登录之后其它动作 111")
    
    
"""方法三"""
@pytest.fixture(autouse=True)
def login3():
    print("====auto===")


"""不是test开头，加了装饰器也不会执行fixture"""
@pytest.mark.usefixtures("login2")
def test_loginss():
    print(123)