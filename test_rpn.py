import unittest

import rpn


class TestBasics(unittest.TestCase):

    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)

    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)

    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)

    def test_pow(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)

    def test_floordiv(self):
        result = rpn.calculate("3 2 //")
        self.assertEqual(1, result)

    def test_percent(self):
        result = rpn.calculate("10 10% +")
        self.assertEqual(11, result)

    def test_rightshift(self):
        result = rpn.calculate("1 1 rs")
        self.assertEqual(0, result)

    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
