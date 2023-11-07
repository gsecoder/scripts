import pytest

"""笛卡尔积，组合数据"""
data_1 = [1, 2, 3]
data_2 = ['a', 'b']


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print(f'笛卡尔积 测试数据为 ： {a}，{b}')