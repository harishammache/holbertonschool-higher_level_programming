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

    def test_json_str(self):
        """test for json string"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            new_file = file.read()
            self.assertEqual(new_file,
                             '[{"id": 1, "width": 10,\
 "height": 7, "x": 2, "y": 8}, '
                             '{"id": 2, "width": 2, "height": 4,\
 "x": 0, "y": 0}]')


if __name__ == '__main__':
    unittest.main()
