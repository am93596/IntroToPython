import math

class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


class SciCalculator(SimpleCalculator):
    def find_sqrt(self, num):
        if num:
            return math.sqrt(num)
        return None

    def find_ceil(self, num):
        if num:
            return math.ceil(num)
        return None