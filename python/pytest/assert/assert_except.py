"""异常断言"""
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
  
"""详细断言异常"""
def test_zero_division_long_info():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0
        
    """断言异常类型"""
    assert excinfo.type == ZeroDivisionError
    
    """断言异常 value 的值"""
    assert "Division by Zero" in str(excinfo.value)
    
    
"""自定义消息"""
def test_zero_division_custom_incinfo():
    with pytest.raises(ZeroDivisionError, match="*.zero.*") as excinfo:
        1 / 0
        
        
"""异常装饰器"""
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_except_decorate():
    1 / 0