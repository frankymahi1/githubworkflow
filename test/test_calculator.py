# test_calculator.py

from .calculator import add


def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_mixed_numbers():
    assert add(-1, 1) == 0
