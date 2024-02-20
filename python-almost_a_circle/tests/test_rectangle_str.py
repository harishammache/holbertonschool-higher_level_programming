#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestId(unittest.TestCase):
    """all test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_no_id(self):
        """test with no id"""
        instance = Rectangle(5, 5, 1)
        self.assertEqual(instance.id, 1)

    def test_id(self):
        """test with an id"""
        instance = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(instance.id, 12)


if __name__ == "__main__":
    unittest.main()
