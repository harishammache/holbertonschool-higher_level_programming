#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_max_in_middle(self):
        """Test with the max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_one_element(self):
        """Test with only one element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_float_numbers(self):
        """Test with a list of float numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_list(self):
        """Test with a list of mixed data types"""
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])
    
    def test_none(self):
        """Test with None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test with a list of non-integer elements"""
        with self.assertRaises(TypeError):
            max_integer(["Hello", 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
