import pytest

@pytest.mark.parametrize("test_input, excepted", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, excepted):
    print(f"测试数据{test_input}, 期望结果{excepted}")
    assert eval(test_input) == excepted