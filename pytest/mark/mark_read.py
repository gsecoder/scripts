"""增加可读性"""
import pytest

data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]

@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect