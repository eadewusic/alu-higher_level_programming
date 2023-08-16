#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)
        self.assertEqual(max_integer([-4, -3, 2, 1]), 2)
        self.assertEqual(max_integer([4, -3, -2, 1]), 4)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_integer_and_float(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1, -2.2, -3, -4.4]), -1)

if __name__ == '__main__':
    unittest.main()
