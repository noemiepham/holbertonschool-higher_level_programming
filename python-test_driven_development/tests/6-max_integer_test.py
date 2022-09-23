#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for “max at the end” list order"""

    def text_max_integer(self):
        """Test list number normal and order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def text_begining_inorder(self):
        """ Test list number normal and inoder"""
        self.assertEquals(max_integer([4, 2, 1, 3]), 4)

    def text_max_inmiddle_list(self):
        """ Test for “max in the middle” exists"""
        self.assertEquals(max_integer([1, 2, 4, 3]), 4)

    def text_only_negative(self):
        """Test for “only negative numbers in the list” exists"""
        self.assertEquals(max_integer([-1, -2, -3, -4]), -1)

    def text_only_one_element(self):
        """Test for “list of one element” exists"""
        self.assertEquals(max_integer([1]), 1)

    def text_list_empty(self):
        """List is empty"""
        self.assertEquals(max_integer([]), None)
