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

    def test_json_to_dict(self):
        """json string to dict"""
        list_input = [
         {'id': 89, 'width': 10, 'height': 4},
         {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), type(list()))
        self.assertEqual(list_input, [{'height': 4, 'width': 10, 'id': 89},
                                      {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(json_list_input), type(str()))
        self.assertEqual(json_list_input,
                         '[{"id": 89, "width": 10, "height": 4},\
 {"id": 7, "width": 1, "height": 7}]')
        self.assertEqual(type(list_output), type(list()))
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])


if __name__ == "__main__":
    unittest.main()
