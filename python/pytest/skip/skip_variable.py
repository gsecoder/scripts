import pytest
import sys


# 标记
skipmark = pytest.mark.skip(reason="不能在window上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")


@skipmark
class TestSkip_Mark(object):

    @skipifmark
    def test_function(self):
        print("测试标记")

    def test_def(self):
        print("测试标记")


@skipmark
def test_skip():
    print("测试标记")