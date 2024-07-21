import pytest
import random

def test_flag():
    flag = random.choice([True, False])
    print(flag)
    assert flag
    
@pytest.mark.repeat(5)
def test_repeat():
    print("测试用例执行")