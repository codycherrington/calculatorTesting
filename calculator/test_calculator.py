import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-2, 2) == 0

def test_subtraction(calculator):
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(10, 5) == 5

def test_multiplication(calculator):
    assert calculator.multiply(1, 2) == 2
    assert calculator.multiply(10, 2) == 20

def test_division(calculator):
    assert calculator.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)