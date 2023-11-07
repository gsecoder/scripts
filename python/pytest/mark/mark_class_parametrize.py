import pytest

data_1 = [1, 2, 3]

@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize:

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数11111 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数22222 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect