# test_calculator.py

def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_mixed_numbers():
    assert add(-1, 1) == 0

def add(a, b):
    return a + b