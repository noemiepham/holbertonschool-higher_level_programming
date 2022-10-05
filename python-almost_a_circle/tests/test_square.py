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
      self.assertEqual(s.size, 5)


      with self.assertRaises(TypeError):
           s = Square(5, "1")
           s = Square()

      with self.assertRaises(ValueError):
           s = Square(-5, 3, 4)

           """Test of Square(1, 2, "3") exists"""
           s = Square("string")






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
      self.assertEqual(s.__str__(), '[Square] (11) 2/0 - 1')



if __name__ == "__main__":
    unittest.main()
