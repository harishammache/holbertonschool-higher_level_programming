#!/usr/bin/python3
"""
    Since the beginning you have been creating “Interactive tests”
    def max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        test for know who is the max
    """
    def all_Integer(self):
        list = [1, 2, 3, 4, 5]
        result = max_integer(list)
        self.assertEqual(result, 5)

    def negativ_Integer(self):
        list = [-1, -3, -9]
        result = max_integer(list)
        self.assertEqual(result, -1)

    def empty_list(self):
        list = []
        result = max_integer(list)
        self.assertEqual(result, None)

    def float_integer(self):
        list = [1.2, 5.2, 8.9]
        result = max_integer(list)
        self.assertEqual(result, 8.9)

    def list_str(self):
        list = ["a", "b", 1]
        self.assertRaises(TypeError, max_integer)

    if __name__ == '__main__':
        unittest.main()
