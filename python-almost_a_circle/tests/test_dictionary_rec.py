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

    def test_dictionary(self):
        """test with all arguments"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'id': 1, 'width': 10,
                                         'height': 2, 'x': 1, 'y': 9})
        r1_test = type(r1_dictionary)
        self.assertEqual(r1_test, type(dict()))

    def test_json_dictionary(self):
        """test for know the type"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([r1_dictionary])
        deserialized_json = eval(json_dictionary)
        self.assertEqual(deserialized_json, [{'id': 1, 'width': 10,
                                             'height': 2, 'x': 1, 'y': 9}])
        r1_test = type(json_dictionary)
        self.assertEqual(r1_test, type(str()))


if __name__ == '__main__':
    unittest.main()
