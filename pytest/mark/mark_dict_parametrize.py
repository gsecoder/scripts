"""字典"""
import pytest

data_1 = (
    {
        'users': 1,
        'pwd': 2
    },
    {
        'users': 3,
        'pwd': 4
    }
)


@pytest.mark.parametrize('dic', data_1)
def test_parametrize_1(dic):
    print(f'测试数据为\n{dic}')
    print(f'users:{dic["users"]},pwd{dic["pwd"]}')