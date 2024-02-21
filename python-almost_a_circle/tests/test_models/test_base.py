#!/usr/bin/python3
"""
    Unittest for file base.py
"""
import unittest
from models.base import Base


class TestId(unittest.TestCase):
    """All Test"""
    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_Only_None_Id(self):
        """test with none Id"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        instance4 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)
        self.assertEqual(instance4.id, 4)

    def test_One_Id(self):
        """test with one Id"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(12)
        instance4 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 12)
        self.assertEqual(instance4.id, 3)

    def test_Negativ_Id(self):
        """test with a negativ number"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(-8)
        instance4 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, -8)
        self.assertEqual(instance4.id, 3)

    def test_zero_Id(self):
        """test with zero id"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(0)
        instance4 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 0)
        self.assertEqual(instance4.id, 3)


if __name__ == '__main__':
    unittest.main()
