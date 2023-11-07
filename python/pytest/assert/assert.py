import pytest

def f():
    return 3

def test_function():
    a = f()
    assert a % 2 == 0, "判断 a 为偶数，当前 a 的值为：%s" % a
    
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0