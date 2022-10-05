#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
  """Testing Square"""
  def test_instance(self):
      """test input size correct standard """
      s = Square(5)
      self.assertEqual(s.width, 5)
      self.assertEqual(s.height, 5)


      with self.assertRaises(TypeError):
          Square(5, "1")

      with self.assertRaises(TypeError):
           Square()

      with self.assertRaises(TypeError):
           Square("1")

      with self.assertRaises(ValueError):
           Square(-5, 3, 4)

      with self.assertRaises(TypeError):
           Square(1, 2, "3")

      with self.assertRaises(ValueError):
           Square(1, -2)

      with self.assertRaises(ValueError):
           Square(1, 2, -3)

      with self.assertRaises(ValueError):
           Square(0)

  def test_dictionary(self):
      s1 = Square(10, 2, 1, 1)
      s1_dict = s1.to_dictionary()
      self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

  def test_case_normal(self):
      """Test of Square(1, 2, 3, 4) exists"""
      s = Square(1, 2, 3, 4)
      self.assertEqual(s.id, 4)
      self.assertEqual(s.size, 1)
      self.assertEqual(s.x, 2)
      self.assertEqual(s.y, 3)
  def test_area(self):
      """testing area"""

      s = Square(5)
      self.assertEqual(s.area(), 25)

      s = Square(1, 2)
      self.assertEqual(s.area(), 1)
  def test_display(self):
      """test display()"""
      s = Square(5)
      with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
        s.display()

      assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

      s = Square(1, 2)
      with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
        s.display()

      assert mock_stdout.getvalue() == "  #\n"
  def test_string(self):
      """Test str"""

      s = Square(1, 2)
      self.assertEqual(s.__str__(), '[Square] (15) 2/0 - 1')

  def test_created(self):
      """Test of Square.create(**{ 'id': 89 }) in Square exists"""
      s = Square.create(**{ 'id': 89 })
      self.assertEqual(s.id, 89)

      s = Square.create(**{ 'id': 89, 'size': 1 })
      self.assertEqual(s.id, 89)
      self.assertEqual(s.size, 1)

      s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
      self.assertEqual(s.id, 89)
      self.assertEqual(s.size, 1)
      self.assertEqual(s.x, 2)

      s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
      self.assertEqual(s.id, 89)
      self.assertEqual(s.size, 1)
      self.assertEqual(s.x, 2)
      self.assertEqual(s.y, 3)



if __name__ == "__main__":
    unittest.main()
