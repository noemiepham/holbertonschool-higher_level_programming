#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
  """Testing Square"""
  def test_instance(self):
      """test input size correct standard """
      s = Square(5)
      self.assertEqual(s.size, 5)



