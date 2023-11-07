import sys
import pytest

if sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")