# Calculator Project

## Overview

This project contains a simple `Calculator` class that supports basic arithmetic operations including addition, subtraction, multiplication, and division. It also provides functionality to reset the calculator and handle division by zero errors. The project includes tests written with pytest to ensure the correctness of the class's behavior.

## Files

1. `calculator.py` – Contains the implementation of the `Calculator` class.
2. `test_calculator.py` – Contains tests for the `Calculator` class using pytest.

## Calculator Class

### Description

The `Calculator` class performs basic arithmetic operations and manages the current value.

### Methods

- **`__init__(self, value=0)`**: Initializes the calculator with a default value of 0 (or another value if specified).

- **`add(self, num)`**: Adds `num` to the current value and returns the updated value.

- **`subtract(self, num)`**: Subtracts `num` from the current value and returns the updated value.

- **`multiply(self, num)`**: Multiplies the current value by `num` and returns the updated value.

- **`divide(self, num)`**: Divides the current value by `num` and returns the updated value. Raises `ZeroDivisionError` if `num` is 0.

- **`get_value(self)`**: Returns the current value of the calculator.

- **`reset(self)`**: Resets the calculator’s value to 0 and returns the reset value.

## Usage

1. Import the `Calculator` class from `calculator.py` to use it in your code:

   ```python
   from calculator import Calculator

   calc = Calculator()
   calc.add(5)
   print(calc.get_value())  # Output: 5
   ```

2. Run the tests to ensure everything is working correctly:
   ```bash
   pytest
   ```

## Running Tests

1. Ensure you have pytest installed. If not, install it using:

   ```bash
   pip install pytest
   ```

2. Run the tests by executing the following command in your terminal:

   ```bash
   pytest
   ```

3. Review the test results to confirm that all tests pass.

## Tests

The `test_calculator.py` file contains the following tests:

- **`test_calculator_init()`**: Tests the initialization of the `Calculator` class.

- **`test_calculator_add()`**: Tests the `add` method of the `Calculator` class.

- **`test_calculator_subtract()`**: Tests the `subtract` method of the `Calculator` class.

- **`test_calculator_multiply()`**: Tests the `multiply` method of the `Calculator` class.

- **`test_calculator_divide()`**: Tests the `divide` method of the `Calculator` class.

- **`test_calculator_divide_by_zero()`**: Tests that dividing by zero raises a `ZeroDivisionError`.

- **`test_calculator_reset()`**: Tests the `reset` method of the `Calculator` class.
