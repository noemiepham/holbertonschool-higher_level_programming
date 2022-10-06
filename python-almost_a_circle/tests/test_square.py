#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
import os
from models.square import Square
from models.rectangle import Rectangle


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
        self.assertEqual(s.__str__(), '[Square] (24) 2/0 - 1')

    def test_created(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

        s = Square.create(**{'id': 89, 'size': 1})
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

    def test_load_from_file(self):
        """Test of Square.load_from_file(None) in Square exists"""
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile('Square.json'))

        load_file = Square.load_from_file()
        self.assertEqual(len(load_file), 0)

    def test_save_to_file(self):
      """Test of Square.save_to_file(None) in Square exists"""
      Square.save_to_file([Square(1)])
      with open("Square.json", mode="r") as read_file:
        s = read_file.read()
        self.assertEqual(len(s), 39)

    def test_save_to_file_list_empty(self):
      """Test of Square.save_to_file([]) in Square exists"""
      Square.save_to_file([])
      with open("Square.json", mode="r") as read_file:
           s = read_file.read()
           self.assertEqual(s, "[]")

    def test_save_to_file_empty(self):
      """Test of Square.save_to_file([]) in Square exists"""
      Square.save_to_file(None)
      with open("Square.json", mode="r") as read_file:
           s = read_file.read()
           self.assertEqual(len(s), 2)
    def test_save_to_file_none(self):
      """Test of Square.save_to_file([]) in Square exists"""
      with self.assertRaises(TypeError):
          Square.save_to_file()


    def test_save_to_file_r(self):
      """Test of Square.save_to_file(None) in Square exists"""
      Rectangle.save_to_file([Rectangle(1, 2)])
      with open("Square.json", mode="r") as read_file:
        s = read_file.read()
        self.assertEqual(len(s), 2)


    def test_save_to_file_list_empty_r(self):
      """Test of Square.save_to_file([]) in Square exists"""
      Rectangle.save_to_file([])
      with open("Rectangle.json", mode="r") as read_file:
        self.assertEqual("[]", read_file.read())


    def test_save_to_file_empty_r(self):
      """Test of Square.save_to_file([]) in Square exists"""
      Rectangle.save_to_file(None)
      with open("Rectangle.json", mode="r") as read_file:
        s = read_file.read()
        self.assertEqual(len(s), 2)


    def test_save_to_file_none_r(self):
      """Test of Square.save_to_file([]) in Square exists"""
      with self.assertRaises(TypeError):
        Rectangle.save_to_file()

    def test_two_args(self):
      """test two args"""
      with self.assertRaises(TypeError):
        Square.save_to_file([], 2)

    def test_save_one_rectangle(self):
      """test for one rectangle"""
      rect = Rectangle(10, 7, 2, 8, 5)
      Rectangle.save_to_file([rect])
      with open("Rectangle.json", "r") as file:
        self.assertTrue(len(file.read()) == 53)

    def test_save_two_rectangles(self):
      """test for two rectangles"""
      rect1 = Rectangle(10, 7, 2, 8, 5)
      rect2 = Rectangle(2, 4, 1, 2, 3)
      Rectangle.save_to_file([rect1, rect2])
      with open("Rectangle.json", "r") as file:
        self.assertTrue(len(file.read()) == 105)

    def test_save_one_square(self):
      """test for one square"""
      square = Square(10, 7, 2, 8)
      Square.save_to_file([square])
      with open("Square.json", "r") as file:
        self.assertTrue(len(file.read()) == 39)

    def test_save_two_squares(self):
      """test for two squares"""
      square1 = Square(10, 7, 2, 8)
      square2 = Square(8, 1, 2, 3)
      Square.save_to_file([square1, square2])
      with open("Square.json", "r") as file:
        self.assertTrue(len(file.read()) == 77)

    def test_save_overwrite(self):
      """test for overwrite"""
      square = Square(8, 5, 9, 2)
      Square.save_to_file([square])
      square = Square(10, 7, 2, 8)
      Square.save_to_file([square])
      with open("Square.json", "r") as file:
        self.assertTrue(len(file.read()) == 39)

    def test_save_empty_list(self):
      """test for an empty list"""
      Square.save_to_file([])
      with open("Square.json", "r") as file:
        self.assertEqual("[]", file.read())

    def test_save_no_args(self):
      """test for no argument"""
      with self.assertRaises(TypeError):
        Rectangle.save_to_file()

    def test_save_two_arg(self):
      """test for two arguments"""
      with self.assertRaises(TypeError):
        Square.save_to_file([], 1)


if __name__ == "__main__":
    unittest.main()
