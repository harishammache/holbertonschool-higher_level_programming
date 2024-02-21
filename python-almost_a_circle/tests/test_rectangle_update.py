#!/usr/bin/python3
"""
    Unittest for file rectangle.py
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
        """test with just the size"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_update(self):
        """test with the size and size"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 5)

    def test_update2(self):
        """test with the size and size and id"""
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 2)

    def test_update3(self):
        """test with the size id and x"""
        s1 = Square(5)
        s1.update(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 2)

    def test_update4(self):
        """test with the size, id, x and y"""
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.size, 2)

        s1.update(x=12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.size, 2)

        s1.update(size=7, y=1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.size, 7)

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.size, 7)


if __name__ == '__main__':
    unittest.main()
