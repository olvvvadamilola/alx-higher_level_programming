#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import io
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    def test_width_setter(self):
        r = Rectangle(10, 20, 5, 10, 1)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height_setter(self):
        r = Rectangle(10, 20, 5, 10, 1)
        r.height = 40
        self.assertEqual(r.height, 40)

    def test_x_setter(self):
        r = Rectangle(10, 20, 5, 10, 1)
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_y_setter(self):
        r = Rectangle(10, 20, 5, 10, 1)
        r.y = 25
        self.assertEqual(r.y, 25)

    def test_width_setter_type_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(TypeError):
            r.width = "invalid_width"

    def test_width_setter_value_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter_type_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(TypeError):
            r.height = "invalid_height"

    def test_height_setter_value_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_setter_type_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(TypeError):
            r.x = "invalid_x"

    def test_x_setter_value_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter_type_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(TypeError):
            r.y = "invalid_y"

    def test_y_setter_value_error(self):
        r = Rectangle(10, 20, 5, 10, 1)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(2, 3)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n##\n')
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        
        r2 = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] ({}) 1/0 - 5/5".format(r2.id)
        self.assertEqual(str(r2), expected_output)


if __name__ == '__main__':
    unittest.main()
