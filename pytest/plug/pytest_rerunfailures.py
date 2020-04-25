"""重新运行指定的测试用例"""
import pytest
import random

@pytest.mark.flasky(reruns=5)
def test_example():
    assert random.choice([True, False, False])