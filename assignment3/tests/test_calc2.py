import pytest
from calculator import multiply, divide, factorial

def test_multiply_positive():
    assert multiply(4, 5) == 20

def test_multiply_by_zero():
    assert multiply(7, 0) == 0

def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)