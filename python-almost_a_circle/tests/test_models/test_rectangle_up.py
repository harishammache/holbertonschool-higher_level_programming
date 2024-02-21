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

    def test_no_id(self):
        """test with no id for the rectangle"""
        instance = Rectangle(10, 10, 10, 10)
        self.assertEqual(instance.id, 1)

    def test_id(self):
        """test with 1 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(89)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)

    def test_id2(self):
        """test with 2 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(89, 2)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)

    def test_id3(self):
        """test with 3 arg who is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(89, 2, 3)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)

    def test_id4(self):
        """test with 4 arg which is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(89, 2, 3, 4)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 10)

    def test_id5(self):
        """test with 5 arg which is the id"""
        instance = Rectangle(10, 10, 10, 10)
        instance.update(89, 2, 3, 4, 5)
        self.assertEqual(instance.id, 89)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)


if __name__ == '__main__':
    unittest.main()
