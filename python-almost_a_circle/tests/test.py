#!/usr/bin/python3
"""import unitest"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
  """Test Base"""
  def test_cound_object(self):
      """test couting number of"""
      Base._Base__nb_object = 0
      self.assertEqual(Base._Base__nb_objects, 0)


