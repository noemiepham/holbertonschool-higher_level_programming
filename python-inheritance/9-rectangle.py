#!/usr/bin/python3
"""BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle"""

    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Raise Exception"""
        return (self.__width * self.__height)

    def __str__(self):
        """Should retirn str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
