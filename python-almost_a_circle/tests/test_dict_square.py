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

    def test_dict_sq(self):
        """test a dictionnary"""
        r1 = Square(10, 2, 1)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        r1_test = type(r1_dictionary)
        self.assertEqual(r1_test, type(dict()))

    def test_dict_up_sq(self):
        """test if r1 = r2"""
        r1 = Square(10, 2, 1)
        r2 = Square(1, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.size, 1)
        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.size, 10)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
