from unittest import TestCase

from src.calculator import sum, subtract, multiply, divide


class CalculatorTests(TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3

    def test_subtract(self):
        assert subtract(2, 1) == 1

    def test_multiply(self):
        assert multiply(2, 3) == 6

    def test_divide(self):
        assert divide(6, 2) == 3

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)
