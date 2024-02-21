#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.rectangle import Rectangle


class TestId(unittest.TestCase):
    """All Test"""
    def test_int(self):
        """test with width > height"""
        instance = Rectangle(3, 2)
        self.assertEqual(instance.area(), 6)

    def test_2_int(self):
        """test with width < height"""
        instance2 = Rectangle(2, 10)
        self.assertEqual(instance2.area(), 20)

    def test_3_int(self):
        """test with an id"""
        instance3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(instance3.area(), 56)


if __name__ == '__main__':
    unittest.main()
