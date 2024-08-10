class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self.value

    def subtract(self, num):
        self.value -= num
        return self.value

    def multiply(self, num):
        self.value *= num
        return self.value

    def divide(self, num):
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        self.value /= num
        return self.value

    def get_value(self):
        return self.value

    def reset(self):
        self.value = 0
        return self.value
