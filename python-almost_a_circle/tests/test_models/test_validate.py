#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.rectangle import Rectangle


class TestId(unittest.TestCase):
    """All Test"""
    def test_not_int(self):
        """test with not an integer"""
        with self.assertRaises(TypeError):
            instance = Rectangle(10, "haris")

    def test_negativ(self):
        """test with a negativ width"""
        with self.assertRaises(ValueError):
            instance = Rectangle(-10, 2)

    def test_x_not_integer(self):
        """test with x is not an integer"""
        with self.assertRaises(TypeError):
            instance = Rectangle(10, 2, "haris")

    def test_y_negativ(self):
        """test with y is negativ"""
        with self.assertRaises(ValueError):
            instance = Rectangle(10, 2, 2, -8)
