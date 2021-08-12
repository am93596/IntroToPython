from calculator import SciCalculator

c = SciCalculator()

def test_find_sqrt():
    assert c.find_sqrt(100) == 10
    assert c.find_sqrt(None) is None
    assert c.find_sqrt(25) == 5

def test_find_ceil():
    assert c.find_ceil(12.7) == 13
    assert c.find_ceil(3.14) == 4

