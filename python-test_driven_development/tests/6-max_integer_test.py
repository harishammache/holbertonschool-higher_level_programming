#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        test for know who is the max
    """
    def test_all_Integer(self):
        """Test with a list of integers"""
        list = [1, 2, 3, 4, 5]
        result = max_integer(list)
        self.assertEqual(result, 5)

    def test_negativ_Integer(self):
        """Test with a list containing negative integers"""
        list = [-1, -3, -9]
        result = max_integer(list)
        self.assertEqual(result, -1)

    def test_empty_list(self):
        """Test with an empty list"""
        list = []
        result = max_integer(list)
        self.assertEqual(result, None)

    def test_float_integer(self):
        """Test with float"""
        list = [1.2, 5.2, 8.9]
        result = max_integer(list)
        self.assertEqual(result, 8.9)

    def test_list_str(self):
        """Test with caractere and integer"""
        list = ["a", "b", 1]
        self.assertRaises(TypeError, max_integer)

if __name__ == '__main__':
    unittest.main()
