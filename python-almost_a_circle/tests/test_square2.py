#!/usr/bin/python3
"""
    Unittest for file square.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestId(unittest.TestCase):
    """all test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_size(self):
        """test with just a size same argument"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual((s1.size), 5)

    def test_no_int(self):
        """test with the size is not an int"""
        with self.assertRaises(TypeError):
            s1 = Square()


if __name__ == '__main__':
    unittest.main()
