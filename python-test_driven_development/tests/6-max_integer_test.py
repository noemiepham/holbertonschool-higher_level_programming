#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for “max at the end” list order"""

    def test_max_int_basic(self):
        """ tests normal list of ints
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def text_max_int_begining_inorder(self):
        """ Test list number normal and inoder"""
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def text_max_integer(self):
        """ Test for “max in the middle” exists"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_int_neg_negative(self):
        """Test for “only negative numbers in the list” exists"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one(self):
        """ tests if list has only one item
        """
        self.assertEqual(max_integer([1]), 1)

    def test_max_int_empty(self):
        """List is empty"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()