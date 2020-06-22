import pytest

@pytest.fixture(scope="session")
def login():
    print("====登录功能，返回账号，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name, token
    print("====退出登录！！！====")


@pytest.fixture(autouse=True)
def get_info(login):
    name, token = login
    print(f"== 每个用例都调用的外层fixture：打印用户token： {token} ==")