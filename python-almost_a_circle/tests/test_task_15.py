#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestId(unittest.TestCase):
    """All Test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_dic_to_json(self):
        """test dictionary to json str"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary,
                         {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8})
        self.assertEqual(type(dictionary), type(dict()))
        self.assertEqual(json_dictionary,
                         '[{"id": 1, "width": 10,\
 "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), type(str()))


if __name__ == '__main__':
    unittest.main()
