import pytest

@pytest.fixture(scope="session")
def open():
    print("===打开浏览器===")

@pytest.fixture
# @pytest.mark.usefixtures("open") 不可取！！！不生效！！！
def test_login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")