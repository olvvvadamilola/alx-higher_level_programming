#!/usr/bin/python3
"""Unit tests for the Base class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_incremented_id(self):
        """Test that the id is incremented correctly."""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_specified_id(self):
        """Test that the id is set correctly when specified."""

        b = Base(42)
        self.assertEqual(b.id, 42)


if __name__ == '__main__':
    unittest.main()
