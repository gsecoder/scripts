import pytest

pexpect = pytest.importorskip("pexpect", minversion="0.3")


@pexpect
def test_import():
    print("test")