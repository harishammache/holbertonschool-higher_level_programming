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

    def test_dict(self):
        """test a dictionnary"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                         'height': 2, 'width': 10})
        r1_test = type(r1_dictionary)
        self.assertEqual(r1_test, type(dict()))

    def test_dict_up(self):
        """test if r1 = r2"""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 1)
        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 9)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
