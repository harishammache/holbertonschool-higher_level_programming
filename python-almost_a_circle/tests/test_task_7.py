import unittest
import io
import sys
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangleDisplay(unittest.TestCase):
    def test_rectangle_display(self):
        """test rectangle display"""
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r2.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
