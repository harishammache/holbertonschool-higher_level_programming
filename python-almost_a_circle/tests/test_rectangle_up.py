#!/usr/bin/python3
"""
    Unittest for file rectangle.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestId(unittest.TestCase):
    """all test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_no_Id(self):
        """test with no id for the rectangle"""
        instance = Rectangle(10, 10, 10, 10)
        self.assertEqual(instance.id, 1)

    def test_Id(self):
        """test with 1 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(height=1)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 1)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)

    def test_Id2(self):
        """test with 2 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(width=1, x=2)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 1)
        self.assertEqual(instance.height, 2)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)

    def test_Id3(self):
        """test with 3 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(y=1, width=2, x=3, id=89)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.x, 3)
        self.assertEqual(instance.y, 1)

    def test_Id4(self):
        """test with 4 arg which is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(x=1, height=2, y=3, width=4)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 4)
        self.assertEqual(instance.height, 2)
        self.assertEqual(instance.x, 1)
        self.assertEqual(instance.y, 3)

    def test_Id5(self):
        """test with 5 arg which is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(id=89, height=3, width=2, x=4, y=5)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)


if __name__ == '__main__':
    unittest.main()
