from calculator import SimpleCalculator
import unittest


class CalculatorTests(unittest.TestCase):
    calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        self.assertEqual(self.calc.add(-2, -7), -9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(9, 4), 36)
        self.assertEqual(self.calc.multiply(-9, -4), 36)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, -6), -2.0)
        self.assertEqual(self.calc.divide(4, 0), "Cannot divide by zero")

# Write a test case or two for each method
# Go and make the tests pass
