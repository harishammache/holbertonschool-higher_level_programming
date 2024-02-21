#!/usr/bin/python3
"""
    Unittest for file square.py
"""
import unittest
from models.base import Base
from models.square import Square


class TestId(unittest.TestCase):
    """All Test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0
    """all test"""
    def test_square(self):
        """test with just a size"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

    def test_square_x(self):
        """test with a size and a x"""
        s1 = Square(2, 2)
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 2")
        self.assertEqual(s1.area(), 4)

    def test_square_x_y(self):
        """test with a size, x and y"""
        s1 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 3")
        self.assertEqual(s1.area(), 9)


if __name__ == '__main__':
    unittest.main()
