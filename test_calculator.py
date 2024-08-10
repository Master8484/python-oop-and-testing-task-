import pytest
from calculator import Calculator


def test_calculator_init():
    calc = Calculator()
    assert calc.get_value() == 0


def test_calculator_add():
    calc = Calculator()
    assert calc.add(5) == 5
    assert calc.add(3) == 8


def test_calculator_subtract():
    calc = Calculator()
    calc.add(10)
    assert calc.subtract(3) == 7
    assert calc.subtract(2) == 5


def test_calculator_multiply():
    calc = Calculator()
    calc.add(5)
    assert calc.multiply(3) == 15
    assert calc.multiply(2) == 30


def test_calculator_divide():
    calc = Calculator()
    calc.add(10)
    assert calc.divide(2) == 5
    assert calc.divide(1) == 5


def test_calculator_divide_by_zero():
    calc = Calculator()
    calc.add(10)
    with pytest.raises(ZeroDivisionError):
        calc.divide(0)


def test_calculator_reset():
    calc = Calculator()
    calc.add(10)
    assert calc.reset() == 0
