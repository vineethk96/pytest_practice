import pytest

@pytest.mark.parametrize("varName, output", [(1,11), (2, 22), (3, 33)])
def test_mult_11(varName, output):
    assert 11 * varName == output