#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestId(unittest.TestCase):
    """All Test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_No_Id(self):
        """test with no id"""
        instance = Rectangle(10, 2)
        instance2 = Rectangle(2, 10)
        instance3 = Rectangle(8, 10)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)

    def test_Id(self):
        """test with id"""
        instance = Rectangle(10, 2)
        instance2 = Rectangle(2, 10)
        instance3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 12)


if __name__ == "__main__":
    unittest.main()
