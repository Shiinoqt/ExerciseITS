from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    return Calculator(10, 5)

def test_addition(calculation):
    assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, "The difference is wrong"

def test_multiplication():
    calc = Calculator(10, 5)
    assert calc.multiplication() == 50, "The product is wrong"

def test_division():
    calc = Calculator(10, 5)
    assert calc.division() == 2, "The quotient is wrong"