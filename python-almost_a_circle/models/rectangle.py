#!/usr/bin/python3
"""Rectangle"""

from models.base import Base
import sys


class Rectangle(Base):
    """Inheritance de Base"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        self.id = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Raise Exception"""
        return self.__width * self.__height

    def display(self):
        """Display #"""

        if self.__y != 0:
            for newline in range(self.__y):
                print()
        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Overriding the str"""
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        id = self.id
        return "[Rectangle] ({}) {}/{}" \
               " - {}/{}".format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """Import argv et argc"""
        if len(kwargs) != 0:
            for item, value in kwargs.items():
                setattr(self, item, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()
