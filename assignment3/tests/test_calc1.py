import pytest
from calculator import add, subtract

def test_add_positive():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-2, -4) == -6

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-3, 5) == -8